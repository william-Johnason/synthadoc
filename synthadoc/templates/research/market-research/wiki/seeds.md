---
title: Getting Started — Market Research
status: draft
confidence: low
type: concept
sources: []
---

# Getting Started — Market Research

## Recommended first ingests

**US Census Bureau economic indicators (public)**
```
synthadoc ingest "https://www.census.gov/economic-indicators/" -w <wiki>
```

**SBA market research guide — industry analysis and competitive landscape (public)**
```
synthadoc ingest "https://www.sba.gov/business-guide/plan-your-business/market-research-competitive-analysis" -w <wiki>
```

## Recommended web searches

- `"<market name>" market size TAM latest report` — market sizing
- `"<industry>" industry analysis Porter five forces` — competitive framework
- `"<competitor name>" annual report investor day latest` — competitor intelligence
- `consumer survey "<product category>" satisfaction NPS latest` — consumer data
- `"<industry>" market share leaders latest IDC Gartner Forrester` — analyst reports

## First steps checklist

- [ ] Ingest the most recent industry report for your market
- [ ] Create a market-overview page with size and growth data
- [ ] Create a competitor profile for your top 3 competitors
- [ ] Document your primary customer segment in [[consumer-segments]]
- [ ] Run scaffold to build the index
