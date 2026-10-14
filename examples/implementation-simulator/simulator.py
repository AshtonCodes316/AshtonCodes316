"""Deterministic fictional customer onboarding workflow; no real integrations."""
from dataclasses import dataclass, asdict
import hashlib
import json

@dataclass(frozen=True)
class Request:
    ticket_id: str
    approved: bool
    consent: bool
    integration_healthy: bool
    attempts: int = 0

def evaluate(request: Request) -> dict:
    if not request.ticket_id.strip():
        raise ValueError("ticket_id is required")
    if request.attempts < 0:
        raise ValueError("attempts must be nonnegative")
    if not request.consent:
        status, next_action = "BLOCKED_CONSENT", "request_consent"
    elif not request.approved:
        status, next_action = "BLOCKED_APPROVAL", "request_approval"
    elif not request.integration_healthy and request.attempts < 2:
        status, next_action = "RETRY_PENDING", "retry_after_review"
    elif not request.integration_healthy:
        status, next_action = "ESCALATED", "human_investigation"
    else:
        status, next_action = "SIMULATED_COMPLETE", "review_receipt"
    evidence = {"request": asdict(request), "status": status,
                "next_action": next_action, "external_calls": 0, "real_customer_data": False}
    digest = hashlib.sha256(json.dumps(evidence, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {"evidence": evidence, "sha256": digest}

if __name__ == "__main__":
    print(json.dumps(evaluate(Request("FICTIONAL-001", True, True, False)), indent=2))
