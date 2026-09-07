---
title: Tax Compliance
status: draft
confidence: low
type: concept
sources: []
---

# Tax Compliance

Federal, state, and local tax filing obligations and compliance calendar. Populate by ingesting tax policy documents, IRS publications, and your tax provision workpapers.

Each tax compliance record captures:

- **Filing obligations** — form type (1120, 1065, 990, state returns), jurisdiction, due date, extension status, filing agent
- **Tax provision** — current and deferred tax expense, effective tax rate, valuation allowance analysis, uncertain tax positions (ASC 740-10 / FIN 48)
- **Estimated payments** — federal and state quarterly payment schedule, safe harbor calculation, amounts paid
- **Depreciation** — MACRS schedules, bonus depreciation elections, Section 179 elections, book-tax differences
- **Key tax attributes** — NOL carryforwards, tax credits (R&D, energy, foreign), carryforward expiration dates
- **Transfer pricing** — intercompany transaction documentation, arm's-length analysis, country-by-country reporting
- **Nexus and apportionment** — state filing obligations, apportionment factors, economic nexus thresholds
- **Open tax years** — statute of limitations by jurisdiction, open examinations, IDR status

**How to populate tax compliance:**

1. Ingest IRS publications relevant to your entity type: `synthadoc ingest "https://www.irs.gov/publications/..." -w <wiki>`
2. Ingest your tax provision memo or ASC 740 workpaper (PDF or exported markdown)
3. Ingest your tax compliance calendar

Cross-link to [[financial-statements]] and [[audit-readiness]].
