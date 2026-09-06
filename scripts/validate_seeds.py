# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 William Johnason / axoviq.com
"""
validate_seeds.py  — Scan all template seeds.md and verify each concrete
ingest URL is (1) accessible via UrlSkill and (2) in-scope per purpose.md.

Usage:
  python scripts/validate_seeds.py                        # all templates
  python scripts/validate_seeds.py --template real-estate/investment
  python scripts/validate_seeds.py --no-scope             # URL check only

Exit code: 0 = all pass, 1 = any failure.

Why two checks?
  1. URL accessibility  — UrlSkill is the actual fetch path used by synthadoc
     ingest.  A blocked (403/429) or empty response causes a skip just as it
     would in production.
  2. Scope alignment    — replicates the LLM purpose-block prepended to the
     ingest decision prompt.  A page whose text is outside the wiki's stated
     domain receives action='skip' in production; this script catches that
     before a user hits it on a fresh wiki.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────

# This script lives in  <repo>/scripts/validate_seeds.py
# Repo root is one level up; synthadoc package is at <repo>/synthadoc/
REPO_ROOT = Path(__file__).parent.parent
TEMPLATES_DIR = REPO_ROOT / "synthadoc" / "templates"

_SYS_PATH_SET = False


def _ensure_path() -> None:
    global _SYS_PATH_SET
    if not _SYS_PATH_SET:
        sys.path.insert(0, str(REPO_ROOT))
        _SYS_PATH_SET = True


# ── URL extraction from seeds.md ──────────────────────────────────────────────

_INGEST_URL_RE = re.compile(r'synthadoc\s+ingest\s+"(https?://[^"]+)"')
_PLACEHOLDER_RE = re.compile(r"<[^>]+>")


def extract_seed_urls(seeds_text: str) -> list[str]:
    """Return concrete https URLs from ``synthadoc ingest`` commands.

    Skips:
    - local file paths (no http scheme)
    - user-placeholder URLs that contain ``<param>`` tokens
    """
    urls: list[str] = []
    for m in _INGEST_URL_RE.finditer(seeds_text):
        url = m.group(1)
        if _PLACEHOLDER_RE.search(url):
            continue
        urls.append(url)
    return urls


# ── Scope check ───────────────────────────────────────────────────────────────

# Mirrors the purpose_block prepended to _DECISION_PROMPT in ingest_agent.py.
# The ingest agent uses action="skip" for out-of-scope content; this prompt
# reduces that to a binary yes/no so we can report it without writing pages.
_SCOPE_PROMPT = """\
You are checking whether a web page is in scope for a knowledge wiki.

Wiki scope (from purpose.md):
{purpose}

Web page content (first 3 000 characters):
{content}

Decide: does this content fall squarely within the wiki's stated domain?

Guidelines:
- in_scope=true  → content is DIRECTLY useful to a practitioner in this domain.
- in_scope=false → content is primarily about excluded topics, or so generic
  that it adds no domain-specific value (e.g. a general housing overview in a
  commercial real-estate investment wiki).

