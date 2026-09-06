---
title: Getting Started — Facility Management
status: draft
confidence: low
type: concept
sources: []
---

# Getting Started — Facility Management

## Recommended first ingests

**Energy Star commercial buildings program (public)**
```
synthadoc ingest "https://www.energystar.gov/buildings" -w <wiki>
```

**OSHA workers — hazard recognition, worker rights, and safety standards (public)**
```
synthadoc ingest "https://www.osha.gov/workers" -w <wiki>
```

## Recommended web searches

- `preventive maintenance schedule template CMMS best practices` — PM planning
- `OSHA inspection checklist general industry 1910` — safety compliance
- `facility asset management ISO 55001 standard overview` — asset management
- `HVAC preventive maintenance schedule commercial building` — HVAC maintenance
- `work order management system best practices facility` — work order process

## First steps checklist

- [ ] Ingest your facility asset register (export from CMMS or spreadsheet)
- [ ] Create an equipment page for your 5 most critical assets
- [ ] Document your PM schedule for critical equipment
- [ ] Ingest your most recent facility inspection report
- [ ] Run scaffold to build the index
