import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/casetable.scss"
// @ts-ignore
import script from "./scripts/casetable.inline"
import { visit } from "unist-util-visit"
import { Root } from "hast"
import {
  COURT_LEVEL_LABELS,
  normStatus,
  weightTierKey,
} from "./caseHelpers"
import { simplifySlug } from "../util/path"

// S3 · R4 #2 — CaseTable.
// Enhances a PLAIN GFM MARKDOWN TABLE (the doctrine-page "Key cases" tables + the Case
// Index) into a sortable / filterable view — sort by case/court/year/weight; filter by
// role/treatment/jurisdiction — by slug-matching case names / [[links]] in the table to
// case-page frontmatter (Appendix B, via the data island emitted below).
//
// R5 portability: the SOURCE stays a plain markdown table authored in the brief-first
// template. With JS disabled, the table renders as a static GFM table (Quartz already
// wraps it in `.table-container { overflow-x: auto }` for mobile). No component-only,
// load-bearing syntax is introduced — enhancement is triggered purely by a heuristic
// ("Case"/"Name" column header), never by authored markup.
//
// This component renders only a hidden JSON data island (the aggregate case index, R10)
// for the client script to slug-match against, and only on pages that actually contain a
// table. It contributes the enhancement script + styles globally via the layout.

export default (() => {
  const CaseTable: QuartzComponent = ({ tree, allFiles }: QuartzComponentProps) => {
    // only emit the data island on pages that contain at least one table
    let hasTable = false
    visit(tree as Root, "element", (node) => {
      if (node.tagName === "table") {
        hasTable = true
        return false
      }
      return undefined
    })
    if (!hasTable) return null

    const cases: Record<string, unknown> = {}
    const names: Record<string, string> = {}
    for (const f of allFiles) {
      const fm = f.frontmatter as Record<string, any> | undefined
      if (!fm || fm.type !== "case" || !f.slug) continue
      const key = simplifySlug(f.slug)
      const roles = Array.isArray(fm.homes)
        ? fm.homes.map((h: any) => (h?.role ? String(h.role) : "")).filter(Boolean)
        : []
      const jurisdiction = fm.circuit
        ? `${fm.circuit} Cir.`
        : COURT_LEVEL_LABELS[fm.court_level as string] ?? (fm.court ? String(fm.court) : "")
      cases[key] = {
        title: fm.title ?? "",
        court: fm.court ?? "",
        courtLevel: fm.court_level ?? "",
        jurisdiction,
        year: fm.year ?? "",
        weight: fm.authority_weight ?? "",
        weightTier: weightTierKey(fm.authority_weight),
        treatment: normStatus(fm.treatment?.status) ?? "",
        roles,
      }
      const title = (fm.title ?? "").toString().toLowerCase()
      if (title) names[title] = key
      const aliases = Array.isArray(fm.aliases) ? fm.aliases : []
      for (const a of aliases) names[String(a).toLowerCase()] = key
    }

    const payload = JSON.stringify({ cases, names }).replace(/</g, "\\u003c")

    return (
      <span class="casetable-data" hidden aria-hidden="true">
        <script
          type="application/json"
          data-casetable-index
          // eslint-disable-next-line react/no-danger
          dangerouslySetInnerHTML={{ __html: payload }}
        />
      </span>
    )
  }

  CaseTable.css = style
  CaseTable.afterDOMLoaded = script
  return CaseTable
}) satisfies QuartzComponentConstructor
