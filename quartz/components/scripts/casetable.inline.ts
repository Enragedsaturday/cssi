// S3 · R4 #2 — CaseTable client enhancement.
// Upgrades a plain GFM markdown table (one with a "Case"/"Name" column) into a
// sortable + filterable table, enriching cells by slug-matching to the case-page
// frontmatter index (data island `[data-casetable-index]`). Fully degraded form = the
// untouched static markdown table (this script simply doesn't run with JS disabled).

interface CaseRec {
  title: string
  court: string
  courtLevel: string
  jurisdiction: string
  year: number | string
  weight: string
  weightTier: string
  treatment: string
  roles: string[]
}
interface CaseIndex {
  cases: Record<string, CaseRec>
  names: Record<string, string>
}

const TREATMENT_LABELS: Record<string, string> = {
  good: "Good law",
  criticized: "Criticized",
  limited: "Limited",
  abrogated: "Abrogated",
  overruled: "Overruled",
}
const WEIGHT_RANK: Record<string, number> = {
  "binding-scotus": 0,
  "binding-circuit": 1,
  persuasive: 2,
  "persuasive-state": 3,
  "persuasive-nonprec": 4,
  historical: 5,
  other: 6,
  unknown: 7,
}
const TREAT_RANK: Record<string, number> = {
  good: 0,
  criticized: 1,
  limited: 2,
  abrogated: 3,
  overruled: 4,
  "": 5,
}

function loadIndex(): CaseIndex {
  const el = document.querySelector("[data-casetable-index]")
  if (el?.textContent) {
    try {
      return JSON.parse(el.textContent) as CaseIndex
    } catch {
      /* ignore */
    }
  }
  return { cases: {}, names: {} }
}

