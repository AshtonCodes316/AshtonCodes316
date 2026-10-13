# Master Key — Live Demo Recording Kit

**A genuine, reproducible screen-recording plan for a public standalone example.**

> This is a demonstration of a small **MK-inspired governance example**, **not** a live run of the private Master Key system. No AI provider or worker is contacted.

## 1. Open Windows Command Prompt

In a **separate clone of the public portfolio repository**, navigate to:

```cmd
cd examples\mk-governance
```

If you are viewing the files on GitHub instead, download or clone the public portfolio repository first. Do **not** use your private MK development checkout for this recording.

## 2. Run the real example on camera

```cmd
python demo.py
```

The script uses fictional data and returns a JSON object with a mission, a decision, `real_worker_called: false`, and a SHA-256 digest. With its current default inputs (`approved=True`, `worker_available=False`), the decision should be `BLOCKED_NO_QUALIFIED_WORKER`. Capture the **actual** output, not a mock terminal.

## 3. Show the tests

```cmd
python -m unittest -v
```

Capture the actual test summary. A previous local verification reported four passing tests; the current recording should show its own result. Do not reuse an old test result as if it came from the new run.

## 4. Explain the two important boundaries

1. **Human approval:** If approval is absent, the example blocks the mission.
2. **Worker qualification:** If no worker is available, it blocks dispatch even when the mission is approved.

The SHA-256 digest identifies the serialized receipt; it is **not** a digital signature or proof of real-world task completion.

## 5. Record a 60–90-second narration

> “This is a public, standalone example inspired by my Master Key project. It demonstrates a basic governance decision: a mission needs approval, and an unavailable worker must not be treated as callable. Here, the mission is approved but no qualified worker is available, so the result is blocked. The script records a deterministic receipt, and these local tests check the example's behavior. This is not a live autonomous AI workforce. The full Master Key project remains private and under development. My focus is making automation understandable, controllable, and verifiable.”

## 6. Publication gate

Before posting a video, review the screen recording for credentials, usernames, local file paths, notifications, and other private data. Do not claim that the public example proves the private system's security or deployment readiness. Publish only after reviewing the actual footage.

## References

- [Runnable public example](../examples/mk-governance/README.md)
- [Engineering case study](mk-engineering-case-study.md)
- [Architecture illustration](mk-architecture.md)
- [Original 90-second storyboard](mk-demo-storyboard.md)
