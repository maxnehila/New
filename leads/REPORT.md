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

### 1. Icon — ❌ DISQUALIFY
Stale record. The LinkedIn URL points to Aptiv Solutions, acquired by ICON plc (~40,000-EE global CRO) in 2014. The Marlborough, MA office is just one ICON plc site; HR/payroll is enterprise-level. Purge or re-map this record.

### 2. Arena AI — 🔥 STRONG
Independent, NYC, ~166 EE. AI foundation models for electronic-hardware testing (customers: AMD, Bausch + Lomb). **$30M Series B (Apr 2025, Initialized; $62M total)** and ~29 open roles in mid-2026 — including a Technical Recruiter and EA, classic signs of scaling without mature People infrastructure. No visible Head of People, no HRIS named in postings. Prime timing for an HRIS/payroll consolidation pitch.

### 3. Touchstorm — ✅ GOOD
Independent (Diginary Holdings), "The YouTube Agency" — video marketing for Toyota, T-Mobile, Gillette. HQ actually NYC with finance/HR in Richmond, VA. Headcount soft (~68 vs. 103 in CRM) and CRO departed, but **~100 staff across 26 countries** including a large India org — a textbook Rippling Global/EOR pain point for a small HR team. Lead with global payroll/EOR.

### 4. Autobooks — 🔥 STRONG
Detroit fintech embedding SMB invoicing/payments inside bank platforms. **$40M growth investment (Runway, May 2025) plus two acquisitions in 12 months** (Allied Payment Network, MinuteLender) — meaning a multi-state, multi-entity workforce being stitched together right now, likely across 3 payroll systems. Best timing trigger in the list: lead with M&A/entity consolidation.

### 5. MultiAd — ❌ DISQUALIFY
Defunct as independent entity: acquired by SGS International, then its Kwikee asset sold to Syndigo (2020). multiad.com redirects to syndigo.com. HR runs through Syndigo corporate. Remove from CRM.

### 6. Litmus — ❌ DISQUALIFY
Acquired by Validity (Apr 2025) and being folded into its platform; HR/payroll consolidating into Validity's stack. Dead as a standalone buyer.

### 7. Bio-Optronics — ❌ DISQUALIFY
Acquired by Advarra (PE-backed, 1,000+ EE) in March 2021. HR/payroll consolidated into Advarra's enterprise stack. Remove from CRM.

### 8. Io.net — 🔥 STRONG
Independent. Decentralized GPU cloud for AI compute; $40M raised (Hack VC/Solana Labs/OKX), new CEO installed Apr 2025, fresh product launches through early 2026. ~90-person **fully remote, multi-jurisdiction workforce** with no visible Head of People or HR roles — classic fit for unified HR/IT/global payroll plus device management for remote staff. Caveat: crypto-sector volatility.

### 9. Fishbowl — ❌ DISQUALIFY
Acquired by Glassdoor (Recruit Holdings) in Sept 2021; now "Fishbowl by Glassdoor." No independent HRIS buying decision exists.

### 10. Forj — ✅ GOOD
Independent, Milwaukee, ~60 EE, $28M raised. Member-experience platform for associations — itself **stitched together from 3 companies** (Web Courseworks merger, Mobilize acquisition) with staff across 4 continents; new CFO and CRO hired for growth. Likely fragmented HR/payroll post-M&A — strong consolidation pitch. Slower hiring tempo keeps it at GOOD.

### 11. FundGuard — ✅ GOOD
Independent, 177 EE. AI investment-accounting platform; **$100M Series C (Mar 2024, ~$400M valuation)** with offices in NY, Boston, London, Toronto, and Tel Aviv. Strong global payroll/EOR + US HRIS story. Caveats: Israeli HQ may mean the people decision-maker sits in Tel Aviv and local payroll vendors are entrenched; hiring tempo moderate.

### 12. Kriptos — ⚠️ WEAK
Operating but partially stale record: real HQ is Quito, Ecuador (~34 actual EE vs. 67 in CRM); LatAm-centric banking customer base, no funding since 2022, no hiring momentum. Low likelihood of a US HRIS purchase — deprioritize.

### 13. ThinkCERCA — ✅ GOOD
Independent, Chicago, ~55 EE. K-12 literacy platform with new gen-AI grading features. Remote-friendly with distributed staff and part-time/contract scorers in multiple states — real payroll/compliance pain. No visible People leadership, likely greenfield HRIS. Tempered by no new funding since 2017 (budget sensitivity).

### 14. Highway.ai (MBS Highway) — ✅ GOOD
Operating; CRM context: this is **MBS Highway**, rebranded "Highway" after acquiring ListReports (2023). Mortgage/real-estate intelligence SaaS, ~54 EE across **3 continents**. Angle: Rippling Global/EOR plus consolidating two merged entities onto one system. Stable rather than high-growth.

### 15. Territorium — ✅ GOOD
Independent EdTech (San Antonio + Monterrey + Bogotá), 11M users in 15 countries, UT System partnership. US+Mexico+Colombia footprint is a textbook Rippling Global/EOR pitch. Caveats: much of the 81 EE likely sits in LatAm entities; only ~$4.4M raised.

### 16. Verivo Software — ❌ DISQUALIFY
Defunct — assets acquired by Appery/Exadel in **2015**. Website dead, LinkedIn page a relic. Purge this record.

### 17. BlueLabs — 🔥 STRONG
Independent DC analytics firm (Obama-campaign data alumni), ~87 EE and growing: recent senior hires (MD CPG Feb 2026, Head of Data Science), ~15 open roles via Greenhouse, distributed/remote staff. **Has a Director of People Operations and an existing unnamed HRIS to displace** — an identifiable, HR-aware buyer. Top-tier call.

### 18. Origin AI — ❌ DISQUALIFY
Acquired by ADT for **$170M cash in Feb 2026** (confirmed via SEC 8-K). Team being absorbed into ADT's enterprise stack. Remove from pipeline.
