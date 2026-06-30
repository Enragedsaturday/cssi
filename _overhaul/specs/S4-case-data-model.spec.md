# SPEC S4 — Case Data Model & Per-Case Pages
status: APPROVED
depends-on: [S1, S2, S3]          gates: [S5, S6]
last-updated: 2026-06-30   <!-- 06-29 original; 06-30 cross-spec coherence amendment: deck rebuild is a SEPARATE later run, not EXECUTE/S9 (U5-S9) -->

> Governed by `docs/STANDARDS.md` (S1, SR-3 supremacy). S4 **defines the case object**, the
> **per-case page template** (BIRAC — restate, don't editorialize), the **universal-linking +
> deep-link/anchor scheme**, the **component data convention**, and the **migration plan** that
> generates a page for every Case-Index case under a full live good-law sweep. S4 **designs**;
> it authors no case pages now — generation, the Case-Index regeneration, and the terminal deck
> rebuild all execute later under `EXECUTE.wrapper.md`. S4 **closes** S1 §9 (anchor scheme +
> deep-link finalization) and S3 §9 (component data convention) and **supersedes** the deck-id
> half of D-3/D-6 per U3-S4.

---

## 1. Objective

Define what a **case IS** in this wiki — a first-class **case object** with one canonical page
per case — and the model that makes a 300-case corpus navigable and trustworthy: (a) the
**frontmatter schema** (canonical name, cite, court, verified CourtListener identity, the S1
authority-weight + treatment axes, home doctrines + role, anchors, related cases); (b) the
**per-case page template** — an officer-readable **BIRAC** (Background → Issue → Rule →
Application → Conclusion) that **restates the holding faithfully** (two-key, L1) and never
editorializes a generalized field rule; (c) **universal linking + deep-link anchors (N7)** so
every named case resolves to its page and doctrine pages can pinpoint the exact holding; (d) the
**component data convention** the S3 components consume (markdown-portable, R5-S3); and (e) the
**migration plan + find→adjudicate→fix gate** that generates every page, regenerates the Case
Index *from* those pages, fills N13's no-blank-status rule via a full live CL sweep (SR-1
installment), and freezes the flashcard decks for a terminal rebuild.

## 2. Scope

### 2.1 In scope (S4 designs)
- The **case object** + its **frontmatter schema** (R1, R2; Appendix B).
- The **BIRAC page template**, verbatim, with the two-key rule baked in (R3; Appendix C).
- The **case-page-restates / doctrine-page-teaches** rule — no agent-authored street takeaway on
  case pages (R4; the scar this interview surfaced — D1-S4).
- The **slug scheme**, filename = canonical short name, disambiguation, `cases/` home, L6 aliases (R5).
- The **section anchor + pinpoint scheme** (R6) and **universal linking** (R7) — *closes S1 §9 / S3 R7*.
- The **comprehensive treatment-status model** + full live sweep at generation (R8).
- The **component data convention** (R9) — *closes S3 §9*.
- The **Case Index → index-of-pages, generated from case frontmatter** (R10).
- The **flashcard-deck policy: freeze now, terminal purge + regenerate from finalized pages** (R11).
- The **migration plan + find→adjudicate→fix gate** (R12).

### 2.2 Out of scope (owned elsewhere)
- **Ingesting / discovering the CORE case universe** (the "missed-case" diff) → **S5** (reads §2.0/§6.3 of S2 + this model).
- **Authoring doctrine-page bodies, the caretaking content split, re-homing cases into the brief-first template, and the doctrine-page *field framing* (N9)** → **S6**. S4 fixes only the case-page side + the link/anchor contract S6 emits against.
- **Wiring glossary links** → **S7**. **Standards/lexicon/verification machine** → **S1**.
- **Building the S3 components** (`CaseTable`, `TreatmentBadge`, `DoctrineFlowchart`, `CaseBrowser`, `CrossRefPanel`) → execution under S3's spec; S4 supplies their **data contract** only.
- **The terminal deck rebuild itself** → **EXECUTE/S9** (S4 sets the policy + L1 derivation contract; the regenerator runs after content is final and verified).
- **Folder creation / `git mv` / the Explorer + alias plumbing** → **S3** (already specified).

---

## 3. Requirements (numbered, testable)

### R1 — The case object: one canonical page per case
Every case in `Case Index.md` (the 261 verified + any S5 additions) gets **exactly one** case
page. The case page is the **single source of truth** for that case's structured data (cite,
court, weight, treatment, homes, CL identity); doctrine-page tables, the Case Index, and the S3
components all **derive from it** — never the reverse. Flagged/`UNVERIFIABLE` captions (e.g. the
"United States v. White" stolen-vehicle entry) get **no page**; they remain Case-Index
exception rows with their flag, never asserted as real cases (L6).
- *Check:* `cases count == verified-Case-Index count`; every doctrine-table case name resolves to
  a case page; no page exists for an `UNVERIFIABLE` caption.

