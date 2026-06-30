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
| S1 | STANDARDS.md + LINT roster | ✅ done | committed ce6b5cd |
| S2 | IA folder restructure + aliases | ✅ done | committed e3f37ca; 44 moves, 0 broken links |
| S3 | Platform/nav/UX + components | ✅ done | nav b713b2b + components 09cdca8; build ok. S9 flags: CaseBrowser live render, data-island scaling, slug-casing deep-link check |
| S4 | Case pages (BIRAC) + index | ⏳ in progress | 262 pages, serial-CL batches of ~15; batch tracker below |
| S5 | Missed-case ingest + concordance | ⏳ blocked(S4) | borderline → USER PAUSE |
| S6 | Doctrine/narrative reformat | ⏳ blocked(S5) | caretaking split, Garrity page |
| S7+S8 | Research pages + glossary wiring | ⏳ blocked(S6) | anchorize-then-wire |
| S9 | Verification + release gate | ⏳ blocked(S7+S8) | STOP before publish |

## S4 batch tracker (262 pages, idx order, ~15/batch → ~18 batches; serial CL ONE at a time)
- Resumable: each batch updates `S4-worklist.json` status (pending→authored|escalated); skip already-authored. Commit after each batch.
- batch 1: idx 1–15 — ✅ committed 133fcab (15 pages, 0 escalations, ~50 CL calls, no throttle; Gant spot-check = instructor-grade)
- batch 2: idx 16–33 — ✅ committed b50167e (18 pages, 0 escalations, 42 CL calls). Caveat: Boyd "limited" call to reviewer-confirm; provisional roles reconcile in S6.
- batch 3: idx 34–53 — ✅ committed (20 pages, 0 escalations, 49 CL calls). Caveats: Coolidge limited→Horton; Carroll/Devenpeck paragraph-pinpoints; Patel/Herlth caption normalization.
- batch 4: idx 54–73 — ✅ committed (20 pages, 0 escalations, 48 CL calls). Jardines=856347; Fernandez↔Randolph N4 coherence tagged both pages (D5).
- batch 5: idx 74–93 — ✅ committed (20 pages, 0 escalations, 51 CL calls). Gates=PC anchor; Herring US-pinpoint cross-confirmed; parallel_cite left blank where unconfirmed.
- batch 6: idx 94–113 — ✅ committed (20 pages, 0 esc, 36 CL calls). Jones(1960) overruled→Historical; Pringle=131150; corrected 2 CL OCR artifacts; SR-5 concordance bonus (Lo-Ji).
- batch 7: idx 114–133 — ✅ committed (20 pages, 0 esc, 29 CL calls). Michigan v. Jackson L6-resolved→opinion 111622, overruled→Historical (spot-checked = excellent); Miranda=107252; Monroe v. Pape limited.
- batch 8: idx 134–153 — ✅ committed (20 pages, 0 esc, 47 CL calls). D5 coherence: Montejo↔Jackson, Belton limited→Gant, Olmstead overruled→Katz, Elstad limited→Seibert all align.
- batch 9: idx 154–173 — ✅ committed (20 pages, 0 esc, ~69 CL calls). Riley=2680439; Saucier limited→Pearson; People v. Hughes state-high→Persuasive-state.
- batch 10: idx 174–193 — ✅ committed (19 pages + idx 177 skipped, 0 esc, ~47 CL calls). L3 traps caught (Mansor cluster→wrong doc, resolved). **SR-5 finding:** Mitcham prior="independent-source" vs live="inevitable discovery" → authored to LIVE; flag for S5/S9 concordance.
- batch 11: idx 194–213 — ✅ committed (19 pages + idx 212 skipped, 0 esc, ~50 CL calls). N2 corrections (August/Basher → Binding in-circuit). **N1 findings for S6/gate:** Anchondo (ratio=SITA, homed Auto-Exc) + Braxton (ratio=inevitable-discovery, homed SITA) — re-home decision.
- batch 12: idx 214–233 — ✅ committed (20 pages, 0 esc, ~80 CL calls). Survived ~12min CL MCP outage (502s, not throttle) + recovered. L3 trap caught: Gastiaburo URL→unrelated case, resolved. Leon, Matlock, US v. Jones 2012.
- batch 13: idx 234–253 — ✅ committed (19 pages + idx 252 skipped, 0 esc, ~67 CL calls). Splits flagged inline (Touset↔Cotterman, Tuggle); Sandoval lexicon fix; Morton N1 (ratio=good-faith, homed Plain View). **CONFIRMED: Thornton NOT in worklist → S5 MUST ingest (class-2 miss); Gant/Belton refs dangle until then.**
- batch 14: idx 254–265 — ✅ committed (12 pages, 0 esc, ~37 CL calls). Weeks, Wong Sun, Whren, Warden v. Hayden, Houghton.
- **✅ S4 GENERATION COMPLETE: 262/262 case pages, 0 escalations, no throttle.** All needs_page=true → authored; pending = idx 177/212/252 (flagged captions, correctly page-less).
- S4 wrap-up: ⏳ Case Index regen (R10) + lint baseline + build validation, then free structural gate (deep legal re-verify deferred to S9 SR-1, to avoid redundant CL).

