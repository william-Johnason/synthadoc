---
title: Financial Models
status: draft
confidence: low
type: concept
sources: []
---

# Financial Models

Repository of valuation models, scenario analyses, and sensitivity tables. Populate by ingesting model summaries or by referencing outputs from your spreadsheet models.

Each financial model page captures:

- **Model overview** — target company or deal, model type (DCF / LBO / comparables / merger), date built, analyst
- **Methodology** — key valuation approach and assumptions (WACC, terminal growth rate, entry/exit multiples, leverage)
- **Key assumptions** — revenue CAGR, margin expansion, capex intensity, working capital, exit assumptions
- **Output range** — implied price or EV range across base / bull / bear cases
- **Sensitivity analysis** — two-dimensional table (e.g. WACC × terminal growth, or entry multiple × exit multiple)
- **Comparables** — trading comps and precedent transactions used to anchor the model
- **Linked deal or company** — cross-reference to [[deals]] or [[companies]]
- **Critical assumption flags** — assumptions with the most valuation sensitivity, sourced and rationale given

**How to add a model:**

1. Build your model in Excel/Sheets
2. Document the summary in `raw_sources/deals/<deal>.md` or `raw_sources/companies/<company>.md` under a "Financial Model" section
3. Run `synthadoc ingest raw_sources/.../<file>.md -w <wiki>`
4. Re-ingest when major assumptions change

Cross-link model pages to [[deals]] and [[companies]].
