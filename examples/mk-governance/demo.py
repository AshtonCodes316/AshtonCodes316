"""Public standalone MK-inspired governance demo; not the private MK runtime."""
import hashlib
import json


def run_mission(approved: bool, worker_available: bool) -> dict:
    mission = {'id': 'PUBLIC-DEMO-001', 'task': 'Classify fictional support request', 'approved': approved}
    if not approved:
        outcome = 'BLOCKED_APPROVAL'
    elif not worker_available:
        outcome = 'BLOCKED_NO_QUALIFIED_WORKER'
    else:
        outcome = 'READY_FOR_DISPATCH'
    evidence = {'mission': mission, 'outcome': outcome, 'real_worker_called': False}
    digest = hashlib.sha256(json.dumps(evidence, sort_keys=True).encode()).hexdigest()
    return {'evidence': evidence, 'sha256': digest}


if __name__ == '__main__':
    print(json.dumps(run_mission(approved=True, worker_available=False), indent=2))
