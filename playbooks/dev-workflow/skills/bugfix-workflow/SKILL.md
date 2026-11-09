---
name: bugfix-workflow
description: Run a bug fix end to end in one session — orchestrate debugger, implementer, reviewer and verifier subagents with human gates. Use when the user runs /dev:bugfix-workflow or asks to run the bug-fix workflow for a ticket.
argument-hint: "<JIRA-KEY | task-key | description>"
disable-model-invocation: true
---
# Bugfix workflow — orchestrator

You orchestrate; stages run in subagents. Follow the **Orchestration rules** of `/dev:feature-workflow` (same contract, same gates logic), with `workflow: bugfix`.

## Stages
0. **Task** — existing folder or `/dev:new-task` with `type: bug`. Steps / expected / actual from the ticket into `spec.md §AS-IS`.
1. **Diagnose** → `dev:debugger`: reproduce, root cause, other places with the same flaw, failing test committed (no fix).
   **GATE A** — always show: root cause (2 lines), fix options with risk, affected users/data. User picks (default: minimal fix). `needs-input` (can't reproduce) → gate with what is needed.
2. **Fix** → `dev:implementer` with steps: "make `<failing test>` pass with <chosen option>; run related suites; one commit". More than 3 steps or several repos → `dev:planner` first, then implementer per phase.
3. **Review** → `dev:reviewer` (focus: the fix is minimal, no behaviour change outside the bug, test asserts the right thing). Max 2 fix rounds.
4. **Verify** → `dev:verifier` — the original repro steps + regression neighbours. Results into `test-cases.md` (Status + Runs), verdict into `task.md §Verification`; manual cases → QA handoff at GATE C. Note whether stored data needs correction (code fix ≠ data fix) → `/kb:capture` if so.
5. **Finish** — `status: review`, PR description. **GATE C** — external actions only on explicit OK. Next = "comments → `/dev:pr-comments`; merged → `/dev:close-task`". `/dev:handoff`.