function slugFromHref(href: string | null): string {
  if (!href) return ""
  try {
    const u = new URL(href, location.origin)
    return u.pathname.replace(/\/$/, "").replace(/^\//, "")
  } catch {
    return ""
  }
}

function lookup(cell: HTMLTableCellElement, index: CaseIndex): CaseRec | null {
  const a = cell.querySelector("a")
  if (a) {
    const p = slugFromHref(a.getAttribute("href"))
    if (index.cases[p]) return index.cases[p]
    const seg = p.split("/").pop() ?? ""
    if (seg) {
      for (const k in index.cases) {
        if (k === seg || k.endsWith("/" + seg)) return index.cases[k]
      }
    }
  }
  const text = cell.textContent?.trim().toLowerCase() ?? ""
  const key = index.names[text]
  if (key && index.cases[key]) return index.cases[key]
  // tolerant fallback: doctrine tables often render "*Case*, 267 U.S. 132 (1925)"
  // (case name followed by a reporter cite, before S6 wires [[links]]). Match the
  // longest case name the cell text starts with.
  let best = ""
  for (const name in index.names) {
    if (name.length > best.length && text.startsWith(name)) best = name
  }
  if (best) {
    const k = index.names[best]
    if (k && index.cases[k]) return index.cases[k]
  }
  return null
}

type ColKind = "case" | "court" | "year" | "weight" | "treatment" | "role" | "jurisdiction" | "other"

function classifyHeader(text: string): ColKind {
  const t = text.toLowerCase()
  if (/\b(case|name)\b/.test(t)) return "case"
  if (/court/.test(t)) return "court"
  if (/year|date|decided/.test(t)) return "year"
  if (/weight|authority/.test(t)) return "weight"
  if (/treatment|status|good.?law/.test(t)) return "treatment"
  if (/role/.test(t)) return "role"
  if (/jurisdiction|circuit/.test(t)) return "jurisdiction"
  return "other"
}

function enhanceTable(table: HTMLTableElement, index: CaseIndex) {
  if (table.dataset.casetableEnhanced) return
  const headRow = table.tHead?.rows[0] ?? table.rows[0]
  if (!headRow) return
  const headers = Array.from(headRow.cells).map((c) => (c.textContent ?? "").trim())
  const kinds = headers.map(classifyHeader)
  const caseCol = kinds.indexOf("case")
  if (caseCol < 0) return // conservative: only enhance tables with a Case/Name column

  table.dataset.casetableEnhanced = "true"
  table.classList.add("casetable")

  const bodyRows: HTMLTableRowElement[] = table.tBodies[0]
    ? Array.from(table.tBodies[0].rows)
    : Array.from(table.rows).slice(1)

  const colIndex = (k: ColKind) => kinds.indexOf(k)

  // populate row datasets (from columns where present, else frontmatter enrichment)
  for (const row of bodyRows) {
    const caseCell = row.cells[caseCol]
    if (!caseCell) continue
    const rec = lookup(caseCell, index)
    const colText = (k: ColKind) => {
      const i = colIndex(k)
      return i >= 0 && row.cells[i] ? (row.cells[i].textContent ?? "").trim() : ""
    }

    const treatment = (colText("treatment") || rec?.treatment || "").toLowerCase()
    const court = colText("court") || rec?.court || ""
    const year = colText("year") || (rec?.year != null ? String(rec.year) : "")
    const jurisdiction = colText("jurisdiction") || rec?.jurisdiction || rec?.courtLevel || ""
    const role = colText("role") || (rec?.roles ?? []).join(", ")
    const weightTier = rec?.weightTier ?? "unknown"

    row.dataset.treatment = treatment
    row.dataset.court = court
    row.dataset.year = year
    row.dataset.jurisdiction = jurisdiction
    row.dataset.role = role
    row.dataset.weightTier = weightTier

    // inject a treatment badge into the case cell when treatment isn't its own column
    if (rec && rec.treatment && colIndex("treatment") < 0) {
      if (!caseCell.querySelector(".casetable-badge")) {
        const badge = document.createElement("span")
        badge.className = `casetable-badge treatment-${rec.treatment}`
        badge.textContent = TREATMENT_LABELS[rec.treatment] ?? rec.treatment
        badge.title = `Treatment: ${rec.treatment}`
        caseCell.appendChild(document.createTextNode(" "))
        caseCell.appendChild(badge)
      }
    }
  }

  // ---- sorting ----
  let sortState: { col: number; dir: 1 | -1 } | null = null
  const sortValue = (row: HTMLTableRowElement, col: number): number | string => {
    const cell = row.cells[col]
    const txt = (cell?.textContent ?? "").trim()
    switch (kinds[col]) {
      case "year":
        return parseFloat(txt) || 0
      case "weight":
        return WEIGHT_RANK[row.dataset.weightTier ?? "unknown"] ?? 99
      case "treatment":
        return TREAT_RANK[(row.dataset.treatment ?? "") as string] ?? 99
      default:
        return txt.toLowerCase()
    }
  }
  const doSort = (col: number) => {
    const dir: 1 | -1 = sortState?.col === col && sortState.dir === 1 ? -1 : 1
    sortState = { col, dir }
    const sorted = [...bodyRows].sort((a, b) => {
      const va = sortValue(a, col)
      const vb = sortValue(b, col)
      if (va < vb) return -1 * dir
      if (va > vb) return 1 * dir
      return 0
    })
    const parent = bodyRows[0]?.parentElement
    if (parent) sorted.forEach((r) => parent.appendChild(r))
    Array.from(headRow.cells).forEach((c, i) => {
      c.setAttribute("aria-sort", i === col ? (dir === 1 ? "ascending" : "descending") : "none")
    })
  }
  Array.from(headRow.cells).forEach((cell, i) => {
    cell.classList.add("casetable-sortable")
    cell.setAttribute("role", "button")
    cell.setAttribute("tabindex", "0")
    cell.setAttribute("aria-sort", "none")
    const handler = () => doSort(i)
    cell.addEventListener("click", handler)
    const keyHandler = (e: KeyboardEvent) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault()
        doSort(i)
      }
    }
    cell.addEventListener("keydown", keyHandler as EventListener)
    window.addCleanup(() => {
      cell.removeEventListener("click", handler)
      cell.removeEventListener("keydown", keyHandler as EventListener)
    })
  })

  // ---- filtering ----
  const facetDefs: { key: "role" | "treatment" | "jurisdiction"; label: string }[] = [
    { key: "role", label: "Role" },
    { key: "treatment", label: "Treatment" },
    { key: "jurisdiction", label: "Jurisdiction" },
  ]
  const controls = document.createElement("div")
  controls.className = "casetable-controls"

  const textInput = document.createElement("input")
  textInput.type = "search"
  textInput.placeholder = "Filter cases…"
  textInput.className = "casetable-search"
  controls.appendChild(textInput)

  const selects: { key: string; el: HTMLSelectElement }[] = []
  for (const def of facetDefs) {
    const values = new Set<string>()
    for (const row of bodyRows) {
      const raw = row.dataset[def.key] ?? ""
      // role can be multi-valued (comma-separated)
      raw
        .split(",")
        .map((v) => v.trim())
        .filter(Boolean)
        .forEach((v) => values.add(v))
    }
    if (values.size < 2) continue
    const sel = document.createElement("select")
    sel.className = "casetable-facet"
    sel.setAttribute("aria-label", `Filter by ${def.label.toLowerCase()}`)
    const optAll = document.createElement("option")
    optAll.value = ""
    optAll.textContent = `${def.label}: all`
    sel.appendChild(optAll)
    Array.from(values)
      .sort()
      .forEach((v) => {
        const o = document.createElement("option")
        o.value = v.toLowerCase()
        o.textContent = def.key === "treatment" ? TREATMENT_LABELS[v] ?? v : v
        sel.appendChild(o)
      })
    selects.push({ key: def.key, el: sel })
    controls.appendChild(sel)
  }

  const count = document.createElement("span")
  count.className = "casetable-count"
  controls.appendChild(count)

  const applyFilters = () => {
    const q = textInput.value.trim().toLowerCase()
    let visible = 0
    for (const row of bodyRows) {
      let show = true
      if (q && !(row.cells[caseCol]?.textContent ?? "").toLowerCase().includes(q)) show = false
      if (show) {
        for (const { key, el } of selects) {
          const want = el.value
          if (!want) continue
          const have = (row.dataset[key] ?? "").toLowerCase()
          const matches = have
            .split(",")
            .map((v) => v.trim())
            .includes(want)
          if (!matches) {
            show = false
            break
          }
        }
      }
      row.style.display = show ? "" : "none"
      if (show) visible++
    }
    count.textContent = `${visible} / ${bodyRows.length}`
  }
  textInput.addEventListener("input", applyFilters)
  selects.forEach(({ el }) => el.addEventListener("change", applyFilters))
  window.addCleanup(() => {
    textInput.removeEventListener("input", applyFilters)
    selects.forEach(({ el }) => el.removeEventListener("change", applyFilters))
  })

  // insert controls before the table (outside the scroll container so they stay put)
  const container = table.closest(".table-container") ?? table
  container.parentElement?.insertBefore(controls, container)
  applyFilters()
}

document.addEventListener("nav", () => {
  const center = document.querySelector(".center")
  if (!center) return
  const tables = center.querySelectorAll("table")
  if (tables.length === 0) return
  const index = loadIndex()
  tables.forEach((t) => {
    try {
      enhanceTable(t as HTMLTableElement, index)
    } catch {
      /* never break the page over an enhancement failure */
    }
  })
})
