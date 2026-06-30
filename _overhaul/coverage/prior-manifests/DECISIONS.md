# CSSI Full Build-Out — Self-Interview & Decision Log

*Run start: 2026-06-25. Orchestrator-adjudicated. Each consequential call: options → red-team → steel-man → adjudication + rationale. Reversible via timestamped backup `backup-vault-20260625-122349`.*

---

## D-0. Reuse base established (fact, not decision)
- 31 existing verified pages (Days 1–3); 19 citation manifests (manifest-grade: proposition + verbatim confirmed quotes + good-law notes); 39 flashcard decks (1176 cards), incl. 14 "Name That Case" decks from yesterday spanning Miranda/confessions, 6A counsel, eyewitness ID, entrapment, special-needs/border, warrants, threshold.
- **Deterministic catalog built**: 327 distinct verified case-keys, 322 with CL URLs, 99 with manifest-grade verdicts. → `_run/verified-cases-catalog.json`. **Consequence: the full build-out is mostly assembly + verification of already-verified law, not net-new research.** Net-new CL work ≈ today's notes + good-law re-checks + a handful of build-out gap-fillers.

---

## D-1. Scope boundary — which adjacent areas are IN
**Question:** The brief says "build out the ENTIRE app … not just what class has reached," and mine yesterday's research (Miranda, 6A counsel, eyewitness ID, entrapment, special-needs/border). `_conventions.md` (Day-1 era) said "do not balloon into not-yet-covered material." These conflict.

**Options:** (A) Honor old convention — only 4A search/seizure + today's notes. (B) Full federal criminal-suppression build-out incl. the already-researched 5A/6A/ID/special-needs/warrants buckets. (C) (B) minus entrapment (a substantive defense, not a suppression doctrine).

**Red-team (B):** Risks scope creep, blurring a *suppression* course into general crim-pro; entrapment isn't suppression; 5A/6A could swamp the 4A core.
**Steel-man (B):** The brief is an explicit, dated override of the Day-1 convention ("FIRST ingest … THEN build out the ENTIRE app"). The research is already done and CL-verified yesterday — *not* building the pages wastes it and leaves the "Name That Case" game pointing at non-existent pages. Miranda is in *today's* notes. Confessions, 6A-counsel-at-interrogation, and eyewitness ID are all **suppression** topics (suppress statements / IDs) — squarely a search-&-seizure-instructor's remit. Border/special-needs/warrants are core 4A.

**ADJUDICATION → B (full build-out), entrapment IN but clearly framed.** Scope = federal criminal-suppression in the broad sense: everything that gets evidence (physical, statements, identifications) admitted or suppressed, plus the standing/procedural doctrines around it. Entrapment is included because (i) the deck exists, (ii) it completes the "Name That Case" game, but it is **labeled a substantive defense, not a suppression doctrine**, and kept compact. Update `_conventions.md`'s "Day-1, don't balloon" note to reflect this run's mandate (additive note, not a deletion). Federal/state guardrail is unchanged and absolute.

---

## D-2. Page model — doctrine pages + a Cases glossary (both)
**Question:** Doctrine pages only, or also a master Cases index/glossary?

**Red-team (both):** A cases index duplicates the per-page Key-cases tables and risks drift.
**Steel-man (both):** With ~45 pages and 300+ cases, a single **Cases index** (one row per case → cite, one-line holding, CL link, the page(s) it anchors) is the natural home base for the Kahoot-style "Name That Case" study and prevents "which page is Gant on?" thrash. It's generated, not hand-maintained, so drift is controlled. The doctrine pages remain the source of truth; the index is a router.

**ADJUDICATION → Both.** Keep the doctrine-page model (the spine). Add **`Case Index`** (auto-generated from manifests in Phase 6, deterministic) as a navigational glossary — every verified case, its cite, one-line holding, good-law flag, CL link, and home page(s). Keep `Common Legal Terms` as the *terms* glossary (distinct from the *case* index).

---

## D-3. Taxonomy / buckets + naming conventions
**Decision:** Eight top-level buckets (MOC sections). Page names are **noun-phrase doctrine titles**, Title Case, no "The " prefix except where idiomatic (`The Exclusionary Rule`, `The Federal Court System` stay — they have study-progress + flashcard ids). New pages get clean slugs (`kebab-case` of title). Buckets:
1. **Foundations & history** — Common Law Origins.
2. **Legal system, research & reference** — Federal Court System; Legal Research & Citations; Common Legal Terms; **Case Index** (new).
3. **The Fourth Amendment — framework & analysis** — Framework; Analysis Checklist; Two Definitions of Search; CREW; **Probable Cause & Reasonable Suspicion** (new, the standards-of-proof page).
4. **Protected areas & threshold** — Curtilage; Abandonment.
5. **Seizures of persons & force** — Seizure of the Person; Terry Stops; Use of Force; **Collective Knowledge / Fellow-Officer Rule** (new).
6. **Recognized exceptions to the warrant requirement** — Arrest in the Home; Community Caretaking & Emergency Aid; Consent; Plain View; Automobile; Search Incident to Arrest; Traffic Stops; **Knock and Talk** (new); **Special Needs & Administrative Searches** (new); **Border Searches** (new); **Securing the Scene: Detention, Protective Sweeps & Freezes During Warrant Execution** (new).
7. **The warrant requirement** — **The Warrant Requirement** (new: PC, particularity, neutral magistrate, Franks, knock-and-announce, anticipatory).
8. **Remedies, standing & accountability** — Exclusionary Rule; **Standing to Challenge a Search** (new, promoted out of Exclusionary Rule); §1983 & Qualified Immunity; Brady & Giglio.
9. **Confessions & identifications (5A/6A — suppression of statements & IDs)** — **Due-Process Voluntariness** (new); **Miranda & Custodial Interrogation** (new); **Miranda: Waiver & Invocation** (new); **Sixth Amendment Right to Counsel** (new); **Eyewitness Identification** (new).
10. **Substantive defenses (adjacent)** — **Entrapment** (new, labeled defense-not-suppression).
11. **Instructor maxims & practical habits** — Three Golden Rules; Instructor Development; CREW.