### R2 — Frontmatter schema (the case object)
Each case page carries the **frontmatter schema in Appendix B**, every field testable. It records
all Part-B items: canonical name, Bluebook cite + parallel/neutral/slip cite, court + level +
circuit (N2), year/date, docket, the **verified CL opinion URL + lead `opinion_id` + `identity_checked`
flag** (L3: cluster→opinion resolved, named case confirmed in returned text), the **authority-weight**
(one of the six S1 tiers, §3.D) **and** the orthogonal **treatment** block (`status` ∈
{good, criticized, limited, abrogated, overruled} + `as_of` date + `by:` limiting cases — N13/N4),
**homes** (doctrine page + role from the S2 §3.3 eight-role set, N1/N6), `related`, and `aliases`
(name/spelling variants for L6-tolerant link resolution).
- *Check:* every required key present and non-empty; `authority_weight` is one of the six tiers;
  `treatment.status` non-blank with an `as_of` date; `identity_checked: true`; each `homes[].role`
  is a valid S2 role.

### R3 — The per-case page template (BIRAC) **[USER]**
Case pages use the **BIRAC** template in **Appendix C**, verbatim: a plain-markdown header line
(cite · court · weight · treatment, enhanced by `TreatmentBadge`) → **Background → Issue → Rule →
Application → Conclusion** → **Treatment & subsequent history** (N4/N13) → **Appears on** (N7
reverse homes) → **Sources** (CL URL + pinpoint pages). The **two-key rule is baked in**: every
quotation is **verbatim with a reporter pinpoint** (L1/LINT-2), and every proposition traces to the
opinion. The **Rule** section states the black-letter holding the case stands for (placement-by-
holding, N1); the **Application** applies it to **this case's own facts** (what the Court did),
not a generalized rule.
- *Check:* every case page matches the Appendix-C section order; every quote has a pinpoint; the
  Rule states the case's ratio; no section is empty.

### R4 — Case page *restates*; doctrine page *teaches* — no editorial street takeaway **[USER, scar D1-S4 → elevated to S1 · L8]**
*This rule is the case-template application of standing scar-rule **L8** (S1 §3.A, added 2026-06-29 from this
interview per the user — see S1 · Appendix A · SI-7).* A case page **restates** its holding faithfully; it
carries **no agent-authored generalized field/
practical takeaway**. Any "what this means on the street across situations" framing — the N9 field-
decisive question, line-drawing, operational advice — lives **only on doctrine pages**, authored as
teaching and **instructor-reviewed** (SR-2). On a case page, the **Application** block is confined
to the case's own facts. Rationale (the scar): a takeaway written in the agent's own voice is, by
construction, an **un-anchored paraphrase of a holding**, and paraphrase that **narrows or expands**
the rule is exactly **L1** (paraphrase drift) + **L7** (negative scope by implication) + **N1**
(framing must track the holding). *(Origin: the S4 draft Field-IRAC takeaway rewrote* Brigham City*'s
"objectively reasonable basis **to believe**" into "**see** it" — silently converting a
source-agnostic standard into a visual-observation requirement the Court never imposed.)*
- *Check (CHECKLIST:D2/D4/D9):* no case page contains generalized field-advice prose beyond a
  faithful restatement of its pinpointed holding; the Application is case-fact-bound; any
  field/operational framing appears on a doctrine page under instructor sign-off, never on the
  case page. *(R4 has been **elevated to a standing S1 rule, L8** — added to the constitution per the
  user, analogous to how L7 was homed there during S2; see S1 · Appendix A · SI-7.)*

### R5 — Slug scheme, filenames, disambiguation, home folder
- **Filename = the canonical short case name** as cited (party-v-party form, no reporter cite, no
  procedural parens): `Brigham City v. Stuart.md`. This keeps `[[Brigham City v. Stuart]]` resolving
  for free under Quartz `markdownLinkResolution: "shortest"` (R4-S2 / S3 R1) — **the wikilink half of
  D-3/D-6 (file-stem stability) is retained.** Quartz auto-slugs to `brigham-city-v-stuart`.
- **Home folder:** all case pages live under **`content/cases/`** (one flat folder), kept out of the
  doctrine Explorer tree; shortest-path resolution means `[[Case]]` resolves regardless of folder, and
  the Explorer can collapse/segregate `cases/` (R2-S3). Case pages are **excluded from the doctrine
  category nav** but reachable via search, graph, links, and the faceted browser.
- **Disambiguation:** when two cases share a short name (e.g. multiple `Michigan v. …`, two
  `United States v. White`), append the year: `United States v. Jones (2012).md`; the colliding wikilink
  is written with the year. `aliases:` carries the bare-name variant so existing `[[bare name]]` links
  still resolve to the intended case (and surface the collision for review).
- *Check:* every case file stem is the canonical short name (+ year only on collision); zero broken
  `[[Case]]` wikilinks post-generation; `cases/` excluded from the category Explorer; no stem renames
  of existing doctrine pages.

### R6 — Section anchor + pinpoint scheme (N7; **closes S1 §9 / S3 R7**)
Deep-linking the **exact holding** uses **deterministic internal anchors** (SPA-safe per S3 R7 —
*not* URL text fragments for internal links):
- **Fixed BIRAC headings → fixed heading-id anchors:** `#background`, `#issue`, `#rule`,
  `#application`, `#conclusion`, `#treatment`, `#sources`. Heading text is **frozen** by the template so
  anchors never drift. **`#rule` is the canonical "the holding" anchor** — a doctrine page deep-links a
  case's holding as `[[Brigham City v. Stuart#rule]]`.
