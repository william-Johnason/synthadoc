---
title: Sectors
status: draft
confidence: low
type: concept
sources: []
---

# Sectors

Sector and industry coverage for the investment portfolio. Populate by ingesting sector reports, industry studies, and equity research.

Each sector page captures:

- **Sector / industry** — GICS classification (sector → industry group → industry → sub-industry)
- **Macro tailwinds / headwinds** — structural drivers and risks at the sector level
- **Key metrics** — revenue growth, margin profile, capital intensity, typical leverage for the sector
- **Valuation norms** — typical EV/EBITDA, P/E, and EV/Revenue ranges; how they've moved over time
- **Regulatory environment** — major regulations affecting the sector
- **Competitive dynamics** — concentration, barriers to entry, pricing power
- **Portfolio exposure** — which [[companies]] in the portfolio belong to this sector
- **Source and date** — report source, publication date, data currency

**How to add a sector:**

1. Find a recent sector report or industry study — broker research (Goldman, Morgan Stanley, JPMorgan), IBISWorld, PitchBook, or S&P Capital IQ
2. Run `synthadoc ingest "https://..." -w <wiki>` or `synthadoc ingest <report.pdf> -w <wiki>`
3. The generated page cross-links here via [[sectors]]

Cross-link sector pages to [[companies]] and [[deals]].
