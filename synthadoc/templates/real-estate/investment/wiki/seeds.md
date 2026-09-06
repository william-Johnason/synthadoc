---
title: Getting Started — Real Estate Investment
status: draft
confidence: low
type: concept
sources: []
---

# Getting Started — Real Estate Investment

## Recommended first ingests

**EDGAR REIT filings — recent 10-K annual reports from real estate investment trusts (public)**
```
synthadoc ingest "https://efts.sec.gov/LATEST/search-index?q=%22real+estate+investment+trust%22&forms=10-K&dateRange=custom&startdt=2024-01-01&enddt=2025-01-01" -w <wiki>
```

**Federal Reserve Z.1 — financial accounts of the US, including real estate debt and REIT sector (public)**
```
synthadoc ingest "https://www.federalreserve.gov/releases/z1/" -w <wiki>
```

## Recommended web searches

- `commercial real estate cap rate by asset class 2024` — market cap rates
- `NOI calculation net operating income real estate formula` — underwriting fundamentals
- `apartment market vacancy rent growth 2024` — multifamily market data
- `DCF real estate model IRR equity multiple tutorial` — financial modeling
- `REIT sector analysis office industrial retail 2024` — sector trends

## First steps checklist

- [ ] Create a property page for each asset in your portfolio
- [ ] Ingest the most recent market report for your primary submarket
- [ ] Build a financial model page for your first property
- [ ] Document your target return metrics in [[portfolio]]
- [ ] Run scaffold to build the index
