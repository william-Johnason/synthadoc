---
title: Close Checklist
status: draft
confidence: low
type: concept
sources: []
---

# Close Checklist

Monthly financial close process records. Populate by ingesting completed close forms from `raw_sources/close/`.

Each close record captures:

- **Close identity** — period, entity, controller/owner, target and actual close dates, audit status
- **Pre-close steps** — sub-ledger cut-off, intercompany eliminations, accruals list, open PO reconciliation
- **Journal entries** — standard recurring JEs (depreciation, amortization, prepaid), accruals, revenue recognition (ASC 606), lease entries (ASC 842), non-recurring adjustments
- **Account reconciliations** — cash, AR, prepaid, fixed assets, AP, accrued liabilities, deferred revenue; reconciler and sign-off status
- **Financial statement review** — P&L, balance sheet, and cash flow tie-out; variance vs. budget and prior period
- **Close package sign-off** — preparer, reviewer, CFO/Controller approval date, open issues

**How to record a close:**

1. Copy `raw_sources/close/template-month-end-close.md` and rename it for the period
2. Complete each section as the close progresses
3. Run `synthadoc ingest raw_sources/close/close-YYYY-MM.md -w <wiki>`
4. Re-ingest after final sign-off

Cross-link to [[journal-entries]], [[financial-statements]], and [[internal-controls]].
