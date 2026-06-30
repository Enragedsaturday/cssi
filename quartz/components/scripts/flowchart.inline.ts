// S3 · R4 #4 — DoctrineFlowchart client enhancement.
// Makes mermaid-rendered nodes that carry a `click <node> "<url>"` directive behave as
// SPA-safe, popover-aware deep-links. Mermaid emits SVG <a> elements; Quartz's SPA
// router ignores them (it reads `a.href`, an SVGAnimatedString for SVG <a>), so without
// this they trigger a full page reload. This routes internal links through
// `window.spaNavigate`. Degraded form: the static mermaid diagram (links still work via
// full page load); with JS off, the portable ```mermaid``` fence stays legible.

function getAnchorHref(a: Element): string | null {
  // SVG <a> exposes href as SVGAnimatedString; also support xlink:href / plain href
  const svgHref = (a as unknown as { href?: { baseVal?: string } }).href?.baseVal
  return (
    svgHref ||
    a.getAttribute("xlink:href") ||
    a.getAttribute("href") ||
    null
  )
}

function isInternal(href: string): boolean {
  try {
    const url = new URL(href, location.href)
    return url.origin === location.origin
  } catch {
    return false
  }
}

function wireAnchor(a: Element) {
  if ((a as HTMLElement).dataset?.flowchartWired) return
  ;(a as HTMLElement).dataset.flowchartWired = "true"
  a.classList.add("flowchart-node-link")
  const href = getAnchorHref(a)
  if (!href || !isInternal(href)) return

  const handler = (e: Event) => {
    const me = e as MouseEvent
    if (me.ctrlKey || me.metaKey) return // let the browser open in a new tab
    const target = (a as Element).getAttribute("target")
    if (target === "_blank") return
    e.preventDefault()
    const url = new URL(href, location.href)
    if (typeof window.spaNavigate === "function") {
      window.spaNavigate(url)
    } else {
      location.assign(url.toString())
    }
  }
  a.addEventListener("click", handler)
  window.addCleanup(() => a.removeEventListener("click", handler))
}

function scan(root: ParentNode) {
  // mermaid wraps clickable nodes in SVG <a>; also tag generic clickable nodes
  root.querySelectorAll("code.mermaid svg a").forEach(wireAnchor)
  root
    .querySelectorAll("code.mermaid svg .clickable, code.mermaid svg .node.clickable")
    .forEach((n) => n.classList.add("flowchart-clickable"))
}

document.addEventListener("nav", () => {
  const center = document.querySelector(".center")
  if (!center) return

  // mermaid renders asynchronously (CDN import), so watch for SVGs being added.
  scan(center)
  const observer = new MutationObserver((mutations) => {
    for (const m of mutations) {
      if (m.addedNodes.length > 0) {
        scan(center)
      }
    }
  })
  observer.observe(center, { childList: true, subtree: true })
  window.addCleanup(() => observer.disconnect())
})
