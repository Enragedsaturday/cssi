# SPEC S5 — Case Ingest / Coverage Completion

status: APPROVED
depends-on: [S1, S2, S4]          gates: [S6, S9]
last-updated: 2026-06-29

> Governed by `docs/STANDARDS.md` (S1, SR-3 supremacy). S5 **designs the method** to find every
> *officer-relevant* case the wiki is missing, **diagnose why each was missed**, generalize that
> failure into a search that surfaces the missed case's siblings, and **ingest** confirmed cases as
> **S4 case pages** homed per **S2**. S5 reads S2 §2.0/§6.3 (the scope contract) and the S4 case model;
> it **ingests into** that model and adds **no decks** (the deck rebuild stays deferred to EXECUTE/S9 per
> S4 · R11). S5 **designs**; it ingests no case now. Every new case is a **full-live-verify (SR-1)** event
> through the single serial CourtListener lane (L4), passed through the standing **find → adjudicate → fix**
> gate (L5). Where S5 research touches live law, **web discovers (L2), serial CL confirms (L3/L4)**.

---

## 1. Objective

Close the coverage gap to an **officer-practical** standard: (a) **diff** the source book's full I–XIII
case roster (the master candidate list) **against the live wiki** by **holding-identity** (not name string),
producing the **missed-case list**; (b) **diagnose each miss** with a fixed **"why-missed" taxonomy**, and —
the heart of the deliverable — turn each failure class into a **generalized search** that catches the missed
case's siblings (the instructor's "apply that logic to find the others"); (c) run a **bounded, expansive
progressive-research pass** (N12) per doctrine to add officer-relevant **clearly-controlling** non-book law
and annotate the most-relevant splits; and (d) **ingest** every confirmed, field-relevant case as an **S4
BIRAC case page**, homed per **S2** (placement-by-holding, N1), wired (N7), live-verified (SR-1), and folded
into the regenerated Case Index. Crucially, S5 keeps our prior research as a **separate, independent thread**
and runs the new pass **conclusion-blind** against it (**SR-5**): where the two threads **agree** the
conclusion is **double-verified**; where they **fundamentally disagree** the divergence is **escalated and
adjudicated against primary authority**; and a **no-regression floor** ensures **no case, circuit authority, or
split we already found is silently lost** (R12). The book is a **candidate pool, not a checklist** —
**field-relevance**, not book-membership, is the gate.

## 2. Scope

### 2.0 INGEST GATE — **[USER, U1-S5]** Officer field-relevance, not book-membership

A candidate case is **INGESTED** iff its holding governs one of:
- **(a) field police conduct** — search, seizure, stop, arrest, entry, frisk, pursuit, interrogation, use of
  force; *or*
- **(b) admissibility / suppression** — the exclusionary rule and its exceptions, standing, fruits, Miranda
  & voluntariness admissibility, identification admissibility; *or*
