# SPEC S2 — Information Architecture & Category Taxonomy
status: APPROVED
depends-on: [S1]          gates: [S3, S4, S5, S6]
last-updated: 2026-06-30   <!-- 06-27 original; 06-30 cross-spec coherence amendments: Garrity OPTIONAL→CORE (D3-S2); deck-id supersession; final-page-inventory note -->

> Governed by `docs/STANDARDS.md` (S1, SR-3 supremacy). S2 **designs** the category tree,
> the case-homing rules, the case-table role set, and the **project-scope decision that gates
> S5**. S2 moves no files and authors no content — the folder mechanics execute in S3/S4 and
> the page re-homing/splitting executes in S6. Where S2's research touched live law it ran
> through the single serial CourtListener lane (L4) with web as discovery-only (L2).

---

## 1. Objective

Define the site's **information architecture**: (a) a parent→child **category tree** in our own
voice, organized around the source book's I–XIII spine so the site mirrors how the instructor
teaches, with every current page and obvious gap assigned a primary home; (b) the **case-homing
algorithm** (placement-by-holding, N1) and the **multi-homing rule** (N6); (c) the complete
**case-table role set** every case can occupy on a page (N5/N6); and (d) the **page
split/merge/create list**. S2 also **settles the project-scope decision** (§2) that S5 reads to
define what a "missed case" is.

## 2. Scope

### 2.0 PROJECT-SCOPE DECISION — **[USER, gates S5]** Whole-book *structure*, suppression-core depth

**Decision:** Organize the taxonomy around the book's **13-part spine** (so the site mirrors the
instructor's teaching order), **but concentrate authored, instructor-grade depth on the 4A core
plus the suppression adjacencies the site already covers.** Far-flung, non-suppression material
is carried as **OPTIONAL/SECONDARY** — represented in the structure and (at most) as Case-Index
entries or brief mentions, **not** as required doctrine pages, and **not** counted as "missed
cases" that block S5 coverage completion.

This is **not** literal book-completeness (option rejected) and **not** 4A-only (option rejected).
The two coverage tiers below are the **contract S5 reads**:

| Tier | Meaning for S5 | What it covers |
|---|---|---|
| **CORE** | The "missed case" universe. S5 must ingest + live-verify (SR-1) every case; doctrine pages authored to instructor-grade depth (SR-2). | Book I–VIII (the full 4A search/seizure spine); Book IX **Miranda/voluntariness suppression line**; Book X **6A counsel-at-interrogation + lineups**; Book XI **Use of Force**; Book XII **§1983/QI + Brady/Giglio**. |
| **OPTIONAL / SECONDARY** | Not required pages; not "missed cases." May appear as Case-Index rows or brief mentions; promoted to a page only on explicit later request. | Book IX 5A **immunity** (Kastigar, Murphy), grand-jury/testimonial-production (Hubbell, Doe); Book X **Confrontation Clause** (Melendez-Diaz, Bullcoming, Bryant — a trial-evidence doctrine, not suppression); Book XII broader **Bivens progeny** beyond §1983/QI/Brady (Reichle, Wood v. Moss, Millbrook); Book XIII **"Other Cases"** (Snyder v. Phelps, Sanchez-Llamas). |

> **⚠ Amendment (2026-06-30 · supersedes the original OPTIONAL tag) — the government-employee 5A /
> *Garrity* cluster is CORE, not OPTIONAL.** Per **S5 · U2-S5 / R11**, the *Garrity* line (Garrity,
> Gardner, Kalkines, Lefkowitz, LaChance, NASA v. FLRA + controlling progeny) is ingested as **CORE**
> case pages on **audience-relevance** grounds (the students *are* the public employees) and homed to a
> new doctrine page **"Public-Employee Compelled Statements (Garrity)"** under category #9 (authored in
> S6 · R9). The rest of Book IX 5A immunity / grand-jury / testimonial-production stays OPTIONAL. This is
> the **one** case-level deviation from the table above; see Appendix A · **D3-S2**.

The book → category crosswalk (with tier tags) is in **§6.3** *(the §6.3 Book-IX row carries the same
Garrity-CORE carve-out)*.

### 2.1 In scope (S2 designs)
- The **category tree** (top-level parents + children, ≤2 levels, 3 only in the warrant-exceptions
  cluster), with a **primary home for every current page** and named gaps (§6.1).
- The **case-homing algorithm** (N1) + **multi-homing rule** (N6) (§3.1–3.2).
- The **case-table role set** (N5/N6) and which roles a circuit/state case may hold (§3.3).
- The **page split/merge/create list** with rationale (§6.2).
- The **folders-for-nav + `category`/`tags`-for-cross-cutting** model (§3.4) and the
  **slug/deck-id stability** constraints it must honor (D-3/D-6).
- The **book I–XIII → category crosswalk** with CORE/OPTIONAL tiers (§6.3).