- **Pinpoint quotes → block anchors** keyed to the reporter page: each pinpoint-quoted proposition in
  the Rule/Treatment sections carries a block id `^pin-<page>` (e.g. `^pin-404`). A doctrine page
  pinpoints a specific passage as `[[Brigham City v. Stuart#^pin-404]]`. Block ids are unique per page;
  collisions disambiguate with a letter (`^pin-404a`).
- **External (CourtListener) pinpoints** use a **URL text fragment** on the opinion URL
  (`…/opinion/145654/brigham-city-v-stuart/#:~:text=<url-encoded quote>`), opened in a new tab, with the
  plain opinion URL as fallback (S3 R7).
- This scheme **finalizes LINT-5's deep-link check** (S1 §9) and satisfies S3's "S4 must give per-case
  pages stable section anchors" requirement.
- *Check:* `[[Case#rule]]` scrolls to the holding under SPA nav; `[[Case#^pin-N]]` lands on the quoted
  span; an external CL text-fragment link highlights the passage in a fresh tab; all three fall back cleanly.

### R7 — Universal linking (N7)
**Every case named anywhere** — doctrine prose, case-tables, the Case Index, other case pages, the
glossary — resolves to its case page via `[[Case]]`; **passage-specific** discussion deep-links the
pinpoint (`[[Case#rule]]` / `[[Case#^pin-N]]`); a **whole-case** reference links the page. No bare,
unlinked case name survives. The reverse direction is the case page's **"Appears on"** block (R3),
listing each home doctrine + role (N6 multi-homing made visible).
- *Check (AUTO:LINT-5 + CHECKLIST:D13):* zero bare case names on any page; every `[[Case]]` /
  `[[Case#anchor]]` target resolves; every case page's "Appears on" matches its frontmatter `homes`.

### R8 — Comprehensive treatment status — full live sweep at generation **[USER]**
Every case page receives a **good-law treatment status verified live against the primary opinion**
through the single serial CL lane at generation — **the first installment of SR-1** (exhaustive,
no tiering); S9 re-confirms exhaustively. The page records the **two orthogonal axes** (S1 §3.D):
**authority-weight** (six tiers) and **treatment** (`status` + `as_of` date + `by:` limiting cases).
**No blank treatment status anywhere** (N13). Negative subsequent treatment is tagged **inline**
"limited/abrogated/overruled by [[case]]" at the point of assertion **and** in the Treatment block, with
a 1–2-sentence *why* only when it changes field application (N4 threshold, U-4 of S1); the tag is
**consistent across every page the case appears on** (multi-home coherence, D5).
- *Check (AUTO:LINT-6 + CHECKLIST:D1/D3):* every case page has a non-blank `treatment.status` + `as_of`;
  `cl-calls.log` evidences a live re-check for every case; N4 tags are identical across all of a case's homes.

### R9 — Component data convention (markdown-portable; **closes S3 §9**)
The S3 components consume **plain markdown + frontmatter — no bespoke load-bearing syntax** (R5-S3):
1. **Canonical structured data = case-page frontmatter** (Appendix B). `TreatmentBadge`, `CaseBrowser`,
   and `CrossRefPanel` read it (directly or via the build index in R10).
2. **Doctrine-page case-tables = plain GFM markdown tables** in the brief-first template (the existing
   "Key cases" table shape). `CaseTable` **enhances them in place** by matching the case name/`[[link]]`
   to the case page's frontmatter (pulling weight + treatment badge); **with JS disabled the table renders
   as a static markdown table** (R5-S3). Author tables in plain markdown — never a component-only syntax.