(Final bucket count/order finalized in Phase 2 IA-SPEC; this is the working taxonomy.)

---

## D-4. Flashcard storage — IndexedDB w/ lossless migration
**Decision (from brief, confirmed):** Migrate study component `app.js` from localStorage to **IndexedDB**. Migration MUST be lossless: on first load, detect the existing localStorage FSRS store, copy every record into IDB keyed by card `id`, preserve scheduling state, then read/write IDB thereafter (leave localStorage intact as a fallback/safety net; do not delete it). Card ids stay stable so progress migrates by id. Keep existing UX. Dogfn headless before publish.
**Red-team:** IDB is async — risk of races / partial migration / quota. **Mitigation:** one-time guarded migration with a `migrated` flag in IDB; keep localStorage as read fallback; feature-detect IDB and fall back to localStorage if unavailable. Dogfood: seed old store → load → verify progress preserved → grade → reload → persisted.

---

## D-5. "Shepardize" depth + circuit-split policy (two-key rule)
**Decision:** Every asserted case must pass the **two-key rule**: (1) existence + proposition + verbatim pinpoint quote CL-verified, AND (2) good-law check (not overruled/abrogated/superseded; treatment recorded as `good|criticized|limited|abrogated|overruled|unknown`).
- **Reuse:** manifest-grade cases (99) already satisfy key-1 (and most note treatment). Deck-verified cases (existence + holding + CL URL) satisfy existence; for any such case **asserted with a quote on a page**, the serial verifier confirms the verbatim quote + good-law. A page may state a holding without a verbatim quote, but the good-law check is still required before assertion.
- **Good-law depth:** for each asserted case, check subsequent treatment for overruling/abrogation (e.g., *Belton*→*Gant*; *Sanders*→*Acevedo*; *Chimel*-as-applied-to-vehicles→*Gant*; *Robbins*; watch *Caniglia* narrowing *Cady*; *Lange* on misdemeanor pursuit). Negative treatment is recorded and surfaced; overruled cases appear only as labeled history.
- **Circuit splits:** flag explicitly with circuits named; never present one circuit as nationwide binding. The **border-device forensic-search split** (e.g., 9th *Cotterman*/*Cano* vs 11th *Touset*) is wanted and labeled. Circuit cases = persuasive.
- **CL throttle:** single serial lane; §3 protocol (tier probe, ≤20/min, STOP on old 5/min tier).

---

## D-6. Lossless flashcard consolidation rules
**Decision:** Consolidation is **lossless** — merge/dedupe **redundant** cards across decks but never drop a fact; if two cards overlap, keep the most complete and fold any unique detail into it. Constraints:
- **Card ids stay stable** (FSRS progress migrates by id). When merging two cards, keep the surviving card's id; never reissue an id that's in use.
- Align decks to the FINAL page slugs/case set (Phase 6 rename map drives `page`/`tags`). The "Name That Case" deck keeps its literal `page:"name-that-case"`/`topic:"Name That Case"` constants (one study filter) — only `tags` realign.
- Net effect on count: roughly flat-to-up (new pages add cards; dedupe trims true duplicates). No fact removed. Reviewer verifies against REVIEW-BRIEF.

---

## D-7. How today's notes fold into the IA
**Decision (routing — finalized in Phase 1/2):**
- Standing / Rakas / actual vs constructive possession / joint possession / willful blindness → **new `Standing to Challenge a Search`** (promoted from Exclusionary Rule; possession concepts as the "standing-via-possession" subsection, framed as the connexion between a possessory interest and a reasonable-expectation-of-privacy standing).
- Collective knowledge (vertical + horizontal) / fellow-officer rule → **new `Collective Knowledge / Fellow-Officer Rule`** (anchors: *Whiteley*, *United States v. Hensley*; vertical = order-to-act on another's PC, horizontal = pooled knowledge).
- House freezes / detain occupants / protective sweep / *McArthur*, *Summers*, *Muehler v. Mena*, *Buie*, *Payton* (enter-and-exclude), *Bailey*, SACO/*Conner* → **new `Securing the Scene: Detention, Protective Sweeps & Freezes`**.
- Knock-and-talk / *French v. Merrill* (1st Cir.) / *Kentucky v. King* / *Jardines* implied license → **new `Knock and Talk`**.
- Miranda / 3 C's (custody, interrogation) / *Rhode Island v. Innis* → **new `Miranda & Custodial Interrogation`** (+ the waiver/voluntariness pages per D-3 bucket 9).
- Instructor quality #4 "predict questions and confusions" → **append** to `Instructor Development`.
All new cases CL-verified through the serial lane before assertion.

---

## D-8. Loop & escalation policy
Any build↔fix loop ≤3 passes; unresolved → `_review-needed/<slug>.md` with the open issue. Ledger checkpointed after every sub-phase (resumable). All consequential routing/merge/rename calls surfaced in the final report.
