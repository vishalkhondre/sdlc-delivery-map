# Field guide integration check

From the repository root, run this after generating the site. Python, ReportLab, pypdf, PyYAML and Inkscape are required. The preview contains the checked-out lessons and carries “Integration preview” on the cover, in the document metadata and on every page.

```sh
python scripts/field_guide_pdf.py --preview SDLC-Field-Guide-Integration.pdf
```

## Results

The build produced 264 A4 pages. The linked index and the 99 PDF bookmarks each resolve to the matching lesson title: 53 overviews, 40 deep dives and six flows. The lesson text includes its responsible role, inputs, steps, worked example, failure path, measurement and source links. Deep dives and flows also carry their detail blocks, and related lessons link within the PDF. All 228 internal link annotations resolved to pages in the guide.

Compared the PDF with the lesson JSON for every detail heading, 169 captions, 66 tables and their headers, all 16 instructional figure placements and their text equivalents, and 357 source citations. The cover also includes the delivery map. The evidence and outcome-analysis lessons each link to the original worked-data CSV and JSON. Preview links use the public integration branch, independently of the CI synthetic merge ref. These two source files match that branch byte for byte. Branch URLs may change after later merges or stop resolving if the branch is deleted. The PDF also embeds the exact CSV and JSON from its build as attachments, allowing offline acquisition. The tagged guide uses its release tag for online links. Cover credits identify Vishal Khondre, link the CC BY 4.0 educational license, identify the MIT tooling license and link the upstream AI SDLC Map.

Rendered the cover, index, six changed overviews and samples from the deep dives and flows. The figure/table pages in the final preview are Hold (22), Policy (27), Measure (38), Environments (56), Handoffs (62) and Evidence record (68). The new cohort bars and 50% marker, four arrow styles, two decision tables and both reused figures fit their pages. Also inspected the CI figure (71), hotfix figure (222), outcome-analysis example (226) and traceability flow (262). A text-and-image bounding-box pass across all 264 pages found no block outside the page margins. All four worked-data link annotations and the displayed credits were checked in the built file. After the final wording pass, verified every source title and both revised evidence-record passages in extracted text. Extracted both PDF attachments and compared their bytes with the checkout and integration base. Revalidated bookmarks, linked index and PDF geometry after embedding.

Exercised the existing tagged CLI locally with the value of content/VERSION and checked that a different tag still fails before output. The integration artifact uses the preview CLI. No tag, edition bump, or release binding was created.
