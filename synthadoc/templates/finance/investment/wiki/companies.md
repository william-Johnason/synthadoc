---
title: Companies
status: draft
confidence: low
type: concept
sources: []
---

# Companies

Index of portfolio companies and investment targets. Populate by ingesting company profiles from `raw_sources/companies/` or by ingesting 10-Ks, earnings releases, and analyst reports via URL.

Each company page captures:

- **Overview** — ticker/CIK, sector/industry, headquarters, employee count
- **Business description** — core product or service, revenue model, primary customers, geographic footprint
- **Financial snapshot** — revenue, growth, gross margin, EBITDA, net income, debt, cash, market cap, EV
- **Key business metrics** — ARR/MRR, net retention, CAC payback, units/subscribers, backlog (as applicable)
- **Capital structure** — share count, debt breakdown, leverage ratio, credit rating, debt maturities
- **Competitive moat** — key differentiators, switching costs, network effects, primary competitors
- **Investment thesis** — bull/bear case, target price, entry point, hold period, current status
- **Source log** — which filings or reports were ingested and when

**How to add a company:**

1. Copy `raw_sources/companies/template-company-profile.md` and rename it after the company
2. Fill in what you know — supplement public companies with URL ingests of their 10-K and earnings transcripts
3. Run `synthadoc ingest raw_sources/companies/<company>.md -w <wiki>`
4. Re-ingest after each earnings cycle or major corporate event

Cross-link company pages to [[deals]], [[financial-models]], and [[sectors]].
