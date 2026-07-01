# S9 — D5 / R8: Cross-Page Coherence Audit

**Scope:** Shared / multi-homed cases audited for consistency across doctrine pages.
**Check:** (1) treatment status identical across every home vs. the canonical case-page `treatment.status`; (2) N4 "limited by [[case]]" tag consistent everywhere the limitation is asserted; (3) overruled cases shown Historical everywhere; (4) no cross-page contradiction on a shared holding. Page-specific N6 framing differences are expected and not flagged.
**Constraint:** Findings only — no content changed.

---

## Summary

| Metric | Count |
|---|---|
| Total case pages | 456 |
| Multi-homed by declared `homes[]` (≥2 homes) | 100 |
| Multi-homed by substantive-page appearances (tables + homes, excl. Case Index / chapter-index / reference pages) | 200 |
| Doctrine-page table rows referencing a case (all pages) | 1,105 |
| Non-good canonical cases (limited/overruled/abrogated) | 18 — **all 18 traced across every page they appear on** |
| Non-good cases that are multi-homed | 12 |
| **Treatment-status mismatches found** | **1** (hard) |
| **Canonical-note / N4-tag gaps found** | **2** (1 medium, 1 minor) |
| Cross-page holding contradictions found | 0 |
| Overruled cases NOT shown Historical somewhere | 0 |

**Bottom line:** Cross-page coherence is strong. Of 200 substantively multi-homed cases, 199 show a treatment status consistent with their canonical case page; 17 of 18 non-good cases carry consistent status + N4 tag on every home. **One hard treatment-status mismatch** (Elstad on Due-Process Voluntariness), plus **one canonical-note gap** (Santana) and **one minor N4-tag wording inconsistency** (Coolidge). All 5 overruled cases (Gouled, Jones-1960, Michigan v. Jackson, Olmstead, Wolf) and both abrogated cases (Aguilar, Spinelli) are shown Historical/overruled/abrogated everywhere. No two doctrine pages contradict each other on a shared holding.

---

## Findings

### F1 — HARD — *Oregon v. Elstad*: treatment-status mismatch + missing N4 tag
- **Case:** *Oregon v. Elstad* — canonical `treatment.status: **limited**` (note: "limited as applied to deliberate question-first two-step interrogations by *Missouri v. Seibert* (2004)").
- **Pages it appears on:** Case Index (limited); Miranda Waiver and Invocation (home); Miranda and Custodial Interrogation; **Due-Process Voluntariness of Confessions**.
- **Divergence:**
  - `Miranda Waiver and Invocation.md:83` — shows **"limited — *limited by* [[Missouri v. Seibert]]"** ✓ (correct; N4 tag present).
  - `Miranda and Custodial Interrogation.md:40` — prose carries **"*Elstad* *limited by* [[Missouri v. Seibert]]"** ✓.
  - **`Due-Process Voluntariness of Confessions.md:74`** — Related-cases table Treatment column shows **"good · 2026-06-30"** and **omits the "limited by [[Missouri v. Seibert]]" N4 tag.** This is the lone outlier; it contradicts the canonical status (`limited`) and its sibling homes.
  - This table *does* track treatment per-row (col header "Treatment"; other rows show good/limited correctly), so it is a genuine per-row error, not a weight-only table. (Note: the page marks *every* related row "good," suggesting the author read the column as "core still good law" — but canonical + all other homes say limited.)
- **Canonical value:** limited.
- **Fix:** In `Due-Process Voluntariness of Confessions.md:74`, change Elstad's Treatment cell from `good · 2026-06-30` to `limited · 2026-06-30` and add the N4 tag `— limited by [[Missouri v. Seibert]]` (matching Miranda Waiver and Invocation). If the author wants to preserve the N6 point that Elstad's *due-process voluntariness* facet is unlimited, phrase it "good on the voluntariness point; Miranda-fruits reading **limited by [[Missouri v. Seibert]]**" — but the status token must not read bare "good."

