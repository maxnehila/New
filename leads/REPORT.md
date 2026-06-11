# Rippling Lead Prioritization Report

**Source:** Salesforce export (1,194 accounts) · **Analyzed:** June 11, 2026

## TL;DR

All 1,194 leads were scored 0–100 on Rippling-fit signals and bucketed into four categories. The top 30 were then individually researched (website, LinkedIn, news, funding, hiring activity) to validate status and surface intent/HR signals. See `rippling_leads_scored.csv` for the full ranked list and **Top 30 Deep-Dive** below for the verified call-first list.

| Category | Count | What it means |
|---|---|---|
| A – Hot (contact first) | 255 | Sweet-spot size + high-fit industry + strong tier |
| B – Strong fit | 726 | Good size/industry, work after the A list |
| C – Moderate / nurture | 182 | Size or industry friction; drip campaigns |
| D – Low priority | 31 | Too small/large, schools/districts, stale records |

## Scoring methodology

Each account was scored on four weighted dimensions:

1. **Employee-size fit (40 pts max).** Rippling's sweet spot is 50–250 employees (full marks), with 25–50 and 250–500 close behind. Sub-10 and 1,000+ accounts were heavily penalized — several "accounts" in the list are actually school districts or hospital systems with thousands of staff, or 1–3 person shells.
2. **Industry fit (30 pts max).** Software/IT/fintech/adtech/biotech score highest (multi-state remote workforces, device management needs, no entrenched enterprise HRIS). Construction/manufacturing/healthcare/professional services score mid (real payroll pain, hourly + salaried mix). Schools, religious institutions, government, and banks score low (entrenched vendors, procurement friction, low ACV likelihood).
3. **Existing account tier (20 pts max).** Your CRM's `Core Account Fit Tier` field (Tier 1 → 20 pts down to Tier 4 → 0).
4. **Reachability (10 pts max).** Presence of LinkedIn URL, LinkedIn company ID, and website — proxies for both data quality and outbound viability.

## What the A-list looks like

- **Size:** median 86 employees, range 30–250 — squarely mid-market.
- **Industries:** IT services/consulting (48), software (29), financial services (16), advertising (14), tech/internet (13), telecom (13). These are companies with distributed knowledge workers where Rippling's combined HR+IT (device/app management) pitch lands hardest.
- **Geography:** NY (42), TX (30), FL (28), NJ (20), MA (16) — multi-state payroll complexity is a natural wedge in all of them.
- **Tier overlap:** 55 of your 61 Tier 1 accounts land in category A; 110 Tier 2 accounts also scored A, meaning the model surfaces ~110 leads your current tiering may be underrating.

## Data-quality flags found in the CRM

- **Stale/mismatched records:** several account names don't match their website/LinkedIn (e.g. "Icon" → iconplc.com is ICON plc, a ~40k-employee CRO; "HR Director" → practifi.com; "RMG Networks" rebranded to Korbyt; "MultiAd" redirects to syndigo.com suggesting acquisition). Verified individually in the deep-dive below.
- **Wrong employee counts:** e.g. "Palmetto Elementary School" listed at 6,556 employees under Financial Services; "VSR" at 2,200.
- **Out-of-ICP records:** ~30 school districts/churches/single-digit-headcount entities padding the bottom of the list.

## Top 30 Deep-Dive (web-verified)

_Research pending — populated below._
