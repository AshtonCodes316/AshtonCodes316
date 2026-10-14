"""Capture genuine rendered screenshots from the checked-out portfolio pages.

No generated mockups, no private data, no external services.
"""
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import json

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1] / "docs"
OUT = Path(__file__).resolve().parents[1] / "browser-evidence"\nPUBLIC_PREVIEWS = ROOT / "assets" / "screenshots"
PAGES = {
    "portfolio": "",
    "automation-lab": "automation-lab/",
    "workflow-studio": "workflow-studio/",
    "implementation-dashboard": "implementation-dashboard/",
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
    OUT.mkdir(parents=True, exist_ok=True)\n    PUBLIC_PREVIEWS.mkdir(parents=True, exist_ok=True)
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
                    if viewport == "desktop" and name != "portfolio":\n                        page.screenshot(path=str(PUBLIC_PREVIEWS / f"{name}.png"), full_page=False, animations="disabled")\n                    page.screenshot(path=str(OUT / f"{name}-{viewport}.png"), full_page=True,
                                    animations="disabled")
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
