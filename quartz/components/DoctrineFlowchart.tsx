import { QuartzComponent, QuartzComponentConstructor } from "./types"
import style from "./styles/flowchart.scss"
// @ts-ignore
import script from "./scripts/flowchart.inline"

// S3 · R4 #4 — DoctrineFlowchart.
// A THIN interactive wrapper over an existing Mermaid code block. The source stays a
// portable ```mermaid``` fence (already rendered by Quartz's mermaid.inline). Authors
// add clickable, deep-linking nodes using PORTABLE mermaid `click` syntax, e.g.:
//
//   ```mermaid
//   flowchart TD
//     A[Emergency aid?] -->|yes| B[Warrantless entry OK]
//     click B "../cases/brigham-city-v-stuart#rule" "Brigham City v. Stuart"
//   ```
//
// `click <node> "<url>"` is standard mermaid — no component-only syntax. This wrapper's
// job is to (a) style clickable nodes as deep-links and (b) route internal node links
// through Quartz's SPA navigator (mermaid emits SVG <a> elements the SPA click handler
// does not catch, because it reads `a.href` which is an SVGAnimatedString for SVG <a>).
//
// Degraded state: with this wrapper stripped, mermaid still renders the static diagram;
// with JS fully off, the portable mermaid fence remains legible as a code block.
//
// This component renders nothing itself; it contributes the enhancement script + styles.

export default (() => {
  const DoctrineFlowchart: QuartzComponent = () => null
  DoctrineFlowchart.css = style
  DoctrineFlowchart.afterDOMLoaded = script
  return DoctrineFlowchart
}) satisfies QuartzComponentConstructor
