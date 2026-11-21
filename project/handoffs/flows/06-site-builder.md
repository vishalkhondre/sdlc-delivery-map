# Reading the six flows

Open the Flows section of the tour at tour.html#flows. Its six links follow inventory order. The reading-order links continue between consecutive flows. Each lesson returns the reader to each map step it touches, and each corresponding overview links back to the flow. There are 49 links in each direction.

The static release candidate builds 86 lessons and four navigation pages. The link validator includes the Jira status search probe. Browser checks use keyboard navigation through the tour and verify the six pages and their links at phone width. The same job also runs the rendered SVG text-clearance checks. The build excludes Python bytecode caches from its public assets and offline preview.

Local source, build, link, unit and reciprocal-link checks passed. Local Chromium exited during startup with a socket permission error. See the pull request's GitHub Actions run for its browser check and generated preview artifact.
