---
name: implement
description: Execute an approved plan.md step by step in the code repositories — change, verify, commit, tick. Use when the user says implement, continue, do the next step, or "go" on a planned task.
argument-hint: "[task-key] [all | phase N]"
---
# Implement the plan (developer)

Read `task.md`, `plan.md`, and only the spec sections the current step references. Build/test commands: project CLAUDE.md; code conventions: the repo's own CLAUDE.md, editorconfig, surrounding code.

Default scope: one phase, then report. `all` → until done or blocked.

Per step:
1. Make the change — nothing beyond the step.
2. Run the step's verify check (build + relevant tests at minimum).
3. Commit in that repo: English, `<KEY>: <imperative summary>`.
4. Step automated test cases → fill `Automated by` (test name) for those TC IDs in `test-cases.md`.
5. Tick: `- [x] … (abc1234)`; update `**Next:**`.
6. Noticed something else → `/kb:capture`, keep going.

Stop and report when: a check fails after two different fix attempts; the plan contradicts the code; a step needs a decision not in the spec. Write it in `task.md §Open questions`, `status: blocked`. Small reordering is fine (note it); bigger plan changes need OK.

Done → `status: review`; draft the PR description (What / Why / How tested / Risks / ticket link) in the reply. Never push or open a PR without explicit OK. Suggest `/dev:verify` in a fresh session.
