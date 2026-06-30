import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/casebrowser.scss"
// @ts-ignore
import script from "./scripts/casebrowser.inline"
import { classNames } from "../util/lang"
import { JSX } from "preact"
import {
  COURT_LEVEL_LABELS,
  TREATMENT_LABELS,
  decadeOf,
  findFileByName,
  isKnownStatus,
  normStatus,
  parseWikilink,
  resolveLink,
} from "./caseHelpers"
import { resolveRelative, simplifySlug } from "../util/path"
import { QuartzPluginData } from "../plugins/vfile"

// S3 · R4 #5 — CaseBrowser.
// A corpus-wide faceted browse / filter surface over the Case Index / build-index data
// (the aggregate of `type: case` frontmatter, R10). Facets: category/home, role, court
// level, treatment, decade.
//
// Opt-in: renders its UI only on a page that requests it via FRONTMATTER —
// `type: case-browser` or `caseBrowser: true`. On every other page it renders null, so
// it is harmless in the global layout.
//
// Degraded state: the cards are SERVER-RENDERED as a plain list of case links (still a
// usable browse with JS off), and a prominent "Browse the full Case Index →" link is
// always shown — satisfying the R5 degraded requirement (a link to the Case Index). The
// page body itself should also carry a portable `[[Case Index]]` link as the fallback if
// the component is stripped/ported. No component-only load-bearing syntax is required.

function slugifyFacet(v: string): string {
  return v
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
}

interface HomeRef {
  slug: string
  title: string
  role: string
}