Return ONLY valid JSON (no markdown fences, no explanation outside the JSON):
{{"in_scope": true_or_false, "reasoning": "one concise sentence"}}"""


async def check_scope(
    purpose: str,
    content: str,
    client: "anthropic.AsyncAnthropic",
    model: str,
) -> tuple[bool, str]:
    """Return ``(in_scope, reasoning)`` from an LLM scope check."""
    prompt = _SCOPE_PROMPT.format(
        purpose=purpose.strip()[:4_000],
        content=content[:3_000],
    )
    resp = await client.messages.create(
        model=model,
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = (resp.content[0].text if resp.content else "").strip()
    # Strip markdown fences in case the model ignores the instruction
    raw = re.sub(r"^```[a-z]*\s*|\s*```$", "", raw, flags=re.MULTILINE).strip()
    try:
        data = json.loads(raw)
        return bool(data.get("in_scope", True)), str(data.get("reasoning", ""))
    except json.JSONDecodeError:
        # Treat parse failure as pass so we do not create false negatives
        return True, f"(JSON parse error — treating as pass; raw={raw[:80]})"


# ── Per-URL validation ────────────────────────────────────────────────────────

async def validate_url(
    url: str,
    purpose: str,
    *,
    skill: "UrlSkill",
    check_scope_flag: bool,
    client,
    model: str,
    url_sem: asyncio.Semaphore,
    llm_sem: asyncio.Semaphore,
) -> dict:
    """Fetch ``url`` and optionally scope-check it.  Returns a result dict."""
    from synthadoc.skills.base import DomainBlockedException

    result: dict = {
        "url": url,
        "url_status": "",
        "chars": 0,
        "in_scope": None,
        "scope_reason": "",
        "error_detail": "",
    }

    # ── Step 1: URL accessibility ────────────────────────────────────────────
    content = ""
    async with url_sem:
        try:
            extracted = await skill.extract(url)
            content = extracted.text.strip()
            result["chars"] = len(content)
            result["url_status"] = "OK" if content else "EMPTY"
        except DomainBlockedException as e:
            result["url_status"] = f"BLOCKED ({e.status_code})"
        except Exception as e:
            result["url_status"] = "ERROR"
            result["error_detail"] = str(e)[:120]

    # ── Step 2: scope check (only when fetch succeeded) ──────────────────────
    if check_scope_flag and purpose and result["url_status"] == "OK":
        async with llm_sem:
            in_scope, reasoning = await check_scope(purpose, content, client, model)
        result["in_scope"] = in_scope
        result["scope_reason"] = reasoning

    return result


# ── Per-template validation ───────────────────────────────────────────────────

async def validate_template(
    template_dir: Path,
    *,
    check_scope_flag: bool,
    skill,
    client,
    model: str,
    url_sem: asyncio.Semaphore,
    llm_sem: asyncio.Semaphore,
) -> list[dict]:
    """Return a list of result dicts for every URL in this template's seeds.md."""
    seeds_path = template_dir / "wiki" / "seeds.md"
    purpose_path = template_dir / "wiki" / "purpose.md"
    if not seeds_path.exists():
        return []

    seeds_text = seeds_path.read_text(encoding="utf-8")
    urls = extract_seed_urls(seeds_text)
    if not urls:
        return []

    purpose = purpose_path.read_text(encoding="utf-8") if purpose_path.exists() else ""
    template_name = template_dir.relative_to(TEMPLATES_DIR).as_posix()

    url_results = await asyncio.gather(*[
        validate_url(
            url, purpose,
            skill=skill,
            check_scope_flag=check_scope_flag,
            client=client,
            model=model,
            url_sem=url_sem,
            llm_sem=llm_sem,
        )
        for url in urls
    ])
    return [{"template": template_name, **r} for r in url_results]


# ── Report ─────────────────────────────────────────────────────────────────────

def print_report(results: list[dict], check_scope_flag: bool) -> list[dict]:
    """Print a colour-coded table and return the list of failed rows."""
    GREEN = "\033[32m"
    RED   = "\033[31m"
    RESET = "\033[0m"

    COL_T = 32   # template name
    COL_S = 18   # url_status

    hdr = f"{'TEMPLATE':<{COL_T}}  {'URL_STATUS':<{COL_S}}"
    if check_scope_flag:
        hdr += f"  {'SCOPE':<6}"
    hdr += "  URL"
    print(f"\n{hdr}")
    print("-" * (len(hdr) + 35))

    failures: list[dict] = []
    for r in results:
        url_ok   = r["url_status"] == "OK"
        scope_ok = r["in_scope"] is None or r["in_scope"]
        passed   = url_ok and scope_ok
        if not passed:
            failures.append(r)

        color = GREEN if passed else RED
        scope_str = ""
        if check_scope_flag and r["in_scope"] is not None:
            scope_str = "YES" if r["in_scope"] else "NO "
        short_url = r["url"][:56] + "…" if len(r["url"]) > 57 else r["url"]

        row = f"{color}{r['template']:<{COL_T}}  {r['url_status']:<{COL_S}}"
        if check_scope_flag:
            row += f"  {scope_str:<6}"
        row += f"  {short_url}{RESET}"
        print(row)

        if not url_ok and r["error_detail"]:
            print(f"  {'':>{COL_T}}  {r['error_detail']}")
        if check_scope_flag and not scope_ok:
            print(f"  {'':>{COL_T}}  ↳ {r['scope_reason']}")

    return failures


