import hashlib
import json
import unittest

from demo import run_mission


class DemoTests(unittest.TestCase):
    def test_requires_approval(self):
        self.assertEqual(run_mission(False, True)["evidence"]["outcome"], "BLOCKED_APPROVAL")

    def test_no_worker_fails_closed(self):
        self.assertEqual(run_mission(True, False)["evidence"]["outcome"], "BLOCKED_NO_QUALIFIED_WORKER")

    def test_approved_worker_is_only_ready_not_dispatched(self):
        receipt = run_mission(True, True)
        self.assertEqual(receipt["evidence"]["outcome"], "READY_FOR_DISPATCH")
        self.assertFalse(receipt["evidence"]["real_worker_called"])

    def test_denial_precedes_worker_availability(self):
        self.assertEqual(run_mission(False, False)["evidence"]["outcome"], "BLOCKED_APPROVAL")
        self.assertEqual(run_mission(False, True)["evidence"]["outcome"], "BLOCKED_APPROVAL")

    def test_all_boolean_state_combinations_have_expected_outcomes(self):
        expected = {
            (False, False): "BLOCKED_APPROVAL",
            (False, True): "BLOCKED_APPROVAL",
            (True, False): "BLOCKED_NO_QUALIFIED_WORKER",
            (True, True): "READY_FOR_DISPATCH",
        }
        for (approved, available), outcome in expected.items():
            with self.subTest(approved=approved, worker_available=available):
                self.assertEqual(run_mission(approved, available)["evidence"]["outcome"], outcome)

    def test_deterministic_receipt(self):
        self.assertEqual(run_mission(True, False)["sha256"], run_mission(True, False)["sha256"])

    def test_receipt_hash_matches_canonical_evidence(self):
        receipt = run_mission(True, False)
        canonical = json.dumps(receipt["evidence"], sort_keys=True).encode()
        self.assertEqual(receipt["sha256"], hashlib.sha256(canonical).hexdigest())

    def test_distinct_decisions_have_distinct_receipts(self):
        self.assertNotEqual(run_mission(False, True)["sha256"], run_mission(True, True)["sha256"])

    def test_no_real_worker_called_in_any_scenario(self):
        for approved in (False, True):
            for available in (False, True):
                with self.subTest(approved=approved, worker_available=available):
                    self.assertIs(run_mission(approved, available)["evidence"]["real_worker_called"], False)

    def test_demo_uses_fictional_fixed_mission(self):
        receipt = run_mission(True, False)
        self.assertEqual(receipt["evidence"]["mission"]["id"], "PUBLIC-DEMO-001")
        self.assertEqual(receipt["evidence"]["mission"]["task"], "Classify fictional support request")


if __name__ == "__main__":
    unittest.main()
