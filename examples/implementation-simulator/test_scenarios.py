import unittest
from scenarios import build_report

class ScenarioMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_exhaustive_boolean_and_attempt_matrix(self):
        self.assertEqual(self.report["scenario_count"], 24)
        self.assertEqual(len(self.report["cases"]), 24)

    def test_all_expected_states_reachable(self):
        self.assertEqual(set(self.report["outcomes"]), {
            "BLOCKED_CONSENT", "BLOCKED_APPROVAL", "RETRY_PENDING",
            "ESCALATED", "SIMULATED_COMPLETE"})

    def test_expected_distribution(self):
        self.assertEqual(self.report["outcomes"], {
            "BLOCKED_CONSENT": 12, "BLOCKED_APPROVAL": 6,
            "RETRY_PENDING": 2, "ESCALATED": 1, "SIMULATED_COMPLETE": 3})

    def test_no_external_calls_across_matrix(self):
        self.assertEqual(self.report["external_calls"], 0)

    def test_reproducible_report(self):
        self.assertEqual(self.report, build_report())

if __name__ == "__main__":
    unittest.main()
