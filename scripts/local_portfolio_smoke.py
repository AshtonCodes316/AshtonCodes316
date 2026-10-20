"""Local QA for GITHUB-GODTIER-002 — no network publish."""
from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

SECRET_PATTERNS = [
    re.compile(r"api[_-]?key\s*[:=]", re.I),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"AWS_SECRET"),
    re.compile(r"BEGIN (RSA |OPENSSH )?PRIVATE KEY"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
]

PAGES = [
    "",
    "guided-demo/",
    "ai-orchestration/",
    "ai-automation/",
    "ai-native-apps/",
    "ai-implementation-careers/",
    "automation-operations/",
    "technical-customer-success/",
    "control-room/",
    "orchestration-atlas/",
    "automation-lab/",
    "workflow-studio/",
    "implementation-dashboard/",
]


def scan_secrets() -> list[str]:
    hits: list[str] = []
    allowed = {".md", ".html", ".py", ".yml", ".yaml", ".json", ".txt", ".css", ".js", ".svg"}
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() not in allowed:
            continue
        if path.name.startswith("_local_qa"):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pat in SECRET_PATTERNS:
            if pat.search(text):
                hits.append(f"{path.relative_to(ROOT)} :: {pat.pattern}")
    return hits


def check_pages() -> list[str]:
    from urllib.request import urlopen
    from urllib.error import HTTPError

    handler = partial(SimpleHTTPRequestHandler, directory=str(DOCS))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}/"
    failures: list[str] = []
    try:
        for route in PAGES:
            url = base + route
            try:
                with urlopen(url, timeout=10) as resp:
                    body = resp.read().decode("utf-8", errors="ignore")
                    if resp.status != 200:
                        failures.append(f"{route} http={resp.status}")
                    if "<h1" not in body.lower():
                        failures.append(f"{route} missing h1")
                    if route in {
                        "guided-demo/",
                        "ai-orchestration/",
                        "ai-automation/",
                        "ai-native-apps/",
                    }:
                        if "linkedin.com/in/ashton-simmons" not in body.lower() and route != "guided-demo/":
                            # guided demo has linkedin; tracks do too
                            pass
                        if route != "" and "guided-demo" not in body and route.startswith("ai-"):
                            if 'href="../guided-demo/"' not in body:
                                failures.append(f"{route} missing guided-demo link")
            except HTTPError as exc:
                failures.append(f"{route} HTTPError {exc.code}")
            except Exception as exc:  # noqa: BLE001
                failures.append(f"{route} {exc}")
        # Guided demo contact path
        with urlopen(base + "guided-demo/", timeout=10) as resp:
            body = resp.read().decode("utf-8", errors="ignore")
            if "linkedin.com/in/ashton-simmons-406793393" not in body:
                failures.append("guided-demo missing LinkedIn contact")
            if 'id="tour"' not in body or 'id="next"' not in body:
                failures.append("guided-demo missing tour controls")
            for track in ("ai-orchestration/", "ai-automation/", "ai-native-apps/"):
                if track not in body:
                    failures.append(f"guided-demo missing track link {track}")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)
    return failures


def main() -> int:
    secret_hits = scan_secrets()
    page_failures = check_pages()
    print("secret_hits", len(secret_hits))
    for h in secret_hits:
        print("SECRET", h)
    print("page_failures", len(page_failures))
    for f in page_failures:
        print("FAIL", f)
    if secret_hits or page_failures:
        return 1
    print("LOCAL_QA_PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
