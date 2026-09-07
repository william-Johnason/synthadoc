---
title: BSA / AML
status: draft
confidence: low
type: concept
sources: []
---

# BSA / AML

Bank Secrecy Act and Anti-Money Laundering program documentation. Populate by ingesting your BSA/AML policy manual, FinCEN guidance, and regulatory examination findings.

Each BSA/AML record captures:

- **Program pillars** — internal controls, independent testing, designated BSA Officer, training program, Customer Due Diligence (CDD) procedures
- **Customer risk rating** — methodology for assigning Low / Medium / High risk; Enhanced Due Diligence (EDD) triggers
- **Transaction monitoring** — system used (automated / manual), alert thresholds, case management process, look-back review procedures
- **SAR filing** — Suspicious Activity Report criteria, escalation path, filing deadlines (30 days / 60 days), SAR log
- **CTR filing** — Currency Transaction Report threshold ($10,000), aggregation rules, exemption program
- **OFAC screening** — SDN list check frequency, match review process, blocked transaction procedures
- **Beneficial ownership / CDD** — FinCEN CDD Rule compliance, ownership threshold (25%), certification form
- **Training** — annual BSA training completion tracking, role-specific requirements
- **Examination history** — most recent exam date, MRA/MRIA findings, corrective action status

**How to populate:**

1. Ingest your BSA/AML policy manual: `synthadoc ingest raw_sources/bsa-aml-policy.pdf -w <wiki>`
2. Ingest FinCEN guidance relevant to your institution type
3. Cross-link examination findings to [[regulatory-compliance]]
