---
name: rank-leads
description: Rank sales-lead accounts in a CSV out of 100 for Rippling fit using ICP scoring, web-verified intent/buying signals, HR contact presence, and US contactability. Use when the user uploads or references a leads/accounts CSV and wants leads scored, sorted, prioritized, or a top-N call list. Args - path to the CSV, optionally how many top leads to deep-research (default 30).
---

# Rank Leads

Score every account in a leads CSV out of 100 and produce a verified call-priority list. The workflow has two phases: **programmatic base scoring** of all rows, then **web verification** of the top N (default 30, or as the user specifies), because CRM data is unreliable — in past runs, ~30% of even top-scoring records were acquired companies, defunct entities, student clubs, or phantom LinkedIn pages.

## Phase 1 — Base score (all rows)

Run `score_leads.py` in this skill's directory: `python3 score_leads.py <input.csv> <output.csv>`. It handles flexible column names and writes a ranked CSV. If the CSV's columns don't map (script prints unmapped warnings), read the script and adapt the column-mapping dict at the top, or score inline with pandas following the same rubric.

Scoring rubric (100 pts):
- **Employee-size fit, 40 pts** — Rippling sweet spot 50–250 EE = 40; 25–50 = 32; 250–500 = 30; 10–25 = 18; 500–1000 = 15; <10 = 8; >1000 = 5. Watch for garbage counts (school districts at 6,000 "employees", 1-person shells).
- **Industry fit, 30 pts** — High (28–30): software, IT services, fintech, adtech, biotech/pharma, security, staffing, consulting, telecom — distributed knowledge workers, multi-state payroll, device-management needs, no entrenched enterprise HRIS. Medium (18–20): construction, manufacturing, healthcare, real estate, hospitality, legal — real payroll pain, hourly+salaried mix. Low (8): schools, religious institutions, government, banks, nonprofits — entrenched vendors, procurement friction.
- **Existing CRM tier, 20 pts** — if the CSV has a fit-tier column: Tier 1 = 20, Tier 2 = 14, Tier 3 = 7, Tier 4 = 0. If absent, redistribute weight to size/industry.
- **Reachability, 10 pts** — LinkedIn URL present (6), website (2), LinkedIn company ID (2).

Categorize: A – Hot ≥85, B – Strong fit ≥70, C – Nurture ≥55, D – Low priority <55.

## Phase 2 — Web verification of top N

Fan out background research agents (general-purpose, `run_in_background: true`, ~5–6 companies each, launched in one block) over the top N rows. Give each agent the company name, EE count, industry, city/state, website, and LinkedIn URL, and have it determine per company:

1. **STATUS** — still independently operating? Acquired, merged, rebranded, defunct, student org, or phantom record? Flag name/domain mismatches (account name pointing at a different company's site). This kills ~30% of records.
2. **INTENT / BUYING SIGNALS** — funding rounds (fresh capital = budget), M&A activity (multi-entity payroll consolidation pain — the single best trigger), new C-suite hires (especially a new CPO/CFO — decisions get revisited), hiring volume on job boards, layoffs (negative), product launches/expansion.
3. **HR SIGNALS** — named HR/People leadership (CPO, Head of People, HR Director), HR roles currently being hired (an HR-function build-out is the classic HRIS re-evaluation moment), incumbent HRIS/payroll stack hints (careers portal domain often reveals it: recruiting.paylocity.com → Paylocity; also ADP, Gusto, BambooHR, Workday mentions in postings).
4. **US CONTACTABILITY** — where do the decision-makers physically sit? A US HQ can be a facade: check exec locations (CEO in Sydney, HR team in Bengaluru = unworkable for a US rep). Offshore-heavy delivery is fine if corporate G&A is US-based — it's even a Rippling Global selling point.
5. **VERDICT** — STRONG / GOOD / WEAK / DISQUALIFY with rationale.

Budget agents to ~3–5 searches per company; instruct them to bail fast on clearly dead records and to return one markdown section per company plus sources.

## Phase 3 — HR contact sweep (verified survivors)

For companies verdicted STRONG/GOOD, run agents to find named, current HR/People contacts. LinkedIn blocks direct fetching — search instead via `site:linkedin.com/in "<company>" HR OR "people operations"` and aggregators (ZoomInfo, RocketReach, TheOrg, LeadIQ, ContactOut snippets) plus company team pages. Rules learned the hard way:
- Aggregator data lags LinkedIn by 6–18 months — always note confidence and flag "verify before emailing" for aggregator-only names. Confirm the person is CURRENT, not "former".
- A company's own website is the gold-standard source.
- If no HR title exists, find who owns payroll instead (CFO/Controller/Office Manager) — at <60 EE that's usually the buyer anyway, and "no HR team" is a greenfield selling point, not a disqualifier.
- A *vacant* HR seat (leader recently departed) at a growing company is a timing signal, not a dead end.

## Deliverables

1. **Scored CSV** — all rows ranked, with columns: rank, lead_score, score breakdown, category, plus for researched rows: `web_verdict`, `web_notes`, `us_contactability`, `hr_contacts`. Demote verified-dead records to category `X - Disqualified`.
2. **REPORT.md** — TL;DR table of category counts, methodology, per-company deep-dive sections with verdict emoji (🔥 STRONG / ✅ GOOD / ⚠️ WEAK / ❌ DISQUALIFY), a final call-priority list, CRM data-quality flags found, and recommended outreach angles per segment.
3. **hr_contacts.csv** — Company, HR Presence, Contact Name, Title, Location, Confidence, Outreach Note.

Send the files to the user with SendUserFile and commit/push if working in a repo. Lead the summary with the top-5 call list and any dead-record findings.
