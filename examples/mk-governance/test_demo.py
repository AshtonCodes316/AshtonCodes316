import unittest
from demo import run_mission

class DemoTests(unittest.TestCase):
    def test_requires_approval(self):
        self.assertEqual(run_mission(False, True)['evidence']['outcome'], 'BLOCKED_APPROVAL')
    def test_no_worker_fails_closed(self):
        self.assertEqual(run_mission(True, False)['evidence']['outcome'], 'BLOCKED_NO_QUALIFIED_WORKER')
    def test_deterministic_receipt(self):
        self.assertEqual(run_mission(True, False)['sha256'], run_mission(True, False)['sha256'])
    def test_never_calls_real_worker(self):
        self.assertFalse(run_mission(True, True)['evidence']['real_worker_called'])

if __name__ == '__main__':
    unittest.main()
