"""Capture genuine rendered screenshots from the checked-out portfolio pages.

No generated mockups, no private data, no external services.
"""
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import json
from urllib.parse import urljoin, urlparse

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1] / "docs"
OUT = Path(__file__).resolve().parents[1] / "browser-evidence"
PUBLIC_PREVIEWS = ROOT / "assets" / "screenshots"
PAGES = {
    "portfolio": "",
    "orchestration-atlas": "orchestration-atlas/",
    "control-room": "control-room/",
    "recruiter-one-pager": "recruiter-one-pager.html",
    "recruiter-case-studies": "recruiter-case-studies.html",
    "automation-lab": "automation-lab/",
    "workflow-studio": "workflow-studio/",
    "implementation-dashboard": "implementation-dashboard/",
    "guided-demo": "guided-demo/",
    "ai-implementation": "ai-implementation/",
    "ai-implementation-careers": "ai-implementation-careers/",
    "automation-operations": "automation-operations/",
    "technical-customer-success": "technical-customer-success/",
}
VIEWPORTS = {"desktop": (1440, 900), "mobile": (390, 844)}

@contextmanager
def local_server():
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    PUBLIC_PREVIEWS.mkdir(parents=True, exist_ok=True)
    report = []
    failures = []
    with local_server() as base, sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            for viewport, (width, height) in VIEWPORTS.items():
                context = browser.new_context(viewport={"width": width, "height": height},
                                              device_scale_factor=1, reduced_motion="reduce")
                for name, route in PAGES.items():
                    page = context.new_page()
                    errors = []
                    page.on("pageerror", lambda exc: errors.append(str(exc)))
                    response = page.goto(base + route, wait_until="networkidle", timeout=20000)
                    if viewport == "desktop" and name != "portfolio":
                        page.screenshot(path=str(PUBLIC_PREVIEWS / f"{name}.png"), full_page=False, animations="disabled")
                    page.screenshot(path=str(OUT / f"{name}-{viewport}.png"), full_page=True,
                                    animations="disabled")
                    if name == "orchestration-atlas":
                        nodes = page.locator(".node")
                        assert nodes.count() == 6, "Atlas must have six stages"
                        nodes.nth(3).click()
                        assert page.locator("#detail-title").inner_text() == "Approval", "Atlas stage interaction failed"
                        assert nodes.nth(3).get_attribute("aria-pressed") == "true", "Atlas selection state failed"
                    if name == "control-room":
                        page.locator("#next").click()
                        page.locator("#next").click()
                        page.locator("#next").click()
                        page.locator("#next").click()
                        assert page.locator("#approve").is_enabled(), "Approval gate must activate"
                        assert page.locator("#next").is_disabled(), "Approval gate must block progression"
                        page.locator("#reject").click()
                        page.locator("#next").click()
                        page.locator("#next").click()
                        assert "REJECTION" in page.locator("#status").inner_text(), "Rejected scenario must fail closed"
                        assert page.locator("#export").is_enabled(), "Evidence export must be available"
                    if name == "portfolio":
                        assert page.locator("#hire").count() == 1, "Recruiter conversion section missing"
                        assert page.locator('a[href="recruiter-case-studies.html"]').count() >= 1, "Case study hub link missing"
                    if name == "recruiter-one-pager":
                        assert page.locator("h1").inner_text() == "Ashton Simmons", "One-pager heading missing"
                        assert page.locator('a[href="control-room/"]').count() == 1, "Featured project link missing"
                    if name == "recruiter-case-studies":
                        assert page.locator("section.card").count() == 4, "Expected four case studies"
                        assert page.locator('a[href="control-room/"]').count() >= 1, "Control Room proof missing"
                    if name == "guided-demo":
                        assert page.locator("#tour-heading").count() == 1, "Guided demo heading missing"
                        assert page.locator(".dot").count() == 6, "Six tour chapters required"
                        page.locator("#next").click()
                        assert "02 / 06" in page.locator("#number").inner_text(), "Next chapter did not advance"
                        page.locator("#prev").click()
                        assert "01 / 06" in page.locator("#number").inner_text(), "Previous chapter did not return"
                        page.locator("#restart").click()
                        assert page.locator("#prev").is_disabled(), "Restart did not reset state"
                        for _ in range(5):
                            page.locator("#next").click()
                        assert page.locator("#next").is_disabled(), "Tour should stop at chapter six"
                        assert page.locator("#status").inner_text().startswith("Chapter 6 of 6"), "Final status missing"
                    if name == "ai-implementation":
                        assert page.locator("[data-step]").count() == 5, "Five architecture stages required"
                        page.locator('[data-step="4"]').click()
                        assert page.locator('[data-step="4"]').get_attribute("aria-pressed") == "true", "Architecture selection failed"
                        assert "Human quality evaluation" in page.locator("#detail-title").inner_text(), "Quality explanation missing"
                    if name in {"ai-implementation-careers", "automation-operations", "technical-customer-success"}:
                        assert page.locator("h1").count() == 1, "Recruiter page must have one main heading"
                        assert page.locator('a[href="../guided-demo/"]').count() >= 1, "Guided demo entry missing"
                    for href in page.locator("a[href]").evaluate_all(
                        "(anchors) => anchors.map(a => a.getAttribute('href'))"
                    ):
                        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
                            continue
                        target = urljoin(page.url, href)
                        if urlparse(target).netloc != urlparse(base).netloc:
                            continue
                        linked = page.request.get(target.split("#", 1)[0], timeout=10000)
                        if linked.status >= 400:
                            failures.append({"page": name, "viewport": viewport,
                                             "broken_link": href, "http_status": linked.status})
                    geometry = page.evaluate("""() => ({
                      scrollWidth: document.documentElement.scrollWidth,
                      clientWidth: document.documentElement.clientWidth,
                      title: document.title,
                      h1: document.querySelector('h1')?.innerText || ''
                    })""")
                    item = {"page": name, "viewport": viewport,
                            "http_status": response.status if response else None,
                            **geometry, "javascript_errors": errors}
                    report.append(item)
                    if item["http_status"] != 200 or item["scrollWidth"] > item["clientWidth"] + 2 or errors:
                        failures.append(item)
                    page.close()
                context.close()
        finally:
            browser.close()
    (OUT / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"screenshots": len(report), "failures": failures}, indent=2))
    if failures:
        raise SystemExit("Browser QA found a page error or horizontal overflow")

if __name__ == "__main__":
    main()
