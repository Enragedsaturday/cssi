import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// Category-grouped left nav (S3 · R2/R3). Renders S2's 12 book-spine categories
// from the numbered content/ folders, with the warrant-exceptions cluster (#7) as
// the single 3-level branch (7a/7b) and a segregated, collapsed `Cases` node
// (S4 · R5/§9). The default numeric `sortFn` already collates 1,2,…,9,10,11,12 and
// sorts the lettered `cases` node after the numbered categories, so it is kept as-is.
//
// `mapFn` MUST be closure-free: Quartz serializes it with `.toString()` and
// re-evaluates it client-side, so it cannot reference any outer-scope variable —
// the slug→display-name table is declared INSIDE the function body.
const categoryExplorer = Component.Explorer({
  folderDefaultState: "collapsed",
  folderClickBehavior: "link",
  useSavedState: true,
  mapFn: (node) => {
    const displayNames: Record<string, string> = {
      "1-foundations-history": "1 · Foundations & History",
      "2-legal-system-research": "2 · Legal System, Research & Reference",
      "3-what-is-a-search": "3 · What Is a Search?",
      "4-what-is-a-seizure": "4 · What Is a Seizure?",
      "5-levels-of-suspicion": "5 · Levels of Suspicion",
      "6-warrant-requirement": "6 · The Warrant Requirement",
      "7-exceptions-warrant": "7 · Exceptions to the Warrant Requirement",
      "7a-pc-needed": "7a · Probable-Cause Exceptions",
      "7b-pc-not-needed": "7b · Suspicion-Based / Per-Se Exceptions",
      "8-exclusionary-rule-remedies": "8 · The Exclusionary Rule, Standing & Remedies",
      "9-confessions-interrogation": "9 · Confessions, Interrogation & Identifications",
      "10-use-of-force-liability": "10 · Use of Force, Liability & Disclosure",
      "11-adjacent-doctrines": "11 · Adjacent Doctrines",
      "12-instructor-craft-study": "12 · Instructor Craft & Study",
      cases: "Cases",
    }
    if (node.isFolder) {
      const mapped = displayNames[node.slugSegment]
      if (mapped) {
        node.displayName = mapped
      }
    }
  },
})

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/jackyzha0/quartz",
      "Discord Community": "https://discord.gg/cRFFHYye7t",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    categoryExplorer,
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    categoryExplorer,
  ],
  right: [],
}