### F2 — MEDIUM — *United States v. Santana*: canonical `treatment.note` empty while all homes assert "limited by [[Lange v. California]]"
- **Case:** *United States v. Santana* — canonical `treatment.status: **good**`, **`note: ""` (empty)**.
- **Pages it appears on:** Arrest in the Home (home, Key — Anchor); Exigent Circumstances and Hot Pursuit (home, Key — Anchor); **Curtilage** (Related — not in `homes[]`).
- **Divergence:**
  - All three doctrine pages consistently carry **"good; limited by *[[Lange v. California]]*** (misdemeanor pursuit no longer categorical)"** — `Arrest in the Home.md:26,53`; `Exigent Circumstances and Hot Pursuit.md:22,43`; `Curtilage.md:72`. The doctrine side is internally consistent (all "good" + same N4 tag). ✓
  - **The canonical case page records none of this** — `treatment.note` is empty, so the Lange partial-limitation that all three homes assert is undocumented on the source of truth.
  - **Convention deviation:** the parallel partially-limited anchor *Michigan v. Summers* is coded `status: good` **with** `note: "Spatial limit set by Bailey v. United States…"`, and its home (Securing the Scene) mirrors that note. Santana should follow the same pattern; instead its note is blank. (Contrast also *New York v. Belton*, an analogous "survives in part / limited in part" anchor, which is coded `status: limited` + note.)
  - Minor sub-point: Santana's `homes[]` lists only Arrest in the Home + Exigent, but it is also cross-cited in a Curtilage table (correctly framed) — a `homes[]` completeness gap, not a treatment inconsistency.
- **Canonical value:** status `good` is defensible (threshold/felony holding intact), but the **note must document the Lange limit** so the canonical page matches its three homes and the Summers convention.
- **Fix:** Add to `content/cases/United States v. Santana.md` `treatment.note`: e.g. "Hot-pursuit reading for *misdemeanor* pursuits limited by *Lange v. California* (2021) — no longer categorical; the threshold/public-place and felony hot-pursuit holdings are intact." (Optionally add `[[Curtilage]]` to `homes[]`.) No status change required; the token is already consistent everywhere.

### F3 — MINOR — *Coolidge v. New Hampshire*: N4 tag names the limiter on one home but not the other
- **Case:** *Coolidge v. New Hampshire* — canonical `treatment.status: **limited**` (note: "*Horton v. California* (1990) abandoned the inadvertence requirement… prior-justification and immediately-apparent requirements survive").
- **Pages it appears on:** Case Index (limited); Plain View Doctrine (home); The Warrant Requirement (home); Fourth Amendment Framework; Probable Cause and Reasonable Suspicion.
- **Divergence (status is consistent; tag wording is not):**
  - `Plain View Doctrine.md:31,56` — **"limited by [[Horton v. California]]"** ✓ (names the limiter).
  - `The Warrant Requirement.md:99` — **"Binding — SCOTUS · limited *(inadvertence prong)*"** — status token correct (`limited`) and scope noted, but the N4 tag **does not name Horton** as the Plain View page does. Per R8 rule 2 (same inline tag everywhere the limitation is asserted), the two homes should match.
  - `Fourth Amendment Framework.md:24` — cited for the still-good **state-action / private-search** proposition in a **weight-only table** (no treatment column exists on that page); shows "SCOTUS — binding," no status token. **Not a defect** — different (unlimited) holding, N6 framing, and the table has no treatment column. (Noted for completeness.)
  - `Probable Cause and Reasonable Suspicion.md:55` — prose citation for the burden-of-proof rule (still-good Coolidge holding); no badge needed. Not a defect.
- **Canonical value:** limited (by Horton, inadvertence prong).
- **Fix (low priority):** For tag parity, make `The Warrant Requirement.md:99` read "limited *(inadvertence prong — [[Horton v. California|Horton]])*". Status is already consistent; this is wording-only.

---

## Verified consistent (no action) — key multi-homed / non-good cases