### 2.2 Out of scope (owned elsewhere)
- **Physically moving files / creating folders / writing redirects/aliases** and the final
  Explorer-vs-frontmatter nav mechanism → **S3** (Platform & Nav/UX).
- The **per-case page skeleton, slug scheme, anchors, and deck-id migration mechanics** → **S4**.
- **Authoring/splitting/re-homing actual page content** (incl. the Community Caretaking ⇄
  Emergency Aid split execution) → **S6**; **ingesting + verifying the CORE case universe** → **S5**.
- The **standards/lexicon/verification machine** → **S1** (`docs/STANDARDS.md`), which S2 obeys.

---

## 3. Requirements (numbered, testable)

### 3.1 — Case-homing algorithm (R1, enforces N1)
A case's **primary home** is assigned by this deterministic ladder; each step is testable:
1. **Placement by holding, not keyword (N1).** Primary home = the doctrine page whose
   **black-letter rule the case establishes or principally defines** — the proposition it is the
   *ratio* for — never surface-keyword overlap. *(Test: Matlock → Consent/common-authority, not
   Abandonment; Cady → Community Caretaking, not Automobile Exception; Carpenter → The Third-Party
   Doctrine (Key), not Border.)*
2. **Multi-doctrine cases:** if a case states rules for several doctrines, primary home = the
   doctrine for which it is the **leading authority**; it is **Key** there and multi-homed (R2).
3. **SCOTUS never to Recent-developments (N5):** any SCOTUS holding homes to the doctrine page as
   a **Key** case regardless of date.
4. **Seed augmentation (S1 §3.F):** the foundational SCOTUS authority a doctrine rests on is added
   to that doctrine's seed even if uncaptured (Chimel→SITA, Schneckloth→Consent).
5. **Minor/illustrative cases** with no page of their own appear as a **case-table row** on the
   governing doctrine page + a **Case-Index** row, homed by holding.
6. **Tie-break:** when two doctrines both claim a case, home by the **proposition the wiki cites
   it for**; primary = the page where that proposition is the case's ratio.
- *Check:* every case placement on every page traces to the proposition the case stands for
  (CHECKLIST:D2/D5); zero keyword-only placements.

### 3.2 — Multi-homing rule (R2, enforces N6)
A case may be **Key on more than one page** if central to each doctrine; **key-status is
non-exclusive**, decided **per-page by centrality to THAT doctrine**, and framing is
page-specific. Across all homes the case carries a **consistent** good-law treatment status (N13)
and **consistent** subsequent-treatment tag (N4); the case's own **case page (S4)** is the
canonical record and every doctrine mention links to it (N7).
- *Check:* multi-homed cases show page-specific framing but identical treatment status + N4 tag
  everywhere (CHECKLIST:D5); no doctrine page silently contradicts another.

