"""Automated axe-core WCAG audit of selected public portfolio pages.

Runs against a local HTTP server; no private MK runtime or external customer data.
Reports violations without claiming full WCAG conformance.
"""
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import json

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1] / "docs"
OUT = Path(__file__).resolve().parents[1] / "browser-evidence"
AXE = Path(__file__).resolve().parents[1] / "scripts" / "vendor" / "axe.min.js"
PAGES = {
    "portfolio": "",
    "guided-demo": "guided-demo/",
    "ai-implementation": "ai-implementation/",
    "ai-implementation-careers": "ai-implementation-careers/",
    "automation-operations": "automation-operations/",
    "technical-customer-success": "technical-customer-success/",
    "recruiter-case-studies": "recruiter-case-studies.html",
}
VIEWPORTS = {"desktop": (1440, 900), "mobile": (390, 844)}

@contextmanager
def server():
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    http = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = Thread(target=http.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{http.server_port}/"
    finally:
        http.shutdown()
        http.server_close()
        thread.join(timeout=3)

def main():
    if not AXE.is_file():
        raise SystemExit("Missing vendored axe.min.js; install it in the CI setup step")
    OUT.mkdir(parents=True, exist_ok=True)
    report = []
    with server() as base, sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            for viewport, (width, height) in VIEWPORTS.items():
                context = browser.new_context(viewport={"width": width, "height": height},
                                              reduced_motion="reduce")
                for name, route in PAGES.items():
                    page = context.new_page()
                    response = page.goto(base + route, wait_until="networkidle")
                    if not response or response.status != 200:
                        raise RuntimeError(f"{name}: HTTP status not 200")
                    page.add_script_tag(path=str(AXE))
                    result = page.evaluate("""async () => {
                      const data = await axe.run(document, {
                        runOnly: {type: 'tag', values: ['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']},
                        resultTypes: ['violations','incomplete']
                      });
                      return {
                        violations: data.violations.map(v => ({
                          id:v.id, impact:v.impact, description:v.description,
                          help:v.help, nodes:v.nodes.map(n=>({target:n.target,
                            failureSummary:n.failureSummary}))
                        })),
                        incomplete: data.incomplete.map(v=>({
                          id:v.id, impact:v.impact, count:v.nodes.length
                        }))
                      };
                    }""")
                    report.append({"page": name, "viewport": viewport, **result})
                    page.close()
                context.close()
        finally:
            browser.close()
    path = OUT / "axe-accessibility-report.json"
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    violations = [(r["page"], r["viewport"], v["id"], len(v["nodes"]))
                  for r in report for v in r["violations"]]
    print(json.dumps({"audited": len(report), "violations": violations,
                      "manual_review_needed": sum(len(r["incomplete"]) for r in report)}, indent=2))
    if violations:
        raise SystemExit("Automated WCAG-tagged axe checks found violations; see report artifact")

if __name__ == "__main__":
    main()
