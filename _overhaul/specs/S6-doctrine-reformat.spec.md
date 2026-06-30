# SPEC S6 — Doctrine & Page Re-format (brief-first)
status: APPROVED
depends-on: [S1, S2, S4, S5]          gates: [S7, S9]
last-updated: 2026-06-29

> Governed by `docs/STANDARDS.md` (S1, SR-3 supremacy). S6 **designs the brief-first page
> template** for every doctrine page (and the in-scope narrative pages) and the **per-page
> change-list** that clears the instructor's quick-fix register. S6 **weaves in the S5-ingested
> case substrate** — the new `[[Case]]` rows + homes S5 emitted (S5 · R7) — **authors the
> doctrine-page field framing (N9)** that S4 · R4 / L8 deliberately kept *off* the case pages,
> **executes the Community Caretaking ⇄ Emergency Aid split** (S2 · R6), and **creates the new
> "Public-Employee Compelled Statements (Garrity)" doctrine page** S5 flagged (S5 · R11). S6
> **designs**; it rewrites no page now — the reformat executes later under `EXECUTE.wrapper.md`
> through the standing find→adjudicate→fix gate (L5), serial CL (L4). **Decks are untouched**
> (S4 · R11 / S5 · R8): the terminal page-derived rebuild at EXECUTE/S9 absorbs every S6 change.
> Where S6's research touched live law it ran **web-discovers → serial-CL-confirms** (L2/L4); the
> *Pringle* and knock-and-talk resolutions (§6.5) were confirmed against the primary opinions.

---

## 1. Objective

Turn every doctrine page into a **brief-first teaching document** (N8): the full integrated brief
(field-decisive question → black-letter rule + named test/prongs stated up front → elements ·
burden · standard of review · remedy → limits · nuances · pitfalls, **woven into one read**) sits
at the top; the Key/Related case tables, role-based recent-developments, Mermaid, and Sources
follow as supporting apparatus. S6 (a) fixes the **canonical template** annotated with which S1
rule governs which slot; (b) produces the **per-page change-list** that executes the quick-fix
register, the S2 structural changes, and the §6.5 research resolutions, each item tagged with the
L#/N# it enforces; (c) **executes the caretaking split** and **authors the new Garrity doctrine
page**; (d) **integrates the S5 case rows + the doctrine-page field framing**; and (e) defines the
**per-page find→adjudicate→fix gate** the reformat runs through. Citation accuracy is necessary but
not sufficient: every reformatted page must also pass the **SR-2 instructor-grade gate** (correct,
complete, *and* teachable) or it is escalated, not shipped.

## 2. Scope

### 2.1 In scope (S6 designs)
- The **brief-first doctrine-page template**, annotated with rule placement (§6.1; R1/R2).
- The **doctrine-page field framing (N9)** — the officer's field-decisive question, line-drawing,
  and operational "what this means," authored *here* (not on case pages, per S4 · R4 / L8) and
  **instructor-reviewed (SR-2)** (R3).
- **Integration of the S5 case substrate** — weaving the new `[[Case]]` rows + homes (S5 · R7)
  into each doctrine page's tables and brief, by holding (N1) and role (S2 · R3) (R4/R5).
- The **authority-weight lexicon sweep** (N2) and the **link-every-case sweep** (N7) across all
  reformatted pages (R6).
- The **per-page change-list** (§6.2; R7) — the concrete edits, each tagged with its lesson.
- The **Community Caretaking ⇄ Emergency Aid split execution** (S2 · R6) (§6.4.A; R8).
- The **new "Public-Employee Compelled Statements (Garrity)" doctrine page** (S5 · R11) (§6.4.B; R9).
- The **§6.5 research resolutions** baked into the change-list — *Pringle* ≠ horizontal-pooling;
  the knock-and-talk implied-license reframe (R10).
- The **in-scope non-doctrine narrative pages** for reformat (§6.3; R11) — excluding Legal Research
  (S8), the glossary (S7 owns the wiring), and the generated Case Index (S4).
- The **decks-untouched rule** for S6 (R12) and the **per-page find→adjudicate→fix gate** (§8; R13).

### 2.2 Out of scope (owned elsewhere)
- The **standards/lexicon/verification machine + the canonical TOC** → **S1** (`docs/STANDARDS.md`),
  which S6 obeys.
- The **category tree, homes, role set, scope contract, and the caretaking-split *decision*** →
  **S2** (S6 *executes* S2 · R6/§6.2).
