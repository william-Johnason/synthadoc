---
title: Deals
status: draft
confidence: low
type: concept
sources: []
---

# Deals

Active deal pipeline and closed transactions. Populate by ingesting deal memos from `raw_sources/deals/`.

Each deal page captures:

- **Deal overview** — target company, deal type (acquisition / merger / minority stake / secondary / IPO), current stage, lead analyst
- **Deal terms** — deal value, enterprise value, price per share, premium to VWAP, consideration mix, expected close date, financing structure
- **Valuation** — EV/Revenue, EV/EBITDA, P/E multiples vs. comparable transactions and trading peers; DCF implied price
- **Investment thesis** — strategic rationale, key value drivers, synergies (revenue / cost / financial), integration risk
- **Key risks** — risk description, severity, and mitigant for each material risk
- **Return analysis** — entry price/EV, target exit multiple, hold period, base/bull/bear case IRR, expected equity multiple
- **Diligence checklist** — financial model, legal, tax, management interviews, QoE, reference checks
- **Status log** — dated record of stage changes and key decisions

**How to open a deal:**

1. Copy `raw_sources/deals/template-deal-memo.md` and rename it after the target
2. Fill in the deal terms and thesis as they develop
3. Run `synthadoc ingest raw_sources/deals/<deal>.md -w <wiki>`
4. Update and re-ingest at each stage gate

Cross-link deal pages to [[companies]], [[financial-models]], and [[sectors]].
