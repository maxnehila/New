# PRD — Lead Tracker

**Version:** 0.1 (draft for review) · **Date:** June 12, 2026 · **Owner:** Max Nehila
**Status:** 🟡 Awaiting approval — do not begin build until this document is signed off.

---

## 1. Problem statement

Max is a Rippling sales rep working lead lists exported from Salesforce as CSVs. His company does not permit Salesforce integrations with external AI tools, so account research, ranking, and enrichment happen outside the CRM (via the `rank-leads` Claude skill in this repo). Today the output lives in static CSVs and a markdown report, which means:

- No way to **search** an account and instantly see its ranking, why it ranked there, and its links while working a call block.
- No way to track **which accounts have been worked**, what happened, or what to do next — re-reading a CSV row is not a workflow.
- No visibility into **daily/weekly productivity** against a personal "accounts worked" KPI.
- Notes end up scattered (or back in Salesforce, where the enrichment context isn't).

## 2. Goal

A lightweight personal web app — effectively a research-enriched working layer on top of CSV exports — where the user can upload account lists, search and view ranked accounts with reasons and links, work accounts through a simple status pipeline with timestamped notes, manage follow-ups and tasks, and track progress against a self-set daily KPI.

**Explicit non-goals (v1):**
- No Salesforce/CRM integration of any kind (company policy).
- No email sending, sequencing, or dialer functionality.
- No team visibility/manager dashboards — data is private per user.
- No in-app web research/enrichment — enrichment continues to come from Claude runs producing enriched CSVs that get uploaded.
- No mobile app (responsive web is sufficient).

## 3. Users

- **Primary:** Max (single user at launch).
- **Secondary (later):** 1–5 coworker reps, each with a fully private workspace (own uploads, notes, KPIs). No shared data in v1; sharing is a possible v2.

## 4. Core user stories

| # | As a rep, I want to… | So that… | Priority |
|---|---|---|---|
| U1 | Upload a Salesforce CSV export (raw or Claude-enriched) | my account list is in the app without any integration | P0 |
| U2 | Have every account scored 0–100 automatically with a visible breakdown | I know who to call first and why | P0 |
| U3 | Re-upload a fresh export without losing my notes/statuses | I can refresh data weekly | P0 |
| U4 | Search accounts by name/industry/state and filter by category, status, verdict | I can find any account in seconds mid-workflow | P0 |
| U5 | Open an account and see score + reason, description/verdict, HR contacts, website + LinkedIn links | everything needed for a call is on one screen | P0 |
| U6 | Set an account's status (pipeline) and log timestamped notes | I have a record of every touch | P0 |
| U7 | Set a daily "accounts worked" target and see today/week progress, pace, and streak | I hold myself to my KPI | P0 |
| U8 | Set follow-up dates on accounts and see what's due today | nothing falls through | P1 |
| U9 | Keep a standalone to-do list (optionally linked to accounts) | non-account tasks live in the same tool | P1 |
| U10 | Get an auto-built Daily Queue (due follow-ups + best untouched accounts, sized to my target) | I open the app and just work down a list | P1 |
| U11 | Log in with a magic link from any device | no password management; coworkers can be added later | P0 |

## 5. Functional requirements

### 5.1 Authentication & tenancy
- Supabase email magic-link (OTP) auth. No passwords.
- Every row of user data is scoped to the authenticated user via Postgres row-level security. One user can never read another's data.
- Unauthenticated visitors are redirected to /login.

### 5.2 CSV upload & merge
- Accepts CSVs with flexible column names (the app maps common aliases for: account name, employees, website, industry, tier, LinkedIn URL, city, state).
- **Two CSV flavors, one path:** raw Salesforce exports get base-scored in-app; Claude-enriched CSVs additionally carry `web_verdict`, `web_notes`, `hr_contacts`, `us_contactability`, which are imported verbatim.
- **Merge rules (the load-bearing feature):** match on normalized account name (+ website as tiebreaker).
  - Existing account → update firmographics, recompute base score. **Never overwrite** status, follow-up date, or notes. Enrichment fields only overwritten when incoming value is non-empty.
  - New account → insert.
  - Account absent from upload → flag `missing from last upload` (never auto-delete).
- Post-upload summary: N added / N updated / N flagged missing / N skipped (unparseable).

### 5.3 Scoring & ranking
- Identical rubric to the `rank-leads` skill (single source of truth documented there): size fit /40, industry fit /30, CRM tier /20 (redistributed if absent), reachability /10. Categories: A ≥85, B ≥70, C ≥55, D <55.
- Every account displays a one-line human-readable **ranking reason** (per-dimension breakdown), plus the deeper Claude enrichment (verdict + notes) when present.

### 5.4 Account workflow
- Status pipeline: `Untouched → Worked → Contacted → Meeting → Disqualified` (single status per account, freely movable).
- Timestamped, append-only notes per account (newest first). Notes are never modified by uploads.
- Optional follow-up date per account.
- **KPI event:** the first status change of the day on an account (or an explicit "Worked ✓" action) records that account as worked today. Working the same account twice in one day counts once.

### 5.5 KPI dashboard
- User-set daily target (default 20).
- Shows: worked today vs target (progress bar), week-to-date total (Mon–Sun), pace vs expected for the weekday, and streak of consecutive workdays hitting target.
- Weekends excluded from streak/pace math.

### 5.6 Tasks
- Standalone to-dos: title, optional account link, optional due date, done flag. Overdue highlighted.
- **Daily Queue view:** (1) accounts with follow-up due ≤ today, (2) open tasks due today, (3) top-ranked Untouched accounts filling remaining capacity up to the daily target.

### 5.7 Search & browse
- Account table: search-as-you-type on name/industry/state; filters for category, status, verdict, contactability; sortable by score (default), name, employees.
- Performance target: smooth with 5,000 accounts.

## 6. Data privacy & constraints
- Lead data is company-sensitive: hosted on the user's own free-tier Supabase project (user controls the data) and a Vercel deployment on the user's account. No third-party analytics. No data sent anywhere except Supabase.
- The app must function with zero connection to Salesforce or any company system. Input: CSV files only.

## 7. Success criteria
- Upload→ranked list in under 30 seconds for a 1,200-row CSV.
- Re-upload preserves 100% of statuses/notes (acceptance test required).
- Finding any account and opening its detail: ≤ 3 interactions.
- Daily workflow (open app → work queue → log notes → KPI updates) requires no CSV/file handling at all.

## 8. Delivery plan (agreed sequence)
1. **PRD** — this document. ⬅️ *you are here; approve or edit before anything is built*
2. **Backend** — Supabase schema + RLS policies + migration SQL, the scoring module, CSV parse/merge logic, and data-access layer. Delivered with tests/verification before any UI.
3. **Design spec** — page-by-page wireframe descriptions, component inventory, interaction and visual design decisions for sign-off.
4. **Frontend build** — implement the design spec against the backend.
5. **Deploy** — README runbook; user creates Supabase project + Vercel deployment (the only steps requiring the user's accounts).

## 9. Open questions for the user
1. Account volume: is ~1,200 per upload typical, or should we design for much larger lists?
2. Should "Disqualified" accounts count toward the daily worked KPI? (Current assumption: yes — dispositioning is work.)
3. KPI weekend handling: assumption is weekends don't break streaks. Correct?
4. Any company naming/branding constraints for an app touching lead data (e.g., must it avoid the word "Rippling" in the repo/app name)?