| Case | Canonical | Homes / pages checked | Result |
|---|---|---|---|
| *New York v. Belton* | limited | Search Incident to Arrest, Traffic Stops (+ Case Index; Instructor Dev. = teaching prose) | ✓ "limited by [[Arizona v. Gant]]" on **both** SITA (`:` Key table) and Traffic Stops (`:76,129`); status `limited` both. |
| *Thornton v. United States* | limited | Search Incident to Arrest, Automobile Exception (+ Case Index) | ✓ "limited by [[Arizona v. Gant]]" + status `limited` on both homes. |
| *United States v. Chadwick* | limited | Automobile Exception, Search Incident to Arrest (+ Case Index) | ✓ "limited by [[California v. Acevedo]]" + status `limited` on both homes. |
| *Coolidge v. New Hampshire* | limited | Plain View, Warrant Req. (status ✓ both; see **F3** for tag wording) | status consistent; tag-wording nit only. |
| *Oregon v. Elstad* | limited | Miranda Waiver ✓, Miranda&Custodial ✓, **Due-Process ✗** | see **F1**. |
| *Aguilar v. Texas* | abrogated | Probable Cause & RS (+ Case Index) | ✓ "abrogated *(by [[Illinois v. Gates]])*" + shown Historical. |
| *Spinelli v. United States* | abrogated | Probable Cause & RS, The Warrant Requirement (+ Case Index) | ✓ "abrogated by [[Illinois v. Gates]]" + Historical on both homes. |
| *Mathis v. United States (1968)* | limited | Miranda and Custodial Interrogation (+ Case Index) | ✓ "limited by [[Howes v. Fields]]" (table `:66` + prose `:28`). |
| *United States v. Agurs* | limited | Brady and Giglio (+ Case Index) | ✓ "superseded/limited by [[United States v. Bagley]]". |
| *Escobedo v. Illinois* | limited | Sixth Amendment Right to Counsel, Miranda and Custodial Interrogation (+ Case Index) | ✓ Historical + limited; "superseded by [[Miranda v. Arizona]]" on both. |
| *Monroe v. Pape* | limited | § 1983 Liability & QI (+ Case Index) | ✓ "overruled in part by Monell / limited" consistent. |
| *Saucier v. Katz* | limited | § 1983 Liability & QI (+ Case Index) | ✓ limited (Pearson) consistent. |
| *Boyd v. United States* | limited | Common Law Origins (+ Case Index) | ✓ limited consistent. |
| **Overruled — shown Historical everywhere:** | | | |
| *Gouled v. United States* | overruled | Two Definitions of Search (+ Case Index) | ✓ "overruled by [[Warden v. Hayden]]" + Historical. |
| *Jones v. United States* (1960) | overruled | Standing to Challenge a Search, Abandonment (+ Case Index) | ✓ "overruled by [[United States v. Salvucci]]" / Rakas; Historical on Standing, overruled on Abandonment. |
| *Michigan v. Jackson* | overruled | Sixth Amendment Right to Counsel (+ Case Index) | ✓ "overruled by [[Montejo v. Louisiana]]" + Historical. |
| *Olmstead v. United States* | overruled | Two Definitions, Fourth Amendment Framework, Fourth Amendment Recalibration (+ Case Index) | ✓ overruled by *Katz* stated inline on every page ("Don't read Olmstead as still good law"). |
| *Wolf v. Colorado* | overruled | The Exclusionary Rule, Fourth Amendment Recalibration (+ Case Index) | ✓ overruled by *Mapp* (remedy) stated inline; right-vs-remedy split handled consistently. |

**Boundary / shared-holding spot checks (all `good`, no contradiction):**
- *Arizona v. Gant* — good on Search Incident to Arrest, Traffic Stops, Automobile Exception (it is the *limiter*; never shown non-good). ✓
- *New York v. Belton* / *Gant* boundary (SITA vs Automobile Exception vs Traffic Stops) — consistent: Belton limited-by-Gant, Gant good, Automobile Exception framed as a separate theory. ✓
- *Rakas v. Illinois* (Standing vs Exclusionary Rule vs Curtilage/Abandonment) — good everywhere; "overruled" tokens near Rakas rows refer to Rakas *disavowing* the *Jones* "legitimately on premises" test, not to Rakas itself. ✓
- *Mincey v. Arizona* / *Michigan v. Tyler* / *Michigan v. Clifford* (Emergency Aid vs Community Caretaking vs Securing the Scene) — all `good`, framed consistently across the overlap pages. ✓
- *Michigan v. Summers* (Securing the Scene vs Seizure of the Person) — `good` + "detention authority spatially limited by [[Bailey v. United States]]" mirrored on the case page note; **correct model** for a partially-limited anchor (contrast Santana, F2). ✓

---

## Method notes / caveats
- Canonical status pulled from each case page's `treatment.status` (438 good / 11 limited / 5 overruled / 2 abrogated). All 18 non-good cases were traced by full-text grep across every doctrine page (not just table-extracted rows), so alternate table formats (plain-italic case name + trailing wikilink, e.g. Traffic Stops, Fourth Amendment Framework/Recalibration) were covered manually.
- The "substantive multi-homed = 200" figure lightly over-counts a few cases where a `homes[]` wikilink alias differs in string from the page's display title (e.g. `[[Section 1983 Liability and Qualified Immunity]]` vs page title "§ 1983 Liability & Qualified Immunity"); this is Quartz alias resolution, not a content defect. The cleaner canonical figure is **100 cases with ≥2 declared `homes[]`**.
- Pure reference/navigation pages (Case Index, CSSI Map of Content, Flashcards, chapter `index.md`, Common Legal Terms, research-tool pages) were excluded from "home" counting but Case Index treatment tokens were still checked against canonical (0 mismatches).
