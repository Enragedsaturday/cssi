# CSSI Overhaul — Orchestration Ledger (resumable)

Thin-orchestrator state for the autonomous build (`_overhaul/wrappers/EXECUTE.wrapper.md`).
Governed by `docs/STANDARDS.md` (S1, SR-3). **Resume from this file, not from scratch.**

- **Branch:** `overhaul/build` (off `main` @ `abefdf3`; baseline commit carries prior FINAL-QA state + specs).
- **Canonical source:** `content/` (U6-S9). **Never run `redeploy.sh`** (retired vault→content sync).
- **CL discipline:** single serial lane (L4), concurrency-1; tier probed before CL work; STOP on old 5/min tier (RUNBOOK §3). Log: `_overhaul/ledger/cl-calls.log`.
- **Orchestration:** thin main thread holds ledger/specs/statuses only; all substantive work in fresh sub-agents; small on-disk hand-offs; find→adjudicate→fix role-separated; loop cap 3 → `_review-needed/`.
- **Decks:** frozen the whole overhaul (U5-S9). No `merge.py`/`make_apkg.py`. Page-derived rebuild is a SEPARATE later run.
- **Mandatory human pauses:** (a) S5 borderline sign-off; (b) final publish go-ahead (before push to `main`/Vercel prod).

## Phase status

| # | Phase | Status | Notes |
|---|---|---|---|
| 0 | Setup (branch, scaffold, ledger) | ✅ done | branch + dirs + task list created |
| — | CL tier probe | ✅ done | **TIER=NEW (≥20/min), MCP auth OK**, cluster→opinion gotcha validated → PROCEED |
| S1 | STANDARDS.md + LINT roster | ⏳ in progress | 2 sub-agents running (free / no-CL) |
| S2 | IA folder restructure + aliases | ⏳ blocked(S1) | git mv, stems stable, no deck work |
| S3 | Platform/nav/UX + components | ⏳ blocked(S2) | Explorer, SCSS, components |
| S4 | Case pages (BIRAC) + index | ⏳ blocked(S3,probe) | HEAVY CL serial |
| S5 | Missed-case ingest + concordance | ⏳ blocked(S4) | borderline → USER PAUSE |
| S6 | Doctrine/narrative reformat | ⏳ blocked(S5) | caretaking split, Garrity page |
| S7+S8 | Research pages + glossary wiring | ⏳ blocked(S6) | anchorize-then-wire |
| S9 | Verification + release gate | ⏳ blocked(S7+S8) | STOP before publish |

## Artifact locations
- Orchestration: `_overhaul/ledger/` (this file, `cl-calls.log`).
- S5 coverage: `_overhaul/coverage/` (missed-cases, omissions, borderline, thread-P, concordance, prior-reconciliation).
- S9: `_run/` (S9-LEDGER.json, assertion-inventory.json, thread-P.json, s9-concordance.json, findings/adjudications, FINAL-S9-REPORT.md).
- Escalations: `_review-needed/{cases,coverage}/<slug>.md`.
- Lint scripts: `scripts/lint/`.

## CL reference (validated by probe 2026-06-30)
- Tier NEW (≥20/min); pace <20/min (~1 call/3.2s); cached opinion reads are free.
- Carpenter v. United States (2018): cluster 4510032, lead `opinion_id` 4287285, url `https://www.courtlistener.com/opinion/4510032/carpenter-v-united-states/`.

## Decision log (consequential calls, with rationale)
- **2026-06-30 · Baseline carry-forward.** Prior FINAL-QA working tree (modified Curtilage/Miranda-Waiver/Special-Needs/index + new Recalibration & Third-Party pages) carried onto the branch as the canonical `content/` start state (U6-S9). Dogfood/backup junk (`idb-dogfood/`, `app.js.bak`) gitignored.
- **2026-06-30 · S2/S3 split.** Per EXECUTE order: S2 = physical folder restructure (git mv, stems stable, aliases); S3 = Explorer/SCSS/components. Caretaking split + Garrity page CONTENT deferred to S6 (content authoring); S2 only moves the existing combined caretaking file into 7a and S6 splits it.
