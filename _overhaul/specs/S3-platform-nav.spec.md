# SPEC S3 — Platform, Navigation & UX
status: APPROVED
depends-on: [S2]          gates: [S4, S7]
last-updated: 2026-06-30   <!-- 06-27 original; 06-30 cross-spec coherence amendments: TreatmentBadge values aligned to S1 §3.D; deck-id supersession -->

> Governed by `docs/STANDARDS.md` (S1, SR-3 supremacy). S3 settles the **platform decision**
> (keep/tune vs. fork vs. switch), turns S2's **category tree** into the actual left-nav, fixes the
> "cramped" sidebar, specifies the **custom-component set** that makes the case corpus usable, and
> records the **deep-link / pinpoint-highlight mechanism (N7)** that S4 implements. S3 **decides**
> the two items S2 §9 deferred to it: the **folder-move-vs-virtual-grouping** nav mechanism and the
> **slug/alias mechanics** for the Community-Caretaking split. S3 **designs**; it builds nothing now —
> the config/layout/SCSS/component work executes later under `EXECUTE.wrapper.md`. Every content spec
> (S4–S8) stays **platform-portable**: components are progressive enhancement over plain markdown.

---

## 1. Objective

Lock the site on **Quartz (kept and enhanced, not forked)** and define the navigation + UX target the
rest of the overhaul renders against: (a) a **docs-style, category-grouped left nav** built from S2's
12-bucket tree via a **physical folder hierarchy**, with the current section auto-expanded/highlighted
and the sidebar de-cramped; (b) the **custom-component set** (treatment-status badge, sortable/filterable
case-table, glossary-popover styling, case-card, plus the larger bespoke layer — interactive doctrine
flowcharts, a faceted case browser, and cross-reference panels) that makes a 300+-case corpus navigable;
and (c) the **deep-link / pinpoint-highlight mechanism (N7)** — internal heading/block anchors for our
own pages and **URL text fragments** for external CourtListener links — recorded for S4 to implement.

## 2. Scope

### 2.1 In scope (S3 designs)
- The **platform decision** with an honest alternatives scan (§ Appendix A · U1-S3, SI-2-S3).
- The **nav mechanism**: physical category folders under `content/` driving the Explorer + breadcrumbs +
  folder pages (R1), and the exact **Explorer configuration** (order, sort, display) (R2).
- The **"not-cramped" sidebar/spacing target** — width, gap, line-height, active-section styling (R3).
- The **custom-component set** + the **portability guardrail** that keeps content markdown-valid (R4, R5).
- The **legal-term popover mechanism** (wikilink → glossary anchor; confirm `enablePopovers` covers it) (R6).
- The **deep-link / pinpoint-highlight mechanism (N7)** for internal and external links (R7).
- The **responsive behavior** target (TOC, tables, mobile Explorer) (R8).
- **Decision of S2 §9 open items:** folder-move vs. virtual grouping (→ R1); caretaking-split slug/alias
  mechanics (→ R9).

### 2.2 Out of scope (owned elsewhere)
- **Authoring the per-case page skeleton, anchor scheme, and the deck-id-preserving split migration**
  → **S4** (S3 hands it the anchor + alias requirements).
- **Writing/splitting/re-homing page content** and creating the per-category landing `index.md` bodies
  → **S6** (S3 fixes the folder skeleton + which pages land where, per S2 §6.1).
- **Wiring the actual glossary links on live pages** → **S7** (S3 fixes the popover mechanism + styling).
- **Ingesting/verifying the case corpus** → **S5**. **Standards/lexicon/verification machine** → **S1**.
- **Upgrading Quartz 4.5.2 → Quartz 5** — explicitly deferred as a separate, non-blocking task (SI-3-S3).

---

## 3. Requirements (numbered, testable)

### 3.1 — Platform: keep & enhance Quartz (R1a) **[USER]**
The site **stays on Quartz** (currently 4.5.2). No fork, no bake-off, no migration. The alternatives
scan (Starlight / Docusaurus / MkDocs-Material / Obsidian Publish — Appendix A · SI-2-S3) found **none**
clears the bar "Quartz can't present the category tree or the case corpus well": Quartz already delivers
graph + Obsidian-style wikilink **popovers** + full-text search + breadcrumbs + the custom FSRS flashcard
app + free Vercel hosting + portable-markdown content; every alternative loses at least one of those.
- *Check:* `quartz.config.ts` / `package.json` remain the build of record; no second SSG is introduced.