# ── Entry point ───────────────────────────────────────────────────────────────

async def async_main(args: argparse.Namespace) -> int:
    _ensure_path()
    from synthadoc.skills.url.scripts.main import UrlSkill

    check_scope_flag = not args.no_scope

    # Anthropic client for scope checks
    client = None
    if check_scope_flag:
        api_key = os.environ.get("ANTHROPIC_API_KEY", "")
        if not api_key:
            print(
                "WARNING: ANTHROPIC_API_KEY not set — running URL-only mode.\n"
                "         Set the key or pass --no-scope to silence this warning.",
                file=sys.stderr,
            )
            check_scope_flag = False
        else:
            try:
                import anthropic
                client = anthropic.AsyncAnthropic(api_key=api_key)
            except ImportError:
                print(
                    "WARNING: anthropic package not installed — running URL-only mode.",
                    file=sys.stderr,
                )
                check_scope_flag = False

    # Template directories to scan
    if args.template:
        dirs = [TEMPLATES_DIR / args.template]
        if not dirs[0].exists():
            print(f"ERROR: template directory not found: {dirs[0]}", file=sys.stderr)
            return 1
    else:
        dirs = sorted({
            p.parent.parent          # templates/<cat>/<name>/wiki/seeds.md → templates/<cat>/<name>
            for p in TEMPLATES_DIR.glob("**/wiki/seeds.md")
        })

    skill   = UrlSkill(fetch_timeout=30)
    url_sem = asyncio.Semaphore(5)   # max 5 concurrent URL fetches
    llm_sem = asyncio.Semaphore(2)   # max 2 concurrent LLM scope checks

    print(f"Scanning {len(dirs)} template(s) …", end="", flush=True)
    if check_scope_flag:
        print(f"  (scope check: {args.model})")
    else:
        print("  (--no-scope: URL check only)")

    batches = await asyncio.gather(*[
        validate_template(
            d,
            check_scope_flag=check_scope_flag,
            skill=skill,
            client=client,
            model=args.model,
            url_sem=url_sem,
            llm_sem=llm_sem,
        )
        for d in dirs
    ])

    all_results: list[dict] = [r for batch in batches for r in batch]

    if not all_results:
        print("No concrete seed URLs found.")
        return 0

    failures = print_report(all_results, check_scope_flag)

    total = len(all_results)
    print(f"\n{'='*60}")
    if failures:
        print(f"FAILED: {len(failures)} of {total} URLs")
        for r in failures:
            tag = r["url_status"] if r["url_status"] != "OK" else "OUT-OF-SCOPE"
            print(f"  [{tag}] {r['template']}: {r['url']}")
            detail = r.get("error_detail") or r.get("scope_reason", "")
            if detail:
                print(f"          {detail}")
        return 1

    print(f"All {total} seed URLs passed ✓")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Validate synthadoc template seed URLs — checks URL accessibility "
            "and in-scope alignment with purpose.md."
        )
    )
    parser.add_argument(
        "--template", metavar="NAME",
        help="Validate a single template (e.g. real-estate/investment). "
             "Omit to scan all templates.",
    )
    parser.add_argument(
        "--no-scope", action="store_true",
        help="Skip the LLM scope check (URL accessibility only).",
    )
    parser.add_argument(
        "--model", default="claude-haiku-4-5-20251001",
        metavar="MODEL_ID",
        help="Model used for LLM scope checks (default: claude-haiku-4-5-20251001).",
    )
    sys.exit(asyncio.run(async_main(parser.parse_args())))


if __name__ == "__main__":
    main()
