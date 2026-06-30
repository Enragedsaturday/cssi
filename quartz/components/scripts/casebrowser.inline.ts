// S3 · R4 #5 — CaseBrowser client enhancement.
// All cards + facets are server-rendered; this script only toggles visibility based on
// the checked facet checkboxes + the search box. No data fetch. Degraded form (JS off):
// the full static list of case links + the Case Index link remain usable.

function setup(root: HTMLElement) {
  if (root.dataset.casebrowserWired) return
  root.dataset.casebrowserWired = "true"

  const cards = Array.from(root.querySelectorAll<HTMLElement>(".casebrowser-card"))
  const search = root.querySelector<HTMLInputElement>(".casebrowser-search")
  const countEl = root.querySelector<HTMLElement>(".casebrowser-count")
  const total = cards.length
  const fieldsets = Array.from(root.querySelectorAll<HTMLElement>(".casebrowser-facet"))

  // map: dataset attribute (e.g. "roles" => row.dataset.roles) -> Set of checked values
  const apply = () => {
    const q = (search?.value ?? "").trim().toLowerCase()
    const activeGroups: { attr: string; checked: Set<string> }[] = []
    for (const fs of fieldsets) {
      const attr = fs.dataset.facetAttr ?? ""
      const checked = new Set<string>()
      fs.querySelectorAll<HTMLInputElement>('input[type="checkbox"]:checked').forEach((cb) =>
        checked.add(cb.value),
      )
      if (checked.size > 0) activeGroups.push({ attr, checked })
    }

    let visible = 0
    for (const card of cards) {
      let show = true
      if (q && !(card.dataset.title ?? "").includes(q)) show = false
      if (show) {
        for (const g of activeGroups) {
          const datasetKey = g.attr.replace(/-([a-z])/g, (_, c) => c.toUpperCase()) // court-level -> courtLevel
          const have = (card.dataset[datasetKey] ?? "").split(" ").filter(Boolean)
          const intersects = have.some((v) => g.checked.has(v))
          if (!intersects) {
            show = false
            break
          }
        }
      }
      card.style.display = show ? "" : "none"
      if (show) visible++
    }
    if (countEl) {
      countEl.textContent = visible === total ? `${total} cases` : `${visible} / ${total} cases`
    }
  }

  search?.addEventListener("input", apply)
  const checkboxes = Array.from(root.querySelectorAll<HTMLInputElement>('input[type="checkbox"]'))
  checkboxes.forEach((cb) => cb.addEventListener("change", apply))
  window.addCleanup(() => {
    search?.removeEventListener("input", apply)
    checkboxes.forEach((cb) => cb.removeEventListener("change", apply))
  })
}

document.addEventListener("nav", () => {
  const root = document.querySelector<HTMLElement>(".casebrowser")
  if (root) setup(root)
})