### 3.2 — Nav mechanism: physical category folders (R1) **[decides S2 §9]**
Adopt a **real folder hierarchy** under `content/` (one folder per S2 top-level category; the exceptions
cluster nests one level deeper), **not** a frontmatter-driven virtual Explorer. Files **physically move**
from the current flat `content/` into the §6.1 folders; **file stems are not renamed** (D-3). This is
testable and Quartz-native:
- **Wikilinks keep resolving** because `markdownLinkResolution: "shortest"` is already set and stems stay
  unique — `[[Page]]` resolves by shortest unique path regardless of folder (R4-S2 honored).
- **Breadcrumbs, folder pages, and current-folder auto-open work for free** — the Explorer already opens
  ancestor folders of the active page (`folderIsPrefixOfCurrentSlug`, `explorer.inline.ts:139`), marks the
  active link `.active`, and scrolls it into view. **No inline-script patch is required.**
- *Check:* post-move, the Explorer shows the 12 S2 categories as collapsible folders; breadcrumbs show the
  category path; visiting any page auto-expands + highlights its section; **zero broken wikilinks** (AUTO).

### 3.3 — Explorer configuration (R2)
Configure `Component.Explorer(...)` in `quartz.layout.ts` to render the category tree in **book-spine
order** (S2 §6.1: 1 Foundations → … → 12 Instructor Craft), not alphabetically:
- **Deterministic order via numbered folder slugs** (`1-foundations-history` … `12-instructor-craft-study`;
  the exceptions cluster `7-exceptions-warrant/7a-pc-needed`, `…/7b-pc-not-needed`). The default `sortFn`
  already uses numeric collation (`numeric: true`), so `7` sorts before `12`.
- **Readable display names** — a self-contained `mapFn` (or per-folder titling) renders the §6.1 labels
  ("3 · What Is a Search?") rather than the raw slug. `mapFn`/`sortFn` must be **closure-free** (Quartz
  serializes them with `.toString()` and re-evaluates them client-side).
- **`folderDefaultState: "collapsed"`**, `folderClickBehavior: "link"` (folder click → its landing page),
  `useSavedState: true`.
- *Check:* Explorer lists exactly the 12 categories in spine order; the single 3-level branch is the
  exceptions cluster (R5-S2); folder click lands on the category page; current page's folder is open.

### 3.4 — "Not-cramped" sidebar & spacing target (R3)
The cramping is **two things**: a narrow panel (2 SCSS values) **and** a flat 46-item alphabetical list
(fixed by R1/R2 grouping). The spacing target, each a concrete diff:
- `variables.scss`: `$sidePanelWidth: 320px → 380px` (the file already carries `//380px` as the intended
  value).
- `base.scss` `.sidebar { gap: 1.2rem → 1.6rem }`.
- `explorer.scss`: increase Explorer row line-height/vertical padding and bump `.explorer-content`
  legibility; **also bold/secondary-color the active page's ancestor folder title** (current `.active`
  styles only the leaf link) so the current section reads at a glance.
- *Check:* desktop left panel = 380px; Explorer rows are visibly roomier; the active category title is
  emphasized; mobile layout (hamburger Explorer) is unaffected/regression-free.

