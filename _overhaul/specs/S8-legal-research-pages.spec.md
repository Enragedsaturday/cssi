# SPEC S8 — Legal-Research & Citations Pages

status: APPROVED
depends-on: [S1]          gates: []
last-updated: 2026-06-30

> Governed by `docs/STANDARDS.md` (S1, SR-3 supremacy). S8 **splits** the single
> `Legal Research and Case Citations` page into **three focused pages**, **teaches federal
> *and* state citation conventions**, and **features free, verified research tools** (with a
> clearly-labeled low-cost subsection). S8 is **largely independent** — it depends only on S1
> and can run any time after it. This spec is **research-heavy**: every tool below was
> **vetted live against current fact** (web, June 2026 — sources cited in §6.5), per the
> instructor's "assume nothing" steer and **L2** (web discovers; nothing is asserted from
> memory). S8 **designs** the pages and the vetted-tool list; the final pages are **authored
> during execution** under `EXECUTE.wrapper.md`, not now.
>
> **Live-vetting already corrected two errors the current page carries** (§6.5, Appendix A · SI-1/SI-2):
> (1) **OpenCase ≠ OpenJurist.** `opencase.com` is a **real, distinct** AI legal-research
> platform — the instructor's named tool — **not** a nickname for OpenJurist as the current
> page speculates (line 102). (2) **Casetext is retired** as a free standalone — acquired by
> Thomson Reuters (2023) and folded into the paid AI product **CoCounsel** — so older library
> guides that list "free Casetext" are stale and must not be carried over.
>
> **S7 ↔ S8 coordination (carry-forward, resolved here — R4 / Appendix A · SI-3).** S7 routed
> ten **citation-mechanics terms** (*supra, id., pinpoint cite, reporter, parallel citation,
> en banc, certiorari, slip opinion, on remand, vacated*) to **this** page as their home and
> **left them unwired** for S8 to claim (S7 §9; SI-5-S7). S8 **homes** them here under
> addressable `### Term` heading anchors (mirroring S7 · R7's `### Term` → auto-slug
> convention) so S7's term-wiring sweep targets `[[Reading and Citing Cases#en-banc]]` rather
> than re-defining them in the glossary. Neither sweep double-defines.

---

## 1. Objective

Replace the single, overloaded `Legal Research and Case Citations` page with **three focused
pages** an instructor can teach from — (1) **Reading & Citing Cases** (citation anatomy +
federal *and* state conventions + the citation-mechanics term anchors), (2) **Free & Low-Cost
Research Tools** (a vetted, currency-stamped tool table), and (3) **Verifying Good Law**
(shepardizing-by-hand for officers) — so a working cop or instructor can **read a citation
cold, find the opinion fast and free, and confirm it still stands**, all from primary-source
tools the audience can actually reach.

## 2. Scope

**In:**
- The **3-page split** (R1) of `Legal Research and Case Citations` into focused pages, with
  alias/redirect from the old slug so inbound links and popovers survive.
- **Reading & Citing Cases** (R2): federal citation anatomy (carried + tightened from the
  current page) **plus** **federal-vs-state conventions** (R3): prosecuting-party names
  (*State / People / Commonwealth / United States v.*), the civil-vs-criminal caption signal,
  the regional reporters, neutral/public-domain citations, parallel cites, and finding a state
  high-court opinion free.
- The **ten citation-mechanics terms** homed here under `### Term` anchors (R4 — the S7
  carry-forward), authored as plain definitions, not as case-tied assertions.
- **Free & Low-Cost Research Tools** (R5/R6): the **free-first backbone** taught path
  (CourtListener → Google Scholar → Justia, + CAP, govinfo, official court sites, Cornell LII,
  OpenJurist) with a **clearly-labeled low-cost/paid subsection** (vLex Fastcase via bar
  membership; OpenCase Pro noted), each row vetted to current fact.
- **OpenCase framing** (R7 — **downplayed** per the user decision): noted briefly as an
  AI-assist "starting point," **not featured**, with a firm discovery-only / verify-against-
  the-primary-opinion caution grounded in the AI-hallucination research.
- The **tool-fact currency rule** (R8): every tool claim carries a "verified current as of
  <date>" stamp and is re-verified at execution + flagged for periodic re-check; the two
  current-page errors (§ above) are corrected.
- **Verifying Good Law** (R9): the by-hand citator workflow for officers, the 6-tier authority
  lexicon (N2), treatment-status awareness (N13), and cross-links to `[[The Federal Court System]]`.
- The **verification discipline** these reference pages must honor (R10): link-every-named-case
  (N7), two-key for any asserted holding/quote (L1/L4), lexicon (N2), glossary wiring for
  page-less terms (N11/S7), D11 reference-page guardrails.
- **Cross-links + IA placement** (R11) and the **find→adjudicate→fix gate** for the sweep (R12).

**Out (owned elsewhere):**
- The **glossary / general legal-term wiring** → **S7** (S8 only homes the ten citation-
  mechanics terms S7 routed here, and links page-less terms to the S7 glossary).
- The **case object / per-case page skeleton + anchors** for N7 deep-links → **S4** (S8 links
  to case pages; it does not define them).
- The **category taxonomy / where these pages sit in the tree** → **S2**; **nav, breadcrumbs,
  popover/alias config** → **S3** (S8 supplies pages + aliases; it edits no config/component).
- The **standards / lexicon / verification machine** → **S1**; the **final exhaustive
  independent verification** → **S9**.
- **Doctrine-page reformatting, case ingest, flashcards** → S5/S6 (decks frozen through the whole
  overhaul; the page-derived rebuild is a **separate later run** — S4 · R11 as amended by U5-S9, **not**
  an S9 step; S8 touches no deck).

---

## 3. Requirements (numbered, testable)

### R1 — The 3-page split **[USER U1-S8; N8/N9 focused pages]**
Replace `content/Legal Research and Case Citations.md` with **three** pages:
1. **`Reading and Citing Cases.md`** — title *Reading & Citing Cases*; `type: reference`.
2. **`Legal Research Tools.md`** — title *Free & Low-Cost Research Tools*; `type: reference`.
3. **`Verifying Good Law.md`** — title *Verifying Good Law (Shepardizing for Cops)*; `type: reference`.

