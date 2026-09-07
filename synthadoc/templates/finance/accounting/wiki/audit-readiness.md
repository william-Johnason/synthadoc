---
title: Audit Readiness
status: draft
confidence: low
type: concept
sources: []
---

# Audit Readiness

Audit preparation status and PBC (prepared by client) list tracking. Populate by ingesting audit management letters, prior-year audit reports, or your own audit readiness assessments.

Each audit readiness record captures:

- **Audit scope** — entity, fiscal year, audit firm, engagement partner, planned fieldwork dates
- **PBC list status** — items requested by auditors, assigned owner, due date, completion status
- **Prior year findings** — open management letter comments, required corrective actions, remediation status
- **Significant estimates** — management estimates subject to audit scrutiny (allowances, useful lives, impairment, revenue recognition) with methodology and support documented
- **Related party transactions** — identification, approval chain, and disclosure status
- **Subsequent events** — material events between period-end and audit report date
- **Internal audit coordination** — reliance on internal audit work, coverage overlap with external auditors
- **Open issues** — items under discussion with auditors; expected resolution

**How to build audit readiness documentation:**

1. Ingest prior-year audit management letter: `synthadoc ingest <management-letter.pdf> -w <wiki>`
2. Ingest your firm's audit readiness checklist or assessment document
3. Update [[internal-controls]] with any deficiency findings from the prior audit

Cross-link to [[internal-controls]], [[financial-statements]], and [[close-checklist]].
