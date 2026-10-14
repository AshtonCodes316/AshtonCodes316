"""Reproducible fictional scenario coverage report; no external integrations."""
import json
from itertools import product
from simulator import Request, evaluate

def build_report():
    cases = []
    for consent, approved, healthy, attempts in product((False, True), (False, True), (False, True), (0, 1, 2)):
        request = Request("FICTIONAL-MATRIX", approved, consent, healthy, attempts)
        receipt = evaluate(request)
        cases.append({"consent": consent, "approved": approved, "healthy": healthy,
                      "attempts": attempts, "status": receipt["evidence"]["status"],
                      "external_calls": receipt["evidence"]["external_calls"]})
    counts = {}
    for case in cases:
        counts[case["status"]] = counts.get(case["status"], 0) + 1
    return {"scenario_count": len(cases), "outcomes": dict(sorted(counts.items())),
            "external_calls": sum(case["external_calls"] for case in cases), "cases": cases}

if __name__ == "__main__":
    print(json.dumps(build_report(), indent=2))
