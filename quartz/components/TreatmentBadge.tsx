import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/treatmentBadge.scss"
import { classNames } from "../util/lang"
import {
  TREATMENT_LABELS,
  isCasePage,
  isKnownStatus,
  normStatus,
  weightTierKey,
} from "./caseHelpers"

// S3 · R4 #1 — TreatmentBadge.
// Renders a case's good-law `treatment.status` (good|criticized|limited|abrogated|
// overruled, S1 §3.D) as a colored inline badge from the case page's FRONTMATTER, and
// — as a SEPARATE, visually distinct label — the orthogonal six-tier `authority_weight`
// (S1 §4). The two axes are never merged.
//
// Data source (R9): case-page frontmatter — `treatment.{status,as_of,note}` +
// `authority_weight` (Appendix B).
// Degraded state: the plain-markdown header line already on the page
// (e.g. "*547 U.S. 398 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good**").
// This component ENHANCES that line; with components stripped, the text remains.

export default (() => {
  const TreatmentBadge: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
    if (!isCasePage(fileData)) return null
    const fm = fileData.frontmatter as Record<string, any>
    const treatment = fm.treatment as { status?: unknown; as_of?: unknown; note?: unknown } | undefined
    const weight = fm.authority_weight
    const status = normStatus(treatment?.status)

    // empty/degraded: nothing to enhance
    if (!status && !weight) return null

    const known = isKnownStatus(status)
    const asOf = treatment?.as_of ? String(treatment.as_of) : undefined
    const note = treatment?.note ? String(treatment.note) : undefined

    return (
      <div class={classNames(displayClass, "treatment-badges")}>
        {status && (
          <span
            class={`treatment-badge treatment-${known ? status : "unknown"}`}
            data-treatment={status}
            title={note}
          >
            <span class="treatment-dot" aria-hidden="true"></span>
            <span class="treatment-label">{TREATMENT_LABELS[status] ?? status}</span>
            {asOf && <span class="treatment-asof">as of {asOf}</span>}
          </span>
        )}
        {weight && (
          <span class="authority-weight" data-weight-tier={weightTierKey(weight)} title="Authority weight">
            {String(weight)}
          </span>
        )}
      </div>
    )
  }

  TreatmentBadge.css = style
  return TreatmentBadge
}) satisfies QuartzComponentConstructor