### 3.3 — Case-table role set (R3, enforces N5/N6)
Every case on a doctrine page occupies exactly one **role** drawn from this fixed set (the
brief-first template's Key-cases / Related / Recent-developments apparatus, S1 §3.I):

| # | Role | Where it appears | Who may hold it |
|---|---|---|---|
| 1 | **Key — Anchor** | Key cases | the case that establishes the page's black-letter rule (SCOTUS; or the leading circuit case where SCOTUS is silent) |
| 2 | **Key — Progeny / Refinement** | Key cases | a case that refines/extends/cabins/applies the anchor and is central to teaching it (Gant↔Belton; Carpenter↔Katz) |
| 3 | **Related (cross-doctrine)** | Related cases | a case central to *another* doctrine that bears here, framed for this page (Riley as Related on Common Law) |
| 4 | **Limits / Narrows** | Key or Related, with N4 tag | a case that materially narrows the doctrine; carries inline "limited by [case]" (Caniglia↔Cady; Lange↔Santana) |
| 5 | **Illustrates a circuit split** | Related / Recent-developments | circuit/state case marking a split; circuits **named**; persuasive-tier; flagged (Cotterman/Cano vs Touset) |
| 6 | **First-impression (circuit/state)** | Recent-developments | circuit/state case deciding a not-yet-SCOTUS question; role-labeled |
| 7 | **Recent development (role-based)** | Recent-developments | circuit/state case that expands/narrows/splits vs SCOTUS — **never a SCOTUS case** (N5) |
| 8 | **Historical / origin** | Sources / inline | English-colonial origin, or overruled case shown as history (lexicon tier 6) |

**Which roles a circuit/state case may hold (instructor's note):** a circuit/state high-court case
may be **Key** *only* when it is the **leading authority on a question SCOTUS has not decided**
(novel / first-impression) **or** the controlling in-circuit rule the page teaches; otherwise it
appears as **Related**, **Illustrates-a-split**, **Limits/Narrows**, or **Recent-development**. It
is never labeled nationwide-binding (N2 lexicon: *Binding in-circuit* / *Persuasive*). A SCOTUS
case is **never** demoted to Recent-developments (N5; AUTO:LINT-3).
- *Check:* every case-table entry carries one role from the set; no SCOTUS case in
  Recent-developments; circuit Key cases are first-impression/in-circuit-controlling only.

### 3.4 — Categories = folders-for-nav + cross-cutting field (R4) **[USER]**
Adopt a **real folder hierarchy** under `content/` to drive the left-nav Explorer + breadcrumbs
(one **primary home** = one folder per page), **plus** a **`category`/`tags` frontmatter field**
for cross-cutting / multi-homed membership (a page conceptually in a second bucket is *tagged*,
not duplicated). Hard constraints (D-3/D-6), each testable:
- **Filenames stay stable** so Quartz's filename-based wikilink resolution keeps every `[[Page]]`
  working after a folder move (no rename of the file stem).
- ~~**Flashcard deck ids stay stable**; any page whose slug/path changes has its deck `page`/`tags`
  fields realigned **losslessly** (card ids unchanged, FSRS progress preserved — D-6).~~ **[SUPERSEDED
  by S4·R11 / U3-S4 (and U5-S9):** the deck-id / FSRS-progress half of D-6 is **dropped** — **no deck
  surgery anywhere in the overhaul**; the **file-stem (wikilink) half of D-3/D-6 above is retained**, and
  the decks are purged + regenerated from the finalized pages in a **separate later run**. So no deck
  realignment is performed during the IA restructure.**]**
- **No broken inbound links:** moved/renamed/split pages get **aliases** (and S3 redirects) so old
  paths and `[[old title]]` wikilinks resolve.
- *Check:* post-restructure, zero broken wikilinks (AUTO, links resolve); zero orphaned deck ids;
  Explorer tree depth ≤3 (§3.5). *Mechanics (move vs virtual group, redirect form) finalized in S3.*

### 3.5 — Tree depth (R5) **[USER]**
Target **2 levels** (parent → child). A **3rd level is permitted only** in the
**Exceptions to the Warrant Requirement** cluster, where the book's own *PC-needed / PC-not-needed*
split genuinely aids navigation (§6.1 #7). No other branch exceeds 2 levels.
- *Check:* exactly one 3rd-level branch (the exceptions cluster); every other path ≤2 deep.

### 3.6 — Community Caretaking ⇄ Emergency Aid split (R6) **[USER, research-driven]**
The bundled page **`Community Caretaking and Emergency Aid` SPLITS into two pages** (§6.2),
scoped by the recalibrated authority (Appendix A · D2-S2; S1 · L7):
- **Emergency Aid** — home/premises *entry* to render aid on an objective basis (*Brigham City v.
  Stuart*, *Michigan v. Fisher*, *Ryburn v. Huff*); **Caniglia** stated as the controlling limit
  (no freestanding community-caretaking entry into the home). Field-decisive question (N9):
  *"Someone inside may be hurt — may I enter?"*
- **Community Caretaking** — the **non-home** doctrine, **scope stated explicitly** (N10) with two
  **labeled strands**: **(a)** vehicles/roadside/impound (*Cady v. Dombrowski*; cross-link
  inventory); **(b)** caretaking & welfare **seizures of persons in public** (*United States v.
  Garner* 10th-Cir. 3-part test; *United States v. Rideau* 5th-Cir.; emergency mental-health
  seizure → **probable cause of dangerousness**, *Graham v. Barnette* 8th-Cir.; the *Caniglia*
  "category error" caveat on the label). Tests stated up front (N3); cross-linked from **Seizure
  of the Person** (these are caretaking-justified seizures, placed by holding — N1 — not
  crime-suspicion Terry stops).
- *Check:* both pages exist; each states its scope explicitly (vehicles / persons-in-public /
  home-barred); *Caniglia* limit appears on both; deck ids preserved across the split (R4).

### 3.7 — Book-spine fidelity + own voice (R7)
The top-level categories **track the book's I–XIII major movements** (so the site mirrors the
teaching order) but are **named in our own voice** — neither copied verbatim nor gratuitously
divergent — and the **§6.3 crosswalk** maps every book Part to its category(ies) + coverage tier.
- *Check:* every book Part I–XIII maps to ≥1 category in §6.3; each category name is justified.

---

## 4. Lessons enforced

- **N1** (placement-by-holding) → the R1 homing ladder. **N6** (non-exclusive key-status) → R2
  multi-homing + R3 role set. **N5** (role-based recent-developments; no SCOTUS there) → R3 +
  LINT-3. **N10** (state scope explicitly; split bundled doctrines) → R6 caretaking split + the
  explicit-scope requirement on the Community Caretaking page. **N9** (field-decisive framing) →
  R6 page framing. **N3** (tests up front) → R6 (Garner 3-part / PC-of-dangerousness stated up
  front). **N7** (link every case) → R2 (every doctrine mention links the case page). **N13/N4**
  (consistent treatment/subsequent-tag across homes) → R2 cross-page consistency.
- **L7** (scope-boundary claims are two-key assertions — *added to S1 during this interview*) is
  the rule this interview's own community-caretaking research vindicated; R6 and §6.2 embody it,
  and Appendix A · D2-S2 logs the recalibration.
- **L2/L4** (web discovers, serial CL confirms) governed S2's caretaking research (Appendix A · D2-S2).
- **D-3/D-6** (slug + deck-id stability) → R4 constraints.

## 5. Method (how execution proceeds against this spec)

1. **S3** builds the nav from §6.1: creates the folder hierarchy (or virtual Explorer grouping),
   wires breadcrumbs, and writes redirects/aliases for any moved/split slug — honoring R4
   (filenames stable, links resolve).
2. **S4** defines the per-case page skeleton + slug scheme + the **deck-id-stable** migration for
   the Community Caretaking split, consuming R6 + R4.
3. **S5** reads **§2.0 + §6.3**: the CORE crosswalk is the "missed-case" universe to ingest +
   live-verify (SR-1); OPTIONAL/SECONDARY items are not gating.
4. **S6** executes the **§6.2 split/merge/create list** and re-homes every case per the **R1/R2/R3**
   rules into the brief-first template, applying the role set to each case table.
5. Every stage **cites `docs/STANDARDS.md`** as governing (SR-3) and routes any CL work through the
   single serial lane (L4).

## 6. Deliverables (the concrete IA — S4–S6 execute against these)

### 6.1 — Target category tree (primary homes; ≤2 levels, 3 only in #7)

```
content/
├── (root)  index.md  ·  flashcards.md
│
├── 1 · Foundations & History
│     └── Common Law Origins
│
├── 2 · Legal System, Research & Reference
│     ├── The Federal Court System
│     ├── Legal Research and Case Citations
│     ├── Common Legal Terms        (glossary — terms, not cases)
│     └── Case Index                (router — every verified case → cite · holding · good-law · CL · home)
│
├── 3 · What Is a Search?            (Book I)        [flat — 2 levels; protected-areas pages sort adjacent, no subfolder]
│     ├── Fourth Amendment Framework         (incl. state-action / private-search)
│     ├── Two Definitions of Search          (trespass + privacy)
│     ├── The Third-Party Doctrine and Digital Surveillance   (Smith/Miller/Carpenter/Kyllo — Book I "Third-Party Control")
│     ├── Fourth Amendment Recalibration      (synthesis: the technology + incorporation arc — cross-link #1)
│     ├── Fourth Amendment Analysis Checklist
│     ├── CREW                                (justifications framework — primary home; referenced from #12)
│     ├── Curtilage                           (incl. open fields)     ┐
│     ├── Tents                                                       │ protected-areas trio
│     └── Abandonment                                                 ┘ (adjacent, not a 3rd level)
│
├── 4 · What Is a Seizure?           (Book II)
│     ├── Seizure of the Person              (show-of-authority / Mendenhall / Hodari / Torres)
│     ├── Terry Stops and Reasonable Suspicion   (incl. the protective frisk of a person)
│     ├── Traffic Stops
│     ├── Arrest in the Home                 (Payton/Steagald/Harris/Lange — tagged: warrant-exceptions)
│     └── Collective Knowledge and the Fellow-Officer Rule   (Whiteley; Hensley)
│
├── 5 · Levels of Suspicion          (Book III)
│     └── Probable Cause and Reasonable Suspicion
│
├── 6 · The Warrant Requirement      (Book IV)
│     └── The Warrant Requirement     (PC · particularity · neutral magistrate · Franks · knock-&-announce · anticipatory)
│
├── 7 · Exceptions to the Warrant Requirement     (Books V–VI)   [3rd level — the one place it earns its keep]
│     ├── 7a · Probable-Cause Exceptions          (Book V — "PC Needed")
│     │     ├── Plain View Doctrine
│     │     ├── Automobile Exception
│     │     ├── Exigent Circumstances and Hot Pursuit
│     │     ├── Emergency Aid              ← NEW (split)
│     │     └── Community Caretaking       ← NEW (split, re-scoped: vehicles + persons-in-public)
│     └── 7b · Suspicion-Based / Per-Se Exceptions   (Book VI — "PC Not Needed")
│           ├── Search Incident to Arrest          (incl. booking/inventory cross-link)
│           ├── Consent Searches
│           ├── Knock and Talk
│           ├── Special Needs and Administrative Searches   (checkpoints · schools · probation/parole · admin · inventory)
│           ├── Border Searches
│           └── Securing the Scene                  (protective sweep Buie · Summers/Muehler/Bailey detentions · McArthur freeze)
│
├── 8 · The Exclusionary Rule, Standing & Remedies   (Book VII)
│     ├── The Exclusionary Rule        (suppression + good-faith / attenuation / independent-source / inevitable-discovery)
│     └── Standing to Challenge a Search
│
├── 9 · Confessions, Interrogation & Identifications   (Books IX–X, suppression line)
│     ├── Due-Process Voluntariness of Confessions
│     ├── Miranda and Custodial Interrogation
│     ├── Miranda Waiver and Invocation
│     ├── Sixth Amendment Right to Counsel
│     └── Eyewitness Identification     (Wade/Gilbert lineups + Biggers/Manson/Perry due-process IDs)
│
├── 10 · Use of Force, Liability & Disclosure   (Books XI–XII)
│     ├── Use of Force                  (Graham/Garner/Scott/Plumhoff — cross-linked from #4)
│     ├── Section 1983 Liability and Qualified Immunity
│     └── Brady and Giglio
│
├── 11 · Adjacent Doctrines            (Book VIII/XIII + defenses — labeled non-suppression; OPTIONAL depth)
│     └── Entrapment
│
└── 12 · Instructor Craft & Study
      ├── Three Golden Rules
      ├── Instructor Development
      └── (CREW referenced here as a mnemonic; flashcards.md at root)
```

**Coverage check:** all **46** content files are assigned above — 44 doctrine/reference pages +
`index.md` (root MOC) + `flashcards.md`; the one bundled caretaking page splits into two, giving
**45 doctrine/reference pages** post-split. No page is unassigned; **only #7 reaches depth 3** (R5);
every other branch is ≤2.

> **Final-page-inventory note (added 2026-06-30, cross-spec coherence pass).** This tree predates two
> later spec decisions; the **executor must fold them in** when it builds the actual folders:
> (1) **S8 splits** `Legal Research and Case Citations` into **three** pages — *Reading & Citing Cases*,
> *Free & Low-Cost Research Tools*, *Verifying Good Law* — all homed under **#2 · Legal System, Research
> & Reference** (replacing the single entry; old slug aliased to *Reading & Citing Cases*);
> (2) **S5/S6 add** the new **"Public-Employee Compelled Statements (Garrity)"** doctrine page under
> **#9** (D3-S2 / S6·R9). So the **count is approximate and runtime-determined** — the prior-state
> "43 pages" (context pack) vs. "46 files" here is reconciled by **enumerating `content/*.md` live** at
> execution (S2·§8 step 1) and assembling the canonical post-overhaul page list from: this tree **+** the
> S8 three-way split **+** the Garrity page **+** the caretaking split **+** every `content/cases/*`
> page (S4/S5). No single spec holds the final inventory; the executor assembles it.

### 6.2 — Page split / merge / create list

| Action | Page(s) | Rationale | Constraints |
|---|---|---|---|
| **SPLIT** | `Community Caretaking and Emergency Aid` → **`Emergency Aid`** (NEW) + **`Community Caretaking`** (re-scoped) | N10 / L7 — three legally distinct things were bundled; recalibrated research (Cady vehicles · Garner/Rideau/Graham persons-in-public · Caniglia home-barred). | Alias the old title; **zero broken inbound links**. Execution = S6. **~~Preserve deck card ids; re-home cards losslessly.~~ [SUPERSEDED by S4·R11 / U5-S9:** no deck migration — decks are frozen through the overhaul; the dangling `page:` resolves via the S3 alias until the **separate later** page-derived rebuild.**]** |
| **MERGE** | *(none)* | The two Miranda pages stay distinct (deliberate, deck-aligned). | — |
| **RENAME** | *(none — file stems frozen)* | D-3/D-6 slug + deck-id stability. The split adds new slugs; it does not rename existing stems. | New pages get clean kebab-case slugs (S4). |
| **CREATE (now)** | `Emergency Aid`, `Community Caretaking` | The split above. | — |
| **DISTRIBUTE (not new pages)** | Book VIII "Related Issues" + parts of XIII | Whren→Traffic Stops; Hiibel/Kolender→Terry Stops; Gerstein/Riverside (prompt presentment)→Arrest in the Home; Zurcher→Warrant Requirement. | Homed by holding (R1); appear as case-table rows + Case-Index, not new pages. |
| **WATCH (possible future split)** | `The Warrant Requirement` | Dense (PC · particularity · Franks · knock-&-announce · anticipatory). | Keep as one page now; if it balloons past the ½–1-page budget in S6, split knock-&-announce out (a permitted 3rd-level move). Flagged, not executed. |
| **OPTIONAL/SECONDARY (deferred)** | Confrontation Clause · 5A immunity · gov't-employee Miranda · broader Bivens progeny · Snyder/Sanchez-Llamas | §2.0 scope — not "missed cases"; promote to pages only on explicit request. | Case-Index rows at most. |

### 6.3 — Book I–XIII → category crosswalk (with coverage tier)

| Book Part | Our category (§6.1) | Tier |
|---|---|---|
| I. What Is a Search? | 3 · What Is a Search? | CORE |
| II. What Is a Seizure? | 4 · What Is a Seizure? (+ Arrest in the Home) | CORE |
| III. Levels of Suspicion | 5 · Levels of Suspicion | CORE |
| IV. Search Warrants | 6 · The Warrant Requirement | CORE |
| V. Warrant Exceptions — PC Needed | 7a · Probable-Cause Exceptions | CORE |
| VI. Warrant Exceptions — PC Not Needed | 7b · Suspicion-Based / Per-Se Exceptions | CORE |
| VII. Exclusionary Rule | 8 · Exclusionary Rule, Standing & Remedies | CORE |
| VIII. Related S&S Issues | *distributed* into #4/#6/#7 by holding | CORE-distribute |
| IX. The Fifth Amendment | 9 · Confessions… (Miranda/voluntariness) | CORE; immunity/Garrity/production = OPTIONAL |
| X. Sixth Amendment Right to Counsel | 9 · Confessions… (counsel + lineups) | CORE; Confrontation Clause = OPTIONAL |
| XI. Use of Force | 10 · Use of Force, Liability & Disclosure | CORE |
| XII. Liability | 10 · … (§1983/QI + Brady) | CORE; broader Bivens progeny = OPTIONAL |
| XIII. Other Cases | 11 · Adjacent Doctrines / distribute | OPTIONAL/SECONDARY |

## 7. Acceptance criteria (definition of done)

- [ ] The **project-scope decision** (§2.0) is recorded as whole-book-structure / suppression-core
      depth, with the **CORE vs OPTIONAL** tiers defined and the **§6.3 crosswalk** present — S5 can
      read a precise "missed-case" universe.
- [ ] The **category tree** (§6.1) assigns a **primary home to every content file** (46: 44
      doctrine/reference pages + index + flashcards) and to the caretaking split; **no page
      unassigned**; depth ≤2 everywhere **except** the single #7 exceptions cluster (≤3) (R5).
- [ ] The **case-homing algorithm** (R1, N1) and **multi-homing rule** (R2, N6) are stated testably.
- [ ] The **case-table role set** (R3) lists all 8 roles + the circuit/state-case rule (no SCOTUS in
      Recent-developments).
- [ ] The **Community Caretaking ⇄ Emergency Aid split** (R6) is specified with the re-homing cases
      and the explicit scope (vehicles / persons-in-public / home-barred), citing Cady · Garner ·
      Rideau · Graham · Caniglia.
- [ ] The **folders + `category`/`tags`** model (R4) is fixed with the **slug + deck-id stability**
      constraints (D-3/D-6) and the zero-broken-link requirement.
- [ ] The **split/merge/create list** (§6.2) is concrete enough for S6 to execute.
- [ ] **L7 cross-reference** present; the caretaking recalibration logged in Appendix A.

## 8. Verification plan (how S2 itself is checked — free, no-CL)

1. **Coverage:** enumerate `content/*.md`; confirm each maps to exactly one primary home in §6.1;
   flag any unassigned page. (The split is the only structural change to the page set.)
2. **Depth invariant:** confirm only the #7 branch reaches level 3; all others ≤2 (R5).
3. **Homing soundness (spot-check):** Matlock→Consent, Cady→Community Caretaking, Carpenter→The
   Third-Party Doctrine (Key, Related on Two Definitions), Riley multi-homed (Key on SITA, Related
   on Common Law) — each justified by holding (R1/R2), not keyword.
4. **No-SCOTUS-in-recent-developments** is expressible against the role set (R3 ↔ LINT-3).
5. **Stability:** confirm no existing file stem is renamed (D-3); confirm the split names a
   deck-id-preserving path (D-6) and an alias for the old title (R4).
6. **Scope contract:** confirm §6.3 maps every book Part I–XIII and tags each CORE/OPTIONAL so S5
   has no ambiguity.
7. **Non-regression vs `DECISIONS.md`:** S2's tree extends D-3's working taxonomy (does not reverse
   it); the Case-Index router (D-2) and federal/state guardrail are preserved.

## 9. Open items / escalations

- **Slug-vs-alias mechanics for the caretaking split** (keep old slug as the Community-Caretaking
  continuation + new Emergency-Aid slug, vs. two new slugs + redirects) → **S3/S4** decide; S2 fixes
  only the requirement (deck-id + link preservation, explicit scope split).
- **Folder move vs. virtual Explorer grouping** (whether to physically relocate files under
  `content/<n>-…/` or drive the tree from frontmatter without moving files) → **S3**. Either honors
  R4 if filenames stay stable.
- **`The Warrant Requirement` possible split** (knock-&-announce / particularity) → re-evaluated in
  **S6** against the ½–1-page budget; flagged in §6.2, not decided now.
- **OPTIONAL/SECONDARY promotion** (Confrontation Clause, 5A immunity, etc.) → only on explicit user
  request; otherwise Case-Index rows. Non-blocking for S5.
- **L7 amendment to S1** was made during this interview (S1 · Appendix A · SI-6). If the user prefers
  L7 live only as an S2 recommendation rather than in S1, revert the S1 edit; S2 still references it.

---

## Appendix A — Decision log

*Format: Question · Options · Red-team · Steel-man · Adjudication. **[USER]** = the user's actual
choice; the rest are self-interviewed.*

### [USER] U1-S2 — Project scope (gates S5) → **Whole-book *structure*, suppression-core depth.**
- *Options:* (a) 4A-complete only; (b) current scope + adjacencies; (c) whole book I–XIII (literal);
  (d) whole-book *structure*, suppression-core depth.
- *Discussion:* The user first leaned to "whole book I–XIII," then clarified the intent on follow-up:
  **mirror the book's 13-part spine in the taxonomy** (so the site matches how he teaches), **but
  keep authored depth on the 4A core + the suppression adjacencies already on the site**, treating
  far-flung XIII/Confrontation/immunity material as **optional/secondary**.
- *Red-team (literal c):* ingesting + live-verifying (SR-1) every case in I–XIII — Confrontation
  Clause, 5A immunity, the full Bivens line, Snyder v. Phelps — balloons the CL load and drifts off a
  search-&-seizure-instructor's remit. *Steel-man (a/b):* cleaner thesis, but (a) orphans existing
  5A/6A/ID/force/Brady pages + decks, and (b) alone loses the book-faithful teaching order.
- *Adjudication:* **(d)** — the **§6.3 crosswalk** carries the full I–XIII spine; the **CORE vs
  OPTIONAL tiers (§2.0)** give S5 a precise, bounded "missed-case" universe. Best of both: structure
  mirrors the book; rigor concentrates where the course actually teaches.

### [USER] D2-S2 — Community-caretaking scope + page split → **Two pages, labeled strands** (recalibrated).
- *Question:* Does community caretaking reach **persons outside the home**, and how should the bundled
  page split?
- *Research (web discovers, serial CL confirms — L2/L4):* **Cady v. Dombrowski, 413 U.S. 433 (1973)**
  (cluster 108850) — caretaking born in the **vehicle**. **Caniglia v. Strom, 593 U.S. 194 (2021)**
  (cluster 4883694) — **no freestanding caretaking exception for the home**; cabins Cady to vehicles
  but **expressly reserves** emergency psychiatric seizures. Frontier (Hop-2): **United States v.
  Garner, 416 F.3d 1208 (10th Cir. 2005)** (cluster 166206) — caretaking **detention of a person** on
  a **3-part test** (articulable facts · interest-balance · scope/duration tailored), independent
  justification needed once the welfare concern is resolved; **United States v. Rideau, 969 F.2d 1572
  (5th Cir. 1992) (en banc)** (cluster 587275) — impaired person in the roadway, public-welfare
  function; **Graham v. Barnette, 5 F.4th 872 (8th Cir. 2021)** (cluster 4900401) — post-Caniglia the
  "community caretaking" **label** for psychiatric seizures is a "**category error**," but brief
  emergency detentions remain reasonable and a **serious** mental-health seizure needs **probable
  cause of dangerousness** (broad circuit agreement).
- *Red-team (the first, narrow framing "vehicles, not persons"):* it was drawn from secondary
  *Caniglia* summaries and **failed** — the circuit person-caretaking line is real and controlling in
  its circuits. *Steel-man (recalibrated):* caretaking **of persons** outside the home is good law but
  bounded — safety-purpose, articulable-facts, scope/duration-limited, ratcheting to PC-of-dangerousness
  for serious mental-health seizures; the home is barred (Caniglia); the *label* is contested.
- *Adjudication:* **Split into two pages** (R6/§6.2): **Emergency Aid** (home entry) + **Community
  Caretaking** (non-home, explicitly scoped to *vehicles* **and** *persons-in-public*, strands
  labeled, tests up front, Caniglia limit on both). Cross-linked from Seizure of the Person. The
  framing miss itself was generalized into **S1 · L7** (scope-boundary claims are two-key assertions).

### SI-1-S2 — Top-level structure: book spine vs. existing MOC vs. fresh → **Evolve the MOC toward the book's I–XIII spine, in our voice.**
- *Options:* (a) keep the existing 12-bucket MOC; (b) adopt the book's 13 Parts verbatim; (c) evolve
  the MOC so top-level parents track the book's major movements, renamed in our voice + a crosswalk.
- *Red-team (b):* the book bundles arrests+stops under "Seizure" and splits exceptions across two
  long Parts — copied verbatim it reads like a table of contents, not a navigable wiki; the book has
  no Foundations/Research/Instructor apparatus the site needs. *Red-team (a):* drifts from the
  teaching order the scope decision asked to mirror.
- *Steel-man (c):* the user wants the site to **mirror how he teaches from the book** *and* be "easy
  to navigate, makes sense at first glance"; (c) keeps the recognizable I–XIII movements as parents,
  brackets them with the apparatus buckets, and documents fidelity via §6.3.
- *Adjudication:* **(c)** — §6.1 tree (12 parents tracking I–XIII + apparatus) with the §6.3 crosswalk.

### SI-2-S2 — Where does the 3rd level go? → **Only the Exceptions cluster (PC-needed / PC-not-needed).**
- *Options:* (a) strictly 2 levels everywhere; (b) 3 levels only in the exceptions cluster; (c) 3
  levels freely. *Red-team (a):* forces ~11 exception pages into one flat list — the site's largest
  bucket becomes the hardest to scan. *Red-team (c):* deeper tree, worse first-glance scannability.
- *Steel-man (b):* the book itself splits exceptions into **V (PC-needed)** and **VI (PC-not-needed)**
  — a split officers already think in; a 3rd level *here* mirrors the book and tames the big bucket
  while every other branch stays flat. *Adjudication:* **(b)** (R5; user-confirmed depth target).

### SI-3-S2 — Homing the arrests + use-of-force pages (book vs. existing site).
- *Question:* The book files **arrests** under "Seizure" (II) and **Use of Force** under its own Part
  XI; the existing site filed Arrest-in-the-Home and Traffic Stops under "exceptions" and paired
  Use-of-Force with seizures.
- *Adjudication (N1 placement-by-holding):* **Arrest in the Home + Traffic Stops → #4 What Is a
  Seizure?** (their holdings are seizure/arrest rules — Payton/Steagald/Whren), cross-tagged to
  warrant-exceptions; their exigency routes (Santana/King/Lange) cross-link #7a. **Use of Force →
  #10** (Books XI–XII accountability bucket, mirroring the book's standalone Part XI), cross-linked
  from #4 since force *is* a seizure. **Protective frisk of a person** stays on **Terry Stops**;
  **Securing the Scene** (Buie sweep · Summers/Bailey detentions · McArthur freeze) homes to **#7b**.

### SI-4-S2 — Case-table role set: minimal vs. explicit.
- *Options:* (a) just "Key / Related"; (b) the explicit 8-role set with a circuit/state-eligibility
  rule. *Red-team (b):* more vocabulary to maintain. *Steel-man (b):* N5/N6 + the instructor's note
  demand role precision — "Key (anchor)" vs "Key (progeny)" vs "Limits/Narrows" vs "Recent-development
  (role-based)" are different teaching objects, and the **no-SCOTUS-in-recent-developments** invariant
  (LINT-3) needs the roles named. *Adjudication:* **(b)** — the §3.3 table; reused by S6 per page.

### SI-5-S2 — CREW (and other multi-bucket pages): duplicate or tag?
- *Options:* (a) duplicate the page into each bucket; (b) one primary folder home + cross-cutting
  tag/`related`. *Red-team (a):* duplicate files drift and split deck ids. *Steel-man (b):* the R4
  folders-for-nav + tags-for-cross-cutting model exists exactly for this — CREW's primary home is
  **#3** (framework); it's *referenced* from **#12** via tag/`related`, never copied. *Adjudication:*
  **(b)** — one file per page; multi-homing lives in tags + the `related:` field + case-table roles,
  not in duplicate files.

### [USER] D3-S2 — *Garrity* / government-employee 5A: OPTIONAL or CORE? → **CORE (amends §2.0).** *(Added 2026-06-30, cross-spec coherence pass.)*
- *Question:* S2 §2.0 originally tagged "government-employee Miranda/*Garrity*" **OPTIONAL**, but the
  later S5 interview (**U2-S5**) promoted the *Garrity* cluster to **CORE** (full case pages + a new
  doctrine page) on audience-relevance grounds and said it "supersedes S2 §2.0's OPTIONAL tag," with
  S5/S6 recommending a one-line S2 cross-ref "at execution." During the cross-spec coherence pass this
  left a live contradiction in the scope contract S5 reads. Record it in S2 now, or defer to execution?
- *Options:* (a) **amend S2 §2.0 now** (mark the *Garrity* cluster CORE with a cross-ref); (b) leave the
  execution-time cross-ref (contradiction persists in the specs until then).
- *Red-team (a):* edits an APPROVED spec. *Steel-man (a):* the decision is already settled (U2-S5);
  recording it now makes the scope contract self-consistent so no executor reconciles a contradiction
  mid-run — exactly the kind of cross-spec drift the coherence pass exists to remove.
- *Adjudication:* **(a)** — the **⚠ Amendment note** added to §2.0 marks the *Garrity* cluster **CORE**
  (homed to "Public-Employee Compelled Statements (Garrity)" under #9; case pages + doctrine page per
  S5·R11 / S6·R9); the rest of Book-IX 5A immunity stays OPTIONAL. **User chose (a)** (cross-spec
  coherence pass). S2 remains APPROVED; additive amendment.
