# Actual GitHub mathematics checks

The [read-only Actions job](../../.github/workflows/hosted-math.yml) checks the published pull-request head. It inventories every tracked Markdown page at that exact Git commit, visits the real commit-pinned GitHub pages in an anonymous browser, and compares each rendered MathML expression with the source. It uses viewport widths of 1440 and 760 pixels. The workflow has only `contents: read`, does not persist checkout credentials, and uses no repository secrets.

The capture includes source hashes, accessible mathematical text and structure, equation labels, bounded display geometry, page HTML and screenshots. The contract adds explicit content checks for headline expressions. A passing automated comparison still requires separate inspection of the actual screenshots and the non-mathematical navigation. It does not prove the science or certify every browser.

## Reproduce on a permitted browser host

Use Node 18 or later, Python 3.10 or later, Git, Playwright 1.56.1 and MathJax Full 3.2.1. Install the two Node packages and Chromium in a separate dependency directory. Set `NODE_PATH` to that directory's `node_modules`, then run:

```bash
node verification/hosted/capture_hosted_math.cjs \
  --root /absolute/path/to/checkout \
  --repository GoGoKo699/Quantum-Repeater-Memory-Limits \
  --revision FULL_COMMIT_SHA \
  --contract verification/hosted/math-contract.json \
  --output /absolute/path/to/new-empty-evidence-directory
```

The revision must exist in the local Git database and be published on GitHub. Use a new output directory for each attempt. A failed capture is retained as failed evidence; a source-only compiler check cannot replace it. An inaccessible hosting route must be reported as such.

The generic collector and mathematical-text checker are copied unchanged from the same tested verification-tool release, 0.13.0. Their SHA256 values are:

| File | SHA256 |
| --- | --- |
| `capture_hosted_math.cjs` | `49182eaf354e86f685a4976814d672de5d7329a2d9e42f62a5227e2bc07c2d18` |
| `check_rendered_math.py` | `edbc2d72af94e96b78166d74b66fcea150134f2f3ebaaea121e9057768e1dbfe` |

The CI artifact contains `hosted-report.json` and the files it identifies. It is a temporary diagnostic artifact, subject to its stated retention period. A report certifies only the recorded commit, page scope and observation time; later source or hosting changes require a new capture.

[Return to the numerical verification guide](../README.md).