### S4 findings carried to S5/S6/S9 (gate)
- **S5 class-2 ingest:** Thornton v. United States (Belton/Gant companion; dangling refs).
- **N1 re-home decisions (S6/gate):** Anchondo (ratio=SITA, homed Auto-Exc); Braxton (ratio=inevitable-discovery, homed SITA); Morton (ratio=good-faith, homed Plain View via concurrence dicta).
- **SR-5 concordance findings:** Mitcham (prior=independent-source vs live=inevitable-discovery — authored live).
- **Pinpoint provenance to spot-check at S9/D8:** slip-op + S.Ct.-only + paragraph-pinpoint cases (Carpenter, Riley, Saucier, Torres, Touset, Strieff, Mansor, et al.) — verbatim-confirmed; only the page provenance is reporter-derived in some.
- Note: verified-cases-catalog.json holds only key/cite/url (no holdings) → generation was live-derived (strong SR-1). Richer prior holdings for S5 Thread-P are in prior-manifests/spec/*.spec.md.
- pinpoint-pagination caveats to revisit at gate/S9: Gant star-pag; Bailey/Berghuis slip-op; Benn paragraph-nums (idx 8/12/13/14)

## Artifact locations
- Orchestration: `_overhaul/ledger/` (this file, `cl-calls.log`).
- S5 coverage: `_overhaul/coverage/` (missed-cases, omissions, borderline, thread-P, concordance, prior-reconciliation).
- S9: `_run/` (S9-LEDGER.json, assertion-inventory.json, thread-P.json, s9-concordance.json, findings/adjudications, FINAL-S9-REPORT.md).
- Escalations: `_review-needed/{cases,coverage}/<slug>.md`.
- Lint scripts: `scripts/lint/`.

## CL reference (validated by probe 2026-06-30)
- Tier NEW (≥20/min); pace <20/min (~1 call/3.2s); cached opinion reads are free.
- Carpenter v. United States (2018): cluster 4510032, lead `opinion_id` 4287285, url `https://www.courtlistener.com/opinion/4510032/carpenter-v-united-states/`.

## S4 facts (from Case Index)
- Case Index: 267 data rows; **261 carry a CL opinion URL → 261 case pages to generate** (S4 target). ~6 flagged captions (no CL URL) get NO page (R1: flagged exception rows).
- Columns: Case | Holding | Good law | Home page(s) | CourtListener. Good-law blank = "good" convention (N13 will fill explicit status).
- Worklist: `_overhaul/ledger/S4-worklist.json` (bootstrap). Collisions: `_overhaul/ledger/S4-collisions.md`.

## Decision log (consequential calls, with rationale)
- **2026-06-30 · S4 ∥ S3 parallelization.** S4 generation is file-disjoint from all of S3 (S4 writes content/cases + Case Index + scripts and is the only CL user; S3 writes quartz/ + category stubs). So S4 runs in PARALLEL with S3-components — the serial-CL lane is internal to S4; S3 is free/no-CL. The S4-blockedBy-S3 task dep is therefore advisory only; S4 needs only content/cases/ (created in S2) + the probe (done).
- **2026-06-30 · S4 batch pipeline.** 261 cases generated via SEQUENTIAL serial-CL batch sub-agents (~20/batch, one CL lane at a time — never parallel CL, L4). Each batch: verify identity (cluster→opinion L3) + good-law (analyze_citations batched) + verbatim pinpoint quotes (search_document) → author BIRAC page → checkpoint S4-worklist.json status. Resumable. find→adjudicate→fix gate (review free/parallel) runs after generation; needs_cl adjudication back on the serial lane.
- **2026-06-30 · Baseline carry-forward.** Prior FINAL-QA working tree (modified Curtilage/Miranda-Waiver/Special-Needs/index + new Recalibration & Third-Party pages) carried onto the branch as the canonical `content/` start state (U6-S9). Dogfood/backup junk (`idb-dogfood/`, `app.js.bak`) gitignored.
- **2026-06-30 · S2/S3 split.** Per EXECUTE order: S2 = physical folder restructure (git mv, stems stable, aliases); S3 = Explorer/SCSS/components. Caretaking split + Garrity page CONTENT deferred to S6 (content authoring); S2 only moves the existing combined caretaking file into 7a and S6 splits it.
