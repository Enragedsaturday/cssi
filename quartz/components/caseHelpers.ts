// Shared server-side helpers for the CSSI case-data component layer (S3 · R4 / S4 · R9).
// These read the documented Appendix-B case frontmatter convention ONLY — no bespoke,
// component-only load-bearing syntax (R5 portability guardrail). All inputs are plain
// frontmatter keys + Obsidian `[[wikilinks]]`, so content stays portable markdown.

import { QuartzPluginData } from "../plugins/vfile"
import { FilePath, FullSlug, resolveRelative, simplifySlug, slugifyFilePath } from "../util/path"

// Canonical good-law treatment axis (S1 §3.D / N13). Kept STRICTLY separate from the
// orthogonal authority-weight axis — the two are never merged.
export const TREATMENT_STATUSES = [
  "good",
  "criticized",
  "limited",
  "abrogated",
  "overruled",
] as const

export type TreatmentStatus = (typeof TREATMENT_STATUSES)[number]

export const TREATMENT_LABELS: Record<string, string> = {
  good: "Good law",
  criticized: "Criticized",
  limited: "Limited",
  abrogated: "Abrogated",
  overruled: "Overruled",
}

// The orthogonal six-tier authority-weight lexicon (S1 §4). Used only to derive a
// stable css key for the (visually distinct) weight label — never to color the
// treatment badge.
export function weightTierKey(weight: unknown): string {
  if (typeof weight !== "string") return "unknown"
  const w = weight.toLowerCase()
  if (w.includes("binding") && w.includes("scotus")) return "binding-scotus"
  if (w.includes("binding")) return "binding-circuit"
  if (w.includes("non-precedential") || w.includes("nonprecedential")) return "persuasive-nonprec"
  if (w.includes("state")) return "persuasive-state"
  if (w.includes("persuasive")) return "persuasive"
  if (w.includes("historical")) return "historical"
  return "other"
}

export function normStatus(status: unknown): string | undefined {
  if (typeof status !== "string") return undefined
  const s = status.toLowerCase().trim()
  return s.length > 0 ? s : undefined
}

export function isKnownStatus(status: string | undefined): status is TreatmentStatus {
  return !!status && (TREATMENT_STATUSES as readonly string[]).includes(status)
}

export interface ParsedWikilink {
  target: string // page name, e.g. "Brigham City v. Stuart"
  anchor?: string // "#rule" or "#^pin-404"
  alias?: string // display text after the pipe
}

// Parse an Obsidian wikilink string from frontmatter, e.g. "[[Case#rule|alias]]".
// Tolerates bare strings (no brackets) so partially-authored frontmatter still works.
export function parseWikilink(raw: unknown): ParsedWikilink | null {
  if (typeof raw !== "string") return null
  let s = raw.trim()
  if (s.length === 0) return null
  const m = s.match(/^\[\[(.+?)\]\]$/)
  if (m) s = m[1]
  let alias: string | undefined
  const pipeIdx = s.indexOf("|")
  if (pipeIdx >= 0) {
    alias = s.slice(pipeIdx + 1).trim()
    s = s.slice(0, pipeIdx)
  }
  let anchor: string | undefined
  const hashIdx = s.indexOf("#")
  if (hashIdx >= 0) {
    anchor = s.slice(hashIdx) // keep leading '#'
    s = s.slice(0, hashIdx)
  }
  const target = s.trim()
  if (target.length === 0) return null
  return { target, anchor, alias }
}

// Resolve a case/page name to a file in the corpus via the documented conventions:
// exact title match, alias slug, or shortest-path slug match (Quartz
// markdownLinkResolution: "shortest"). Returns undefined if unresolved (degraded path).
export function findFileByName(
  allFiles: QuartzPluginData[],
  name: string,
): QuartzPluginData | undefined {
  const wanted = name.trim().toLowerCase()
  if (!wanted) return undefined

  // 1) exact title match
  const byTitle = allFiles.find(
    (f) => (f.frontmatter?.title ?? "").toString().toLowerCase() === wanted,
  )
  if (byTitle) return byTitle

  // 2) slug match (shortest path)
  let wantedSlug: FullSlug | undefined
  try {
    wantedSlug = slugifyFilePath((name.trim() + ".md") as FilePath)
  } catch {
    wantedSlug = undefined
  }
  if (wantedSlug) {
    const bySlug = allFiles.find(
      (f) => f.slug === wantedSlug || (f.slug?.endsWith("/" + wantedSlug) ?? false),
    )
    if (bySlug) return bySlug

    // 3) alias slug match (frontmatter aliases are slugified into file.aliases)
    const byAlias = allFiles.find((f) =>
      ((f as { aliases?: FullSlug[] }).aliases ?? []).some(
        (a) => a === wantedSlug || a.endsWith("/" + wantedSlug),
      ),
    )
    if (byAlias) return byAlias
  }

  return undefined
}

export interface ResolvedLink {
  href: string
  title: string
  resolved: boolean
  anchor?: string
}

// Resolve a frontmatter wikilink to a real href when possible; otherwise hand back the
// bare name so callers degrade to plain (still-legible) text.
export function resolveLink(
  allFiles: QuartzPluginData[],
  currentSlug: FullSlug,
  raw: unknown,
): ResolvedLink | null {
  const parsed = parseWikilink(raw)
  if (!parsed) return null
  const file = findFileByName(allFiles, parsed.target)
  if (file?.slug) {
    const base = resolveRelative(currentSlug, file.slug)
    return {
      href: base + (parsed.anchor ? slugAnchor(parsed.anchor) : ""),
      title: parsed.alias ?? (file.frontmatter?.title ?? parsed.target).toString(),
      resolved: true,
      anchor: parsed.anchor,
    }
  }
  return {
    href: "",
    title: parsed.alias ?? parsed.target,
    resolved: false,
    anchor: parsed.anchor,
  }
}

// Convert "#rule" / "#^pin-404" to the auto-slugged anchor Quartz emits.
function slugAnchor(anchor: string): string {
  if (anchor.startsWith("#^")) return anchor // block ref kept as-is
  // heading anchor: Quartz lowercases + dashes
  return "#" + anchor.slice(1).toLowerCase().replace(/\s+/g, "-")
}

export function decadeOf(year: unknown): string | undefined {
  const y = typeof year === "number" ? year : parseInt(String(year ?? ""), 10)
  if (!Number.isFinite(y) || y < 100) return undefined
  return `${Math.floor(y / 10) * 10}s`
}

export const COURT_LEVEL_LABELS: Record<string, string> = {
  scotus: "U.S. Supreme Court",
  circuit: "Federal Circuit",
  district: "Federal District",
  "state-high": "State High Court",
  "state-app": "State Appellate",
  other: "Other",
}

export function isCasePage(fileData: QuartzPluginData): boolean {
  return fileData.frontmatter?.type === "case"
}

export function caseSlugKey(file: QuartzPluginData): string {
  return simplifySlug(file.slug!)
}
