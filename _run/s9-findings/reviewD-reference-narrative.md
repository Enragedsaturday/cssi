# S9 Review D — Reference + Narrative Cluster

**Reviewer role:** S9 reference/narrative reviewer (D11 accuracy + D6 guardrails + D13 links).
**NOT** the full doctrine SR-2 gate — these are reference/mechanics pages.
**Mode:** FREE (no CourtListener) · FINDINGS ONLY (L5, no page edits).
**Branch:** `overhaul/build` · **Date:** 2026-06-30

Cases were **not** live-verified on CourtListener (FREE mode). D11 accuracy is judged against
internal consistency, established legal fact, anchor/link resolution, and the specific
correction claims the task enumerated.

---

## Per-page verdict (D11 / D6 / D13)

| Page | D11 | D6 | D13 | Findings |
|---|---|---|---|---|
| 1-foundations-history/Common Law Origins | PASS | PASS | **FAIL** | 1 (D13) |
| 2-legal-system-research/The Federal Court System | PASS | PASS | PASS | 0 |
| 2-legal-system-research/Reading and Citing Cases | PASS | PASS | PASS | 0 |
| 2-legal-system-research/Legal Research Tools | PASS | PASS | PASS | 0 |
| 2-legal-system-research/Verifying Good Law | PASS | PASS | PASS | 0 |
| 2-legal-system-research/Common Legal Terms (glossary) | PASS | PASS | PASS | 0 |
| 3-what-is-a-search/Fourth Amendment Framework | PASS | PASS | PASS | 0 (1 trivial) |
| 3-what-is-a-search/Fourth Amendment Analysis Checklist | PASS | PASS | PASS | 0 |
| 3-what-is-a-search/Fourth Amendment Recalibration | PASS | PASS | PASS | 0 (1 trivial) |
| 3-what-is-a-search/CREW | PASS | PASS | PASS | 0 |
| 12-instructor-craft-study/Three Golden Rules | PASS | PASS | PASS | 1 (needs_cl, low) |
| 12-instructor-craft-study/Instructor Development | PASS | PASS | PASS | 0 |
| index.md (home MOC) | PASS | PASS | PASS | 0 (1 informational) |

**Net:** 12/13 pages fully PASS. One D13 FAIL (Common Law Origins). No D11 rot, no D6
guardrail breach anywhere in the cluster.

---

## Findings

### F1 — Common Law Origins · D13 · MEDIUM (the only page-level FAIL)
**Problem:** The four cases the page rests on are **not wikilinked even though pages exist** in
`content/cases/`:
- `*Boyd v. United States*, 116 U.S. 616 (1886)` — page `cases/Boyd v. United States.md` exists; the page itself labels Boyd "binding U.S. authority." Named in the Rule, the Key-cases table, and Sources — all plain italic, no `[[ ]]`.
- `*Riley v. California*, 573 U.S. 373 (2014)` — page `cases/Riley v. California.md` exists; same treatment (plain italic throughout).
- `*Entick v. Carrington*` — page `cases/Entick v. Carrington.md` exists (type: case, authority_weight: Historical).
- `*Wilkes v. Wood*` — page `cases/Wilkes v. Wood.md` exists (type: case, authority_weight: Historical).

