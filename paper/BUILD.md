# Building the paper

From this directory, using a local LaTeX installation and BibTeX:

```bash
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
bibtex cf_bridge_relation_atlas
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
```

The output is `cf_bridge_relation_atlas.pdf`. A valid final log has no errors,
undefined references or citations, or overfull boxes. Inspect every rendered
page, including tables and bibliography. Repeat the suite and this build from
a clean export of the same candidate before distributing the revision.

For an offline MiKTeX build, add `-disable-installer -disable-write18
-dont-parse-first-line` to each pdflatex invocation and `-disable-installer`
to BibTeX. Missing packages then cause an explicit failure rather than a download.
Local update reminders are separate from the compilation result.

The older sixteen-page build and June2026 export notes belong to the antecedent
package. They are not evidence that the October candidate was built.

The October 10, 2026 candidate was built with the four commands above in offline
MiKTeX mode: 16 pages, no undefined references or citations, no overfull boxes,
and no LaTeX errors. Every rendered page was inspected. The intentionally
disabled shell escape produces an epstopdf warning; the paper uses no EPS asset.