3. **Flowcharts = Mermaid code-fences** (S3 R4 #4) — already portable.
4. **Optional convenience directive:** a fenced ```` ```casetable ```` / ```` ```case-browser ```` block
   *may* be offered for generated widgets whose only markdown fallback is a link to the Case Index; it is
   **documented but never load-bearing** — every such block degrades to a plain link/table.
- *Check:* disabling components leaves every doctrine page legible; no S4–S8 deliverable is expressed in a
  syntax only a custom component can render; `CaseTable` enhances a static table by slug-match.

### R10 — The Case Index becomes an index *of* pages, generated *from* frontmatter
`Case Index.md` is **regenerated by a build script from the aggregate of case-page frontmatter** (single
source of truth; cannot drift from the pages). Each row: **Case** = `[[Case]]` wikilink to its page;
**Holding** = the one-line ratio; **Treatment** = the verified status glyph + label (no blanks, N13);
**Home page(s)** = the `homes` links + roles; **CourtListener** = the verified opinion link. The same
aggregate **build index** feeds `CaseBrowser` (facets: category/home, role, court level, treatment, decade)
and `CrossRefPanel` (other homes, `related`, limited-by/limits) per R9.
- *Check:* the Case Index is reproducible from `content/cases/*` frontmatter alone; every Case cell is a
  resolving `[[wikilink]]`; no blank treatment cell; regenerating yields no diff vs. the committed index.

### R11 — Flashcard-deck policy: freeze now, terminal purge + regenerate **[USER, U3-S4 — supersedes deck-id half of D-6]**
The flashcard decks are **left untouched throughout the ENTIRE overhaul (S4–S9)** (no deck surgery, no
`page`-field re-pointing, **no deck-id-preserving caretaking-split migration** — that mechanism is
**dropped**). **[Amended 2026-06-30 · U5-S9:** the page-derived rebuild is **NOT** an S9 step — **no
flashcard work happens anywhere in the overhaul**; it is a **separate later flashcard run** after the
overhaul + the full content corpus are finalized.**]** In that separate run, the **entire deck set is
purged and regenerated from the finalized, 100%-verified pages** (decks derive FROM pages, **L1**),
preserving the existing **deck taxonomy**
(per-doctrine decks + the "Name That Case" decks; **no per-case decks** — Part-A answer) as the organizing
scheme while drawing card content from the final doctrine pages (rules/tests) and case pages (one-line
holdings). This **consciously relaxes the deck-id / FSRS-progress half of D-3/D-6**: regenerated cards get
fresh ids and the in-browser app treats them as New (study progress on the ~1,660 current cards resets) —
an accepted cost of a clean page-derived rebuild. The **file-stem (wikilink) half of D-3/D-6 is retained.**
- *Ownership:* the page-derived rebuild is a **SEPARATE later flashcard run** (U5-S9), **not** S4 and
  **not** S9; S4 sets the policy + the L1 derivation contract. The frozen combined caretaking deck's
  dangling `page:` resolves via the S3 alias (R9-S3) until that run.
- *Check:* no deck file is modified during the overhaul (S4–S9); the rebuild runs in the separate later
  run after content is finalized; the regenerated set validates under `merge.py` (ids prefixed by deck
  slug) and round-trips through `make_apkg.py`; the deck taxonomy is preserved; no per-case decks exist.

### R12 — Migration plan + find→adjudicate→fix gate (L5/L4)
Generation of the ~261 pages runs as the standing machine (S1 §3.G), serial-CL throughout (L4):
1. **GENERATE.** For each Case-Index case, emit the Appendix-C page from the verified manifests **plus a
   live CL re-verify** (identity L3, proposition, every quote+pinpoint, good-law R8). Resolve cluster→lead
   `opinion_id`; confirm the named case in returned text before trusting any quote. Misspelling-tolerant
   ID (L6) before any "fake" call.
2. **REVIEW** (parallel, free, no CL). Structured findings on template compliance (R3), schema completeness
   (R2), universal linking + anchors (R6/R7), no-blank-status (R8), no-editorial-takeaway (R4),
   restate-not-narrow fidelity (L1). Reviewers do not edit.
3. **ADJUDICATE.** `needs_cl` findings (status, pinpoint, identity, existence) → serial CL lane, verdict
   must cite CL evidence; non-legal findings → free editor-adjudicator; DISMISSED logged with reason.
4. **FIX** (parallel, free). Apply only UPHELD/MODIFIED fixes; ESCALATE → `_review-needed/cases/<slug>.md`.
   **Loop cap 3**, checkpoint the ledger after each sub-phase (resumable).
Then **regenerate the Case Index** (R10) from the finished pages and **re-point doctrine-table case names to
`[[Case]]` wikilinks** (the link wiring; the brief-first reformat itself is S6).
- *Check:* a page exists for every verified case; `cl-calls.log` shows the serial live sweep; every fix
  traces to an adjudicated verdict; escalations are logged; the regenerated Case Index matches the pages.

---

## 4. Lessons enforced

- **L1** (two-key / no paraphrase drift) → R3 (verbatim quotes + pinpoints baked into the template) +
  **R4** (case page restates, never editorializes the holding) + R12 (live re-verify).
- **L3** (cluster-id ≠ opinion-id) → R2 (`opinion_id` + `identity_checked`) + R12 step 1.
- **L4** (one serial CL lane) → R8 + R12 throughout.
- **L5** (find→adjudicate→fix) → R12 gate.
- **L6** (not-found ≠ fake; misspelling-tolerant) → R1 (no page for `UNVERIFIABLE`) + R5 (`aliases`) + R12.
- **L7** (scope-boundary = assertion) → **R4** (a narrowing takeaway is a negative-scope assertion; barred
  from case pages).
- **L8** (restatement, not editorialization — *the standing rule R4 was elevated into*, S1 · SI-7) → **R4**
  (case pages restate; a takeaway that moves the holding carries the two-key burden).
- **N1** (placement by holding) → R3 (Rule = the case's ratio) + R2 (`homes` by holding).
- **N2** (authority lexicon) → R2 (`authority_weight` ∈ six tiers; circuit named).
- **N4** (subsequent treatment inline) → R8 (inline + Treatment block, consistent across homes).
- **N6** (non-exclusive multi-homing) → R2 `homes[].role` + R7 "Appears on" + R9 cross-ref panel.
- **N7** (link every case; deep-link pinpoints) → R6 anchors + R7 universal linking.
- **N9** (field-decisive framing) → **R4** routes it to doctrine pages, instructor-reviewed (not case pages).
- **N13** (no blank treatment status) → R8 + R10 (no blank Index cell).
- **SR-1** (exhaustive live re-verify) → R8 (generation installment) + R12.
- **SR-2** (instructor-grade gate) → R4 (field framing is instructor-reviewed on doctrine pages).
- **D-3/D-6** → R5 retains the file-stem (wikilink) half; **R11 supersedes the deck-id (FSRS) half** per U3-S4.

## 5. Method (how execution proceeds against this spec)

1. **S3** has already created `content/cases/` + the folder/Explorer/alias plumbing; S4's generator writes
   into it. 2. **GENERATE** every case page (R12 step 1) via the serial CL lane (SR-1 installment). 3.
   **REVIEW → ADJUDICATE → FIX** (R12 steps 2–4). 4. **Regenerate `Case Index.md`** from frontmatter (R10).
5. **S5** ingests the missed-case universe **into this same model**. 6. **S6** reformats doctrine pages to
   the brief-first template, **emitting `[[Case#rule]]`/`[[Case#^pin-N]]` deep-links and plain `CaseTable`
   markdown** (R6/R9), and authors the **doctrine-page field framing (N9)** that R4 keeps off case pages. 7.
   The **S3 components** are built against R9's data contract. 8. **After S9 verification, EXECUTE purges and
   regenerates the decks** from the finalized pages (R11). Every stage cites `docs/STANDARDS.md` (SR-3) and
   routes CL work through the single serial lane (L4).

## 6. Deliverables (what execution produces or changes)

- **`content/cases/<Canonical Name>.md`** — one BIRAC page per verified case (~261 + S5 additions), each
  with the Appendix-B frontmatter and Appendix-C body. *(Bodies generated in execution, not now.)*
- **`Case Index.md`** — regenerated as an index *of* pages (R10): Case cells become `[[wikilinks]]`,
  treatment cells filled, generated from frontmatter.
- **A build script** (`scripts/build-case-index.*` or similar) that aggregates `content/cases/*` frontmatter
  → the Case Index table + the `CaseBrowser`/`CrossRefPanel` data index (R9/R10). Exact filename at execution.
- **The component data contract** (R9) documented for the S3 component build (frontmatter keys; plain-table
  enhancement; optional fenced directives).
- **Doctrine-page case-name → `[[Case]]` link wiring** (R12 tail; the brief-first reformat is S6).
- **Deck policy recorded** (R11): decks frozen; terminal rebuild deferred to EXECUTE/S9. *(No deck files
  change in S4.)*
- **`_overhaul/specs/S4-case-data-model.spec.md`** — this spec (incl. Appendices A–C).

## 7. Acceptance criteria (definition of done)

- [ ] A **case page exists for every verified Case-Index case**; `UNVERIFIABLE` captions get no page (R1).
- [ ] **Every named case anywhere links to its case page** (`[[Case]]`); passage discussions deep-link the
      pinpoint; zero bare case names; zero broken `[[Case]]`/`[[Case#anchor]]` targets (R7, N7).
- [ ] **No blank treatment status** on any case page or Case-Index row; each carries the six-tier
      authority-weight **and** a `treatment.status` + `as_of` date, live-verified at generation (R2/R8, N13/SR-1).
- [ ] The **frontmatter schema** (Appendix B) is present and complete on every case page; `identity_checked:
      true` with a resolved `opinion_id` (R2, L3).
- [ ] Case pages follow the **BIRAC template** (Appendix C) verbatim; every quote is verbatim + pinpointed
      (R3, L1/LINT-2); the **Application is case-fact-bound** and **no case page carries an agent-authored
      generalized field takeaway** (R4).
- [ ] **Deterministic anchors** (`#rule`, `#^pin-N`) exist on every case page and resolve under SPA nav;
      LINT-5's deep-link check is finalized (R6 — closes S1 §9).
- [ ] The **component data convention** is fixed and markdown-portable; doctrine tables stay plain markdown;
      no component-only syntax (R9 — closes S3 §9).
- [ ] The **Case Index is regenerable from frontmatter** with no diff (R10).
- [ ] The **deck policy** is recorded: decks frozen through S4–S8, terminal purge+regenerate from finalized
      pages owned by EXECUTE/S9; no per-case decks; deck-id half of D-6 consciously superseded (R11).
- [ ] The **migration find→adjudicate→fix gate** (serial CL, loop cap 3, escalation path) is specified (R12).

## 8. Verification plan (how S4's output gets independently verified)

1. **Linking integrity (AUTO/LINT-5):** build; assert zero bare case names and zero broken
   `[[Case]]`/`[[Case#anchor]]` links; spot-check internal `#rule`/`#^pin-N` deep-links scroll correctly under
   SPA; an external CL `#:~:text=` link highlights in a fresh tab.
2. **Status completeness (AUTO/LINT-6):** every case page + Index row has a non-blank treatment status with an
   `as_of` date; `cl-calls.log` evidences a live re-check for every case (SR-1 installment).
3. **Schema well-formedness:** every Appendix-B required key present; `authority_weight` ∈ six tiers;
   `identity_checked: true`; `homes[].role` ∈ S2 role set; aliases resolve.
4. **Template + no-editorial-takeaway (CHECKLIST:D2/D4/D9):** sample case pages match Appendix C; the
   Application is case-fact-bound; **no generalized field-advice prose** beyond a faithful restatement —
   spot-check the *Brigham City* page does **not** reintroduce a "must see it" narrowing (the D1-S4 scar).
5. **Two-key fidelity (CHECKLIST:D1):** quotes verbatim + pinpointed; the Rule states the case's ratio
   (placement-by-holding); re-read against the CL opinion for a sample.
6. **Index regeneration (AUTO):** regenerate `Case Index.md` from `content/cases/*` frontmatter → byte-diff
   clean vs. committed.
7. **Portability spot-check (R9):** disable components → three sample doctrine pages remain legible markdown;
   `CaseTable` enhances a static table by slug-match.
8. **Deck non-touch:** confirm no deck file changed in S4–S8; the terminal rebuild (post-S9) validates under
   `merge.py` and round-trips `make_apkg.py`; taxonomy preserved; no per-case decks.
9. **Non-regression vs `DECISIONS.md`:** file stems unchanged (D-3); the deck-id supersession (R11) is the
   **only** D-6 relaxation and is consciously logged (D1-S4 / U3-S4); the Case-Index router (D-2) survives.

## 9. Open items / escalations

- **Elevate R4 to a standing S1 rule? — RESOLVED (done).** Per the user's instruction, R4 has been
  **elevated to standing scar-rule L8** in the S1 constitution (§3.A; decision log SI-7; lessons count
  20 → 21; mapped to D2/D4/D9). R4 remains the case-template application of L8.
- **Disambiguation collisions** (multiple `Michigan v. …`, two `United States v. White`) — R5 resolves by
  year suffix + alias; the **full collision list** is enumerated during generation (S5 may add more). Execution
  surfaces the list for a quick review pass; non-blocking now.
- **`cases/` in the Explorer** — R5 segregates case pages from the doctrine nav; the **exact** Explorer
  treatment (hidden vs. a collapsed "Cases" node vs. reachable only via search/graph/browser) is an S3
  layout detail — recommend a single collapsed `Cases` node, decided at execution. Non-blocking.
- **Deck-rebuild design depth** — R11 sets the policy + L1 contract; the **detailed regeneration design**
  (card-type mix, cloze coverage, Name-That-Case sourcing from case-page holdings) is an EXECUTE/S9 concern.
  If the user later wants to **preserve FSRS progress** after all, that requires an id-stable rebuild + an
  app-side id-alias map (out of current scope) — re-open before the terminal purge.
- **`Case Index.md` aliases/frontmatter** — the regenerated index keeps its `type: index` + alias; the
  generator must not clobber the human-readable header prose. Minor; execution detail.

---

## Appendix A — Decision log

*Format: Question · Options · Red-team · Steel-man · Adjudication. **[USER]** = the user's actual choice;
the rest are self-interviewed.*

### [USER] U1-S4 — House case-page format → **BIRAC (no agent-authored street takeaway).**
- *Options (shown as filled* Brigham City *previews):* (a) **Field-IRAC** (Background→Issue→Holding→Reasoning→
  **Field Application**→**Bottom line**→Teaching points→Treatment); (b) **BIRAC** (Background→Issue→Rule→
  Application→Conclusion); (c) **CRuPAC** (answer-first).
- *Discussion / red-team (Field-IRAC):* the draft Field-IRAC takeaway **narrowed the holding** — it rewrote
  *Brigham City*'s "objectively reasonable **basis to believe**" into "**see** violence/injury," converting a
  source-agnostic standard (dispatch, 911, a witness, sounds all suffice) into a visual-observation requirement
  the Court never imposed. The user flagged this and questioned whether an agent should author field takeaways
  at all. The two takeaway blocks are the *only* un-anchored prose in the template — by construction an
  invitation to paraphrase a holding, which **L1** forbids. *Steel-man (BIRAC/CRuPAC):* both **restate** the
  rule with pinpoints and confine "Application" to the case's own facts — no generalized street rule to drift.
- *Adjudication:* **(b) BIRAC.** Case pages **restate; doctrine pages teach** — generalized field framing (N9)
  moves to doctrine pages under instructor review (SR-2). Generalized as **R4** and, per the user, **elevated
  to standing scar-rule L8** in S1 (§3.A; SI-7), mirroring how L7 was homed during S2. The user explicitly
  chose BIRAC.

### [USER] U2-S4 — Treatment-status verification scope → **Full live check at generation.**
- *Options:* (a) full live good-law check for every case at generation (SR-1 installment); (b) carry catalog
  statuses forward, live-check only deltas now, defer full re-verify to S9.
- *Adjudication:* **(a)** — every case page gets a live-CL-verified status + `as_of` at generation (R8), the
  first installment of **SR-1** (exhaustive, no tiering); S9 re-confirms. Consistent with S1; the heavy CL load
  starts at ingest and runs patiently through the single serial lane (L4). User selected (a).

### [USER] U3-S4 — Flashcard decks → **Leave alone now; terminal purge + regenerate from finalized pages.**
- *Options:* (a) deck-id-preserving caretaking-split migration now (freeze ids, re-point `page`) + per-change
  realignment through S5–S8, honoring D-6; (b) **freeze decks untouched through the overhaul, then purge the
  whole set and regenerate from the finalized, verified pages** (L1), accepting an FSRS-progress reset; (c) add
  per-case decks. *No new per-case decks* was already the recommended answer (Part A).
- *Mechanical finding:* `merge.py:5-6` keys FSRS progress to the card **`id`**, and `merge.py:49` **enforces**
  that every id is prefixed with its deck-file slug. So a deck *file* split would force an **id rename** →
  reset progress anyway; the only truly id-stable migration keeps the **old combined deck file** and re-points
  only the `page` field — fiddly, and still leaves stale cards against rebuilt content.
- *Red-team (b):* discards study progress on ~1,660 cards (the exact thing D-6 protected). *Steel-man (b):* in a
  100%-verified rewrite, ids preserved against *old* content guard progress on cards that no longer match the
  finalized pages; a page-derived rebuild is the cleanest guarantee of **deck↔page fidelity (L1)** and removes a
  fragile migration from every later stage.
- *Adjudication:* **(b)** (R11). Decks frozen S4–S8; **terminal purge + regenerate from finalized pages**, owned
  by EXECUTE/S9; existing **deck taxonomy preserved**, **no per-case decks**. **Consciously supersedes the
  deck-id/FSRS half of D-3/D-6** (file-stem half retained). The deck-id-preserving caretaking-split migration is
  **dropped** from S4. User chose (b); re-opening to preserve FSRS progress is flagged in §9.

### SI-1-S4 — Case slug / filename scheme → **Filename = canonical short name; `cases/` folder; year-suffix on collision.**
- *Options:* (a) filename = canonical short name (`Brigham City v. Stuart.md`); (b) include the reporter cite in
  the slug; (c) CL-style numeric slug.
- *Red-team (a):* short names collide (multiple `Michigan v. …`); a period/comma in captions. *Steel-man (a):*
  Quartz `markdownLinkResolution: "shortest"` makes `[[Brigham City v. Stuart]]` resolve to the file stem with
  **zero link rewriting**, preserving the wikilink half of D-3/D-6; periods are filesystem-safe; collisions are
  rare and cleanly handled with a year suffix + alias.
- *Adjudication:* **(a)** (R5) — stem = canonical short name, `content/cases/` home (segregated from doctrine
  nav), year suffix + `aliases` only on collision. Cite/court/etc. live in **frontmatter**, not the slug.

### SI-2-S4 — Internal deep-link mechanism → **Fixed-heading anchors + reporter-keyed block ids.**
- *Options:* (a) rely on Quartz auto-slugged headings as-is; (b) **freeze the BIRAC heading text** so anchors are
  deterministic, with `#rule` as the canonical holding anchor + `^pin-<page>` block ids for quotes; (c) URL text
  fragments for internal links too.
- *Red-team (a):* auto-slugs drift if heading text changes, breaking inbound deep-links. *Red-team (c):* S3 R7
  established text fragments are **unreliable under Quartz SPA** for internal links. *Steel-man (b):* frozen
  headings give stable, human-legible anchors; reporter-keyed block ids let doctrine pages pinpoint the exact
  passage; SPA-safe; finalizes LINT-5.
- *Adjudication:* **(b)** (R6) — closes S1 §9 and satisfies S3's anchor requirement. External CL pinpoints still
  use text fragments (new-tab full load), per S3 R7.

### SI-3-S4 — Component data convention → **Frontmatter canonical + plain-markdown tables enhanced in place.**
- *Options:* (a) a bespoke code-fence DSL the components parse; (b) **frontmatter as canonical structured data +
  plain GFM tables that `CaseTable` enhances by slug-match**, Mermaid for flowcharts, optional non-load-bearing
  fenced directives only for generated widgets.
- *Red-team (a):* a DSL locks content into a component-only syntax — violates the R5-S3 portability guardrail.
  *Steel-man (b):* every page stays legible markdown if components are stripped or the site is ported; the case
  page's frontmatter is already the canonical record (R2), so components read it without new syntax.
- *Adjudication:* **(b)** (R9) — closes S3 §9. The Case Index + browser + cross-ref panel all derive from the
  frontmatter aggregate (R10); no S4–S8 deliverable hard-depends on a component to be readable.

### SI-4-S4 — Case Index: hand-maintained vs. generated → **Generated from case-page frontmatter.**
- *Options:* (a) keep the Index hand-curated; (b) **regenerate it from the aggregate of case-page frontmatter.**
- *Red-team (b):* a generator must preserve the human header prose + `type: index`. *Steel-man (b):* a
  hand-maintained index of 300 rows **drifts** from the pages it indexes — the exact L1 "decks derive from pages"
  hazard, one level up. Generating it makes the case pages the single source of truth and the Index a guaranteed-
  faithful projection (R1).
- *Adjudication:* **(b)** (R10) — build script aggregates frontmatter → Index table + component data index;
  regeneration is diff-clean; the header prose is preserved by the generator.

### SI-5-S4 — Migration verification gate → **Adopt the S1 §3.G find→adjudicate→fix machine, serial CL.**
- *Options:* (a) generate pages and spot-check; (b) run the full find→adjudicate→fix machine over generation.
- *Red-team (b):* heavier process for a generation pass. *Steel-man (b):* generation **asserts** ~261 cases'
  holdings, statuses, and quotes live — exactly the assertion surface the machine exists to discipline (L5/L4);
  reusing it (loop cap 3, DISMISSED-logged, escalation to `_review-needed/cases/`) is battle-tested and keeps S4
  consistent with S9.
- *Adjudication:* **(b)** (R12) — generate (serial CL, SR-1) → review (free) → adjudicate (serial CL for
  `needs_cl`) → fix; then regenerate the Index and wire doctrine-table links.

---

## Appendix B — Case object frontmatter schema (verbatim)

```yaml
---
title: "Brigham City v. Stuart"          # canonical short name == filename stem (+ " (YYYY)" only on collision)
type: case
citation: "547 U.S. 398 (2006)"          # Bluebook (U.S. Reports preferred)
parallel_cite: "126 S. Ct. 1943"         # optional parallel reporter
neutral_cite: ""                          # neutral / slip / vendor-neutral cite, if any
court: "U.S. Supreme Court"
court_level: scotus                       # scotus | circuit | state-high | district | state-app | other
circuit: ""                               # e.g. "10th" — REQUIRED when court_level: circuit (N2)
year: 2006
date_decided: 2006-05-22                  # optional ISO date
docket: "05-502"
authority_weight: "Binding — SCOTUS"      # EXACTLY one of the six S1 §3.D tiers (N2)
treatment:                                # orthogonal good-law axis (S1 §3.D, N13/N4)
  status: good                            # good | criticized | limited | abrogated | overruled
  as_of: 2026-06-29                       # N13 live-check date (R8 / SR-1)
  note: ""                                # e.g. "narrowed by Gant in vehicles"
  by: []                                  # ["[[Case]]"] that limit/abrogate/overrule (N4)
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145654/brigham-city-v-stuart/"
  opinion_id: 145654                      # lead opinion id (L3: cluster→opinion resolved)
  identity_checked: true                  # L3: named case confirmed in returned text
homes:                                    # home doctrine(s) + role per page (N1 placement / N6 multi-home)
  - page: "[[Emergency Aid]]"
    role: "Key — Anchor"                  # one of the S2 §3.3 eight roles
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Related (cross-doctrine)"
related: ["[[Michigan v. Fisher]]", "[[Mincey v. Arizona]]", "[[Caniglia v. Strom]]"]
aliases: []                               # name / spelling variants for L6-tolerant link resolution
tags: ["case", "fourth-amendment", "emergency-aid"]
---
```

**Required (non-empty) keys:** `title`, `type: case`, `citation`, `court`, `court_level`, `year`,
`authority_weight` (∈ six tiers), `treatment.status` + `treatment.as_of`, `courtlistener.opinion_url` +
`opinion_id` + `identity_checked: true`, `homes` (≥1, each with `page` + a valid `role`). `circuit` required
iff `court_level: circuit`. All others optional.

## Appendix C — BIRAC per-case page template (verbatim, filled with *Brigham City v. Stuart*)

> Heading text is **frozen** (R6) — anchors are `#background #issue #rule #application #conclusion #treatment
> #sources`. `#rule` is the canonical "the holding" deep-link target; pinpoint quotes carry `^pin-<page>` block
> ids. The header line is plain markdown (the `TreatmentBadge`/weight component enhances it; it degrades to this
> text). **Quotes are verbatim with a reporter pinpoint (L1). The Application is confined to this case's own
> facts (R4) — no generalized street takeaway.**

```markdown
---
# (Appendix-B frontmatter)
---

# Brigham City v. Stuart

*547 U.S. 398 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-29)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers responded to a 3 a.m. loud-party call, saw juveniles drinking in the yard, and through a screen
door watched a juvenile punch an adult in the kitchen. An officer announced his presence and entered to stop
the altercation; the occupants were arrested for offenses including disorderly conduct.

## Issue
May police make a warrantless entry into a home under the emergency-aid exception when their subjective intent
may have been to make an arrest?

## Rule
Yes. Police "may enter a home without a warrant when they have an **objectively reasonable basis for believing
that an occupant is seriously injured or imminently threatened with such injury**." — 547 U.S. at 400. ^pin-400
The "officer's subjective motivation is irrelevant." — *Id.* at 404. ^pin-404 The Fourth Amendment asks only
whether "the circumstances, viewed objectively, justify [the] action." — *Id.* (quotation omitted). ^pin-404b

## Application
The officers saw an ongoing assault — a juvenile striking an adult hard enough to draw blood — which supplied
an objectively reasonable basis to believe an occupant was injured or imminently threatened. Because the
standard is objective, any arrest motive did not defeat the entry; the entry and the announcement were
reasonable on these facts. *Id.* at 406.

## Conclusion
The warrantless entry was reasonable; the Utah Supreme Court's suppression was reversed. Subjective intent is
irrelevant to an objectively justified emergency-aid entry.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-29)* — **Binding — SCOTUS**.
- **Followed / applied by** [[Michigan v. Fisher]] (per curiam) — no ironclad proof required; objective basis
  judged at the moment of entry.
- **Home-entry caretaking limit:** [[Caniglia v. Strom]] — no *freestanding* community-caretaking entry into a
  home; welfare entries must route through emergency aid / exigency (does **not** disturb *Brigham City*).

## Appears on
- [[Emergency Aid]] — *Key — Anchor*
- [[Exigent Circumstances and Hot Pursuit]] — *Related (cross-doctrine)*

## Sources
- *Brigham City v. Stuart*, 547 U.S. 398 (2006) — https://www.courtlistener.com/opinion/145654/brigham-city-v-stuart/ — pinpoints: 400, 403, 404, 406.
```
