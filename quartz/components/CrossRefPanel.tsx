import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/crossref.scss"
import { classNames } from "../util/lang"
import { isCasePage, resolveLink } from "./caseHelpers"
import { JSX } from "preact"

// S3 · R4 #6 — CrossRefPanel.
// Per-page panel surfacing a case's OTHER HOMES (multi-homing, N6), `related:` cases,
// and limited-by / limits links (N4), driven entirely by FRONTMATTER (Appendix B):
//   homes: [{ page: "[[Doctrine]]", role: "..." }]
//   related: ["[[Case]]", ...]
//   treatment: { status, by: ["[[Case]]"], note }
// Degraded state: renders nothing; the frontmatter (and the page's own "Appears on" /
// "Treatment" markdown sections per the BIRAC template) remain on the page. No
// component-only syntax is introduced.

interface CrossRefOptions {
  hideWhenEmpty: boolean
}

const defaultOptions: CrossRefOptions = { hideWhenEmpty: true }

export default ((opts?: Partial<CrossRefOptions>) => {
  const options = { ...defaultOptions, ...opts }

  const CrossRefPanel: QuartzComponent = ({
    fileData,
    allFiles,
    displayClass,
  }: QuartzComponentProps) => {
    if (!isCasePage(fileData)) return null
    const fm = fileData.frontmatter as Record<string, any>
    const currentSlug = fileData.slug!

    const renderLinks = (items: unknown): JSX.Element[] => {
      const arr = Array.isArray(items) ? items : items != null ? [items] : []
      const out: JSX.Element[] = []
      for (const raw of arr) {
        const link = resolveLink(allFiles, currentSlug, raw)
        if (!link) continue
        out.push(
          <li>
            {link.resolved ? (
              <a href={link.href} class="internal">
                {link.title}
              </a>
            ) : (
              <span class="crossref-unresolved">{link.title}</span>
            )}
          </li>,
        )
      }
      return out
    }

    // homes — multi-homing (N6): doctrine page + role
    const homes = Array.isArray(fm.homes) ? fm.homes : []
    const homeItems: JSX.Element[] = []
    for (const home of homes) {
      const link = resolveLink(allFiles, currentSlug, home?.page)
      if (!link) continue
      const role = home?.role ? String(home.role) : undefined
      homeItems.push(
        <li>
          {link.resolved ? (
            <a href={link.href} class="internal">
              {link.title}
            </a>
          ) : (
            <span class="crossref-unresolved">{link.title}</span>
          )}
          {role && <span class="crossref-role">{role}</span>}
        </li>,
      )
    }

    const relatedItems = renderLinks(fm.related)

    // negative subsequent treatment (N4): limited / abrogated / overruled by
    const treatment = fm.treatment as { by?: unknown; status?: unknown } | undefined
    const byItems = renderLinks(treatment?.by)
    const byVerb =
      typeof treatment?.status === "string"
        ? `${treatment.status[0].toUpperCase()}${treatment.status.slice(1)} by`
        : "Limited by"

    const hasContent =
      homeItems.length > 0 || relatedItems.length > 0 || byItems.length > 0
    if (!hasContent && options.hideWhenEmpty) return null

    return (
      <div class={classNames(displayClass, "crossref-panel")}>
        <h3>Cross-references</h3>
        {homeItems.length > 0 && (
          <section class="crossref-section">
            <h4>Appears on</h4>
            <ul>{homeItems}</ul>
          </section>
        )}
        {byItems.length > 0 && (
          <section class="crossref-section crossref-negative">
            <h4>{byVerb}</h4>
            <ul>{byItems}</ul>
          </section>
        )}
        {relatedItems.length > 0 && (
          <section class="crossref-section">
            <h4>Related</h4>
            <ul>{relatedItems}</ul>
          </section>
        )}
      </div>
    )
  }

  CrossRefPanel.css = style
  return CrossRefPanel
}) satisfies QuartzComponentConstructor