export default (() => {
  const CaseBrowser: QuartzComponent = ({
    fileData,
    allFiles,
    displayClass,
  }: QuartzComponentProps) => {
    const fm = fileData.frontmatter as Record<string, any> | undefined
    const enabled = fm?.type === "case-browser" || fm?.caseBrowser === true
    if (!enabled) return null

    const currentSlug = fileData.slug!
    const caseIndexLink = resolveLink(allFiles, currentSlug, "[[Case Index]]")

    const cases = allFiles
      .filter((f) => f.frontmatter?.type === "case" && f.slug)
      .sort((a, b) =>
        (a.frontmatter?.title ?? "")
          .toString()
          .localeCompare((b.frontmatter?.title ?? "").toString()),
      )

    // collect facet value sets
    const homeSet = new Map<string, string>() // slug -> title
    const roleSet = new Set<string>()
    const levelSet = new Set<string>()
    const treatSet = new Set<string>()
    const decadeSet = new Set<string>()

    const homesOf = (f: QuartzPluginData): HomeRef[] => {
      const out: HomeRef[] = []
      const homes = Array.isArray(f.frontmatter?.homes) ? (f.frontmatter!.homes as any[]) : []
      for (const h of homes) {
        const parsed = parseWikilink(h?.page)
        if (!parsed) continue
        const target = findFileByName(allFiles, parsed.target)
        const slug = target?.slug ? simplifySlug(target.slug) : slugifyFacet(parsed.target)
        const title = target?.frontmatter?.title?.toString() ?? parsed.target
        out.push({ slug, title, role: h?.role ? String(h.role) : "" })
      }
      return out
    }

    interface CardModel {
      file: QuartzPluginData
      homes: HomeRef[]
      level: string
      treatment: string
      decade: string
      roleSlugs: string[]
      homeSlugs: string[]
    }

    const cards: CardModel[] = cases.map((f) => {
      const fmc = f.frontmatter as Record<string, any>
      const homes = homesOf(f)
      const level = (fmc.court_level ?? "").toString()
      const treatment = normStatus(fmc.treatment?.status) ?? ""
      const decade = decadeOf(fmc.year) ?? ""
      const roleSlugs: string[] = []
      const homeSlugs: string[] = []
      for (const h of homes) {
        if (h.slug) {
          homeSlugs.push(h.slug)
          homeSet.set(h.slug, h.title)
        }
        if (h.role) {
          const rs = slugifyFacet(h.role)
          roleSlugs.push(rs)
          roleSet.add(h.role)
        }
      }
      if (level) levelSet.add(level)
      if (treatment) treatSet.add(treatment)
      if (decade) decadeSet.add(decade)
      return { file: f, homes, level, treatment, decade, roleSlugs, homeSlugs }
    })

    const facet = (
      label: string,
      attr: string,
      options: { value: string; label: string }[],
    ): JSX.Element | null => {
      if (options.length < 2) return null
      return (
        <fieldset class="casebrowser-facet" data-facet-attr={attr}>
          <legend>{label}</legend>
          {options.map((o) => (
            <label class="casebrowser-option">
              <input type="checkbox" value={o.value} />
              <span>{o.label}</span>
            </label>
          ))}
        </fieldset>
      )
    }

    const homeOptions = Array.from(homeSet.entries())
      .map(([slug, title]) => ({ value: slug, label: title }))
      .sort((a, b) => a.label.localeCompare(b.label))
    const roleOptions = Array.from(roleSet)
      .sort()
      .map((r) => ({ value: slugifyFacet(r), label: r }))
    const levelOptions = Array.from(levelSet)
      .sort()
      .map((l) => ({ value: l, label: COURT_LEVEL_LABELS[l] ?? l }))
    const treatOptions = Array.from(treatSet)
      .sort()
      .map((t) => ({ value: t, label: TREATMENT_LABELS[t] ?? t }))
    const decadeOptions = Array.from(decadeSet)
      .sort()
      .map((d) => ({ value: d, label: d }))

    const indexHref = caseIndexLink?.resolved ? (
      <a href={caseIndexLink.href} class="internal">
        Browse the full Case Index →
      </a>
    ) : (
      <span>See the Case Index</span>
    )

    return (
      <div class={classNames(displayClass, "casebrowser")}>
        <div class="casebrowser-toolbar">
          <input
            type="search"
            class="casebrowser-search"
            placeholder="Search cases by name…"
            aria-label="Search cases by name"
          />
          <span class="casebrowser-count" data-total={cards.length}>
            {cards.length} cases
          </span>
          <span class="casebrowser-indexlink">{indexHref}</span>
        </div>

        {cards.length > 0 && (
          <div class="casebrowser-facets">
            {facet("Home", "homes", homeOptions)}
            {facet("Role", "roles", roleOptions)}
            {facet("Court level", "court-level", levelOptions)}
            {facet("Treatment", "treatment", treatOptions)}
            {facet("Decade", "decade", decadeOptions)}
          </div>
        )}

        {cards.length === 0 ? (
          <p class="casebrowser-empty">
            No cases indexed yet. {indexHref}
          </p>
        ) : (
          <ul class="casebrowser-list">
            {cards.map((c) => {
              const fmc = c.file.frontmatter as Record<string, any>
              const href = resolveRelative(currentSlug, c.file.slug!)
              const title = (fmc.title ?? c.file.slug)!.toString()
              const status = normStatus(fmc.treatment?.status)
              const known = isKnownStatus(status)
              return (
                <li
                  class="casebrowser-card"
                  data-title={title.toLowerCase()}
                  data-homes={c.homeSlugs.join(" ")}
                  data-roles={c.roleSlugs.join(" ")}
                  data-court-level={c.level}
                  data-treatment={c.treatment}
                  data-decade={c.decade}
                >
                  <a href={href} class="internal casebrowser-card-title">
                    {title}
                  </a>
                  <div class="casebrowser-card-meta">
                    {fmc.citation && <span>{String(fmc.citation)}</span>}
                    {fmc.court && <span>{String(fmc.court)}</span>}
                    {status && (
                      <span
                        class={`casebrowser-treat treatment-${known ? status : "unknown"}`}
                      >
                        {TREATMENT_LABELS[status] ?? status}
                      </span>
                    )}
                  </div>
                  {c.homes.length > 0 && (
                    <div class="casebrowser-card-homes">
                      {c.homes.map((h) => (
                        <span class="casebrowser-home-tag">
                          {h.title}
                          {h.role && <em> · {h.role}</em>}
                        </span>
                      ))}
                    </div>
                  )}
                </li>
              )
            })}
          </ul>
        )}
      </div>
    )
  }

  CaseBrowser.css = style
  CaseBrowser.afterDOMLoaded = script
  return CaseBrowser
}) satisfies QuartzComponentConstructor