### 3.5 — Custom-component set (R4) **[USER — larger bespoke investment]**
Build a layered component set. **Core (surgical):**
1. **Treatment-status badge** — renders the verified good-law **treatment status** as a colored inline
   badge using the **canonical S1 §3.D status set** — `good | criticized | limited | abrogated |
   overruled` (N13; the badge reads the case page's `treatment.status` frontmatter). The orthogonal
   **authority-weight** (the 6-tier lexicon — *Binding — SCOTUS* / *Binding in-circuit* / *Persuasive
   (outside circuit)* / *Persuasive — state, illustrative* / *Persuasive only — non-precedential* /
   *Historical*) is a **separate** label the badge/header may show alongside it — the two axes are kept
   distinct (S1 §3.D), never merged. Used on case pages, doctrine case-tables, and the Case Index.
2. **Case-table** — a **sortable / filterable** rendering of doctrine-page case tables and the Case Index
   (sort by case/court/year/weight; filter by role, treatment status, jurisdiction). Subsumes case-card
   styling.
3. **Glossary popover styling** — typography/sizing tuned for short legal-term definitions on hover (R6).

**Larger bespoke layer (user-elected):**
4. **Interactive doctrine flowcharts** — the field-decision trees (e.g. knock-and-talk line-drawing, the
   PC-needed/PC-not-needed exception fork). Built **on top of the already-supported Mermaid** plus a thin
   interactive wrapper (clickable nodes → deep-link to the governing doctrine/case section), so the source
   stays a portable Mermaid code block (R5).
5. **Faceted case browser** — a corpus-wide browse/filter surface over the **Case Index data** (facet by
   category/home, doctrine role, court level, treatment status, decade), complementing full-text search.
6. **Cross-reference panel** — a per-page panel surfacing a case's **other homes** (multi-homing, N6),
   `related:` doctrines, and "limited by / limits" links (N4), driven by frontmatter + the case record.
- *Check:* each component has a named source-of-truth (markdown table / frontmatter / Case Index data),
  a defined empty/degraded state, and is reused (not one-off). Build cost is logged (Appendix A · U3-S3).

### 3.6 — Portability guardrail: progressive enhancement (R5)
**Every** custom component is **progressive enhancement over portable markdown + frontmatter.** The
underlying content must remain valid, readable markdown if the components are stripped or the site is
ported off Quartz:
- Case-tables enhance a **plain markdown table** (or a frontmatter case list); without JS they render as a
  static table.
- Flowcharts enhance a **Mermaid code block**; without the wrapper they render as a static Mermaid diagram.
- Badges/cross-ref panels read **frontmatter / the Case Index**, not bespoke non-markdown syntax that a
  generic markdown reader can't parse.
- Components consume data via a documented convention (a code-fence directive or frontmatter key), so **S4–S8
  author plain markdown** and never hard-depend on a component to be legible.
- *Check:* disabling components leaves every page readable; no S4–S8 deliverable is expressed in a syntax
  that only a custom Quartz component can render.

### 3.7 — Legal-term popover mechanism (R6, enforces N11; hands S7)
Confirm and fix the glossary hover mechanism: `enablePopovers: true` (already set) gives **hover previews
for internal wikilinks**, and Quartz fetches the target page and **scrolls the preview to the hash**. So a
glossary term is wired as a wikilink to a **heading/block anchor** in `Common Legal Terms.md`
(`[[Common Legal Terms#stare-decisis]]`); hover shows that definition, click navigates to it. Requirements
S3 fixes (S7 wires the links):
- Each glossary entry must be an addressable **`## Term` heading** (or `^block`) so the anchor exists.
- A **glossary-popover style** (R4 #3) constrains popover width/length for short definitions.
- *Check:* a wikilink to a glossary anchor shows the term's definition on hover and lands on it on click;
  popover is sized for a definition, not a full page.

### 3.8 — Deep-link / pinpoint-highlight mechanism (R7, enforces N7; recorded for S4)
Two distinct mechanisms, chosen by link target:
- **Internal (within the site):** use **heading-id anchors** (Quartz auto-slugs every heading) and Obsidian
  **block/heading references** (`[[Case#Held]]`, `[[Case#^pin-cite]]`). The SPA router handles `#anchor`
  scrolling and popovers honor it. **Do not use URL text fragments for internal links** — Quartz's SPA
  (`enableSPA: true`) navigates via `pushState`, which does not reliably trigger `:~:text=` scrolling.
  → **S4 must give each per-case page stable section anchors** (Facts / Issue / Held / Reasoning, plus a
  pinpoint-cite structure) so doctrine pages can deep-link to the exact holding.
- **External (CourtListener):** use a **URL text fragment** on the opinion URL —
  `…/opinion/<id>/<slug>/#:~:text=<url-encoded pinpoint quote>` — which highlights the quoted passage on a
  full page load (case links open in a new tab). Browser support is now universal: Chrome 80+, Edge 83+,
  **Safari 16.1+, Firefox 131+**. **Fallback:** the plain opinion URL when a quote is long/ambiguous/
  duplicated. **Do not depend on CourtListener's own star-pagination anchors** — Free Law Project lists
  better star pagination as *planned/incomplete*, so it is not a reliable anchor source today.
- *Check:* an internal pinpoint wikilink scrolls to the right section under SPA nav; an external CL link
  with a text fragment highlights the quoted passage in a fresh tab; both have a defined fallback.

### 3.9 — Caretaking-split slug & alias mechanics (R9) **[decides S2 §9]**
The S2 split `Community Caretaking and Emergency Aid` → **`Emergency Aid`** + **`Community Caretaking`**
executes as **two new clean files** (kebab-case slugs), the **old combined file retired**, with:
- `aliases: ["Community Caretaking and Emergency Aid"]` placed on the new **`Community Caretaking`** page
  (it inherits the bulk/most-linked identity). Quartz's `AliasRedirects` emitter (already enabled) then
  **redirects the old URL** and resolves `[[Community Caretaking and Emergency Aid]]` wikilinks to it.
- **Emergency-aid-specific inbound links** (home-entry / Brigham City / Caniglia-on-the-home context) are
  **re-pointed to `[[Emergency Aid]]` during S6** (content-aware, not a blind redirect).
- **Decks:** ~~deck-id preservation is S4's mechanism (cards keep ids; deck `page`/`tags` realigned
  losslessly, D-6)~~ — **[SUPERSEDED by S4·R11 / U5-S9:** there is **no deck-id preservation** and **no
  deck work in the overhaul**; the dangling `page:` resolves via the alias below until the **separate
  later** page-derived rebuild.**]** S3 guarantees only the **alias + zero-broken-link** half (R4-S2).
- *Check:* old slug 301/alias-redirects to Community Caretaking; both new pages exist with their own slugs;
  no broken inbound link; emergency-aid links resolve to Emergency Aid after S6.

### 3.10 — Responsive behavior (R8)
- Keep **TableOfContents desktop-only** (`<1200px` hidden) — it is secondary to the brief-first read; the
  page's own headings carry structure on tablet/mobile.
- Ensure the **case-table component degrades to a horizontally scrollable table** on mobile (the existing
  `.table-container { overflow-x: auto }` covers the markdown fallback; the component must not regress it).
- The **mobile Explorer (hamburger)** reflects the same category grouping as desktop.
- *Check:* at <800px the case-tables scroll without breaking layout; the mobile Explorer shows categories;
  TOC hidden as today (no regression).

---

## 4. Lessons enforced

- **N7** (link every case; deep-link pinpoints) → R7 (internal anchors + external text fragments) + the S4
  anchor requirement. **N11** (wire the glossary; hover-preview + click-through) → R6. **N13/N4**
  (explicit, consistent treatment + subsequent-treatment) → R4 #1 treatment badge + #6 cross-ref panel.
  **N6** (non-exclusive multi-homing) → R4 #6 cross-reference panel surfacing other homes. **N9**
  (field-decisive framing) → R4 #4 interactive decision flowcharts.
- **D-3 / D-6** (slug + deck-id stability) → R1 (stems frozen on folder move) + R9 (alias-preserving split).
- **R4-S2** (folders-for-nav + tags-for-cross-cutting; zero broken links) → R1 + R2 + R9; multi-homing
  stays in `tags`/`related:` + component cross-refs, never duplicate folders.
- **SR-3** (`docs/STANDARDS.md` supremacy) → every execution step cites S1; the treatment badge keys to the
  S1/§4 authority-weight lexicon.

## 5. Method (the decided platform + ordered UX/nav changes)

**Platform = Quartz 4.5.2, kept and enhanced.** Execution (later, under `EXECUTE.wrapper.md`) proceeds in
this order so nav is correct before content moves and components land before pages depend on them:

1. **Folders first (R1/R2).** Create the §6.1 numbered category folders (incl. the `7a/7b` nesting);
   `git mv` every content file into its primary home **without renaming stems**; add `aliases:` to any page
   whose URL path changes so old paths redirect (R4-S2). Configure the Explorer (`order`, numeric `sortFn`,
   closure-free `mapFn` for display names, `folderDefaultState: collapsed`, `folderClickBehavior: link`).
   Verify zero broken wikilinks and that breadcrumbs + current-folder auto-open work.
2. **Sidebar de-cramp (R3).** Apply the SCSS diffs: `$sidePanelWidth 380px`; `.sidebar` gap `1.6rem`;
   Explorer row spacing; active-ancestor-folder emphasis.
3. **Caretaking split plumbing (R9).** When S6 performs the content split, S4's deck-stable migration runs;
   S3's contribution is the two clean slugs + the `aliases:` on Community Caretaking + S6 re-pointing the
   emergency-aid links.
4. **Component layer (R4/R5).** Build core components (treatment badge → case-table → glossary popover
   styling), then the bespoke layer (Mermaid-based interactive flowcharts → faceted case browser over the
   Case Index → cross-reference panel). Each ships with its degraded/empty state and a documented
   markdown/frontmatter data convention (R5). Register components in `quartz.layout.ts` and/or as a
   transformer that upgrades the agreed code-fence/frontmatter convention.
5. **Glossary popovers (R6).** Confirm `enablePopovers` + anchored glossary headings; ship the popover
   style. (Actual link-wiring is S7.)
6. **Deep-link anchors (R7).** S4 builds the per-case anchor scheme; doctrine pages (S6) emit internal
   `[[Case#Held]]` pinpoints and external CL `#:~:text=` links per R7.
7. **Responsive pass (R8).** Verify TOC/table/mobile-Explorer behavior; no regressions.

## 6. Deliverables (files the execution will create or change)

**Config / layout / styles**
- `quartz.layout.ts` — Explorer options (order/sortFn/mapFn/title, collapsed default, link behavior);
  register the new components.
- `quartz.config.ts` — no platform change; confirm `markdownLinkResolution: "shortest"`, `enablePopovers`,
  `AliasRedirects` stay on; adjust `ignorePatterns` only if a build helper requires it.
- `quartz/styles/variables.scss` — `$sidePanelWidth: 380px`.
- `quartz/styles/base.scss` — `.sidebar` gap; minor table tweaks for the case-table fallback.
- `quartz/components/styles/explorer.scss` — row spacing/line-height; active-ancestor-folder emphasis.
- `quartz/components/styles/popover.scss` — glossary-definition popover sizing/typography.

**New components (under `quartz/components/`, each with its `.scss` and any `.inline.ts`)**
- `TreatmentBadge.tsx` · `CaseTable.tsx` (+ `scripts/casetable.inline.ts`) · `DoctrineFlowchart.tsx`
  (Mermaid wrapper + `scripts/flowchart.inline.ts`) · `CaseBrowser.tsx` (+ `scripts/casebrowser.inline.ts`)
  · `CrossRefPanel.tsx`. Optionally one **transformer plugin** that upgrades the agreed
  code-fence/frontmatter convention into these components (keeps content portable, R5).

**Content-structure changes (skeleton only here; bodies = S6)**
- New `content/<n>-…/` category folders (12 + the `7a/7b` nesting); every page `git mv`'d into its home.
- Per-top-level-folder `index.md` **stubs** (category landing pages; bodies authored in S6).
- New `content/.../Emergency Aid.md` + `content/.../Community Caretaking.md`; old combined file retired
  with the alias on Community Caretaking (R9). `aliases:` added to any moved page whose URL path changed.

## 7. Acceptance criteria (definition of done)

- [ ] **Platform recorded as Quartz, kept & enhanced** (R1a); the alternatives scan is documented with the
      reason each was rejected (Appendix A · SI-2-S3); no second SSG introduced.
- [ ] **Folder mechanism decided = physical move** (R1), with the file-stems-frozen + shortest-link-
      resolution justification; S2 §9 open item #2 is closed.
- [ ] **Explorer config** (R2) renders the 12 S2 categories in **book-spine order**, collapsible, with the
      current section auto-expanded/highlighted and exactly one 3-level branch (exceptions).
- [ ] **Sidebar de-cramp** (R3) names the exact SCSS diffs (380px width, 1.6rem gap, row spacing, active-
      ancestor emphasis).
- [ ] **Component set** (R4) is enumerated — core (badge, sortable/filterable case-table, glossary popover
      styling) **plus** the user-elected bespoke layer (interactive Mermaid flowcharts, faceted case
      browser, cross-reference panel) — each with a data source and degraded state.
- [ ] **Portability guardrail** (R5) is stated: components are progressive enhancement; S4–S8 stay
      markdown-valid.
- [ ] **Glossary popover mechanism** (R6) confirmed (wikilink → glossary anchor under `enablePopovers`).
- [ ] **Deep-link mechanism** (R7) recorded for S4: internal heading/block anchors (not text fragments
      under SPA) + external CL **URL text fragments** with a plain-URL fallback; the S4 anchor requirement
      is stated.
- [ ] **Caretaking-split slug/alias mechanics** decided (R9): two new slugs + alias on Community Caretaking
      + S6 re-point of emergency-aid links; S2 §9 open item #1 is closed.
- [ ] **Responsive target** (R8) fixed (TOC desktop-only; tables scroll; mobile Explorer grouped).

## 8. Verification plan (how S3's output gets checked — free, no-CL)

1. **Link integrity (AUTO):** after the folder move, build and assert **zero broken wikilinks/internal
    links**; assert old paths redirect via `AliasRedirects` (the caretaking old slug + any path-changed page).
2. **Nav render:** build and confirm the Explorer shows the 12 categories in spine order, collapsible, with
   the active page's folder open + leaf highlighted; breadcrumbs show the category path; depth ≤2 except the
   exceptions cluster (≤3) — i.e. S2 R5 holds in the rendered tree.
3. **Spacing:** computed `$sidePanelWidth` = 380px; sidebar gap = 1.6rem; Explorer rows visibly roomier;
   active ancestor folder emphasized. Visual check at desktop/tablet/mobile.
4. **Component contracts:** each component renders from its named data source **and** degrades correctly
   when disabled (R5) — case-table → static table; flowchart → static Mermaid; badge/cross-ref read
   frontmatter/Case Index.
5. **Popover:** a wikilink to a glossary anchor previews the definition on hover and lands on it on click.
6. **Deep-links:** an internal `[[Case#Held]]` scrolls correctly under SPA nav; an external CL
   `#:~:text=` link highlights the passage on a fresh tab; both fall back cleanly.
7. **Portability spot-check:** open three S4/S6-style sample pages with components disabled — all remain
   legible markdown (no component-only syntax).
8. **Non-regression vs build:** Vercel build still succeeds; graph, search, backlinks, flashcard app,
   `CustomOgImages` unaffected.

## 9. Open items / escalations

- **Quartz 4.5.2 → Quartz 5 upgrade** — deferred as a **separate, non-blocking** task (SI-3-S3). The repo
  vendors `quartz/` source with minor SCSS edits, so a major upgrade carries merge cost; do not entangle a
  framework bump with the content overhaul. Re-evaluate after S9.
- **Component data convention (code-fence directive vs. frontmatter key)** — the exact authoring syntax the
  case-table / flowchart / cross-ref components consume is finalized in **S4** (it co-designs the per-case
  data model); S3 fixes only the **portability constraint** (R5).
- **`The Warrant Requirement` possible split** (S2 §6.2 WATCH) — if S6 splits knock-&-announce out, that is
  the one permitted extra 3rd-level move under R5-S2; the folder mechanism (R1) already supports it.
- **Faceted case browser data source** — depends on the final **Case Index** machine-readable shape (S4/S5);
  S3 fixes the component + its facets, not the index schema.

---

## Appendix A — Decision log

*Format: Question · Options · Red-team · Steel-man · Adjudication. **[USER]** = the user's actual choice;
the rest are self-interviewed.*

### [USER] U1-S3 — Platform direction → **Keep & enhance Quartz.**
- *Options:* (a) keep & enhance Quartz; (b) formal bake-off vs. one alternative (Starlight); (c) switch now.
- *Red-team (a):* a flat 46-page Explorer and a 320px sidebar genuinely read as "cramped," and the case
  corpus is static tables — "keep" only wins **if** we actually invest the nav + component work. *Steel-man
  (b/c):* a docs-first SSG (Starlight/MkDocs-Material) ships a category sidebar out of the box.
- *Adjudication:* **(a).** The bar to leave is "Quartz can't present the category tree or the case corpus
  well" — and it can: the tree is a folder Explorer (R1/R2) and the corpus is Case Index + per-case pages +
  search + graph + the R4 components. Switching would **lose** the graph, Obsidian-style wikilink popovers,
  and the bespoke FSRS flashcard app, none of which the alternatives replace together. User confirmed (a).

### [USER] U2-S3 — Navigation model → **Docs-style, category-grouped left nav.**
- *Options:* (a) docs-style category nav (collapsible, current-section auto-expanded/highlighted, roomier);
  (b) category nav but all sections collapsed on load; (c) keep the flat alphabetical tree, only fix spacing.
- *Red-team (c):* spacing alone leaves 46 undifferentiated rows — the real cramping is the *flatness*.
  *Steel-man (a):* mirrors the book's teaching order (S2 spine) and is what stock Quartz auto-expand already
  supports.
- *Adjudication:* **(a)** (R1–R3). User confirmed. Stock Explorer already auto-opens + highlights the
  current section once folders exist (`explorer.inline.ts:139`), so the "auto-expanded" half needs **no
  patch** — only the folder structure + spacing diffs.

### [USER] U3-S3 — Custom components, how far → **Larger bespoke investment.**
- *Options:* (a) small surgical set; (b) badge only; (c) markdown-only; (d) larger bespoke investment.
- *Red-team (d):* more components = more build + maintenance surface, and risk of locking content into
  component-only syntax. *Steel-man (d):* a 300+-case teaching corpus genuinely benefits from interactive
  decision flowcharts (N9 field-framing), a faceted case browser (corpus scale), and cross-reference panels
  (N6 multi-homing) — these are teaching objects, not chrome.
- *Adjudication:* **(d)** — build the core set (badge, sortable/filterable case-table, glossary popover
  styling) **and** the bespoke layer (Mermaid-based interactive flowcharts, faceted case browser,
  cross-ref panel). The maintenance risk is contained by the **R5 portability guardrail**: every component
  is progressive enhancement over portable markdown/frontmatter, so content survives them. Cost logged:
  core ≈ 2–3 days; bespoke layer ≈ adds 3–5 days; gated on the S4 data convention.

### SI-1-S3 — Folder move vs. virtual Explorer grouping (S2 §9 open item) → **Physical folder move.**
- *Options:* (a) physically `git mv` files into numbered category folders; (b) keep files flat, drive the
  tree from frontmatter via a custom Explorer data layer (virtual grouping).
- *Red-team (a):* moving files churns git history and requires aliases so old URL paths don't 404. *Red-team
  (b):* a virtual tree needs a custom `mapFn`/data pipeline (serialized, closure-free, re-evaluated client-
  side) and **breaks breadcrumb + folder-page semantics**, which are path-based — more code, less Quartz-
  native behavior for free.
- *Steel-man (a):* with `markdownLinkResolution: "shortest"` already set and stems frozen, `[[wikilinks]]`
  keep resolving after a move; breadcrumbs, folder pages, and current-folder auto-open all come for free; the
  only cost is one-time `git mv` + `aliases:`.
- *Adjudication:* **(a)** (R1). The alias requirement (R9 / R4-S2) absorbs the only real downside; the
  Quartz-native wins (breadcrumbs/folder pages/auto-open with zero custom JS) decide it.

### SI-2-S3 — Alternatives scan (honest) → **None beats tuned Quartz for this project.**
- **Astro Starlight** — zero-JS, fast, excellent built-in category sidebar; **but no graph view, no
  Obsidian-style wikilink hover popovers, no FSRS flashcard app**, and migrating orphans the existing build.
  *Better category nav, worse everything-else this site relies on.*
- **Docusaurus** — mature, React/MDX, strong docs nav; **no graph, no wikilink popovers natively**, heavier
  JS, and an MDX rewrite of markdown content. *No corpus/graph advantage to justify the rewrite.*
- **MkDocs-Material** — superb nav + search, Python toolchain; **no graph, no wikilink popovers, no Obsidian
  round-trip** with the vault (the source of truth). *Breaks the Obsidian ⇄ site workflow.*
- **Obsidian Publish** — closest match (native wikilinks, graph, popovers); **but a paid subscription, far
  less control over custom components, can't host the custom FSRS flashcard app, and is vendor lock-in.**
  *Loses the bespoke components (U3) and the free, fully-controlled Vercel build.*
- *Adjudication:* keep **Quartz** (R1a). It is the only option that holds graph **and** wikilink popovers
  **and** portable-markdown content **and** the custom flashcard app **and** free hosting **and** full
  component control simultaneously. (Facts current as of 2026-06; text-fragment + version notes below.)

### SI-3-S3 — Quartz 4.5.2 vs. upgrade to Quartz 5 → **Stay on 4.5.2 for the overhaul; treat 5 as a separate task.**
- *Finding:* Quartz **v5.0.0** now exists and retains graph, popovers, search, backlinks, and the Explorer.
- *Red-team (upgrade now):* the repo vendors `quartz/` source with local SCSS edits (and will add bespoke
  components), so a major bump means a non-trivial merge **entangled with** a content overhaul — two big
  changes at once, harder to bisect failures.
- *Steel-man (upgrade now):* doing it before the component work avoids porting new components twice.
- *Adjudication:* **stay on 4.5.2** through the overhaul; schedule the 5 upgrade as a **separate, non-
  blocking** task after S9 (Open items). The component API surface we touch is stable across the bump.

### SI-4-S3 — Deep-link / pinpoint-highlight mechanism (N7) → **Internal anchors + external text fragments.**
- *Question:* how does "click a case reference → land on the highlighted passage" work, internally and on
  CourtListener?
- *Findings:* **URL text fragments** (`#:~:text=`) are now broadly supported (Chrome 80+, Edge 83+, Safari
  16.1+, Firefox 131+) and need no author anchors — but Quartz runs **SPA navigation** (`pushState`), which
  doesn't reliably fire text-fragment scrolling on **internal** links. CourtListener opinions are selectable
  HTML, but CL's own **star-pagination anchors are incomplete/"planned"**, so they're not a dependable
  anchor source.
- *Adjudication (R7):* **internal** pinpoints use Quartz **heading-id + Obsidian block/heading anchors**
  (SPA-safe, popover-aware); **external** CL pinpoints use **URL text fragments** on the opinion URL (new-
  tab = full load = fragment works), with the **plain opinion URL as fallback**. **S4** must give per-case
  pages stable section anchors so doctrine pages can deep-link the exact holding.

### SI-5-S3 — Caretaking-split slug/alias mechanics (S2 §9 open item) → **Two new slugs + alias on Community Caretaking.**
- *Options:* (a) keep the old slug as the Community-Caretaking continuation + a new Emergency-Aid slug; (b)
  two brand-new clean slugs, old combined slug retired with a redirect/alias.
- *Red-team (a):* reusing the old combined slug for one of the two pages is semantically muddy (the old slug
  *means* "both") and complicates the deck `page` realignment. *Steel-man (b):* two clean kebab-case slugs
  are unambiguous; Quartz `AliasRedirects` (already enabled) makes the old slug redirect and resolves
  `[[old title]]` wikilinks if the alias sits on the inheriting page.
- *Adjudication:* **(b)** (R9). Put `aliases: ["Community Caretaking and Emergency Aid"]` on **Community
  Caretaking** (it inherits most inbound links); re-point **emergency-aid-specific** links to **Emergency
  Aid** during S6 (content-aware). Deck-id preservation is S4's mechanism; S3 guarantees the alias + zero-
  broken-link half.
