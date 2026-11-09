---
name: fix-bug
description: Fix a bug — reproduce, find the root cause, write a failing test, apply the minimal fix, verify. Use for bug tickets, regressions, "this doesn't work", or a bug found while working on another task.
argument-hint: "[task-key]"
---
# Fix a bug

1. Read `task.md`, `spec.md`. Steps / expected / actual → `spec.md §AS-IS` if missing.
2. **Reproduce** — test, script, API call or read-only query. Can't → stop, record what you tried and what data you need, ask.
3. **Root cause** — trace to `file:line`; mechanism in ≤10 lines in §AS-IS. Separate cause from symptom. Grep for the same flaw elsewhere; list it (in scope or `/kb:capture`).
4. **Failing test** encoding the bug; confirm it fails for the right reason. Commit it alone: `<KEY>: failing test for <summary>`. Record it as `TC-01` in `test-cases.md` (regression candidate) with the original repro steps for manual QA.
5. **Minimal fix** — change the code, never the step-4 test (review blocks any edit to it). Refactoring ideas → `/kb:capture`.
6. Test green + related suites green. Commit `<KEY>: fix <summary>`.
7. >3 steps → write them in `plan.md`; otherwise a checklist in `task.md` is enough.
8. `task.md §Verification`: how to check manually, which data/users. Note whether stored data needs correction (code fix ≠ data fix).
9. `status: review`; suggest `/dev:verify` in a fresh session.