Each page is **self-contained and focused** (leads with the field-decisive question it answers,
teaches top-to-bottom — N9). The **old slug** `Legal Research and Case Citations` is preserved as
an **alias** on `Reading and Citing Cases` (`aliases: ["Legal Research and Case Citations"]`, via
S3's `AliasRedirects`) so old inbound wikilinks/popovers resolve; execution **greps inbound links**
to the old page and **rewires** each to the most specific new page.
- *Check:* three pages exist with the titles/types above; the old page is gone or stubbed to a
  redirect; `aliases` resolves the old slug; no broken inbound wikilink to the retired page;
  exact slugs reconciled with S2/S3 IA (deferred, §9).

### R2 — Page 1 outline: *Reading & Citing Cases* (federal anatomy, carried + tightened) **[N3 tests-up-front spirit; L1]**
Carry the current page's **federal** citation teaching, tightened, in this order:
1. **Field-decisive question** up front: *"You're handed a cite — what does each part tell you,
   and is it worth trusting?"*
2. **Anatomy of a cite** (running example *Terry v. Ohio*, 392 U.S. 1, 30 (1968)): parties ·
   volume · reporter · first page · pinpoint · court/year parenthetical (+ the existing Mermaid
   left-to-right breakdown).
3. **Which reporter = which court** (the federal reporter table: `U.S.` / `S. Ct.` / `L. Ed. 2d`
   / `F.4th…F.` / `F. Supp.…` / `F. App'x`), tied to precedential weight via `[[The Federal Court System]]`.
4. **Parallel citations** (federal): same SCOTUS opinion, three reporters.
5. **Signals, short forms, and back-references**: no-signal / *See* / *See also* / *Cf.* /
   *E.g.* / *But see* / *Contra*; short forms; **`Id.`**; **`Supra`**.
6. **Published vs. unpublished / per curiam** (carried; weight tie to `[[The Federal Court System]]`;
   FRAP 32.1 caveat retained).
7. **Federal-vs-state conventions** (R3) follow as the second half of the page.
8. **The citation-mechanics term anchors** (R4) live as a labeled subsection (e.g. *"Citation &
   posture terms (quick reference)"*) so each term is an addressable heading.
- *Check:* the federal anatomy is present and accurate; the running example case links to its
  case page (N7); no asserted holding without two-key (L1); the Mermaid renders.

### R3 — Federal-vs-state citation conventions (verified content) **[research-heavy; N10 state scope; L8 restatement care]**
The page teaches the **state** patterns students actually need, each verified (sources §6.5):
- **Prosecuting-party names.** Criminal captions put the **government first**: federal
  *United States v. ___*; state *State v. ___* (most states), *People v. ___* (e.g. CA, NY, IL,
  MI), *Commonwealth v. ___* (PA, MA, VA, KY). **Bluebook short-form rule:** when the deciding
  court sits in that state, shorten to *State / People / Commonwealth* alone; when a court
  **outside** that state decides (e.g. SCOTUS reviewing a Florida case), keep the **state name**
  (*Stern v. Florida*).
- **Caption as a civil-vs-criminal *signal* (not an absolute — L8).** Government-first usually =
  **criminal**; two private-party names usually = **civil**. State it as a **heuristic** and name
  the exceptions so the page does not overclaim: civil enforcement (*United States v. [Corp.]*),
  *in rem* forfeiture (*United States v. $124,700*), *In re ___*, *Ex parte ___*, and habeas
  (*[Petitioner] v. [Warden]*) all break the rule of thumb.
- **Regional reporters (West National Reporter System — 7).** Atlantic (`A.`/`A.2d`/`A.3d`),
  North Eastern (`N.E.`), North Western (`N.W.`), Pacific (`P.`/`P.2d`/`P.3d`), Southern
  (`So.`/`So. 2d`/`So. 3d`), South Eastern (`S.E.`), South Western (`S.W.`). Each covers a fixed
  cluster of states; **Bluebook Table T1** gives each state's official reporter + citation
  preference. (Present as a short table; do **not** assert a full state→region map from memory —
  point to T1 / the volume's front map.)
- **Neutral / public-domain (medium-neutral) citations.** Year + court abbreviation + sequential
  number + **¶** paragraph — e.g. *1997 ND 15, ¶ 21*; *2021 WI 5, ¶ 7*. Adopted by a set of
  states (CO, ME, MT, ND, NH, NM, OK, SD, UT, VT, WI, WY, and others — verify the current list at
  execution, do not freeze it). The `¶` distinguishes paragraph from page; Bluebook pairs the
  neutral cite with a **parallel** regional-reporter cite.
- **Parallel cites (state).** Some state practice strings the official state reporter + the
  regional reporter (*Commonwealth v. Serge*, 586 Pa. 671, 896 A.2d 1170). Many states
  discontinued their official reporters → cite the regional reporter (+ neutral cite). Don't read
  a parallel cite as two different cases.
- **Finding a state high-court opinion free.** CourtListener (all 50 states), Google Scholar
  (state appellate coverage from ~1950), the **state court's own site**, Justia's state
  collections, and vLex Fastcase (bar members). Confirm on the court's own site or CourtListener.
- *Check:* each convention matches the §6.5 sources; lists that drift over time (neutral-cite
  states; T1 specifics) are pointed to the authority, not asserted from memory (L2/R8); the
  civil-vs-criminal point is stated as a signal with exceptions (L8), not an absolute.

### R4 — Citation-mechanics terms homed here (the S7 carry-forward) **[S7 §9/SI-5-S7; S7 · R7 convention; N11 routing]**
Define the **ten** terms S7 routed here, as a labeled quick-reference subsection of *Reading &
Citing Cases*, **each a `### Term` heading** (Quartz auto-slugs it — same mechanism as S7 · R7),
so S7's wiring resolves `[[Reading and Citing Cases#<slug>]]`:
*supra · id. · pinpoint cite (pin cite) · reporter · parallel citation · en banc · certiorari
(cert.) · slip opinion · on remand · vacated.*
- **Authoring discipline** (mirrors S7 · R9): each is a **plain-English definition** (≤ ~2
  sentences) **+ one concrete example**; these are **definitional**, carry **no citation**, and
  **assert no case-tied holding** — if a definition would assert a case-tied proposition, it is a
  two-key (L1) event (serial CL, L4) **or** is kept generic with the proposition routed to the
  owning page. Several terms (*en banc, certiorari, vacated, on remand, slip opinion*) interact
  with **authority weight / good-law status** — cross-link `[[The Federal Court System]]` for
  weight and note that **`vacated`** sets aside the decision (treatment-status interaction, N13).
- **No double-definition.** These ten are **not** added to `Common Legal Terms` (the glossary);
  S7's term sweep **routes** them here (S7 leaves them unwired; S8 claims them). Record the
  S7↔S8 coordination so the two sweeps don't collide.
- *Check:* all ten are `### Term` headings with resolvable slugs; each has a definition + example
  in the reference voice; none asserts an uncited case-tied holding; none is duplicated in the
  glossary; a `[[Reading and Citing Cases#term]]` link resolves for each.

### R5 — Page 2 outline + tier policy: *Free & Low-Cost Research Tools* **[USER U2-S8; L2]**
The page is **free-first**, with a **clearly-labeled low-cost/paid subsection**:
1. **Field-decisive question:** *"You don't have Westlaw or Lexis. How do you find — and trust —
   a free copy of the opinion?"*
2. **The taught path (primary-source, verifiable):** **CourtListener → Google Scholar → Justia.**
   These are the backbone the course teaches and the wiki itself verifies against.
3. **The free backbone (full table, R6):** CourtListener, Google Scholar, Justia, Caselaw Access
   Project, govinfo, official court/SCOTUS sites, Cornell LII, OpenJurist.
4. **Low-cost / paid (optional — clearly flagged):** **vLex Fastcase** (free **only** via a
   bar-association membership — flag that a police instructor is usually **not** a bar member);
   **OpenCase Pro** (~$82/mo) noted under R7's downplayed framing. **Casetext is not listed** —
   it is retired into the paid CoCounsel (R8 correction).
5. **Search by what you have** (carried: by citation · by party name · by proposition/full text).
- *Check:* free tools lead and are visually primary; the paid subsection is labeled and optional;
  the bar-membership caveat is explicit; no retired/defunct tool (Casetext, Ravel) is featured.

### R6 — The vetted-tool table (content + columns) **[research-heavy; L2; the §6.4 deliverable]**
The page carries a table with columns **Tool · Use · Free-tier · Reliability · Caution**, grouped
**Free backbone** then **Low-cost/paid**, populated with the **verified-current** facts in **§6.4**
and the **per-tool vetting sources** in **§6.5**. No tool is listed that web-vetting did not
confirm is **real and live** (the rule the current page states but its "opencase" guess violated).
- *Check:* every row's facts trace to a §6.5 source; every tool resolves to a real live resource;
  the table matches §6.4; OpenJurist and OpenCase appear as **distinct** rows (de-conflated).

### R7 — OpenCase framing: downplayed, discovery-only, verify-against-primary **[USER U3-S8; L2; AI-hallucination research]**
OpenCase (`opencase.com`) is **real** — an AI-assisted research platform (case law, statutes,
regs, court rules; Word/Docs/Outlook integrations) built on Cornell LII + RECAP + govinfo data,
with ISO 42001 / SOC 2 Type II governance and a **limited free tier** (exact limits not publicly
documented — re-confirm live at execution; Pro ~$82/mo). Per the user decision it is **downplayed,
not featured**:
- Appears **briefly** — e.g. *"Some students like OpenCase's free AI tier; treat it as a starting
  point only."* — under the low-cost subsection, **after** the primary-source tools.
- Carries a **firm caution** grounded in research: **AI legal-research tools hallucinate** — even
  top-tier tools are only ~78–81% accurate (≈ 1 in 5 wrong; 17–33% hallucination rates measured
  for Lexis+ AI / Westlaw AI). So OpenCase is **discovery only**: **verify every case, holding,
  and quote against the primary opinion on CourtListener before relying on it** (this is the
  wiki's **L2** discipline applied to the tool itself — AI output is discovery, never assertion).
- *Check:* OpenCase is present but not visually featured above the free primary tools; the
  discovery-only / verify-against-primary caution is explicit and sourced; it is **not** conflated
  with OpenJurist.

### R8 — Tool-fact currency rule (assume-nothing, dated) **[L2; L6; N13-analog]**
Tool descriptions are **factual claims about third-party services that change**. Therefore:
- Every tool claim carries a **"verified current as of <date>"** stamp (page-level note is fine);
  the page is **re-verified at execution** and **flagged for periodic re-check** (the same "good
  as of <date>" discipline N13 applies to cases, applied to tools).
- Execution **corrects the two current-page errors**: (a) **OpenCase ≠ OpenJurist** (delete the
  line-102 speculation; list both as distinct tools); (b) **Casetext is retired** into paid
  CoCounsel (do not carry "free Casetext"); and **drops defunct tools** older guides still list
  (e.g. **Ravel Law**, absorbed by LexisNexis) unless re-vetted live.
- *Check:* the currency stamp is present; both corrections are made; no defunct/retired tool is
  asserted as live; any list that drifts (neutral-cite states; free tiers) cites the authority
  rather than freezing a snapshot.

### R9 — Page 3 outline: *Verifying Good Law (Shepardizing for Cops)* **[N2 lexicon; N13; L1; D11]**
The by-hand good-law workflow for officers (no Shepard's/KeyCite budget):
1. **Field-decisive question:** *"Before I teach or rely on this case — is it still good law?"*
2. **Citator-by-hand:** CourtListener's **"Cited By" / "Authorities"** and Google Scholar's
   **"How cited"** — what they do and don't give you (a citation graph, **not** an editorial
   red-flag system).
3. **Scan the treatment:** has a later court **followed / criticized / distinguished / limited /
   overruled** it? A narrowed or reversed case is a trap (ties to N4 subsequent-treatment, N13
   status).
4. **Read the opinion — never a headnote or summary** (carried; headnotes are editorial,
   not the court's words).
5. **Confirm court, published status, and currency**, and **flag circuit splits** rather than
   picking a side — using the **6-tier authority lexicon** (N2: *Binding — SCOTUS* / *Binding
   in-circuit* / *Persuasive (outside circuit)* / *Persuasive — state, illustrative* /
   *Persuasive only — non-precedential* / *Historical*), **never** "persuasive, not binding."
   Cross-link `[[The Federal Court System]]`.
6. **Save the unit:** cite + CourtListener permalink + pinpoint (carried — the trustworthy-research
   triple).
- *Check:* the workflow is officer-usable and primary-source-grounded; weight language uses the
  6-tier lexicon (LINT-4); treatment language matches N13/N4; "read the opinion" rule present.

### R10 — Verification discipline for these reference pages **[L1, L2, N2, N7, N11, N13, D11]**
Though these are **reference** pages (not doctrine pages, so the brief-first doctrine TOC of
S1 §3.I does not bind them), the standards still apply:
- **N7 link-every-named-case:** every example case named (e.g. *Terry v. Ohio*) links to its case
  page (S4); whole-case reference → case page; passage reference → pinpoint deep-link.
- **L1 two-key:** any asserted **holding/quote** is verified live against the primary opinion via
  the **serial CL lane** (L4). The CL load here is **light** (these pages teach *mechanics*, not
  holdings) but non-zero (named example cases) — paced in the single lane.
- **N2 lexicon:** any authority-weight statement uses the 6 tiers; banned "persuasive, not binding".
- **N11 glossary wiring:** non-vernacular terms that have **no page home** link to the S7 glossary;
  the ten citation-mechanics terms are homed here (R4), not glossary-linked.
- **N13 treatment status:** where a case's good-law status is discussed (Page 3), it is explicit.
- **D11 reference-page guardrails:** no apocryphal cases, no uncited mnemonics, no inline
  `## Flashcards` (LINT-8).
- *Check:* LINT-5 (link-every-case), LINT-4 (lexicon), LINT-7 (glossary best-effort), LINT-1
  (any CL URL resolves to the named case), LINT-8 (guardrails) pass; any asserted holding shows
  CL evidence.

### R11 — Cross-links & IA placement **[N7; S2/S3/S4/S7]**
- **Cross-links:** `[[The Federal Court System]]` (court hierarchy + weight), the **S7 glossary**
  (page-less terms), **case pages** (S4, every named case), `[[Fourth Amendment Analysis Checklist]]`,
  and **between the three new pages** (Reading ↔ Tools ↔ Verifying). Each page's `related:`
  frontmatter lists its siblings + the above.
- **IA placement** defers to **S2** (which category/section the three reference pages sit in) and
  **S3** (nav, breadcrumbs, popovers, the `AliasRedirects` for the old slug). S8 supplies the
  pages, the `aliases`, and the `related:` graph; it **edits no config/component**.
- *Check:* every cross-link target resolves; the three pages are mutually linked; the old slug
  aliases; `related:` is reciprocal where appropriate; slugs reconciled with S2/S3 (§9).

### R12 — The find→adjudicate→fix gate for the sweep **[L5, L4, L1, §8]**
The split + authoring runs the standing machine (S1 §3.G):
- **REVIEW** (parallel, free, **no-CL**): outline compliance (R2/R5/R9), tool-table accuracy vs
  §6.5 sources (R6/R8), term-anchor resolution (R4), lexicon (R9/R10), link-every-case (R10),
  the two error corrections (R8). Reviewers **do not edit**.
- **ADJUDICATE:** a **tool-fact** finding is adjudicated **against the live tool + a current
  source** (web re-vet — the tool analog of CL evidence); a finding that a page **asserts a
  case-tied holding/quote** is `needs_cl=true` → the **single serial CL lane** (L1/L4); link/format
  findings → a free editor-adjudicator; **DISMISSED logged with reason**.
- **FIX:** apply only UPHELD/MODIFIED; introduce no new asserted holdings; **ESCALATE →
  `_review-needed/<slug>.md`**. **Loop cap 3**, checkpointed.
- *Check:* every tool row + asserted holding traces to an adjudicated verdict; case-tied
  assertions show CL evidence in `cl-calls.log`; tool-fact corrections trace to a current source;
  escalations logged.

---

## 4. Lessons enforced

- **L2 (web discovers; nothing asserted from memory)** → the **whole spec**: every tool was
  live-vetted (§6.5), the two memory-errors on the current page are corrected (R8), and R7 applies
  L2 to AI output itself (OpenCase = discovery, verify against the primary opinion). **L6
  ("not found" ≠ "doesn't exist")** → its inverse also bit here: the current page declared
  "opencase" *was* OpenJurist from a single guess; R8 forces live confirmation before any tool
  claim. **L1/L4 (two-key, serial CL)** → R10/R12 (asserted holdings only). **L8 (restate, don't
  drift)** → R3's civil-vs-criminal *signal* (stated with exceptions, not as an absolute).
- **N2 (6-tier lexicon)** → R9/R10 (weight language; banned "persuasive, not binding"). **N3
  (tests up front)** spirit → R2/R5/R9 lead with the field-decisive question. **N7 (link every
  case)** → R10. **N9 (frame around the officer's question)** → each page's lead question.
  **N10 (state scope explicitly)** → R3 (federal *and* state conventions; lists pointed to the
  authority, not frozen). **N11 (wire the glossary; route to home)** → R4 (citation-mechanics
  terms homed here, not double-defined) + R10 (page-less terms → S7 glossary). **N13 (no blank
  treatment status; "good as of <date>")** → R8 (the same dated-currency discipline applied to
  tools) + R9 (good-law status explicit).
- **D11 (practical/reference-page accuracy + guardrails)** → R6/R8/R10. **D13 (linking & wiring)**
  → R4/R10/R11. **SR-3 (`docs/STANDARDS.md` supremacy)** → every step cites S1; LINT-1/4/5/7/8 key
  to S1's roster.
- **S7** (it routed the ten citation-mechanics terms here and left them unwired) → R4 claims them
  under the S7 · R7 anchor convention. **S4** (case pages) → R10/R11 link targets. **S2/S3** (IA,
  nav, alias config) → R1/R11 placement. **S1 §3.I** notes these are reference pages, so the
  brief-first *doctrine* TOC does not bind them, but L1/N2/N7/N11/N13 do (R10).

## 5. Method (how execution proceeds against this spec)

Runs **after S1** (independent of S2–S7 content, but **coordinates with S7** on the ten terms):

1. **Split (R1).** Create the three pages with frontmatter (`type: reference`, `related:`); add
   `aliases: ["Legal Research and Case Citations"]` to `Reading and Citing Cases`; **grep inbound
   links** to the old page and rewire each to the most specific new page; retire/stub the old page.
2. **Author Page 1 (R2–R4).** Carry + tighten the federal anatomy; add the verified federal-vs-
   state conventions (R3); add the ten `### Term` citation-mechanics anchors (R4) — plain
   definitions, no case-tied assertions; **coordinate with S7** so those ten are routed here and
   not glossary-defined.
3. **Author Page 2 (R5–R8).** Build the free-first table from **§6.4** with the **§6.5** sources;
   add the labeled low-cost subsection (vLex Fastcase + bar caveat; OpenCase Pro under R7's
   downplayed framing); stamp **"verified current as of <date>"**; make the two corrections (R8).
4. **Author Page 3 (R9).** The by-hand good-law workflow; 6-tier lexicon; treatment-status; "read
   the opinion."
5. **Wire & cross-link (R10/R11).** Link every named case to its case page (N7); route page-less
   terms to the S7 glossary; mutually link the three pages + `[[The Federal Court System]]`.
6. **Gate (R12).** find→adjudicate→fix; tool-fact findings re-vetted against a live source;
   case-tied holdings → serial CL (L4); run LINT-1/4/5/7/8; escalate to `_review-needed/`.
7. **Touch no deck, no config, no component** (S2/S3/S4 own those). Hand to **S9** for final
   verification (S8 re-vetting of tool facts feeds S9's currency check).

## 6. Deliverables (what execution produces or changes)

### 6.1 — The three pages
- `content/Reading and Citing Cases.md` (`type: reference`; alias `Legal Research and Case Citations`).
- `content/Legal Research Tools.md` (`type: reference`).
- `content/Verifying Good Law.md` (`type: reference`).
- The retired `content/Legal Research and Case Citations.md` (stub/redirect; inbound links rewired).
*(Exact filenames/slugs reconciled with S2/S3 IA — §9; the `related:` graph per R11.)*

### 6.2 — Page outlines
**Page 1 — *Reading & Citing Cases*** (R2/R3/R4): lead question → anatomy (+ Mermaid) → reporter→court
table → parallel cites (federal) → signals/short forms/`Id.`/`Supra` → published vs. unpublished /
per curiam → **federal-vs-state conventions** (prosecuting-party names + Bluebook short-form rule;
civil-vs-criminal *signal* + exceptions; regional reporters table → T1; neutral/public-domain cites
with `¶`; parallel cites; finding a state opinion free) → **Citation & posture terms (quick
reference)** = the ten `### Term` anchors (R4).

**Page 2 — *Free & Low-Cost Research Tools*** (R5/R6/R7/R8): lead question → taught path
(CourtListener → Scholar → Justia) → **free backbone table** (§6.4) → **low-cost/paid** subsection
(vLex Fastcase + bar caveat; OpenCase noted, downplayed, with the verify-caution) → search-by-what-
you-have → **"verified current as of <date>"** stamp.

**Page 3 — *Verifying Good Law (Shepardizing for Cops)*** (R9): lead question → citator-by-hand
(CourtListener Cited By/Authorities; Scholar How cited) → scan treatment (followed/criticized/
distinguished/limited/overruled) → read the opinion, not the headnote → confirm court/published/
current + flag splits (6-tier lexicon, `[[The Federal Court System]]`) → save the cite+permalink+pin unit.

### 6.3 — The citation-mechanics term set (R4, homed here)
Ten `### Term` anchors on Page 1, plain definitions + example, no case-tied assertion:
*supra · id. · pinpoint cite (pin cite) · reporter · parallel citation · en banc · certiorari (cert.)
· slip opinion · on remand · vacated.* S7's sweep targets `[[Reading and Citing Cases#<slug>]]`;
**not** added to the glossary.

### 6.4 — The vetted-tool table (verified current, June 2026 — sources §6.5)

**Free — the backbone (the taught path is the first three):**

| Tool | Use | Free-tier | Reliability | Caution |
|---|---|---|---|---|
| **CourtListener** (Free Law Project) | Full-text + citation search across ~10M federal & state opinions; integrated citator ("Cited By"/"Authorities"); **RECAP** docket archive; stable permalinks. **The wiki's verification source.** | Fully free; no account to search (account for alerts). | **Highest** — primary-source; also the search route into the CAP corpus. | Citator is a citation **graph**, not an editorial Shepard's red-flag — read the treatment yourself. |
| **Google Scholar** (Case law) | Fastest full-text start; **"How cited"** lightweight citator. | Fully free. Coverage: state appellate/supreme ~1950→, federal 1923→, SCOTUS 1791→. | Good for **finding**. | "Makes no guarantees regarding currency"; not as current as paid; no red-flag system — read the opinion. |
| **Justia** | Clean browsable directory by court/jurisdiction; strong free SCOTUS collection + summaries. | Fully free (for-profit, ad-supported). | Good for **access**. | Summaries are **editorial secondary** — read the opinion; coverage dates vary. |
| **Caselaw Access Project (CAP / case.law)** | Harvard LIL digitization of **all official book-published US case law through 2020**; API + bulk download. | Fully free. | **High** (official book-published). | Native search **retired Sept 2024** → search via **CourtListener**; coverage **ends at 2020** (no newer cases). |
| **govinfo** (GPO) | Authenticated government PDFs incl. historic bound **U.S. Reports** (~1790s–early 1990s). | Fully free, authoritative. | **High** (authenticated). | Not a search-by-proposition tool; for official PDFs / older volumes. |
| **Official court / SCOTUS sites** (supremecourt.gov; circuit & district sites) | **Authoritative** slip opinions day-of; bound U.S. Reports. | Free. | **Highest** (the court's own text). | Each hosts only **its own** opinions; no cross-court search; slip-op pagination is provisional. |
| **Cornell LII** | Free primary law (statutes, rules), SCOTUS from 1990 + historic decisions, **Wex** legal dictionary. | Free. | **High** (Cornell). | Limited older case-law coverage; best for statutes/definitions, not deep case search. |
| **OpenJurist** | Free **public-domain** federal case law (SCOTUS back to 1790; Federal Reporter back to 1880); fallback. | Free (ad-supported). | Moderate (older corpus). | Older/clunkier UI; ads; not comprehensive for modern cases. **≠ OpenCase** (distinct tool). |

**Low-cost / paid (optional — clearly flagged):**

| Tool | Use | Free-tier | Reliability | Caution |
|---|---|---|---|---|
| **vLex Fastcase** | Comprehensive — all 50 states + SCOTUS + all federal courts + statutes/regs/rules + citator. | **Free via bar-association membership** (80+ bars); otherwise paid. | **High**. | Requires a **bar membership** — a police instructor is usually **not** a bar member, so often inaccessible to this audience. (Fastcase merged into vLex, now part of Clio.) |
| **OpenCase** (`opencase.com`) — *downplayed, R7* | AI-assisted Q&A over case law/statutes/regs/rules; Word/Docs/Outlook integrations. Built on Cornell LII + RECAP + govinfo. | **Limited free tier** (exact limits not publicly documented — re-confirm live); Pro ~$82/mo, 3-day trial; US-only. | ISO 42001 / SOC 2 Type II governance — **but a new AI tool.** | **AI hallucinates** (top legal-AI ~78–81% accurate; 17–33% hallucination measured for Lexis+ AI / Westlaw AI). **Discovery only — verify every output against the primary opinion on CourtListener** (L2). |

**Not featured (corrections — R8):** **Casetext** (retired into Thomson Reuters' paid **CoCounsel**;
old guides listing "free Casetext" are stale); **Ravel Law** (absorbed by LexisNexis; defunct as a
standalone). Do not carry either unless re-vetted live.

### 6.5 — Per-tool vetting sources (the standard requires verification, not memory)
- **OpenCase (real; ≠ OpenJurist; free tier; AI caution):**
  [opencase.com](https://www.opencase.com/) ·
  [opencase.com/pricing](https://www.opencase.com/pricing) ·
  [OpenCase press release (Barchart)](https://www.barchart.com/story/news/33637041/opencase-makes-u-s-law-more-accessible-with-new-ai-driven-legal-information-platform) ·
  [Microsoft Marketplace listing](https://marketplace.microsoft.com/en-us/product/saas/wa200009633?tab=overview)
- **AI-hallucination caution (R7):**
  [Stanford HAI — Legal models hallucinate 1 in 6+](https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries) ·
  [Stanford RegLab — *Hallucination-Free?* (arXiv 2405.20362)](https://arxiv.org/pdf/2405.20362) ·
  [AI Law Librarians — what the science says (2026)](https://www.ailawlibrarians.com/2026/02/19/what-the-science-says-about-hallucinations-in-legal-research/)
- **CourtListener / RECAP / CAP route:**
  [courtlistener.com](https://www.courtlistener.com/) ·
  [LOC — CourtListener & CAP](https://guides.loc.gov/free-case-law/courtlistener-and-caselaw-access-project)
- **Caselaw Access Project (search retired 2024; through 2020):**
  [case.law](https://case.law/) · [case.law/about](https://case.law/about/) ·
  [Jenkins Law Library — Open-Access Caselaw (2025)](https://www.jenkinslaw.org/blog/2025/04/03/open-access-caselaw)
- **Google Scholar (coverage; currency caveat):**
  [LOC — Google Scholar](https://guides.loc.gov/free-case-law/google-scholar) ·
  [NYLS LibGuide — low-cost case law](https://libguides.nyls.edu/lowcostlegalresearch/caselaw)
- **Justia / Cornell LII / FindLaw / general free-research guides:**
  [NYLS LibGuide — case law](https://libguides.nyls.edu/lowcostlegalresearch/caselaw) ·
  [Georgetown — Free & Low-Cost Legal Research](https://guides.ll.georgetown.edu/freelowcost) ·
  [Pace Law — Free & Low-Cost case law](https://libraryguides.law.pace.edu/free/freecaselaw)
- **vLex Fastcase (free via bar; coverage):**
  [vLex Fastcase Library](https://vlex.com/fastcase-library) ·
  [NYSBA — free vLex Fastcase](https://nysba.org/attorney-resources/vlex-fastcase-legal-research/) ·
  [Florida Bar — vLex Fastcase free to members](https://www.floridabar.org/the-florida-bar-news/improved-vlex-fastcase-is-free-to-florida-bar-members/)
- **Casetext → CoCounsel (retired free; acquired by Thomson Reuters):**
  [TR completes Casetext acquisition (2023)](https://www.thomsonreuters.com/en/press-releases/2023/august/thomson-reuters-completes-acquisition-of-casetext-inc) ·
  [TR CoCounsel](https://www.thomsonreuters.com/en/cocounsel)
- **State-citation conventions (R3):**
  [Suffolk — Bluebook Rule 10 / state cases](https://www.suffolk.edu/law/faculty-research/library-services/a-bluebook-guide-for-law-students/case-citation-rule-10) ·
  [USC Law — Citing State Cases](https://guides.law.sc.edu/LRAWFall/CitingStateCases) ·
  [Georgetown — Bluebook State Courts](https://guides.ll.georgetown.edu/c.php?g=261289&p=2339384) ·
  [NYU Law — State & Regional Reporters](https://nyulaw.libguides.com/c.php?g=773843&p=5551864) ·
  [ND Courts — Rule 11.6 medium-neutral citations](https://www.ndcourts.gov/legal-resources/rules/ndrct/11-6) ·
  [Justia — Public Domain Legal Citations](https://lawblog.justia.com/2010/12/17/public-domain-legal-citations/) ·
  [Cornell — caption (Wex)](https://www.law.cornell.edu/wex/caption)

### 6.6 — The currency-stamp + corrections note
A short page-level "verified current as of <date>" note on Page 2, the two error-corrections made
(OpenCase≠OpenJurist; Casetext retired), and a flag for periodic re-vetting (R8) — closing the loop
the current page's "opencase" guess left open.

## 7. Acceptance criteria (definition of done)

- [ ] **Split (R1):** three `type: reference` pages exist (*Reading & Citing Cases*, *Free &
      Low-Cost Research Tools*, *Verifying Good Law*); the old slug aliases to *Reading & Citing
      Cases*; inbound links rewired; no broken wikilink to the retired page.
- [ ] **Page 1 (R2/R3):** federal anatomy carried + tightened (Mermaid renders); federal-vs-state
      conventions present and matching §6.5 sources (prosecuting-party names + short-form rule;
      civil-vs-criminal **signal** with exceptions; regional reporters → T1; neutral cites with `¶`;
      parallel cites; finding a state opinion free).
- [ ] **Citation-mechanics terms (R4):** all ten are `### Term` anchors with resolvable slugs +
      definition + example; none asserts an uncited case-tied holding; none duplicated in the
      glossary; `[[Reading and Citing Cases#term]]` resolves for each; S7↔S8 coordination recorded.
- [ ] **Tools page (R5/R6):** free tools lead and are visually primary; the table carries
      Tool·Use·Free-tier·Reliability·Caution; every row traces to a §6.5 source; OpenJurist and
      OpenCase are **distinct** rows.
- [ ] **OpenCase (R7):** present but downplayed (after the primary tools); the discovery-only /
      verify-against-primary caution is explicit and sourced; not conflated with OpenJurist.
- [ ] **Currency + corrections (R8):** "verified current as of <date>" stamp present; OpenCase≠
      OpenJurist and Casetext-retired corrections made; no defunct/retired tool asserted live.
- [ ] **Verifying Good Law (R9):** by-hand citator workflow; 6-tier lexicon (no "persuasive, not
      binding"); treatment-status; "read the opinion" rule; cite+permalink+pin unit.
- [ ] **Discipline (R10):** every named case links to its case page (N7); any asserted holding is
      two-key (CL evidence); LINT-1/4/5/7/8 pass; D11 guardrails clean.
- [ ] **Cross-links/IA (R11):** the three pages are mutually linked + `[[The Federal Court System]]`,
      glossary, case pages, checklist; slugs reconciled with S2/S3; aliases resolve.
- [ ] **Gate (R12):** every tool row + asserted holding traces to an adjudicated verdict; tool-fact
      corrections trace to a current source; case-tied assertions show CL evidence; escalations
      logged; loop cap 3; no deck/config/component touched.

## 8. Verification plan (how S8's output gets verified)

Through the standing **find → adjudicate → fix** machine (S1 §3.G), serial CL (L4) only where a
page asserts a case-tied holding:

1. **REVIEW (parallel, free, NO CL).** Per page, findings `{id, page, locator, problem, severity,
   proposed_fix, needs_cl, confidence}` against: outline compliance (R2/R5/R9), tool-table accuracy
   vs §6.5 (R6/R8), term-anchor resolution (R4), lexicon (R9/R10), link-every-case (R10), and the
   two corrections (R8). **Reviewers do not edit.**
2. **ADJUDICATE.** **Tool-fact** findings → re-vetted against the **live tool + a current source**
   (the tool analog of CL evidence) and the verdict cites it. **Case-tied holding/quote** findings
   (`needs_cl=true`) → the **single serial CL lane** (two-key, L1); verdict cites CL evidence (or
   the assertion is removed/routed to the owning page). Link/format/definition findings → a **free
   editor-adjudicator**. **DISMISSED logged with reason.**
3. **FIX (parallel, free).** Apply only UPHELD/MODIFIED; introduce no new asserted holdings;
   **ESCALATE → `_review-needed/<slug>.md`**. **Loop cap 3.**
4. **Automated lint gate (pre-publish):** **LINT-5** (every named case → a case-page wikilink),
   **LINT-4** (6-tier lexicon; banned "persuasive, not binding"), **LINT-7** (page-less terms →
   glossary, best-effort), **LINT-1** (any CL URL resolves to the named case), **LINT-8**
   (guardrails). Plus an S8-specific **anchor check**: every `### Term` (R4) slug resolves and the
   old-slug **alias** resolves.
5. **Tool-currency re-vet:** the "verified current as of <date>" claims are re-confirmed live at
   execution and at S9; any drifted fact (free-tier change, a tool going dark) is corrected, not
   frozen (R8). Specifically re-confirm: OpenCase's **free-tier limits**, the **neutral-cite state
   list**, and **vLex Fastcase** bar-access terms.
6. **Popover/alias spot-check (S3):** hover a wired citation-mechanics term → its definition
   previews from the anchor; the old `Legal Research and Case Citations` link resolves via alias.
7. **Non-regression:** no doctrine page, deck, config, or component changed; the build succeeds;
   `[[The Federal Court System]]`, glossary, and case-page links resolve.

## 9. Open items / escalations

- **Exact slugs / IA placement (R1/R11) defer to S2/S3.** S8 proposes filenames
  (`Reading and Citing Cases`, `Legal Research Tools`, `Verifying Good Law`) and the old-slug alias;
  S2 decides which category/section they sit in and S3 owns nav/breadcrumbs/redirects. Non-blocking.
- **OpenCase free-tier specifics (R7/R8).** The free-tier limits are **not publicly documented**
  (the pricing page is JS-rendered; press coverage omits them). Execution **re-confirms the live
  free tier** before publishing any specifics; until then the page describes it conservatively
  ("limited free tier; a starting point only").
- **Lists that drift (R3/R8).** The **neutral-citation state list** and **Bluebook T1** specifics
  change; the page points to the authority (T1 / the court's rule) rather than freezing a snapshot,
  and S9 re-checks currency.
- **S7 coordination ordering (R4).** S7 left the ten citation-mechanics terms **unwired** for S8 to
  claim. If S8 executes **before** S7's sweep, S8 still homes the terms here (anchors ready); if
  **after**, S8 confirms S7 did not glossary-define them. Either way: **route, don't duplicate**.
- **vLex Fastcase accessibility (R5/R6).** Free **only** via bar membership — flagged as often
  inaccessible to a police-instructor audience. If the instructor wants a member-only tool dropped
  entirely, that's a one-line edit at execution. Non-blocking.
- **Two-key load (R10/R12).** Light — these pages teach mechanics, not holdings — but any named
  example case still hits the serial CL lane (L4) for its case-page link + good-law status; paced/
  checkpointed; RUNBOOK §3 STOP-and-notify governs if the CL tier regresses.

---

## Appendix A — Decision log

*Format: Question · Options · Red-team · Steel-man · Adjudication. **[USER]** = the user's actual
choice; the rest are self-interviewed.*

### [USER] U1-S8 — Page split structure → **Three focused pages.**
- *Options:* (a) **4 pages** (Reading · Fed-vs-State · Tools · Verify-Good-Law); (b) **3 pages**
  (Reading & Citing Cases [fed+state] · Tools · Verify-Good-Law); (c) **2 pages** (Citations · Tools).
- *Red-team (a):* a standalone "Fed-vs-State" page risks thinness and overlaps "Reading." *Red-team
  (c):* under-split — a 2-page version recombines distinct jobs (find vs. verify). *Steel-man (b):*
  keeps reading+citing as one coherent skill, keeps the genuinely-distinct "is it still good law?"
  workflow on its own page (the shepardizing-sparse gap, N13), and keeps the vetted tool table
  focused. *Adjudication:* **(b)** — user selected the 3-page split. Federal+state conventions live
  together on Page 1; Tools and Verifying-Good-Law are their own focused pages.

### [USER] U2-S8 — Tool tiers to feature → **Free-first + a labeled low-cost subsection.**
- *Options:* (a) **free-first + labeled low-cost** (free backbone primary; a flagged low-cost/paid
  subsection); (b) **free-only** (no paid alternatives featured); (c) **free + paid, equal billing.**
- *Red-team (c):* equal billing steers a no-budget police-academy audience toward subscriptions.
  *Red-team (b):* drops genuinely useful low-cost options (vLex Fastcase via bar) the instructor
  asked to surface. *Steel-man (a):* free primary-source tools lead and are visually primary; a
  small, clearly-labeled low-cost subsection honors "verified low-cost alternatives" without
  burying the free path. *Adjudication:* **(a)** — user selected. Free backbone is the taught path
  (CourtListener → Scholar → Justia); low-cost/paid is a flagged, optional subsection.

### [USER] U3-S8 — OpenCase framing (given the AI-hallucination risk) → **Downplay; lead with free primary tools.**
- *Context:* The instructor **named opencase.com** and students like its free tier; vetting confirms
  it's **real** (≠ OpenJurist) and credentialed (ISO 42001 / SOC 2 Type II, built on Cornell LII +
  RECAP + govinfo) — **but** it's an AI tool, and independent research finds even top legal-AI tools
  hallucinate (≈ 1 in 5 wrong; 17–33% for Lexis+ AI / Westlaw AI). This sits in tension with the
  wiki's "verify against the primary opinion, never trust AI/secondary" ethos.
- *Options:* (a) feature it with a firm verify-caution; (b) feature it plainly; (c) **downplay;
  lead with free primary tools.**
- *Red-team (b):* featuring an AI tool plainly undercuts the verify-everything discipline the whole
  overhaul exists to enforce. *Red-team (a):* even cautioned, prominence signals endorsement.
  *Steel-man (c):* the taught path stays primary-source and verifiable; OpenCase is **acknowledged**
  (students use it) but framed as a **starting point only**, with the discovery-only / verify-
  against-primary caution. *Adjudication:* **(c)** — user selected. R7 implements: brief mention,
  not featured, firm L2 caution, de-conflated from OpenJurist.

### SI-1-S8 — Is "opencase" the OpenJurist nickname the current page claims? → **No — OpenCase is a real, distinct tool; correct the page.**
- *Question:* The current page (line 102) asserts *"This is the resource the class notes meant by
  'opencase' — older and clunkier than CourtListener"* — i.e. it guesses "opencase" = **OpenJurist**.
- *Findings (live web):* **`opencase.com` is a real, distinct** AI legal-research platform (NY
  company; rep Raymond Lei; Cornell LII + RECAP + govinfo data; free tier + Pro ~$82/mo; ISO 42001 /
  SOC 2 Type II). **OpenJurist** is a separate, older public-domain case-law site. They are not the
  same resource.
- *Red-team (keep the guess):* the guess is "good enough" and avoids featuring an AI tool. *Steel-man
  (correct it):* this is exactly the **L2/L6 scar** — a confident assertion from a single guess,
  never confirmed. The instructor explicitly named opencase.com; honoring "assume nothing" means
  vetting and correcting. *Adjudication:* **correct it** (R8): list **OpenCase** and **OpenJurist**
  as **distinct** tools; delete the line-102 speculation. Sources: §6.5.

### SI-2-S8 — Carry "free Casetext" (and Ravel) from older guides? → **No — both are retired/defunct; drop them.**
- *Question:* Older library guides (Georgetown, etc.) list **Casetext** and **Ravel Law** as
  low-cost tools. Feature them?
- *Findings (live web):* **Casetext** was acquired by Thomson Reuters (2023, $650M) and folded into
  the **paid AI product CoCounsel** — the free standalone is gone. **Ravel Law** was absorbed by
  LexisNexis (2017) and is defunct as a standalone. The guides listing them as live free/low-cost
  tools are **stale**.
- *Adjudication:* **drop both** (R8); note Casetext→CoCounsel as a correction so a future editor
  doesn't re-add "free Casetext." Re-vet before listing any tool an older guide names. This is the
  **tool-fact currency rule** (R8) in action.

### SI-3-S8 — Where do the ten S7-routed citation-mechanics terms live? → **Homed here under `### Term` anchors; not in the glossary.**
- *Question:* S7 routed *supra, id., pinpoint cite, reporter, parallel citation, en banc,
  certiorari, slip opinion, on remand, vacated* to **this** page and **left them unwired** (S7 §9 /
  SI-5-S7). Define them here, or let the glossary take them?
- *Options:* (a) **home them here** under addressable `### Term` headings (mirroring S7 · R7's
  `### Term` → auto-slug convention), so S7's sweep targets `[[Reading and Citing Cases#term]]`;
  (b) define them in the **glossary** instead (override S7's routing); (c) define inline in prose
  with **no anchors** (no wiring target).
- *Red-team (b):* contradicts S7's explicit decision (these are citation/posture mechanics whose
  natural home is the Legal Research page) and would **double-define** what S7 deliberately left for
  S8. *Red-team (c):* leaves S7's wiring nothing to point at — N7/N11 want a stable target.
  *Steel-man (a):* citation-mechanics + procedural-posture terms belong **with the citation
  teaching**; `### Term` anchors give S7's sweep a clean, stable target and avoid duplication; the
  page already half-covers several (`Id.`, `supra`, pinpoint, reporter, parallel citation,
  published/unpublished). *Adjudication:* **(a)** (R4). Home all ten here as `### Term` anchors,
  plain definitions (no case-tied assertion), **not** glossary-defined; record the S7↔S8
  coordination ("route, don't duplicate"). This was the carry-forward delegated to S8 to decide.

### SI-4-S8 — Treat the tool list as static or dated/re-vettable? → **Dated, with a currency rule and periodic re-vet.**
- *Question:* Tool facts (free tiers, ownership, whether a site is live) change. Freeze a snapshot,
  or build in re-verification?
- *Red-team (freeze):* simpler, but it is precisely how the current page rotted (the "opencase"
  guess; "free Casetext" elsewhere). *Steel-man (dated):* N13 already makes the wiki stamp cases
  "good as of <date>"; the same discipline applied to **tools** prevents silent staleness.
- *Adjudication:* **dated** (R8) — a "verified current as of <date>" stamp, re-vetted at execution
  and S9, lists pointed to the authority where they drift (neutral-cite states, T1). Maps to L2/L6
  and the N13 dated-currency pattern.

### SI-5-S8 — Do the reference pages owe the brief-first doctrine TOC (S1 §3.I)? → **No — but they owe L1/N2/N7/N11/N13.**
- *Question:* S1 §3.I defines a brief-first **doctrine-page** TOC. These are **reference** pages.
- *Adjudication:* the doctrine TOC does **not** bind reference pages (S1 §3.I is explicit it governs
  doctrine pages), but the **cross-cutting rules do** (R10): link-every-case (N7), two-key for any
  asserted holding (L1), 6-tier lexicon (N2), glossary wiring for page-less terms (N11), treatment
  status where good-law is discussed (N13), D11 reference-page guardrails. The pages still **lead
  with the field-decisive question** (N9) even though they are not doctrine briefs.