This is inconsistent with every sister page in the cluster (Framework, Recalibration, Three
Golden Rules) which wikilink their SCOTUS cases. Not a broken link (info still reachable via
Case Index), but a genuine D13 gap: named cases with existing pages should be wikilinked.
**Fix:** Wikilink `[[Boyd v. United States]]` and `[[Riley v. California]]` at first mention
(Rule + Key-cases table), and `[[Entick v. Carrington]]` / `[[Wilkes v. Wood]]` where they are
named. (Paxton's Case has no page — correctly left plain.) The page's "not in CourtListener /
non-binding" framing for the English/colonial cases is still fine as prose; it does not require
suppressing the internal wikilink to the wiki's own case page.

### F2 — Three Golden Rules · needs_cl · LOW (informational for CL-gated reviewers)
**Problem:** This instructor-craft page carries **asserted holdings** with pin cites and quotes
(*Graham* 490 U.S. at 396; *Buie* 494 U.S. at 334, 336; *Gaetjens* 4 F.4th at 493–94; *Terry*,
*Brinegar*, *Gates*). The task notes reference pages should carry ~0 asserted holdings ("they
teach mechanics"). This page is a hybrid — heuristics grounded in case law — so the holdings are
expected here, and each is properly weighted (SCOTUS binding; *Gaetjens* correctly flagged
"Binding in-circuit — 7th Cir."; state applications flagged "Persuasive — state, illustrative").
**Flag:** `needs_cl` for the CL-gated pass to confirm the six pins/quotes verbatim; nothing
appears wrong on its face. Not a D11/D6/D13 failure.

### F3 (trivial) — Riley CourtListener slug inconsistency · informational
`Common Law Origins` links Riley as `.../opinion/2680439/riley-v-california/`, while `Fourth
Amendment Framework` and `Fourth Amendment Recalibration` use
`.../opinion/2680439/riley-v-cal-united-states/`. **Same opinion ID (2680439)** — CourtListener
routes on the numeric ID and ignores the slug, so all resolve. Cosmetic only; not verified live
(FREE mode). No action required beyond optional slug normalization.

### F4 (informational) — index.md MOC · [[Community Caretaking and Emergency Aid]]
The MOC (§7) links `[[Community Caretaking and Emergency Aid]]`. There is **no** page with that
title; it resolves via an **alias** defined in `7-exceptions-warrant/7a-pc-needed/Community
Caretaking.md`. Link works. Slightly indirect (title is "Community Caretaking"); left as-is.

---

## Confirmations requested by the task

- **CREW mnemonic fix (C·RE·W):** CONFIRMED. `CREW.md` lists **C — Consent**, **RE — Recognized
  Exception**, **W — Warrant** (lines 16–18). `index.md` states it twice as "C·RE·W" /
  "Consent · Recognized Exception · Warrant." Verbatim and consistent. Sources note: "C.R.E.W. is
  an instructor mnemonic, not a case" → **uncited**, as required.
- **Tool-table corrections (Legal Research Tools):** CONFIRMED.
  - **OpenCase ≠ OpenJurist:** distinct rows — **OpenJurist** in the free-backbone table (free
    public-domain federal case law); **OpenCase** in the separate low-cost/paid table (AI Q&A).
    The `[!note]` block and the "On OpenCase" paragraph both state they are different tools.
  - **Casetext retired / not-listed:** CONFIRMED — Casetext appears in **neither** table; the note
    says it is retired into TR's paid *CoCounsel* and "not listed"; Sources carry the acquisition
    citation. (Ravel Law likewise dropped, per the note.)
  - **Currency stamp:** CONFIRMED — `> [!note] Verified current as of 2026-06-30`.
  - **OpenCase downplayed + verify-against-primary caution:** CONFIRMED — "downplayed on purpose,"
    "Discovery only — verify every case, holding, and quote against the primary opinion on
    CourtListener before relying on it," with the ~1-in-5 hallucination framing.
- **Glossary anchors (Common Legal Terms):** CONFIRMED — every entry is a `### Term` anchor across
  the four sections; definitions are accurate, in-voice, and citation-free (as the intro states);
  no case-tied holding is restated as a definition. The cross-referenced anchors used by other
  pages all resolve: `#totality-of-the-circumstances`, `#stare-decisis`, `#dissenting-opinion`,
  `#concurring-opinion`. The 5 additions (incl. Totality of the circumstances, De novo, Clear
  error, Per se, Respondeat superior) are sound; Respondeat superior correctly cross-links its
  Monell limit rather than overstating.
- **No apocryphal Holiday/McCall trio:** CONFIRMED — repo-wide grep for "holiday/mccall" returns
  only calendar "weekends and holidays" in *County of Riverside v. McLaughlin* (a real
  Gerstein-timing case). No fabricated Holiday/McCall case trio anywhere.
- **No inline `## Flashcards` heading:** CONFIRMED — none of the 13 cluster pages contains a
  `## Flashcards` heading. `index.md` has a `## Study` section that *links* `[[flashcards|
  Flashcards]]` (a link, not an inline flashcards block) — compliant.

---

## D11 accuracy — additional spot-checks (all PASS)

- **Reading and Citing Cases:** the **10 `### Term` anchors** are present, defined, and not
  case-tied — Supra · Id. · Pinpoint cite · Reporter · Parallel citation · En banc · Certiorari ·
  Slip opinion · On remand · Vacated. Federal↔state conventions accurate: prosecuting-party names
  (US / State / People / Commonwealth) with correct Bluebook short-form rule; 7 West regional
  reporters correct (incl. the "Oklahoma is Pacific, not South Western" caution); neutral-cite
  format `1997 ND 15, ¶ 21` / `2021 WI 5, ¶ 7` correct; FRAP 32.1 (cite unpublished ≥ Jan 1, 2007)
  correct; state parallel `586 Pa. 671, 896 A.2d 1170` correct.
- **Verifying Good Law:** by-hand citator workflow complete (Cited By/Authorities + How-cited →
  scan treatment → read the opinion not the headnote → confirm court/publication/currency → save
  the cite+link+pin unit). **Six-tier lexicon** intact: Binding–SCOTUS · Binding in-circuit ·
  Persuasive (outside circuit) · Persuasive–state, illustrative · Persuasive only–non-precedential
  · Historical.
- **The Federal Court System:** three-tier hierarchy + 13 courts of appeals (12 regional = 11
  numbered + D.C.; 1 Federal/subject-matter) correct; vertical vs. horizontal stare decisis
  correct; SCOTUS = 9, fixed since 1869, ranged 6–10, Congress sets the number, Constitution names
  only the Chief Justice (Art. I impeachment-presiding), Roberts = 17th CJ, cert ~1% / rule of four
  — all accurate; *Marbury* 5 U.S. (1 Cranch) 137 (1803) wikilinked + CL-linked.
- **Fourth Amendment Recalibration:** timeline accurate (Milam 1924 → Carroll 1925 → Lee 1927 →
  Olmstead 1928 → Wolf 1949 → Mapp 1961 → Katz 1967 → Kyllo 2001 → Riley 2014 → Carpenter 2018);
  incorporation two-step (1949 right / 1961 remedy) correct; *Olmstead* overruled by *Katz*
  correct; expand/contract/incorporation direction labels correct. Milam (4th Cir.) and Lee
  correctly left as plain text + CL link (no wiki page exists — no D13 miss).
- **Fourth Amendment Framework:** two-clause structure, C.R.E.W. reasonableness, state-action /
  private-search sub-rules (Jacobsen/Walter/Skinner/Coolidge/Hicks) accurate; "Recent
  developments" (Chatrie/Smith/Moore-Bush/Wilson/Reddick/Miller) current with circuit weights and
  split flags. These recent circuit cases are correctly **plain text + CL link** (no wiki pages;
  and note `[[United States v. Miller]]` would mis-resolve to the 1976 SCOTUS bank-records case,
  so a wikilink was rightly avoided). No D13 miss.
- **Fourth Amendment Analysis Checklist:** 5-step order correct; the *Rakas* standing note
  (standing folded into the merits, 439 U.S. at 138–40) accurate; C.R.E.W. + "Strive for Five"
  consistent with CREW and Three Golden Rules.

---

## D13 — anchor/link resolution (all resolve unless noted)

All internal wikilinks used by cluster-D pages resolve to existing files, including:
`[[Terry v. Ohio]]`, `[[Marbury v. Madison]]`, `[[Rakas v. Illinois]]`, `[[Arizona v. Gant]]`,
`[[New York v. Belton]]`, `[[Consent Searches]]`, `[[Case Index]]`, `[[Two Definitions of
Search]]`, all §1–§12 doctrine pages linked from the MOC, and the cross-page **anchors**
(`Common Legal Terms#…`, `Reading and Citing Cases#vacated`, `#published-unpublished-and-per-
curiam`). The MOC mirrors the twelve-category S2 tree (dirs `1-…` through `12-…`) exactly.
**Only exception:** F1 (Common Law Origins does not wikilink Boyd/Riley/Entick/Wilkes despite
existing pages).

---

## needs_cl summary
- **Three Golden Rules** — asserted holdings present (Graham/Buie/Gaetjens quotes + pins); flag for
  CL-gated verbatim confirmation. Low priority; all weight labels correct.
- **Common Law Origins** — asserts Boyd/Riley founding-history holdings; grounded + CL-linked;
  history page, low priority.
- All other reference pages (Federal Court System, Reading & Citing, Legal Research Tools,
  Verifying Good Law, Common Legal Terms, Checklist, CREW, Instructor Development, MOC): **0
  asserted holdings** — they teach mechanics, as expected.
