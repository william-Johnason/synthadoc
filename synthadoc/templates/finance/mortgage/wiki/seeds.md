---
title: Getting Started — Mortgage
status: draft
confidence: low
type: concept
sources: []
---

# Getting Started — Mortgage

## Recommended first ingests

**VA home loan types — fixed-rate, ARM, cash-out refi, and jumbo (public)**
```
synthadoc ingest "https://www.va.gov/housing-assistance/home-loans/loan-types/" -w <wiki>
```

**FHFA House Price Index — measures repeat-sale home price changes (public)**
```
synthadoc ingest "https://www.fhfa.gov/data/hpi" -w <wiki>
```

## Recommended web searches

- `Fannie Mae conforming loan limits latest county list` — current limits
- `CFPB TRID disclosure requirements lenders guide` — regulatory compliance
- `FHA handbook 4000.1 underwriting guidelines` — government loan policy
- `mortgage underwriting DTI ratio guidelines latest` — debt-to-income standards
- `non-QM loan products lender guidelines latest` — non-agency products

## First steps checklist

- [ ] Ingest your current underwriting guidelines document
- [ ] Create a product page for each loan type you originate
- [ ] Ingest CFPB TRID disclosure requirements
- [ ] Run scaffold to build the index