- The **case object, BIRAC case-page template, slug/anchor scheme, case-page restatement rule,
  Case-Index regeneration, and the case-name→`[[Case]]` link wiring** → **S4** (S6 *emits against*
  S4's anchors and homes the case rows; it authors no case page).
- **Ingesting/discovering the case universe, the Garrity *case* pages, and the dual-thread
  concordance pass** → **S5** (S6 consumes S5's output; it ingests no case).
- **Glossary/term wiring (N11)** → **S7**; **legal-research/citation pages** → **S8**; the **final
  exhaustive independent verification** → **S9**.
- **Folder creation / `git mv` / Explorer + alias plumbing / components** → **S3** (S6 reformats
  page *content* into the brief-first template and emits plain-markdown `CaseTable` rows per the S4
  · R9 data contract; it builds no component and moves no file).
- **The flashcard rebuild** → **EXECUTE/S9** (S4 · R11): S6 touches no deck (R12).

---

## 3. Requirements (numbered, testable)

### R1 — The brief-first doctrine-page template (the reformat target) **[N8, S1 §3.I; USER]**
Every doctrine page is reformatted to the **§6.1 template**, whose section order is fixed by S1
§3.I, with the **user-confirmed structure**: **Nuances and Pitfalls fold *into* the brief
narrative** (not labeled trailing subsections), so the brief reads top-to-bottom as one coherent
teaching read. Order: **Frontmatter** (single controlling amendment; `aliases` for renamed/split
pages; `related:`) → **The Brief** (field-decisive question N9 → black-letter rule + named
test/prongs stated up front N3 → elements · burden + who bears it · standard of review · remedy →
limits & nuances & pitfalls woven in) → **Key cases** (table) → **Related cases across doctrines**
→ **Recent developments** (role-based, circuit/state only — **no SCOTUS**, N5) → **Visual
(Mermaid)** → **Sources**.
- *Check (CHECKLIST:D14/D10 + AUTO:LINT-3):* every reformatted doctrine page matches the order;
  the brief is the first substantive content and is self-contained; nuances/pitfalls appear as
  integrated prose, not as `## Nuances` / `## Common pitfalls` headings; apparatus follows.

### R2 — Brief completeness + the SR-2 instructor-grade gate (blocking) **[SR-2, N3, N9, D4]**
Each brief covers the **D4 completeness checklist** with no unlogged gap: field-decisive question ·
black-letter rule · the named test + **all** its prongs/elements stated **up front** (N3, e.g. the
*Dunn* four factors; the consent three prongs; the *Garner* 3-part caretaking test) · burden + who
bears it · standard of review · remedy · controlling authority + progeny **by role** · limits ·
nuances · pitfalls · the operational "apply it" angle (N9). A page with perfect citations but a
muddled or incomplete brief **FAILS** the composite gate **D2 ∧ D4 ∧ D9 ∧ D14** and is escalated
to `_review-needed/`, not shipped.
- *Check (CHECKLIST, composite blocking):* the gate is signed per page; the completeness checklist
  has no unlogged gap; named tests are stated up front, not left for the reader to reconstruct.

### R3 — Field framing authored *here*, never on case pages **[N9, L8, S4 · R4, SR-2]**
S6 authors the **generalized field framing** — the officer's field-decisive question, the
line-drawing, the operational "what this means across situations" — **only on doctrine pages**,
authored as teaching and **instructor-reviewed (SR-2)**. This is the framing S4 · R4 / **L8**
deliberately kept **off** the case pages (case pages **restate**; doctrine pages **teach**). The
framing must **restate holdings faithfully** and may **not add, drop, narrow, or broaden** a
condition (L8) — e.g. it states *Brigham City*'s "objectively reasonable **basis to believe** an
occupant is injured," never narrows it to "**see** it"; any boundary on a doctrine's reach carries
the two-key burden (L7).
- *Check (CHECKLIST:D2/D4/D9):* every doctrine page carries field framing; no framing imports a
  narrowed/broadened holding (spot-check against the opinion); the parallel case pages remain
  restatement-only (cross-checked with S4 · R4) — no field-advice migrated onto a case page.

### R4 — Integrate the S5 case substrate (rows + homes + links) **[S5 · R7, N1, N6, N7]**
S6 **weaves the S5-ingested `[[Case]]` rows** into each doctrine page: every S5 case **homed** to a
doctrine page (S5 · R7 step 4, by holding N1, with a role from the S2 · R3 8-role set) appears in
that page's correct table (Key / Related / Recent-developments) with **page-specific framing**
(N6 non-exclusive key-status; multi-homing expected). S5 emitted the *rows + `[[Case]]` links*; S6
**integrates them into the briefs and tables** and writes the framing. Passage-specific discussion
**deep-links** the holding (`[[Case#rule]]` / `[[Case#^pin-N]]`, S4 · R6); a whole-case reference
links the case page (N7).
- *Check:* every S5 case homed to a doctrine page appears on that page in its assigned role with
  page-specific framing; no orphan S5 row (homed-but-unwoven); deep-links resolve under SPA nav.

### R5 — Apply the case-table role set + apparatus rules **[S2 · R3, N5, N6, N2]**
Each page's Key cases / Related / Recent-developments tables draw every entry from the **8-role
set** (S2 · R3): a **SCOTUS** case is **never** in Recent-developments (N5; AUTO:LINT-3) — it homes
to Key regardless of date; a circuit/state case is **Key** only when first-impression /
in-circuit-controlling, else Related / Illustrates-a-split / Limits-Narrows / Recent-development;
circuits are **named** and labeled with the lexicon (N2); recent-developments entries carry an
expand/narrow/split/first-impression **role label**.
- *Check (AUTO:LINT-3 + CHECKLIST:D10/D6):* every table entry carries a valid role; zero SCOTUS in
  Recent-developments; every circuit case names its circuit and a 6-tier weight.

### R6 — The lexicon sweep + the link-every-case sweep (all pages) **[N2, N7]**
Across **every** reformatted page: (a) replace **every** "persuasive, not binding" and kindred
banned phrasing with the **6-tier lexicon** (N2) — circuit holding in its circuit → *Binding
in-circuit*; viewed from elsewhere → *Persuasive (outside circuit)*; unpublished/non-precedential
→ *Persuasive only — non-precedential*; state-court illustration → *Persuasive — state,
illustrative*; English/colonial origins or overruled-as-history → *Historical*; (b) **link every
named case** to its S4 case page (`[[Case]]`), deep-linking passage-specific discussion
(`[[Case#rule]]`/`[[Case#^pin-N]]`) — **no bare case name survives** (N7).
- *Check (AUTO:LINT-4 + LINT-5):* zero banned weight phrasings; every weight label ∈ the 6 tiers;
  zero bare case names; every `[[Case]]`/`[[Case#anchor]]` target resolves.

### R7 — The per-page change-list (THE deliverable) **[quick-fix register + S2 + §6.5]**
The **§6.2 change-list** enumerates, for every flagged page, the **specific** edits — drawn from
the instructor's quick-fix register, the S2/S5 structural changes, and the §6.5 research
resolutions — as a table **Page · Change · Lesson (L#/N#) · Cases affected**. Every concrete item
is present and tagged; nothing in the register's S6 column is lost.
- *Check:* every quick-fix-register item routed to S6 appears in §6.2; every row carries a lesson
  tag and the affected cases; the change-list is concrete enough for the EXECUTE run to apply
  without re-deciding.

### R8 — Execute the Community Caretaking ⇄ Emergency Aid split **[S2 · R6, N10, N5, N3, L7]**
S6 authors the **two** pages the bundled page splits into (S2 · §6.2): **Emergency Aid** (home
entry to render aid on an objective basis — *Brigham City* · *Fisher* · *Mincey*; **re-home *Case
v. Montana* from Recent-developments → Key cases**, N5; *Caniglia* as the controlling home-entry
limit; field question "*Someone inside may be hurt — may I enter?*") + **Community Caretaking**
(the **non-home** doctrine, **scope stated explicitly**, N10, with two **labeled strands**:
**(a) vehicles/roadside/impound** — *Cady* · cross-link *Opperman*/*Bertine* inventory; **(b)
caretaking/welfare seizures of persons in public** — *United States v. Garner* (10th Cir.) 3-part
test stated up front N3, *United States v. Rideau* (5th Cir.), and emergency mental-health
seizure → **probable cause of dangerousness** *Graham v. Barnette* (8th Cir.); the *Caniglia*
"category-error" caveat on the label). The *Caniglia* home-bar appears on **both** pages;
cross-link Community Caretaking ⇄ **Seizure of the Person** (caretaking-justified seizures, placed
by holding N1, not Terry crime-suspicion stops). Old title gets an `alias` (zero broken inbound
links). **No deck touch** (R12).
- *Check:* both pages exist; each states its scope explicitly (home-barred / vehicles /
  persons-in-public); *Case v. Montana* is Key on Emergency Aid; the persons-in-public strand
  carries *Garner*/*Rideau*/*Graham* with PC-of-dangerousness and the *Garner* test up front;
  *Caniglia* limit on both; old title aliased.

### R9 — Author the new Garrity doctrine page **[S5 · R11, U2-S5]**
S6 authors **"Public-Employee Compelled Statements (Garrity)"** under S2-tree **#9 (Confessions,
Interrogation & Identifications)**, the **provisional home** S5 assigned to the ingested Garrity
cluster (S5 · R11) — homing the S5 case pages **Garrity v. New Jersey**, **Gardner v. Broderick**,
**Kalkines v. United States**, **Lefkowitz v. Turley**, **LaChance v. Erickson**, **NASA v. FLRA**,
and controlling progeny — in the brief-first template. The field framing (R3) is **audience-relevant
to officers** (the students *are* the public employees): the field-decisive question is "*I am
ordered to give a statement at an internal-affairs interview — what is compelled, what is immunized,
and what can be used against me criminally?*" The page records the **audience-relevance basis** and
the **S2 §2.0 OPTIONAL→CORE supersession** (recommend the one-line S2 cross-ref at execution, per
S5 · §9).
- *Check:* the page exists, brief-first, passes the SR-2 gate, and homes the Garrity-cluster case
  pages by holding; the audience-relevance/S2-supersession note is present.

### R10 — Bake in the research resolutions (§6.5) **[L2/L4 confirmed; N1, L7/L8, N2]**
The two open questions are resolved against **primary authority** and written into the change-list:
1. ***Pringle* is NOT horizontal-pooling.** *Maryland v. Pringle*, 540 U.S. 366 (2003) (opinion id
   **131150**, Rehnquist, C.J., unanimous; identity confirmed) is an **aggregate / particularized
   probable-cause-as-to-a-person** case — PC "must be particularized with respect to the person"
   (*Ybarra v. Illinois*, 444 U.S. 85, 91), satisfied by the reasonable inference of a **"common
   enterprise among the three men"** (drawing on *Wyoming v. Houghton* and *United States v. Di
   Re*). It is **not** a collective-knowledge / horizontal-pooling-**among-officers** case (no
   pooling/imputation across officers anywhere in the opinion). The **Collective Knowledge** page's
   internal contradiction is therefore resolved by **correcting the *Pringle* framing** (it is *not*
   SCOTUS support for horizontal pooling); the page's other statement — "no single SCOTUS holding
   adopts a pure horizontal-pooling rule" — is **correct and stands**.
2. **Knock-and-talk implied-license scope** (confirmed against *Jardines*, opinion id **856347**,
   Scalia, J.). The license is limited **by area *and* by purpose**: "the background social norms
   that invite a visitor to the front door do not invite him there **to conduct a search**," and
   the test is **objective** — "their behavior objectively reveals a purpose to conduct a search."
   The resolved line-drawing the page must teach is in **§6.5**.
- *Check:* the Collective Knowledge page no longer frames *Pringle* as horizontal-pooling SCOTUS
  authority and carries no internal contradiction; the knock-and-talk page is reframed per §6.5 with
  the controlling cases and the circuit split annotated (circuits named).

### R11 — In-scope non-doctrine narrative pages **[N2, N7, N8 where applicable]**
S6 reformats the **narrative/reference pages** to the extent the lessons apply — the lexicon sweep
(R6), link-every-case (R6), brief-first **where the doctrine template fits** — **without** forcing
the full doctrine brief onto a page that is not a doctrine. In scope: `index.md` (home MOC —
refresh the narrative to the S2 tree, fix link integrity), `Fourth Amendment Framework`, `Fourth
Amendment Analysis Checklist`, `Fourth Amendment Recalibration`, **`CREW`** (the mnemonic-fix
below — stays a `type: practical` mnemonic page, lightly reformatted), `Three Golden Rules`,
`Instructor Development`, `The Federal Court System` (reference). **Excluded:** `Legal Research and
Case Citations` (**S8**), `Common Legal Terms` (the glossary — **S7** owns the wiring), and `Case
Index` (**S4** regenerates it).
- *Check:* each in-scope narrative page is addressed (lexicon + links at minimum); the CREW
  mnemonic-letter fix is applied; no doctrine-brief template is forced onto a reference/mnemonic
  page; the three excluded pages are untouched by S6.

### R12 — Decks untouched in S6 **[S4 · R11, S5 · R8; USER-confirmed]**
S6 **reformats pages only**; it **creates, modifies, and re-points no flashcard deck**. The
**separate later flashcard run** (decks derive **from** the finalized, verified pages — L1) absorbs
every S6 change at once. (User confirmed "no deck touch in S6" over the interim-refresh alternative;
**U5-S9** further confirms **no deck work anywhere in the overhaul** — the rebuild is a separate run,
not an S9 step.)
- *Check:* **zero** deck files modified during S6; no S6 deliverable emits a deck artifact.

### R13 — The per-page find→adjudicate→fix gate **[L5, L4, SR-1, §8]**
Each reformatted/new page runs the standing machine (S1 §3.G): **REVIEW** (parallel, free, no-CL —
template compliance R1, completeness/SR-2 R2, role set R5, lexicon+links R6, no-field-advice-on-
case-pages R3, restate-not-narrow L8) → **ADJUDICATE** (`needs_cl` findings — any newly-asserted
holding/quote/treatment, a re-homing's holding basis, a frontier add — to the **single serial CL
lane**, verdict cites CL evidence; non-legal findings to a free editor-adjudicator; DISMISSED
logged with reason) → **FIX** (apply only UPHELD/MODIFIED). **Loop cap 3**, checkpoint the ledger
(resumable), ESCALATE → `_review-needed/<slug>.md`. Any holding/quote S6 newly asserts (incl. the
N9 field framing and the new Garrity/caretaking content) is an **SR-1 live-verify** event through
the serial lane; S9 re-confirms.
- *Check:* every page change traces to an adjudicated verdict (UPHELD/MODIFIED) with evidence;
  `cl-calls.log` shows the serial lane; reviewers produced findings only; escalations logged.

---

## 4. Lessons enforced

- **N8 brief-first** → R1 template (brief reads top-to-bottom; apparatus follows). **N3 tests up
  front** → R2 + the *Dunn*/consent-prongs/*Garner* change-list items. **N9 field-decisive framing**
  → R3 (authored on doctrine pages, instructor-reviewed) + the knock-and-talk reframe (R10/§6.5).
- **N1 placement-by-holding** → R4 homing + R10 (*Pringle* re-framed to its true ratio; *Matlock*
  home = Consent). **N6 non-exclusive key-status** → R4/R5 (*Herring* promoted on Collective
  Knowledge; *Riley* → Related on Common Law). **N5 no-SCOTUS-in-recent-dev** → R5 + R8 (*Case v.
  Montana* → Key on Emergency Aid). **N4 subsequent-treatment inline** → §6.2 (*Santana* "limited by
  *Lange*"), consistent across homes. **N10 state scope explicitly** → R8 (caretaking split, strands
  labeled). **N2 lexicon** + **N7 link-every-case** → R6 sweep.
- **L8 restate-don't-editorialize / L7 scope-as-assertion / L1 two-key** → R3 (field framing
  restates, never narrows; the *Brigham City* "basis to believe" ≠ "see it" scar) + R13 (live
  re-verify). **L2/L4** (web discovers, serial CL confirms) → §6.5 resolutions + R13. **L5
  find→adjudicate→fix** → R13 gate.
- **SR-2 instructor-grade gate** → R2 (blocking composite). **SR-1 exhaustive live re-verify** →
  R13 (S6 newly-asserted content is an SR-1 installment; S9 re-confirms).
- **S1** template/TOC (§3.I) → R1; **S2** homes/role set/scope/split → R4/R5/R8; **S4** case
  anchors + restatement boundary + R9 data contract → R3/R4/R6; **S5** ingested rows + Garrity flag
  + N9-deferred + deck-deferred → R4/R9/R3/R12.

## 5. Method (how execution proceeds against this spec)

1. **Reformat each doctrine page** (S2-tree order) into the §6.1 template (R1): write the integrated
   brief (R2, fold-in), pull named tests up front (N3), author the field framing (R3, L8-faithful).
2. **Weave the S5 case rows** (R4) into the Key/Related/Recent-developments tables by holding +
   role (R5); apply the lexicon + link sweep (R6).
3. **Execute the structural changes:** the caretaking split (R8) and the new Garrity page (R9).
4. **Apply the §6.2 change-list** item by item (R7), baking in the §6.5 resolutions (R10).
5. **Reformat the in-scope narrative pages** (R11); leave the S7/S8/S4-owned pages alone.
6. **Run the per-page find→adjudicate→fix gate** (R13), serial CL (L4), SR-1 live-verify of new
   assertions, checkpointed/resumable; escalate to `_review-needed/`.
7. **Touch no deck** (R12). Hand off to **S7** (term/glossary wiring over the finalized page text).
   Every stage cites `docs/STANDARDS.md` (SR-3) and routes CL through the single serial lane (L4).

## 6. Deliverables (what execution produces or changes)

### 6.1 — The brief-first doctrine-page template (annotated)

```
---
# Frontmatter: single controlling amendment · aliases (renamed/split pages) · related:
---

# <Doctrine>

## The Brief                                   ← N8 brief-first · D14 · SR-2 (one integrated read)
**Field-decisive question:** <the call the officer must make>          ← N9 (lead with it)
<Black-letter rule>, stating the named test + ALL its prongs/elements   ← N3 (up front)
<elements · burden + who bears it · standard of review · remedy>        ← D4 completeness
<limits · nuances · pitfalls — WOVEN INTO THIS NARRATIVE as prose>      ← USER fold-in
   · subsequent treatment inline: "limited by [[Case]]" + why-if-field-changing   ← N4
   · every named case linked; passage discussion deep-links [[Case#rule]]/[[#^pin-N]] ← N7/S4·R6
   · scope boundaries restated faithfully, never narrowed/broadened     ← L8 / L7 / L1

## Key cases                                   ← table: Case · holding · WEIGHT(6-tier) · treatment · CL · case-page
   roles: Key—Anchor / Key—Progeny ; non-exclusive (N6) ; placement-by-holding (N1) ; weight lexicon (N2)

## Related cases across doctrines              ← role: Related(cross-doctrine) ; framed for THIS page

## Recent developments                         ← role-based: expand/narrow/split/first-impression
   circuit/state ONLY — NO SCOTUS (N5 / LINT-3) ; circuits named ; persuasive-tier (N2)

## Visual (Mermaid)                            ← where a multi-factor/branching test exists (D8)

## Sources                                     ← CL opinion URLs + pinpoint pages
```
*Cross-cutting on every doctrine page:* two-key quotes verbatim + pinpoint (L1/LINT-2); treatment
status non-blank (N13/LINT-6); the SR-2 composite gate (D2 ∧ D4 ∧ D9 ∧ D14) blocks shipping a
muddled brief. **Visual placement** follows S1 §3.I (#6, after Recent developments). **`type:
practical`/reference/mnemonic pages** (e.g. CREW) keep their own shape — lexicon + links only (R11).

### 6.2 — The per-page change-list (Page · Change · Lesson · Cases affected)

| Page | Change (concrete) | Lesson | Cases affected |
|---|---|---|---|
| **Abandonment** | Confirm ***Matlock*** home = **Consent** (Key there); on Abandonment it stays a **Related (cross-doctrine)** row marking the abandonment/consent line, *not* a key/abandonment case — and ensure no pitfall routes "common authority" to abandonment. Lexicon sweep (*Hunt* 9th, *Small* 4th, *Crumble* 8th → "Persuasive (outside circuit)"). Brief-first fold-in (field Q: "*Did the suspect retain a reasonable expectation of privacy?*"). Link every case + deep-links. | N1, N2, N7, N8 | *Matlock*, *Hunt*, *Small*, *Crumble*, *Greenwood*, *Hodari D.* |
| **CREW** | Fix the mnemonic: "**R** — Recognized Exception" → "**RE** — Recognized Exception" so **C·RE·W** = Consent · Recognized Exception · Warrant (the "E" is currently dropped). Confirm pitfalls route common-authority → **[[Consent Searches]]**, never abandonment. Light reformat only (mnemonic page): lexicon + links; **not** the full doctrine brief. | N1 | *Matlock* (common-authority → Consent) |
| **Collective Knowledge and the Fellow-Officer Rule** | **Promote *Herring* → Key cases** (central to imputed/mistaken collective knowledge; non-exclusive — also Key on Exclusionary Rule). **Resolve *Pringle*** (§6.5 #1): it is **aggregate/particularized PC**, *not* horizontal pooling — remove it from the "horizontal-pooling side" Related slot (or reframe explicitly as aggregate-PC, primary home **[[Probable Cause and Reasonable Suspicion]]**, expressly *distinguished* from collective knowledge), curing the page's internal contradiction. Keep ***Trent*** (6th Cir.) but label **Persuasive only — non-precedential** (unpublished). Lexicon sweep (*Massenburg*/*Chavez*/*Ramirez*; circuits named; split flagged). | N6, N2, N1, L7/L8 | *Herring*, *Pringle*, *Trent*, *Massenburg*, *Chavez*, *Ramirez*, *Whiteley*, *Hensley* |
| **Common Law Origins** | **Move *Riley v. California* from Key cases → Related cases** (Riley is Key on SITA/digital; *here* it only recounts founding history — page-specific framing, N6). ***Boyd*** stays the Key case. Keep English/colonial antecedents labeled **Historical** / non-binding (tier 6). Brief-first fold-in. | N6, N2 | *Riley*, *Boyd*, (Entick/Wilkes/Paxton — Historical) |
| **Community Caretaking and Emergency Aid** → **SPLIT** | Execute the **S2 · R6 split** into **Emergency Aid** + **Community Caretaking** (R8/§6.4.A). **Re-home *Case v. Montana* Recent-dev → Key cases** on Emergency Aid (N5). Author the Community Caretaking **persons-in-public** strand (*Garner* 3-part test up front · *Rideau* · *Graham* PC-of-dangerousness) + **vehicles** strand (*Cady* · *Opperman*/*Bertine*); ***Caniglia* limit on both**; *Caniglia* "category-error" caveat on the label. Reconsider *Mincey* → stays Emergency Aid (aid + protective sweep scope). Alias old title. Exhaustive depth. | N5, N10, N3, N9, L7 | *Case v. Montana*, *Cady*, *Caniglia*, *Brigham City*, *Fisher*, *Mincey*, *Garner*, *Rideau*, *Graham*, *Opperman*, *Bertine* |
| **Consent Searches** | **Bullet the three prongs** (1) Voluntariness (2) Authority (3) Scope on their **own lines** in the brief (currently inline) — N3. Add the **scope-exceeded pitfall**: general consent does **not** authorize **destruction** of the vehicle/contents (the "knife-through-the-seat"/slashing-upholstery move) — illustrative authority ***United States v. Osage*, 235 F.3d 518 (10th Cir. 2000)** ("before an officer may actually destroy or render completely useless a container… the officer must obtain explicit authorization") with ***Jimeno***'s locked-briefcase dictum as the SCOTUS anchor (confirm at execution). Exhaustive depth (scope/withdrawal). Lexicon sweep (*Lewis* 6th, *Williams* 3d). | N3, N9, N2 | *Jimeno*, *Osage*, *Schneckloth*, *Matlock*, *Randolph*, *Fernandez*, *Lewis*, *Williams* |
| **Curtilage** | **Move the *Dunn* four factors into the Rule/brief, stated explicitly** — (1) proximity to the home, (2) within the enclosure surrounding the home, (3) nature of the use, (4) steps taken to shield from observation (currently buried in Nuances) — N3. Brief-first fold-in. Lexicon sweep (*Basher* 9th, the pole-camera split *Tuggle*/*Moore-Bush*/*May-Shaw*, *Lundin* 9th; keep state trio "Persuasive — state, illustrative"). Exhaustive depth. | N3, N2, N8 | *Dunn*, *Oliver*, *Hester*, *Jardines*, *Collins*, *Ciraolo*, pole-camera split cases |
| **Exigent Circumstances and Hot Pursuit** | Add the Bandiero **"hot on the tail / fresh on the trail"** teaching line + the **hot-vs-fresh-pursuit** distinction (hot = immediate & continuous, *Hayden*/*Santana*; fresh = promptly-resumed, often cross-jurisdiction). Frame ***Newman v. Underhill*** (9th Cir. 2025) as the **fresh-pursuit illustration** (9-min gap did not break continuity). Add **"limited by [[Lange v. California]]"** inline to ***Santana*** (Lange rejected categorical misdemeanor hot-pursuit-into-home — N4). Lexicon sweep; exhaustive depth. | N4, N9, N2 | *Santana*, *Lange*, *Newman v. Underhill*, *Hayden*, *King*, *McNeely*, *Mitchell* |
| **Knock and Talk** | **N9 exhaustive reframe** around **lawful presence / implied-license scope** (§6.5 #2): lead with the field-decisive question ("*Am I within the implied license a private visitor would have — in area, purpose, time, and manner?*"); teach the resolved line-drawing exhaustively (area / front-vs-other-doors / purpose-to-talk-not-search / time / the hard line to leave / "No Trespassing" / plain-view limits / articulation), annotating the circuit split (circuits named). Lexicon sweep. Exhaustive depth. | N9, N2, N7 | *Jardines*, *King*, *Carloss*, *Lundin*, *French*, *Banks*, *Meyer*, *Walker*, *Bostick*, *Drayton* |
| **Case v. Montana** *(cross-page item)* | Re-home from Recent developments → **Key cases** on **Emergency Aid** (a SCOTUS holding belongs in Key regardless of date). *(Executed within the caretaking split, R8.)* | N5 | *Case v. Montana* |
| **NEW · Emergency Aid** | Create (split target). Home-entry-to-aid doctrine; *Brigham City*/*Fisher*/*Mincey* Key; *Case v. Montana* Key; *Caniglia* limit. Field Q: "*Someone inside may be hurt — may I enter?*" | N9, N5, L8 | *Brigham City*, *Fisher*, *Mincey*, *Case v. Montana*, *Caniglia* |
| **NEW · Community Caretaking** | Create (split target, re-scoped). Non-home; vehicles strand + persons-in-public strand; scope explicit; *Caniglia* category-error caveat; cross-link Seizure of the Person. | N10, N3, L7 | *Cady*, *Garner*, *Rideau*, *Graham*, *Opperman*, *Bertine*, *Caniglia* |
| **NEW · Public-Employee Compelled Statements (Garrity)** | Create (S5 · R11; §6.4.B). Brief-first; home the Garrity-cluster case pages; audience-relevant officer framing; record the audience-relevance + S2 OPTIONAL→CORE supersession. | N9, SR-2 | *Garrity*, *Gardner*, *Kalkines*, *Lefkowitz*, *LaChance*, *NASA v. FLRA* + progeny |
| **ALL doctrine + narrative pages (sweep)** | (a) Replace "persuasive, not binding" / kindred → 6-tier lexicon (LINT-4). (b) Link every named case (`[[Case]]`); deep-link passage discussion (`[[Case#rule]]`/`#^pin-N`) — no bare names (LINT-5). (c) State named tests up front (N3). (d) Fold nuances/pitfalls into the brief (N8/D14). (e) Re-home by holding (N1); apply role set + non-exclusive key (N5/N6); SCOTUS out of Recent-dev (LINT-3). (f) "limited by [[case]]" inline wherever asserted, consistent across homes (N4). | N1–N9, N2, N7, L8 | *all* |

### 6.3 — Non-doctrine narrative pages in scope (R11)

**Reformat (lessons applied to fit):** `index.md` (home MOC → refresh to the S2 tree; link
integrity), `Fourth Amendment Framework`, `Fourth Amendment Analysis Checklist`, `Fourth Amendment
Recalibration`, `Three Golden Rules`, `Instructor Development`, `The Federal Court System`, **`CREW`**
(mnemonic-letter fix; light reformat). **Excluded from S6:** `Legal Research and Case Citations`
(**S8**), `Common Legal Terms` (glossary wiring → **S7**), `Case Index` (generated → **S4**),
`flashcards.md` + all decks (frozen → EXECUTE/S9). The reference/mnemonic pages get the **lexicon +
link sweeps** but **not** the full doctrine brief template.

### 6.4 — The two structural authoring jobs

**A · Caretaking split (R8).** `Community Caretaking and Emergency Aid` → **`Emergency Aid`** (NEW)
+ **`Community Caretaking`** (NEW, re-scoped). Emergency Aid: home entry on the *Brigham City*
objective-basis standard; *Fisher* (no ironclad proof); *Mincey* (no murder-scene exception; aid +
prompt protective sweep, scope tied to the emergency; *Tyler/Clifford* fire-scene dissipation);
**Case v. Montana** Key (*Brigham City* reasonableness, not PC); *Caniglia* home-entry limit.
Community Caretaking: **strand (a) vehicles** (*Cady*; inventory cross-link *Opperman*/*Bertine* →
Special Needs/SITA); **strand (b) persons in public** (*Garner* 10th-Cir. 3-part caretaking-detention
test stated up front; *Rideau* 5th-Cir. impaired-person-in-roadway; *Graham v. Barnette* 8th-Cir.
PC-of-dangerousness for serious mental-health seizures); the *Caniglia* "category-error" caveat;
cross-link **Seizure of the Person**. *Caniglia* limit on **both**; old title aliased; deck-id
migration **dropped** (R12 — decks rebuilt terminally).

**B · Garrity page (R9).** `Public-Employee Compelled Statements (Garrity)` under S2-tree #9. Brief
(field Q for the officer-student): the *Garrity* immunity rule (compelled IA statements + their
fruits are inadmissible in a **criminal** case), the *Gardner*/*Lefkowitz* limit (an employer may
compel a statement on pain of dismissal **only** by immunizing it — it may not fire for invoking the
privilege *and* use the statement), the *Kalkines* warning, *LaChance*, *NASA v. FLRA*. Homes the
S5 Garrity-cluster case pages; records audience-relevance + the S2 §2.0 supersession.

### 6.5 — Research resolutions (web-discovers → serial-CL-confirms; primary-source-checked)

**① *Maryland v. Pringle* is NOT horizontal pooling (cures the Collective Knowledge contradiction).**
*Pringle*, 540 U.S. 366 (2003) (opinion id **131150**, Rehnquist, C.J., **unanimous**; CL identity
confirmed) holds that probable cause to arrest each of three car occupants existed because PC "must
be particularized with respect to the person to be searched or seized" (*Ybarra v. Illinois*, 444
U.S. 85, 91) **and** the officer could reasonably infer a **"common enterprise among the three men"**
(citing *Wyoming v. Houghton* and *United States v. Di Re*). This is **aggregate/particularized
PC-as-to-a-person** — aggregation of facts about a small group of *suspects* to find individualized
PC — **not** the collective-knowledge **pooling/imputation across *officers***. The opinion contains
**no** collective-knowledge, fellow-officer, pooling, or imputation reasoning. **Resolution:** remove
*Pringle* from the page's "horizontal-pooling side" slot (its true home is **[[Probable Cause and
Reasonable Suspicion]]**); if retained on Collective Knowledge, frame it expressly as an aggregate-PC
case **distinguished** from collective knowledge. The page's statement that "no single SCOTUS holding
adopts a pure horizontal-pooling rule" is **correct and stands** — the contradiction was caused solely
by the mis-tagged *Pringle* row (an N1 placement-by-holding error; an L7/L8 framing-as-assertion miss).

**② Knock-and-talk implied-license scope (confirmed against *Jardines*, opinion id 856347, Scalia,
J.).** The license is bounded by **area, purpose, time, and manner**; the page must teach, exhaustively:
- **Area / route.** Default = the customary visitor route to the **front door**. Officers may use
  walkways/driveways/porches a visitor would; a **"small departure"** to a back/side door a normal
  visitor would use after no front-door answer is permissible (*United States v. Walker*, 11th Cir.);
  but **deviating to explore curtilage** (back yard, peering around the side) **exceeds** the license
  (*Jardines*; *Lundin* 9th Cir.). Where there is no usable front door / visitors customarily use a
  side door, the license follows that route. **Front-vs-other-public-doors is circuit-developed,
  fact-specific** — annotate, don't overstate.
- **Purpose — the "talk," not a search.** *Jardines*: "the background social norms that invite a
  visitor to the front door do not invite him there **to conduct a search**"; the test is **objective**
  — "their behavior objectively reveals a purpose to conduct a search." Deploying a drug dog
  (*Jardines*), peering with a flashlight, or snooping **exceeds** it. A **subjective** intent to
  arrest, by itself, does **not** void an otherwise-ordinary knock (*Kentucky v. King* — subjective
  intent irrelevant to a lawful knock-and-announce). **Circuit split (annotate, circuits named):**
  whether bare investigative/arrest purpose (no dog, no snooping) breaks the license — *French v.
  Merrill* (1st Cir.) majority + *United States v. Lundin* (9th Cir.) say it **can** (esp. paired with
  manner/time); *United States v. Carloss* (10th Cir.) + the *French* dissent treat ordinary
  knock-and-talks as **undisturbed** by *Jardines*.
- **Time / reasonableness.** No implied license to knock in the **middle of the night** while
  occupants sleep — a **4 a.m.** knock-and-talk exceeded the license (*Lundin*, 9th Cir.).
- **The hard line to leave.** The license is to knock, **wait briefly**, and (absent invitation to
  linger) **leave**; overstaying or **repeated** intrusion after a refusal exceeds it (*French*).
- **"No Trespassing" signs** generally do **not** revoke the approach-and-knock license (*Carloss*,
  10th Cir.) — circuit-developed; persuasive-tier.
- **Plain-view limits.** From the **lawful front-door vantage** officers may use what they observe
  in plain view, but the approach authorizes **no** entry into curtilage, **no** seizure, and **no**
  sense-enhancing/instrument search (cross-link **[[Plain View Doctrine]]**; *Collins* curtilage limit).
- **Articulation.** The officer must be able to articulate staying within **area · purpose · time ·
  manner** — the field-decisive checklist the page leads with.

### 6.6 — Exhaustive-treatment set (USER-confirmed)

Deep, exhaustive line-drawing (beyond standard brief-first depth): **Knock and Talk** (flagged) +
**Consent Searches** (scope/withdrawal) + **Curtilage** (Dunn / open-fields) + **Community
Caretaking** (re-scoped strands) + **Exigent Circumstances and Hot Pursuit** (hot-vs-fresh; Lange;
dissipation; police-created exigency). All other doctrine pages get standard brief-first depth.

---

## 7. Acceptance criteria (definition of done)

- [ ] **Template (R1):** every doctrine page matches the §6.1 brief-first order; nuances + pitfalls
      are **folded into the brief narrative** (no `## Nuances`/`## Common pitfalls` headings); the
      brief is the first, self-contained content; apparatus follows; Visual placed per S1 §3.I.
- [ ] **Instructor-grade (R2/SR-2):** every doctrine page passes the composite gate D2 ∧ D4 ∧ D9 ∧
      D14; named tests/prongs are stated up front; no muddled brief ships (escalated instead).
- [ ] **Field framing (R3):** every doctrine page carries N9 field framing, instructor-reviewed,
      that **restates** holdings faithfully (no narrowing/broadening — L8); no field-advice prose
      appears on any case page (cross-checked with S4 · R4).
- [ ] **S5 integration (R4/R5):** every S5-homed case is woven into its doctrine page in the correct
      role with page-specific framing; no orphan row; SCOTUS never in Recent-developments; circuits
      named.
- [ ] **Sweeps (R6):** zero "persuasive, not binding" / banned phrasings remain (LINT-4); zero bare
      case names (LINT-5); every weight ∈ the 6 tiers; every `[[Case]]`/`[[Case#anchor]]` resolves.
- [ ] **Change-list (R7):** every quick-fix-register S6 item appears in §6.2, tagged with its lesson
      and affected cases — *Matlock* home, CREW "RE", *Herring* promoted, *Pringle* corrected, *Riley*
      → Related, *Dunn* factors into the Rule, consent three prongs bulleted + the destruction/Osage
      pitfall, the Bandiero hot-vs-fresh line + *Newman* + *Santana* "limited by *Lange*", the
      knock-and-talk reframe, *Case v. Montana* re-homed, the lexicon/link/tests-up-front all-pages
      sweep.
- [ ] **Caretaking split (R8):** Emergency Aid + Community Caretaking both exist; scopes explicit
      (home-barred / vehicles / persons-in-public); *Case v. Montana* Key on Emergency Aid;
      persons-in-public strand carries *Garner*/*Rideau*/*Graham* with PC-of-dangerousness and the
      *Garner* test up front; *Caniglia* on both; old title aliased.
- [ ] **Garrity page (R9):** "Public-Employee Compelled Statements (Garrity)" exists, brief-first,
      passes SR-2, homes the S5 Garrity-cluster case pages; audience-relevance + S2 supersession noted.
- [ ] **Research resolutions (R10/§6.5):** the Collective Knowledge page no longer frames *Pringle*
      as horizontal-pooling SCOTUS authority and is internally consistent; the knock-and-talk page is
      reframed per §6.5 with the circuit split annotated (circuits named).
- [ ] **Narrative pages (R11):** in-scope narrative pages reformatted (lexicon + links ≥); Legal
      Research (S8), glossary (S7), Case Index (S4), and decks untouched by S6.
- [ ] **Decks (R12):** zero deck files modified in S6.
- [ ] **Gate (R13):** every page's changes trace to an adjudicated verdict; `cl-calls.log` evidences
      the serial lane; SR-1 live-verify ran on newly-asserted content; escalations logged; loop cap 3.

## 8. Verification plan (how S6's output gets verified — the per-page gate)

The reformat runs through the standing **find → adjudicate → fix** machine (S1 §3.G), **per page**,
serial CL (L4), checkpointed/resumable:

1. **REVIEW (parallel, free, NO CL).** Per page, dimensional reviewers emit structured findings
   `{id, page, dimension(D1–D14), locator, problem, severity, proposed_fix, needs_cl, confidence}`
   against: template/brief-first order (D14/R1), SR-2 completeness+teachability (D4/D9/R2),
   field-framing-restates-faithfully (D2/D9/L8/R3), placement-by-holding + role set (D2/D5/R4/R5),
   lexicon + link-every-case (D6/D13/R6), no-field-advice-on-case-pages (cross-page, D2/R3),
   no-SCOTUS-in-recent-dev (D10/R5). **Reviewers do not edit.**
2. **ADJUDICATE.** Every finding → a verdict in {UPHELD, MODIFIED, DISMISSED, ESCALATE} with
   `adjudicated_fix` + `evidence`. **`needs_cl=true`** — any newly-asserted holding/quote/treatment,
   a re-homing's holding basis, a frontier add, the N9 framing, the Garrity/caretaking content → the
   **single serial CL lane (SR-1 live-verify)**; the verdict **must cite CL evidence** (no CL evidence
   → cannot UPHOLD a change to a legal assertion). Non-legal findings (structure, fold-in, links,
   role labels) → a free editor-adjudicator. **DISMISSED findings are logged with the reason.**
3. **FIX (parallel, free).** Apply **only** UPHELD/MODIFIED adjudicated fixes; introduce no new
   content; **ESCALATE → `_review-needed/<slug>.md`**. **Loop cap 3**, then escalate.
4. **Automated lint gate (pre-publish):** LINT-3 (brief-first order present; **no SCOTUS in
   recent-developments**), LINT-4 (lexicon vocabulary; no banned phrasing; circuits named), LINT-5
   (link-every-case; targets resolve; deep-links land), LINT-2 (quote↔pinpoint), LINT-6 (treatment
   status non-blank). A page ships only when the roster is green **and** the SR-2 checklist is signed
   (or escalations are logged).
5. **Cross-page coherence (D5):** a multi-homed case (e.g. *Riley*, *Caniglia*, *Herring*, *Santana*)
   shows page-specific **framing** but **identical** treatment status + N4 "limited by" tag on every
   home; the field framing on doctrine pages never contradicts the restatement on the case page (R3).
6. **Deck non-touch (R12):** confirm zero deck files changed during S6.
7. **Non-regression vs S1/S2/S4/S5:** the reformat honors the S1 §3.I order, the S2 homes/role
   set/split, the S4 case-restatement boundary + anchors, and the S5 ingested rows — reversing none;
   the **one** deliberate structural creation (Garrity page) is the S5 · R11 flag, logged.

## 9. Open items / escalations

- **Consent destruction-pitfall illustrative case.** §6.2 proposes ***United States v. Osage*,
  235 F.3d 518 (10th Cir. 2000)** (explicit-authorization-before-destruction) as the "knife-through-
  the-seat" illustration, anchored to *Jimeno*'s locked-briefcase dictum. **Confirm identity +
  pinpoint live at execution** (serial CL, L3/L1); if a closer-circuit or SCOTUS-anchored example
  surfaces in the frontier pass, substitute and log. Non-blocking for the design.
- **Knock-and-talk circuit split is *annotated, not resolved*.** Whether bare investigative/arrest
  purpose breaks the license is an **open split** (1st/9th vs 10th); the page **names the circuits**
  and presents it as unsettled (no SCOTUS holding past *Jardines*) — per N2/L7, not stated as a
  national rule. If the user later wants a recommended field posture, that is a teaching call to add.
- **CREW mnemonic "E".** The fix makes **C·RE·W** = Consent · Recognized-Exception · Warrant. If the
  instructor prefers the acronym expanded differently, flag at execution; the design assumes the "RE"
  reading the register specifies.
- **Garrity doctrine-page home + S2 §2.0 supersession.** S6 authors the page under S2-tree #9 per
  S5 · R11; recommend adding the **one-line OPTIONAL→CORE cross-ref to S2 §2.0** at execution (the
  APPROVED S2 is not edited here without the user's say-so).
- **`The Warrant Requirement` possible split** (knock-&-announce / particularity) — S2 · §6.2 flagged
  it to re-evaluate against the ½–1-page budget **in S6**. **Recommendation:** keep it **one page** for
  now; if the brief-first reformat pushes it past the digestible budget, split **knock-&-announce** out
  (a permitted 3rd-level move). Decided at execution against the realized length; flagged, not forced.
- **SR-1 CL load.** S6's newly-asserted content (field framing, caretaking strands, Garrity) adds to
  the serial-lane budget (with S4/S5/S9); paced through the single lane (L4), checkpointed; if the CL
  tier regresses to 5/min, RUNBOOK §3 STOP-and-notify governs.

---

## Appendix A — Decision log

*Format: Question · Options · Red-team · Steel-man · Adjudication. **[USER]** = the user's actual
choice; the rest are self-interviewed.*

### [USER] U1-S6 — Brief structure: fold nuances/pitfalls into the brief, or keep labeled subsections? → **Fold into the brief.**
- *Options:* (a) weave limits/nuances/pitfalls **into** the brief narrative as one integrated
  top-to-bottom read; (b) keep `## Nuances & limits` + `## Common pitfalls` as labeled subsections
  after the brief (closer to today's pages).
- *Red-team (a):* a single long narrative is slightly harder to **scan** as a quick reference.
  *Steel-man (a):* the overhaul's central thrust is **N8 brief-first / "read the brief in its
  entirety first"** + D14 teachability-up-front — a labeled-subsection layout is exactly the
  "optimized for reference lookup, not teaching" template the instructor asked to leave behind.
- *Adjudication:* **(a)** — fold-in (§6.1 / R1). The case tables, recent-developments, and Mermaid
  remain the scannable apparatus *after* the brief, preserving reference value without splitting the
  teaching read. User selected (a).

### [USER] U2-S6 — Which pages get exhaustive treatment beyond Knock-and-Talk? → **All four candidates.**
- *Options:* any subset of {Consent scope/withdrawal, Curtilage/open-fields, Community Caretaking,
  Exigent Circumstances}. *Adjudication:* the user selected **all four** (§6.6). These join the
  flagged **Knock and Talk** as the exhaustive-treatment set; every other doctrine page gets standard
  brief-first depth. Rationale the user's selection tracks: each is a high-error, frequently-litigated
  boundary the instructor's notes already flagged (consent scope-exceeded; Dunn line; the re-scoped
  caretaking strands; hot-vs-fresh / Lange / dissipation).

### [USER] U3-S6 — Flashcards during S6: interim refresh, or no touch? → **No deck touch in S6.**
- *Options:* (a) S6 touches no deck — the terminal page-derived rebuild at EXECUTE/S9 absorbs every
  S6 change (decks derive **from** finalized pages, L1); (b) regenerate each rewritten page's deck as
  we go (interim).
- *Discussion:* This was **already settled** by **S4 · R11** (U3-S4: freeze decks S4–S8, terminal
  purge+regenerate; FSRS reset accepted; no per-case decks) and **S5 · R8**. The interview's Part-A
  Q3 (written before U3-S4) was surfaced as a **confirm-or-override**, not re-opened. *Red-team (b):*
  re-introduces the staged deck surgery R11 deliberately removed and forks from S4/S5. *Steel-man (a):*
  consistency + a single clean page-derived rebuild after 100% verification.
- *Adjudication:* **(a)** (R12) — the user confirmed "no deck touch in S6." S6 reformats pages only.

### SI-1-S6 — *Pringle*: horizontal-pooling example, or not? → **Not — it is aggregate/particularized PC; correct the page.**
- *Question (instructor-flagged contradiction):* the Collective Knowledge page calls *Maryland v.
  Pringle* "the horizontal-pooling side" **and** says "no single SCOTUS holding adopts a pure
  horizontal-pooling rule." Which is right?
- *Research (web discovers, serial CL confirms — L2/L4):* read the primary opinion (id **131150**,
  Rehnquist, **unanimous**). *Pringle* turns on **particularized PC as to the person** (*Ybarra*, 444
  U.S. at 91) satisfied by an inferred **"common enterprise among the three men"** (*Houghton*; *Di
  Re*). It aggregates **facts about suspects**, not **knowledge across officers**; it contains **no**
  collective-knowledge/fellow-officer/pooling reasoning.
- *Red-team (keep it as horizontal-pooling support):* the word "aggregate" appears in both ideas —
  but *Pringle* aggregates *suspects' shared enterprise*, the collective-knowledge doctrine aggregates
  *officers' separate knowledge*; conflating them is the N1 keyword-vs-holding error the overhaul
  exists to kill. *Steel-man (correct it):* removing the mis-tagged row **cures the contradiction** and
  the page's "no SCOTUS horizontal-pooling holding" statement becomes correct and unambiguous.
- *Adjudication:* ***Pringle* is not horizontal pooling** (§6.5 #1 / R10). Re-home it to **[[Probable
  Cause and Reasonable Suspicion]]** (its ratio); if retained on Collective Knowledge, frame it as an
  aggregate-PC case **expressly distinguished** from collective knowledge. An L7/L8 framing-as-assertion
  + N1 placement fix.

### SI-2-S6 — Knock-and-talk reframe: how to draw the implied-license lines? → **Area · purpose · time · manner, split annotated.**
- *Research (confirmed against *Jardines*, id **856347**, Scalia):* the license is limited "not only
  to a particular area but also to a specific purpose"; behavior that "objectively reveals a purpose to
  conduct a search" exceeds it. Frontier (web → CL): *Carloss* (10th, signs don't revoke), *Lundin*
  (9th, 4 a.m. + arrest purpose exceeds), *French* (1st, repeated pre-dawn exceeds), *Banks* (7th,
  curtilage arrest can't be laundered), *Walker* (11th, "small departure" to a back door OK), *King*
  (subjective intent irrelevant to a lawful knock).
- *Red-team:* stating the back-door / purpose questions as settled would overstate a **live circuit
  split**. *Steel-man:* the field value is exactly the **exhaustive line-drawing** (N9) the instructor
  asked for, *with* the split honestly **annotated** (circuits named, N2) rather than flattened.
- *Adjudication:* the §6.5 #2 line-drawing — area / front-vs-other-doors / purpose-to-talk-not-search /
  time / the-hard-line-to-leave / signs / plain-view / articulation — with the purpose split annotated,
  not resolved (R10; Knock and Talk is in the exhaustive-treatment set, §6.6).

### SI-3-S6 — *Herring* and *Riley*: re-home how? → **Promote *Herring* (Key on Collective Knowledge); demote *Riley* (Related on Common Law).**
- *Adjudication (N6 non-exclusive key-status):* **Key-status is per-page by centrality to *that*
  doctrine.** *Herring* is central to imputed/mistaken collective knowledge → **Key** on Collective
  Knowledge (and remains Key on the Exclusionary Rule — multi-homed). *Riley* is **Key** on its own
  SITA/digital home but, on **Common Law Origins**, it merely **recounts** the founding history → it
  moves to **Related**; *Boyd* stays the Key case there. No exclusivity; framing is page-specific.

### SI-4-S6 — Where does the N9 field framing live, given S4 · R4 / L8 keeps it off case pages? → **On doctrine pages, instructor-reviewed (SR-2).**
- *Question:* S4 · R4 / **L8** bar an agent-authored generalized field takeaway on **case** pages
  (the *Brigham City* "basis to believe" → "see it" scar). So the field-decisive question, the
  line-drawing, and the operational "what this means" have to live **somewhere** — where?
- *Adjudication:* **on doctrine pages** (R3), authored as teaching under the **SR-2** instructor gate,
  **restating** holdings faithfully (no narrowing/broadening — L8). This is the exact division S5 · N9
  routed to S6 ("case pages restate; doctrine pages teach"): S5 ingested the restatement substrate;
  S6 writes the framing. Cross-checked at the gate (R13/§8.5) so a doctrine page's framing never
  contradicts the case page's restatement.

### SI-5-S6 — Reformat the narrative/reference pages into the doctrine brief too? → **No — apply the lessons that fit; keep their shape.**
- *Options:* (a) force every page into the doctrine brief-first template; (b) reformat **doctrine**
  pages fully, and apply only the **applicable** lessons (lexicon, link-every-case, glossary-ready) to
  reference/mnemonic/MOC pages, preserving their form.
- *Red-team (a):* a mnemonic (CREW) or a court-system reference is not a doctrine — forcing a
  field-decisive-question brief onto it is artificial. *Steel-man (b):* the lessons that matter
  site-wide (N2 lexicon, N7 links) apply everywhere; the brief-first **architecture** applies where
  there is a doctrine to teach. *Adjudication:* **(b)** (R11) — Legal Research (S8), the glossary (S7),
  and the generated Case Index (S4) stay out of S6 entirely.

### SI-6-S6 — *Santana*'s subsequent treatment: how to tag it? → **"limited by [[Lange v. California]]" inline.**
- *Adjudication (N4):* *Santana* (hot pursuit into the home, 1976) was historically read broadly; *Lange
  v. California* (2021) held misdemeanor flight does **not** categorically justify warrantless home
  entry. Wherever *Santana* is asserted (Exigent Circumstances; cross-pages), tag **"limited by [[Lange
  v. California]]"** inline + a 1–2-sentence why (it **changes field application** for misdemeanor
  pursuits — U-4 threshold), stated **consistently** across every home (D5).
