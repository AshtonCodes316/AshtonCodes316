import hashlib
import json
import unittest
from simulator import Request, evaluate

class ImplementationTests(unittest.TestCase):
    def request(self, **overrides):
        data = dict(ticket_id="FICTIONAL-001", approved=True, consent=True, integration_healthy=True)
        data.update(overrides)
        return Request(**data)

    def test_success_is_simulated(self):
        self.assertEqual(evaluate(self.request())["evidence"]["status"], "SIMULATED_COMPLETE")

    def test_missing_consent_blocks(self):
        self.assertEqual(evaluate(self.request(consent=False))["evidence"]["status"], "BLOCKED_CONSENT")

    def test_missing_approval_blocks(self):
        self.assertEqual(evaluate(self.request(approved=False))["evidence"]["status"], "BLOCKED_APPROVAL")

    def test_consent_precedes_approval(self):
        self.assertEqual(evaluate(self.request(consent=False, approved=False))["evidence"]["status"], "BLOCKED_CONSENT")

    def test_unhealthy_integration_retries(self):
        self.assertEqual(evaluate(self.request(integration_healthy=False))["evidence"]["status"], "RETRY_PENDING")

    def test_retry_limit_escalates(self):
        self.assertEqual(evaluate(self.request(integration_healthy=False, attempts=2))["evidence"]["status"], "ESCALATED")

    def test_no_external_calls(self):
        for healthy in (True, False):
            self.assertEqual(evaluate(self.request(integration_healthy=healthy))["evidence"]["external_calls"], 0)

    def test_deterministic_receipt(self):
        req = self.request()
        self.assertEqual(evaluate(req), evaluate(req))

    def test_receipt_integrity(self):
        result = evaluate(self.request())
        payload = json.dumps(result["evidence"], sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(result["sha256"], hashlib.sha256(payload).hexdigest())

    def test_invalid_ticket_rejected(self):
        with self.assertRaises(ValueError):
            evaluate(self.request(ticket_id=" "))

    def test_negative_attempts_rejected(self):
        with self.assertRaises(ValueError):
            evaluate(self.request(attempts=-1))

    def test_no_customer_data_claim(self):
        self.assertIs(evaluate(self.request())["evidence"]["real_customer_data"], False)

if __name__ == "__main__":
    unittest.main()