- **(c) the officer's civil / qualified-immunity exposure** for that conduct (§1983, *Bivens*-as-applied-to-
  police, QI, *Graham*/*Garner* force).

It is **EXCLUDED** (→ omissions register, R10) iff it is **purely prosecutor / defense / trial craft** with
no field-conduct or suppression hook: Confrontation-Clause analyst/testimonial rules, 5A immunity &
grand-jury practice, act-of-production privilege, charging/speedy-trial/sentencing mechanics, and the Book
XIII 1A/civil one-offs — **even when the book carries them**.

**One deliberate exception (U2-S5):** the **government-employee Fifth-Amendment / *Garrity*** cluster is
ingested as **CORE** on **audience-relevance** grounds (the students *are* officers; *Garrity* warnings bear
on them directly), though it is an employment/IA matter rather than field S&S. This **supersedes S2 §2.0's
OPTIONAL tag** for that one cluster (R11; §9).

**Borderline cases are not auto-decided (U1-S5).** Where the gate does not cleanly resolve, the case goes to a
**borderline sign-off list** for the user before it is ingested or dropped (R2).

This gate **refines** — does not reverse — S2 §2.0: it applies a **case-level field-relevance filter inside the
CORE Parts**, so the "missed-case" universe S5 closes is the **officer-relevant subset**, not "every CORE-Part
book case." (S2 already excluded the OPTIONAL tier from the missed-case count; S5 adds the per-case relevance
test S2's "officer-practical" spirit implied.)

### 2.1 In scope (S5 designs)
- The **ingest gate** (§2.0) and the **borderline sign-off** mechanism (R1, R2).
- The **diff method** — holding-identity reconciliation of the book roster + named-in-prose roster against
  the live wiki, misspelling-tolerant (L6), serial-CL-confirmed (L3/L4) (R3).
- The **"why-missed" diagnostic taxonomy** + the **class → generalized-search** table (R4; §6.2) — the core.
- The **coverage = union** definition (book ∪ named-in-prose ∪ **prior-research corpus** ∪ bounded frontier) (R5).
- The **dual-thread concordance verifier + no-regression guard** (SR-5 application): a conclusion-blind new
  thread reconciled against the frozen prior thread — agreement double-verifies, fundamental disagreement
  escalates (R12).
- The **progressive research protocol for coverage** (N12, web-first → CL-confirm, expansive discovery /
  controlling-only inclusion, splits annotated) (R6).
- The **ingest pipeline** (discover → verify → author S4 page → home per S2 → wire links → find/adjudicate/fix
  → regenerate index) (R7).
- The **decks-untouched** rule (R8), the **no-fabricated-cases** verification contract (R9), the **omissions
  register** (R10), and the **Garrity-as-CORE** cluster (R11).

### 2.2 Out of scope (owned elsewhere)
- The **case object, BIRAC template, frontmatter schema, slug/anchor scheme, Case-Index-as-generated** → **S4**
  (S5 ingests *into* this model; it changes none of it).
- **Doctrine-page brief-first reformat, the field framing (N9), the caretaking content split, case-table
  reformatting** → **S6**. S5 emits the **new case pages + link/row wiring**; S6 weaves them into the briefs.
- **Glossary wiring** → **S7**; **legal-research/citation pages** → **S8**; the **final exhaustive independent
  verification** → **S9** (S5's live-verify is the ingest installment of SR-1, re-confirmed by S9).
- **Standards / lexicon / the find→adjudicate→fix machine definition** → **S1** (S5 *uses* it).
- **Folder creation / `git mv` / Explorer + alias plumbing** → **S3**.
- **The flashcard-deck rebuild** → **EXECUTE/S9** (S4 · R11): S5 touches no deck.

---

## 3. Requirements (numbered, testable)

### R1 — The ingest gate (officer field-relevance) **[USER, U1-S5]**
Every candidate case carries an explicit **in/out verdict** decided by the §2.0 gate, with the governing
**reason-class** recorded. INGEST iff (a) field conduct ∨ (b) admissibility/suppression ∨ (c) officer civil/QI
exposure; EXCLUDE iff purely prosecutor/defense/trial craft. The **book section is a relevance *hint*, never
the test** — a case in a CORE Part that is purely trial craft is still excluded; a case in an OPTIONAL Part
that is squarely field-decisive is reconsidered (and, if genuinely so, surfaced via R2). The *Garrity* cluster
is the one audience-relevance inclusion (R11).
- *Check:* every candidate has an in/out verdict + a reason-class; no book case is silently unaddressed; a
  sample of EXCLUDED cases is genuinely trial-only and a sample of INGESTED cases is genuinely field-relevant.

### R2 — Borderline sign-off (no auto-decide on the 50/50s) **[USER, U1-S5]**
Candidates whose field-relevance the gate does **not** cleanly resolve are **not** decided by the agent. They
are written to **`_overhaul/coverage/borderline.md`** with: case · book section · the proposition · the
specific ambiguity (why it could be in or out) · a recommended disposition. The list is **surfaced to the user
for sign-off** before any borderline case is ingested or dropped; the user's call is recorded back into the
register (R10) or the missed-case list (§6.1).
- *Check:* every genuinely-ambiguous candidate appears once on the borderline list with a stated ambiguity;
  none is ingested or excluded without a recorded user disposition.

### R3 — Diff method: holding-identity reconciliation, not name-string **[L6, L3, L4]**
The missed-case list is produced by reconciling **two candidate rosters** against the **live wiki state** by
the **legal proposition each case stands for**, not by surface name match:
1. **Build the candidate pool.** (i) Extract the **book roster** — every case in the I–XIII TOC with its
   **section** (the doctrine the book teaches it under = a *homing hint*) and page. (ii) Extract the
   **named-in-prose roster** — every case **name appearing in existing doctrine-page text/holdings** but
   carrying **no row/page** (the N7 "named but never tabled" surface; e.g. *Kyllo* inside *Carpenter*'s
   holding; *Dunn* named in N3; *Ryburn v. Huff* and *Case v. Montana* named in S2 · R6 / N5). (iii) Extract the
   **prior-research roster into the frozen Thread-P conclusion set** — every case, **circuit authority**, and
   **split identifier** (with its prior holding/home/role/treatment) named in the **verified citation
   manifests** and the **41 prior per-page specs** (`…/CSSI/_run/spec/*.spec.md`). This is **Thread P** — the
   **reconciliation reference and no-regression floor** (R12 / SR-5), **withheld** from Thread N's blind
   discovery, never silently dropped.
2. **Normalize + match (misspelling-tolerant, L6).** Tolerate party-order, abbreviation, `v.`/`v`, reporter
   noise, and OCR/caption variants; match each candidate against (a) Case-Index rows, (b) existing
   `content/cases/*` pages, and (c) prose mentions — by **holding**, not just caption.
3. **Classify the disposition.** Each candidate resolves to **exactly one** of:
   `already-covered` (asserted in an index row / case page / prose with a page) · `confirmed-miss` (→ ingest,
   R7) · `excluded` (→ omissions, R10) · `borderline` (→ sign-off, R2).
4. **Confirm before "miss" or "fake" (L3/L6).** A `confirmed-miss` is only declared after the case's
   **existence + identity** is confirmed on CL (cluster → lead `opinion_id` resolved; **named case present in
   returned text**); a candidate that fails the full L6 escalation ladder (reporter cite → name/phonetic
   variants → proposition full-text → web → relocate) is recorded **UNVERIFIABLE** (no page; R9/R1-S4),
   **never** asserted and **never** silently dropped.
- *Check:* the candidate pool ⊎ partitions cleanly into the four dispositions (complete, no gaps/overlaps);
  matching is by holding (spot-check that a name-collision pair is **not** falsely merged — R4 class 5); every
  `confirmed-miss` has a CL identity confirmation logged before ingest.

### R4 — The "why-missed" diagnostic taxonomy → generalized search (THE CORE) **[N1, N7, N12]**
Every `confirmed-miss` is tagged with **≥1 diagnostic class** explaining *why* it was missed, and **each class
carries a generalized search** that surfaces the missed case's **siblings** — so a single miss becomes a net
that catches the others like it. The **seven classes** and their generalized searches are the **§6.2 table**;
the inclusion gate (R1) is applied to everything a generalized search surfaces. The classes:
1. **Out-of-prior-scope / section-never-mined** — a whole book section the prior curated build never
   harvested. *Generalized search:* enumerate the section's **full** roster; ingest the field-relevant
   remainder.
2. **Companion / progeny dropped** — one case of a doctrinal pair/line captured, its partner not
   (*Aguilar* without *Spinelli*; the third-party **pair** *Smith v. Maryland* + *United States v. Miller*
   behind *Carpenter*; *McNeely* without *Schmerber*; *Belton/Gant* without *Thornton*). *Generalized search:*
   for every captured anchor, pull the **canonical companion/progeny line** it is always taught with.
3. **Named-in-prose, never tabled (N7)** — discussed in a holding/brief but never given a row/page (*Kyllo*,
   *Dunn*, *Ryburn*, *Case v. Montana*). *Generalized search:* extract **every** case name in existing page
   prose; any without a page is a miss.
4. **Keyword-homing failure (N1)** — dropped or mis-filed because surface keyword ≠ holding (placement-by-
   holding). *Generalized search:* per doctrine, audit for cases whose **ratio** belongs there but were
   filed elsewhere or omitted.
5. **De-duped by name collision** — distinct cases sharing a short name collapsed into one (*Henry v. United
   States* ≠ *United States v. Henry*; multiple *Harris* / *Davis* / *White* / *Jackson*). *Generalized
   search:* for every short-name collision, confirm **each distinct holding** has its own page (S4 · R5
   year-suffix disambiguation).
6. **Too-recent / post-capture** — decided after the prior build or after the book went to print. *Generalized
   search:* a **date-bounded CL sweep** per doctrine for controlling law since last capture.
7. **Frontier-not-run (N12 Hop-2 skipped)** — controlling circuit/state or split-defining law on a live
   question never discovered. *Generalized search:* the **bounded progressive frontier pass** (R6) per
   doctrine — controlling-only inclusion, splits annotated.
- *Check:* every `confirmed-miss` carries ≥1 class tag; every class has a **runnable** generalized search; the
  §6.2 table is the execution's per-doctrine worklist.

### R5 — Coverage = the union (book ∪ named-in-prose ∪ bounded frontier) **[N12]**
The missed-case universe S5 closes is **(officer-relevant book cases ∪ officer-relevant named-in-prose cases ∪
officer-relevant prior-research-surfaced cases ∪ officer-relevant clearly-controlling frontier cases) −
(already-covered ∪ excluded)**. The book is the **spine** of the candidate pool, not its boundary; the
**prior-research corpus (R12)** is the **floor** it may not regress below; classes 6–7 and R6 extend it.
**Coverage completion is measured against this union**, with the **omissions register (R10)** accounting for the
complement so nothing is silently lost.
- *Check:* the diff partition + the frontier additions + the omissions register together account for **every**
  candidate; "done" is defined against the union, not the book alone.

### R6 — Progressive research protocol for coverage **[N12, S1 §3.F; USER U3-S5]**
Per doctrine (S2-tree order), research is **expansive in discovery, disciplined in inclusion**:
- **Expansive, progressive discovery — blind to the prior thread (SR-5).** Seed each doctrine from the
  **candidate pool** (book / named-in-prose / frontier, R3) **plus** the foundational SCOTUS authority the
  doctrine rests on (S1 §3.F), and derive conclusions from **primary authority**. Per **SR-5 / R12**, the
  **prior research thread is withheld** from this discovery — it is the *reconciliation reference and floor*
  (R12), **not** the seed — so that agreement between the two threads carries verification weight (seeding
  would manufacture agreement and void the check). Then run the full **Hop-0 → Hop-2** (seed proposition →
  named test + controlling authority + significant progeny by role → **frontier**: circuit splits,
  first-impression, recent/digital developments). Thorough discovery is **the point** — it surfaces the
  adjacent terms, theories, and doctrines worth chasing next (the self-expanding loop).
- **Order: WEB FIRST, then CourtListener [USER].** Web search **generates the vocabulary, doctrine names, and
  candidate case names** and sharpens the CL query; CourtListener then **confirms** existence + identity +
  proposition + verbatim pinpoint + good-law. **Web never asserts (L2); CL is the authority (L3/L4 serial
  lane).** Rationale (recorded): web is *lead-generation* and misses cases CL holds, so it **feeds** CL rather
  than replacing it.
- **Disciplined inclusion.** A discovered **non-book** case earns a **page** only if it states a **clearly
  controlling rule** — **Binding — SCOTUS**, or **Binding in-circuit** on a question the book predates/omits.
  The **most-relevant splits are annotated** (circuits **named**, persuasive-tier per N2), **not** exhaustively
  ingested. **Persuasive-only / illustrative** cases get **no page by default** — a doctrine-page **mention at
  most**. Everything is **field-relevance-gated (R1)**.
- **Bound (no ballooning).** **≤ 2 expansion hops** beyond seed (S1 §3.F). **Stop on any of:** the doctrine's
  D4 completeness checklist is covered · a full hop adds no **controlling** authority · the page would exceed
  the **½–1-page** digestible budget (then cut to load-bearing authority).
- *Check:* `cl-calls.log` evidences **web-first → CL-confirm** order; every ingested non-book case is
  controlling-or-split-marker **and** field-relevant; **no doctrine page balloons** past budget from frontier
  adds; the ≤2-hop bound + a satisfied stop condition are logged per doctrine.

### R7 — The ingest pipeline (discover → verify → author → home → wire → gate → index) **[S4, S2, L5, L4, SR-1]**
Each `confirmed-in` case runs the full pipeline through the **single serial CL lane**:
1. **DISCOVER** (web-first, R6) — candidate name + proposition + section/home hint.
2. **VERIFY** (serial CL — L3/L1/SR-1) — resolve **cluster → lead `opinion_id`**; confirm the **named case in
   returned text** (`identity_checked: true`); confirm the **proposition**; capture **verbatim pinpoint
   quotes**; record **live good-law treatment** + `as_of` (N13, no blank status). L6 ladder before any "fake".
3. **AUTHOR** the **S4 BIRAC** case page (Appendix-B frontmatter + Appendix-C body): **restate, don't
   editorialize** (S4 · R4 / **L8**); two-key baked in (L1); Application confined to the case's own facts.
4. **HOME per S2** — **placement-by-holding (N1 / S2 · R1)**; role from the **8-role set (S2 · R3)**;
   **multi-home** where central to more than one doctrine (N6). The **book section is a hint, overridden by the
   holding** (e.g. a case the book files under "Inventories" homes by its actual ratio).
5. **WIRE links (N7)** — `[[Case]]` at every mention; deep-links to `#rule` / `#^pin-N` for passage-specific
   discussion (S4 · R6); the reverse **"Appears on"** block; **new case-table rows** on each home doctrine page
   where the case is Key/Related (the *rows*; the brief-first reformat itself is **S6**).
6. **find → ADJUDICATE → fix gate** (S1 §3.G) over the new pages — review (free, no-CL) → adjudicate
   (`needs_cl` → serial CL, verdict cites CL evidence) → fix (apply UPHELD/MODIFIED only). **Loop cap 3**;
   **checkpoint the ledger** after each sub-phase (resumable); ESCALATE → `_review-needed/coverage/<slug>.md`.
7. **REGENERATE the Case Index** (S4 · R10) **from frontmatter** — new rows appear automatically; the index is
   **not** hand-edited.
- *Check:* every ingested case completes all 7 stages; `identity_checked: true`; non-blank treatment + `as_of`;
  homed by holding with a valid S2 role; linked (no bare name); present in the regenerated index; its
  adjudications appear in the gate ledger.

### R8 — Decks untouched in S5 **[S4 · R11]**
S5 **adds case pages only**. It **creates, modifies, and re-points no flashcard deck**. Newly ingested cases
flow into decks **only** at the **separate later flashcard run** (decks derive **from** finalized, verified
pages — L1; **no deck work anywhere in the overhaul** — U5-S9, not even at S9). The Name-That-Case and
per-doctrine decks absorb the S5 additions at that separate run, not incrementally here.
- *Check:* **zero** deck files modified during S5; no S5 deliverable emits a deck artifact.

### R9 — No fabricated cases; identity-checked CL links **[L2, L3, L6 — the anti-scar contract]**
**Nothing is ingested from web discovery alone.** Every ingested case carries a **CL-confirmed identity**
(cluster → opinion resolved; **named case present in returned text**) and a **verbatim-pinpointed proposition**
**before** the page is authored. This is the guard against the prior build's scar — **4 fabricated cases and 26
wrong CL URLs** (L2/L3). A candidate that fails the **L6** escalation ladder is recorded **UNVERIFIABLE** in the
omissions register (no page, per S4 · R1) and is **never** asserted. The good-faith/bad-faith-warrant bare-name
captures already flagged in the Case Index (the `United States v. Cruz / West / Jackson` trio; the stolen-vehicle
`United States v. White`; the `self-help doctrine` entry) **remain page-less** and are carried forward as flagged
exception rows, not resurrected.
- *Check (AUTO:LINT-1):* **zero** case pages without `identity_checked: true`; `cl-calls.log` shows an
  identity + proposition confirmation for **every** ingested case; **zero** web-only assertions; every
  UNVERIFIABLE candidate has **no** page and a logged ladder.

### R10 — The omissions register (logged, not silent) **[USER default]**
Every candidate **not ingested** is logged once in **`_overhaul/coverage/omissions.md`** with: **case name ·
book section · reason-class · disposition**. Reason-classes: `out-of-remit (prosecutor/defense/trial)` ·
`trial-evidence (Confrontation)` · `OPTIONAL-tier deferred (S2 §2.0)` · `UNVERIFIABLE (L6 ladder run)` ·
`duplicate-of-existing`. Disposition: `index-row` · `brief-mention` · `nothing (logged only)` ·
`promote-on-request`. This makes **"deliberately excluded" auditable against "missed again"** — the exact
failure S5 exists to prevent — and lets a future "why isn't *X* here?" be answered in one lookup.
- *Check:* every non-ingested candidate appears **once** with a reason-class + disposition; the **ingested set
  ⊎ omissions register = the full candidate pool** (no gaps, no overlaps).

### R11 — Garrity / government-employee 5A cluster = CORE **[USER, U2-S5]**
The government-employee Fifth-Amendment line — **Garrity v. New Jersey**, **Gardner v. Broderick**, **Kalkines
v. United States**, **Lefkowitz v. Turley**, **LaChance v. Erickson**, **NASA v. FLRA**, and controlling progeny
— is **ingested as full S4 case pages** (the one deliberate **audience-relevance** exception to the R1
field-conduct gate). S5 ingests the **case pages** and assigns a **provisional home** — a new doctrine page
**"Public-Employee Compelled Statements (Garrity)"** under S2-tree **#9 (Confessions, Interrogation &
Identifications)** — and **flags S6 to author that doctrine page**. This **supersedes S2 §2.0's OPTIONAL tag**
for this cluster (§9 open item; recommend a one-line S2 cross-ref at execution).
- *Check:* the *Garrity* cluster has case pages, live-verified (R7), homed to the provisional doctrine page; the
  decision log records the audience-relevance basis and the S2 supersession; S6 is flagged for the doctrine page.

### R12 — Dual-thread concordance verification & no-regression guard (SR-5 application) **[USER, U4/U5-S5]**
S5 applies the constitution's **SR-5 (independent-replication concordance)** to coverage. The prior build
already **surfaced and verified** a large corpus — the **verified citation manifests**, the **41 prior per-page
specs** (`…/CSSI/_run/spec/*.spec.md`: per-doctrine case lists, **circuit authorities**, **split identifiers**,
recent-developments rosters), and the live `content/` pages. S5 keeps this as a **separate, independent thread,
not a seed**:
- **Thread P (prior), frozen up front.** Extract the prior conclusion set — per case: holding/ratio, home (by
  holding), role, treatment/good-law; per doctrine: case set + split calls (§6.4 `thread-P.md`). Held aside;
  **withheld from Thread N's reasoning**.
- **Thread N (new), conclusion-blind.** S5 re-derives each doctrine's case set + each case's
  holding/home/role/treatment/split from **primary authority** (book diff + frontier + serial CL, R3/R6) and
  **records its conclusions before** Thread P is revealed to the reconciliation step. SR-1 already re-reads
  every case live — N forms a *fresh* reading; it simply does not peek at P's answer first.
- **Reconciliation gate (the agreement engine)** — diff N against P at **two levels**, *coverage* (same case
  set per doctrine?) and *judgment* (same holding/home/role/treatment/split per shared case?), tagging each:
  - **Concordant** → **`double-verified`** — two independent threads agree (a stronger grade than single-pass).
  - **Fundamentally discordant** (presence/absence · holding/ratio · home-by-holding (N1) · role Key↔Related ·
    treatment/good-law · split direction differ; cosmetic wording/order does **not**) → **escalate** to the
    find→adjudicate→fix machine (R7.6 / S1 §3.G): adjudicate against the **primary opinion** (serial CL), the
    verdict stating **what diverged** (prior wrong / new wrong / scope-or-framing shift) and **which stands**.
  - **Cosmetic** → reconcile freely.
- **No-regression floor.** A Thread-P item **absent** from Thread N is a coverage-discordance that **must** be
  investigated — `re-surfaced` / `re-verified` (the SR-1 double-check) / `dropped-with-prior-reason`
  (already-rejected: the 4 fakes / UNVERIFIABLE / flagged bare-name captures → carried as flagged omissions,
  R10, never silently re-lost) / `regression → relevant, re-ingest` (routed back into R7). Nothing we already
  verified disappears unaccounted.
- **Blindness is enforced by orchestration** — *freeze P → run N with P withheld from its context → reconcile*
  — using separate sub-agents/steps with controlled inputs; one agent holding both threads at once would void
  the check.

*This is a double-check **and** a new check:* SR-1 re-verifies what we have, the frontier (R6) extends it, and
the concordance gate makes their **agreement a verifier** and their **fundamental disagreement a tripwire** —
while the floor guarantees the re-verify never silently shrinks the corpus.
- *Check:* Thread P was frozen before Thread N ran; N recorded its conclusions before reconciliation; every
  case/split carries a concordant/discordant disposition at **both** levels; **every** fundamental discordance
  was adjudicated with primary-authority evidence + a logged verdict; **zero** prior verified conclusions are
  absent from both the live wiki and the omissions register; the `thread-P.md` / `concordance.md` /
  `prior-reconciliation.md` ledgers (§6.4) evidence the pass.

---

## 4. Lessons enforced

- **L1** (two-key / no paraphrase drift) → R7 step 2–3 (verify + verbatim pinpoints before authoring; restate).
- **L2** (web discovers, never asserts) → **R6** (web-first lead-generation) + **R9** (no web-only ingest).
- **L3** (cluster-id ≠ opinion-id; identity) → **R3** step 4 + **R7** step 2 + **R9** (`identity_checked`).
- **L4** (one serial CL lane) → R3/R6/R7 (all CL through the serial lane).
- **L5** (find → adjudicate → fix) → **R7** step 6 (gate, loop cap 3, checkpointed, escalation).
- **L6** (not-found ≠ fake; misspelling-tolerant) → **R3** (tolerant matching + escalation) + **R9** (UNVERIFIABLE).
- **L7** (scope-boundary = assertion) → R6 split annotation + R7 homing (a "limited-to" framing is two-keyed).
- **L8** (restate, not editorialize) → **R7** step 3 (BIRAC restate; no agent-authored field takeaway on case pages).
- **N1** (placement by holding) → **R3** (holding-identity diff) + **R4** class 4 + **R7** step 4 (home by ratio).
- **N4** (subsequent treatment inline) → R7 step 2 (treatment + limiting cases captured at ingest; consistent across homes).
- **N5** (no SCOTUS in recent-developments) → R7 step 4 homing (SCOTUS → Key regardless of date).
- **N6** (non-exclusive key-status / multi-home) → R7 step 4–5 (multi-home + "Appears on").
- **N7** (link every case; named-but-untabled is a miss) → **R4** class 3 + **R7** step 5 (universal linking).
- **N9** (field-decisive framing) → routed to **S6** doctrine pages (instructor-reviewed, SR-2); **kept off S5
  case pages** (L8).
- **N12** (progressive, bounded research) → **R6** (≤2 hops, stop conditions, web-discovers/CL-confirms).
- **N13** (no blank treatment status) → R7 step 2 (live status + `as_of` at ingest).
- **SR-1** (exhaustive live re-verification) → **R7** step 2 (S5 ingest is an SR-1 installment; S9 re-confirms);
  **R12** (prior manifests are a starting reference, re-verified live — never trusted on grade alone).
- **SR-5** (independent-replication concordance — *added to S1 from this interview, SI-8*) → **R12** (the
  dual-thread blind-then-reconcile gate: agreement → `double-verified`, fundamental disagreement → escalate to
  §3.G); strengthens SR-1 with a cross-source agreement axis; inherited by **S9**.
- **SR-2** (instructor-grade framing gate) → S5 ingests the **case substrate** the S6 doctrine briefs need to
  pass SR-2; S5 itself authors case pages (restate), not doctrine briefs.
- **S2** (homing algorithm + role set + scope contract) → R1/R3/R7 read S2 §2.0/§3/§6; **S4** (case model) → R7
  ingests into Appendix-B/-C; **D-3/D-6** stems stable (R7 uses S4 slug scheme) / **decks deferred** (R8).

## 5. Method (how execution proceeds against this spec)

1. **Build the candidate pool (R3.1).** Extract the **book roster** (case · section · page) from the TOC and
   the **named-in-prose roster** (scan `content/*` for case names lacking a page). Union = the master candidate
   list.
2. **Diff by holding-identity (R3.2–3.4).** Misspelling-tolerant match against index + pages + prose; partition
   into `{already-covered, confirmed-miss, excluded, borderline}`; CL-confirm identity before any `confirmed-miss`.
3. **Borderline sign-off (R2).** Emit `borderline.md`; **pause for the user**; fold dispositions back.
4. **Diagnose + generalize (R4).** Tag every miss with its class(es); run each class's **generalized search**
   per doctrine (S2-tree order) to surface siblings; gate (R1) the surfaced cases.
5. **Frontier pass (R6).** Per doctrine, **web-first → serial CL**, expansive discovery / controlling-only
   inclusion; annotate splits; honor the ≤2-hop bound + budget stop conditions.
6. **Ingest (R7).** Run each `confirmed-in` case through the 7-stage pipeline, serial CL, find→adjudicate→fix,
   **checkpointed/resumable**; escalate to `_review-needed/coverage/`.
7. **Regenerate + wire.** Regenerate `Case Index.md` from frontmatter (S4 · R10); add doctrine-page case-table
   **rows** + `[[Case]]` links (the brief-first **reformat** is S6).
8. **Account (R10) + hand off.** Write `omissions.md`; flag **S6** for the *Garrity* doctrine page and the new
   rows to weave into briefs. Every stage cites `docs/STANDARDS.md` (SR-3) and uses the single serial CL lane (L4).

## 6. Deliverables (what execution produces or changes)

### 6.1 — The missed-case list **format** (the diff output)
`_overhaul/coverage/missed-cases.md` — one row per `confirmed-miss`:

| Field | Meaning |
|---|---|
| **Case** | Canonical short name (S4 stem; year-suffix on collision) |
| **CL identity** | Resolved `opinion_id` + URL, `identity_checked` (L3) |
| **Holding / ratio** | The one-line proposition it stands for (the homing basis, N1) |
| **Book section** | I–XIII section (homing *hint* only) — or `frontier`/`prose` if non-book |
| **Diagnostic class** | ≥1 of the 7 classes (R4 / §6.2) |
| **Gate verdict** | `ingest` (field-relevant) — with reason-class (a/b/c) |
| **Proposed home(s) + role** | S2 doctrine page(s) + role from the 8-role set (N1/N6) |
| **Status** | `pending → verified → authored → homed → wired → indexed` |

### 6.2 — The diagnostic-class → generalized-search table (THE CORE DELIVERABLE)

| # | Why-missed class | Exemplar(s) | Generalized search (catches the siblings) | Gate |
|---|---|---|---|---|
| 1 | **Out-of-prior-scope / section-never-mined** | whole book sub-sections never harvested by the curated build | Enumerate the **full roster** of each book section; ingest the field-relevant remainder. | R1 |
| 2 | **Companion / progeny dropped** | *Aguilar* w/o *Spinelli*; *Smith v. Maryland* + *United States v. Miller* (third-party pair behind *Carpenter*); *McNeely* w/o *Schmerber*; *Belton/Gant* w/o *Thornton* | For each captured **anchor**, pull the **canonical companion/progeny line** it is always taught with. | R1 |
| 3 | **Named-in-prose, never tabled (N7)** | *Kyllo* (inside *Carpenter*); *Dunn* (N3); *Ryburn v. Huff*, *Case v. Montana* (S2 · R6 / N5) | Extract **every** case name in existing page prose/holdings; any without a page is a miss. | R1 |
| 4 | **Keyword-homing failure (N1)** | cases mis-filed by surface keyword vs. holding | Per doctrine, audit for cases whose **ratio** belongs there but were filed elsewhere/omitted; re-home by holding. | R1 |
| 5 | **De-duped by name collision** | *Henry v. United States* ≠ *United States v. Henry*; multiple *Harris* / *Davis* / *White* / *Jackson* | For each short-name collision, confirm **each distinct holding** has its own page (S4 · R5 year-suffix). | R1 |
| 6 | **Too-recent / post-capture** | controlling law decided after the prior build / after print | **Date-bounded CL sweep** per doctrine for controlling law since last capture. | R1 |
| 7 | **Frontier-not-run (N12 Hop-2 skipped)** | controlling circuit/state or split-defining law on a live (esp. digital) question | The **bounded progressive frontier pass** (R6) per doctrine — controlling-only inclusion, splits annotated. | R1 |

### 6.3 — The omissions register **format**
`_overhaul/coverage/omissions.md` — one row per **non-ingested** candidate: **Case · Book section ·
Reason-class** (`out-of-remit` / `trial-evidence` / `OPTIONAL-tier (S2)` / `UNVERIFIABLE` / `duplicate`) **·
Disposition** (`index-row` / `brief-mention` / `logged-only` / `promote-on-request`).

### 6.4 — Other execution outputs
- `_overhaul/coverage/borderline.md` — the R2 sign-off list (with user dispositions folded back).
- `_overhaul/coverage/thread-P.md` — the **frozen prior conclusion set** (per case: holding/home/role/
  treatment; per doctrine: case set + splits), extracted **before** Thread N runs and withheld from it (R12/SR-5).
- `_overhaul/coverage/concordance.md` — the **reconciliation ledger**: per case/split, the Thread-N vs Thread-P
  diff at coverage + judgment levels · disposition (`double-verified` / `fundamental-discordant → adjudicated`
  / `cosmetic`) · the adjudication verdict + CL evidence for each discordance (R12/SR-5).
- `_overhaul/coverage/prior-reconciliation.md` — the **no-regression ledger**: every Thread-P item · disposition
  (`re-surfaced` / `re-verified` / `dropped-with-prior-reason` / `regression→re-ingest`) · evidence.
- **The ingested case pages** — `content/cases/<Name>.md` in S4 BIRAC format (generated in execution).
- **Regenerated `Case Index.md`** (from frontmatter; S4 · R10) and **doctrine-page case-table rows + `[[Case]]`
  links** (the brief-first reformat is S6).
- **A flag to S6** — author the *Garrity* doctrine page + weave the new rows into the briefs.
- **No deck files** (R8).

## 7. Acceptance criteria (definition of done)

- [ ] The **candidate pool** (book roster ∪ named-in-prose roster) is built and **partitions completely** into
      `{already-covered, confirmed-miss, excluded, borderline}` — no gaps, no overlaps (R3).
- [ ] The **diagnostic taxonomy** is applied: every `confirmed-miss` carries ≥1 of the **7 classes**, and the
      **§6.2 class → generalized-search table** is present and runnable (R4 — the core deliverable).
- [ ] **Coverage = the union** (book ∪ named-in-prose ∪ **prior-research corpus** ∪ bounded frontier);
      completion is measured against it, with the **omissions register** accounting for the complement (R5/R10).
- [ ] **Dual-thread concordance (R12 / SR-5):** Thread P was frozen before Thread N ran (blind); every
      case/split carries a concordant/discordant disposition at coverage + judgment levels; **agreement is
      tagged `double-verified`**, every **fundamental disagreement was adjudicated** against primary authority
      with a logged verdict, and **zero** prior verified conclusions are absent from both the live wiki and the
      omissions register; the `thread-P.md` / `concordance.md` / `prior-reconciliation.md` ledgers evidence it.
- [ ] Every **ingested case** is **field-relevant (gate, R1)**, **CL-identity-checked (L3)**, **live-verified
      (SR-1, non-blank treatment)**, **authored in S4 BIRAC (restate, L8)**, **homed by holding with a valid
      S2 role (N1/N6)**, **linked (N7)**, and **present in the regenerated Case Index**.
- [ ] **No fabricated cases:** zero pages without `identity_checked: true`; every ingest has a logged CL
      confirmation; UNVERIFIABLE candidates get **no page** and a logged L6 ladder (R9).
- [ ] **Non-book adds are clearly-controlling or split-markers** and field-relevant; **splits annotated
      (circuits named)**; **no doctrine page ballooned** past budget; ≤2-hop + stop condition logged (R6).
- [ ] **Web-first → CL-confirm** order is evidenced in `cl-calls.log` (R6).
- [ ] The **borderline list** is surfaced and **dispositioned by the user** (R2).
- [ ] The **omissions register** logs every non-ingested candidate with reason-class + disposition; ingested ⊎
      omissions = the full pool (R10).
- [ ] The **Garrity cluster** is ingested as CORE pages with a provisional home; S6 flagged; S2 supersession
      recorded (R11).
- [ ] **No deck file changed** in S5 (R8).

## 8. Verification plan (how S5's output gets independently verified — the gate)

1. **No-fabrication audit (L2 — primary gate).** Every ingested case traces to a CL confirmation in
   `cl-calls.log`; **no web-only assertion** survives; re-read a random sample of pages against the CL opinion —
   the proposition and every quote must match verbatim with a correct pinpoint (L1/LINT-2).
2. **Identity-checked-link audit (L3 — primary gate, AUTO:LINT-1).** Every case page has `identity_checked:
   true`; every CL URL resolves **and** the returned text contains the **named** case; cluster → lead opinion
   resolved. Zero `UNVERIFIABLE` captions carry a page (R9).
3. **Partition completeness.** Reconcile counts: candidate pool = `already-covered ⊎ confirmed-miss ⊎ excluded
   ⊎ borderline`; ingested ⊎ omissions register = candidate pool ∪ frontier adds. No silent drops (R5/R10).
4. **Gate soundness (R1).** Sample `ingested` cases are genuinely field/suppression-relevant; sample `excluded`
   cases are genuinely prosecutor/defense/trial-only; the **borderline** list is non-empty-if-any and **fully
   dispositioned** by the user.
5. **Homing soundness (N1/N6).** Spot-check that placements trace to the **holding**, not the book section or a
   keyword (e.g. a case the book files under "Inventories" homed by its actual ratio); multi-homes carry
   consistent treatment + N4 tag across pages (D5).
6. **No-blank-status (N13 — AUTO:LINT-6).** Every new case page + Case-Index row has a non-blank
   `treatment.status` + `as_of`.
7. **Link integrity (N7 — AUTO:LINT-5).** Every new case name is a resolving `[[Case]]`; passage discussions
   deep-link; each page's "Appears on" matches its `homes`; zero bare case names.
8. **Budget / bound (R6).** No doctrine page ballooned by frontier adds; the ≤2-hop bound and a satisfied stop
   condition are logged per doctrine; web-first → CL order present in `cl-calls.log`.
9. **Deck non-touch (R8).** Confirm zero deck files changed during S5.
10. **Non-regression vs S2/S4.** S5 ingests **into** the S4 model and **S2** homes without reversing them; the
    **one** deliberate deviation — the *Garrity* OPTIONAL→CORE promotion (U2-S5) — is consciously logged and
    cross-referenced (R11/§9).
11. **Dual-thread concordance + no-regression (R12 / SR-5 — the guard).** Confirm Thread P was frozen and
    Thread N ran **blind** (recorded its conclusions before reconciliation); audit `concordance.md`: concordant
    items are `double-verified`, **every fundamental discordance carries a CL-adjudicated verdict** naming what
    diverged and which conclusion stands; confirm **nothing verified before is silently absent** from both the
    live wiki and the omissions register and that `regression` items were re-ingested. This is the explicit
    "did we also find it; if not, what happened; is it relevant?" check **plus** the agreement-as-verifier.

## 9. Open items / escalations

- **Garrity doctrine-page home + S2 supersession (R11).** S5 ingests the *Garrity* **case pages** and assigns a
  provisional home ("Public-Employee Compelled Statements (Garrity)" under S2-tree #9); **S6 authors the
  doctrine page**. **U2-S5 supersedes S2 §2.0's OPTIONAL tag** for this cluster — recommend a one-line cross-ref
  added to S2 §2.0 at execution (the APPROVED S2 is not edited here without the user's say-so; flagged instead).
- **`Case v. Montana` / `Ryburn v. Huff`.** Already **named in S2 · R6 / N5** but absent from the Case Index —
  confirmed class-3 (named-in-prose) misses; both home to **Emergency Aid** (the S2 split target). Verify
  identity at ingest (esp. *Case v. Montana*, a recent/possibly-2025 case — class 6 overlap).
- **Final magnitude is method-determined, not fixed.** S5 sets the diff + research method; the precise count of
  ingested cases is produced when the pass runs. Early signal: the officer-relevant book gap is **substantial**
  (foundational misses incl. *Smith v. Maryland*, *United States v. Miller*, *Kyllo*, *Dunn*, *Schmerber*,
  *Spinelli*, *Ybarra*, *Banks*, *Thornton*, *Birchfield*, *Plumhoff*), but far below the raw book delta once
  the field-relevance gate and "already-covered" set are applied.
- **Disambiguation collisions** surfaced by R4 class 5 feed **S4 · R5**'s year-suffix list (e.g. *Henry v.
  United States* vs *United States v. Henry*; multiple *Harris/Davis/White/Jackson*) — execution surfaces the
  full collision list for a quick review pass. Non-blocking.
- **Borderline volume.** If the R2 list is large, batch the sign-off by doctrine; non-blocking for the method.
- **SR-1 CL load.** S5's ingest live-verify adds to the heaviest-pass CL budget (with S4/S9); paced through the
  single serial lane (L4), checkpointed; if the CL tier regresses to 5/min, RUNBOOK §3 STOP-and-notify governs.
- **Prior-research corpus location (R12).** The Thread-P sources are the **verified citation manifests** and the
  **41 prior per-page specs** in the Obsidian vault (`~/Library/.../CSSI/_run/spec/*.spec.md`) plus the prior
  `IA-SPEC.md` / `DECISIONS.md`. Execution must locate the manifests at run start; if any prior artifact is
  unavailable, that gap is itself logged (a known-unknown), not silently skipped. SR-1 still re-verifies every
  re-surfaced case live — Thread P **floors** coverage but never substitutes for the CL re-check.
- **SR-5 inheritance + blinding orchestration (R12).** SR-5 is now a **standing rule in S1** (Appendix A · SI-8),
  so **S9's final verification inherits the same instrument** (the S9 interview operationalizes the clean-room
  pass). The **blind-then-reconcile** discipline is an **orchestration requirement** on the EXECUTE run (freeze
  Thread P → run Thread N with P withheld from context → reconcile via a separate step/sub-agent); a single
  agent holding both threads at once voids the verifier. Flag this to S9 and to EXECUTE.

---

## Appendix A — Decision log

*Format: Question · Options · Red-team · Steel-man · Adjudication. **[USER]** = the user's actual choice; the
rest are self-interviewed.*

### [USER] U1-S5 — What is a "missed case"? → **Officer field-relevance is the gate (book = candidate pool); borderline cases get user sign-off.**
- *Options:* (a) **book-CORE-complete** — ingest every CORE-Part book case (~200+, ~doubling the corpus);
  (b) **selective CORE** — only load-bearing CORE cases, agent's judgment; (c) **field-relevance gate** — ingest
  iff the holding governs field conduct ∨ suppression ∨ officer civil/QI exposure, book is a candidate pool, the
  agent decides clear calls and **surfaces the 50/50s for sign-off**.
- *Discussion:* The user corrected the framing: the book "is a little more complete than we need." CSSI trains
  **legal instructors who are themselves police officers**; the wiki is for **police conduct + suppression +
  standing + Miranda**, not prosecutor/defense/trial craft. "Most things we already have covered." So the test
  is **field-relevance, not book-membership**, applied **case-by-case inside the CORE Parts**.
- *Red-team (a/b):* (a) ingests Confrontation-Clause analyst rules, 5A immunity, act-of-production privilege,
  Book XIII one-offs — off an officer's remit and a huge CL load; (b) leaves the in/out test undefined and
  unauditable. *Steel-man (c):* a principled gate makes "in vs out" testable, shrinks the universe to what the
  course teaches, and the **borderline sign-off** keeps the genuinely-ambiguous cases from being silently
  decided by the agent.
- *Adjudication:* **(c) + borderline sign-off.** The §2.0 gate; the book is the candidate **spine**; excluded
  cases are **logged** (R10), not dropped. **Refines, does not reverse, S2 §2.0** (adds the per-case relevance
  filter S2's "officer-practical" intent implied). The user selected "confirm, with a borderline sign-off."

### [USER] U2-S5 — Government-employee 5A / *Garrity* (about cops, not field S&S) → **Ingest as CORE.**
- *Options:* (a) **index-row / OPTIONAL** (consistent with the field-conduct gate — *Garrity* is employment/IA,
  not suppression); (b) **ingest as CORE** (full pages); (c) **omit** (out of scope, logged).
- *Red-team (b):* it is the one cluster that breaks the clean field-conduct gate — *Garrity* is about
  compelled internal-affairs statements, not what an officer may do in the field. *Steel-man (b):* the
  **audience are officers**; *Garrity* warnings bear on them directly and an instructor will teach it — for
  **this** course, audience-relevance is decisive for this one cluster.
- *Adjudication:* **(b)** — ingest the *Garrity* line (Garrity, Gardner, Kalkines, Lefkowitz, LaChance, NASA v.
  FLRA + progeny) as **CORE** case pages with a provisional doctrine home (S6 authors the page). The **one
  deliberate exception** to R1; **supersedes S2 §2.0's OPTIONAL tag** for the cluster (R11/§9). User chose (b).

### [USER] U3-S5 — Non-book bound → **Expansive research, clearly-controlling inclusion, splits annotated; web-first → CL-confirm.**
- *Options:* (a) **book-relevant only** (no non-book adds); (b) **book + clearly-controlling recent** (minimal
  frontier); (c) **expansive frontier sweep** (hunt persuasive frontier per doctrine).
- *Discussion:* The user split the two knobs the menu had conflated: **discovery breadth** vs **inclusion
  strictness**. He wants discovery **expansive and progressive** — "as you conduct extensive research you see
  legal terms and theories and doctrines that are relevant," the self-expanding loop — **but** the **inclusion
  rule tight**: "add a circuit case [when] clearly controlling," "annotat[e] any splits that are most relevant,"
  "it needs to be relevant," "we don't want it to balloon." And he set the **discovery order**: **web first,
  then CourtListener** — web helps with legal terms and what to search for, even though it "doesn't always show
  every case that CourtListener should."
- *Red-team (c-inclusion):* an expansive *inclusion* sweep balloons doctrine pages with persuasive-only cases
  that crowd the teaching (violates the ½–1-page budget, D14). *Red-team (a):* freezes the wiki at print
  horizon and abandons the live digital frontier the instructor most wants surfaced. *Steel-man (the blend):*
  push **discovery** wide (catches the terms/doctrines to chase) while gating **inclusion** to controlling-or-
  split-marker keeps thoroughness without bloat.
- *Adjudication:* **Expansive discovery + controlling-only inclusion** (R6): full Hop-0→Hop-2 per doctrine,
  **web-first → serial CL confirm** (L2/L4); ingest non-book cases only when **Binding—SCOTUS or Binding
  in-circuit** on a question the book predates/omits; **annotate** the most-relevant splits (circuits named);
  persuasive-only → mention at most; ≤2-hop bound + budget stop conditions. (Inclusion ≈ option b; discovery
  breadth dialed up per the user.)

### [USER] U4-S5 — Treat our own prior research as discardable or as a guiding light? → **Guiding-light source + an explicit no-regression check.**
- *Options:* (a) diff **only** the book + named-in-prose against the live wiki (treat prior research as already
  baked into the wiki); (b) add the **prior-research corpus** (verified manifests + 41 prior per-page specs,
  with their circuit authorities and split identifiers) as a **third candidate source**, **seed** research from
  it, and run an explicit **no-regression reconciliation** so nothing we already surfaced is silently lost.
- *Discussion:* The user flagged that "we've already done a lot of research" — surfaced our own SCOTUS cases,
  circuit cases, and split identifiers — and that re-verifying must not mean **tossing them out**: "I would
  hate for this run to miss something we've already discovered… maybe there should be an extra check: did we
  also find this case, and if not, what happened, and is it relevant?" The run is "a double-check **and** a new
  check."
- *Red-team (a):* assumes the live wiki is a lossless projection of prior research — but the prior build itself
  proved cases get **named in prose but never tabled** (N7) and research can be **dropped between manifest and
  page**; a fresh book-only diff could re-derive a *different* set and quietly shrink the corpus. *Steel-man
  (b):* prior research is verified work; using it as the **seed** (start from what we have) and the **floor**
  (regress below nothing) makes the re-verify strictly additive, and the reconciliation check makes "did we
  keep everything?" **provable**. SR-1 still governs — manifests are a starting reference, re-confirmed live
  (S1 · SR-1), so no accuracy is traded for the convenience.
- *Adjudication:* **(b)** (R12, + R3/R5 hooks) — the prior-research corpus is a guiding-light **reconciliation
  reference and no-regression floor** (**not** a seed — see **U5-S5**, which made the new thread *blind* so that
  agreement carries verification weight); every prior-surfaced case/circuit/split is dispositioned and
  `regression` items re-ingested. Added on the user's follow-up after the initial spec draft.

### [USER] U5-S5 — Prior research as a seed, or as an independent verifier? → **Independent (conclusion-blind) thread + concordance gate; elevated to standing rule SR-5.**
- *Options:* (a) **seed** the new research from the prior conclusions (cheap — but agreement is then
  manufactured and meaningless); (b) keep the prior work a **separate, conclusion-blind thread** and use the
  **comparison** as a verifier — agreement → double-verified, fundamental disagreement → investigate.
- *Discussion:* The user: keep "a separate thread of research"; if the new thread "fundamentally say[s] a
  different thing … we need to figure out what's going on," and if it "come[s] to the same conclusion, then
  that's … an additional verifier, a built-in check." Confirmed **blind-and-compare at both coverage and
  judgment levels**, and the **fundamental-vs-cosmetic** boundary (presence · holding · home · role · treatment
  · split = fundamental; wording/order = cosmetic). **Delegated the scope call.**
- *Red-team (b):* full independence is impractical (both threads use CL/primary law) and it costs more than
  seed-and-confirm. *Steel-man (b):* independence need only be **conclusion-blind** (record N's reading before
  revealing P's) — and since SR-1 already re-reads every case live, the marginal cost is "withhold + compare,"
  not a second research run; the payoff is a genuine **consensus verifier** + a hard **tripwire** on divergence.
  The first S5 draft's **seed-from-prior** line (U4) is therefore **walked back** — it would have manufactured
  agreement and voided the check.
- *Adjudication:* **(b)**, and — on the delegated scope call — **elevated to a standing constitutional rule,
  SR-5** (S1 · §3.C, Appendix A · SI-8), so **S9 inherits** the same instrument (mirroring how L7/L8 were routed
  into S1 from later interviews). **Applied** in **R12** (dual-thread gate); the **R6 seed walked back**; the
  Thread-P freeze + `concordance.md` added. The user blessed surfacing/elevating new mechanisms mid-process as
  the point of the exercise.

### SI-1-S5 — Diff by name-string vs. holding-identity → **Holding-identity (misspelling-tolerant, CL-confirmed).**
- *Options:* (a) reconcile by **case-name string** match; (b) reconcile by **holding-identity** — the
  proposition each case stands for — with L6-tolerant name matching and L3 CL identity confirmation.
- *Red-team (b):* heavier than a string diff. *Steel-man (b):* a string diff (i) **false-merges** name
  collisions (*Henry v. United States* ≠ *United States v. Henry*; multiple *Harris/Davis/White*) — losing real
  cases — and (ii) **misses** cases captured under a variant caption or named only in prose. Holding-identity
  matching + the L6 ladder is the only diff that respects N1 (placement-by-holding) and N7 (named-but-untabled)
  and won't fabricate or vanish a case.
- *Adjudication:* **(b)** (R3) — match by holding; tolerate caption/spelling variants; CL-confirm identity
  before "miss" or "fake."

### SI-2-S5 — A flat missed-case list vs. a diagnosed taxonomy → **Diagnose each miss + generalize to a sibling search.**
- *Options:* (a) produce a flat list of missed cases and ingest them; (b) **classify each miss by why it was
  missed** and turn each class into a **generalized search** for its siblings.
- *Red-team (b):* more design up front. *Steel-man (b):* the interview's explicit core ("diagnose why each was
  missed … apply that logic to find others") — a flat list closes only the cases we happened to notice, while a
  **class → generalized-search** table (out-of-scope-section, dropped-companion, named-in-prose, keyword-homing,
  name-collision, too-recent, frontier-not-run) **systematically nets the cases we did not** and makes coverage
  *provable*, not anecdotal.
- *Adjudication:* **(b)** (R4 / §6.2) — the seven-class taxonomy with a runnable generalized search per class is
  the central deliverable.

### SI-3-S5 — Excluded book cases: silent drop vs. logged → **Logged omissions register.**
- *Options:* (a) silently skip out-of-scope cases; (b) **log every non-ingested candidate** with reason-class +
  disposition.
- *Red-team (b):* a register of skipped cases is bookkeeping overhead. *Steel-man (b):* without it,
  "deliberately excluded" is **indistinguishable from "missed again"** — exactly the failure S5 exists to
  prevent — and the next "why isn't *X* here?" has no answer. The register makes the whole diff **auditable**:
  ingested ⊎ omissions = the candidate pool.
- *Adjudication:* **(b)** (R10) — `omissions.md`; the interview's recommended default, taken as confirmed.

### SI-4-S5 — Coverage measured against the book vs. the union → **The union (book ∪ named-in-prose ∪ bounded frontier).**
- *Options:* (a) "done" = every officer-relevant **book** case ingested; (b) "done" = the **union** of book +
  named-in-prose + bounded-frontier officer-relevant cases, minus already-covered/excluded.
- *Red-team (b):* an open-ended target. *Steel-man (b):* the book is **dated** (the digital frontier moves
  fastest and is where officers are most exposed) and the prior build **named cases it never tabled** — book-
  only completeness would re-bake both gaps. The ≤2-hop bound + budget stop conditions keep the union **bounded**.
- *Adjudication:* **(b)** (R5) — coverage is the bounded union; the omissions register accounts for the complement.

### SI-5-S5 — Decks during S5: incremental vs. deferred → **Untouched; terminal page-derived rebuild (S4 · R11).**
- *Options:* (a) add cards for each newly ingested case as we go; (b) **touch no deck in S5**; the whole set is
  purged and **regenerated from the finalized, verified pages** at EXECUTE/S9 (L1).
- *Red-team (b):* the new cases aren't drillable until the terminal rebuild. *Steel-man (b):* S4 · R11 already
  froze the decks S4–S8 for a clean page-derived rebuild (decks derive **from** pages, L1); incremental S5 deck
  surgery would re-introduce the exact drift R11 removed and fork from S4. Consistency wins.
- *Adjudication:* **(b)** (R8) — zero deck work in S5; the additions land at the terminal rebuild.
