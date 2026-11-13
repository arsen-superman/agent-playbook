---
name: implement
description: Execute an approved plan.md step by step in the code repositories — change, verify, commit, tick. Use when the user says implement, continue, do the next step, or "go" on a planned task.
argument-hint: "[task-key] [all | phase N]"
---
# Implement the plan (developer)

Read `task.md`, `plan.md`, and only the spec sections the current step references. Build/test commands: project CLAUDE.md; code conventions: the repo's own CLAUDE.md, editorconfig, surrounding code.

Default scope: one phase, then report. `all` → until done or blocked.

Per step:
1. Make the change — nothing beyond the step. Before writing a helper, check or service, grep for an existing one and use it (the plan's Placement names what to reuse).
2. Run the step's verify check (build + relevant tests at minimum). A new or changed test: check once that it fails when the behaviour it guards is broken (temporary change; revert it before committing).
3. Commit in that repo: English, `<KEY>: <imperative summary>`.
4. Step automated test cases → fill `Automated by` (test name) for those TC IDs in `test-cases.md`. Step names F-IDs → remove each row's problem, not only apply its suggested fix, then set its Status in `review.md` to `fixed <hash>`; problem remains → don't tick, stop and report (below).
5. Tick: `- [x] … (abc1234)`; update `**Next:**`. Done differently from the step text (other files, other approach) → rewrite the step to what was done and add `(changed: <why>)`, in the same commit as the code.
6. Noticed something else → `/kb:capture`, keep going.

Stop and report when: a check fails after two different fix attempts; the plan contradicts the code; a step needs a decision not in the spec. Write it in `task.md §Open questions`, `status: blocked`. Small reordering or a changed step is fine (noted as in 5); bigger plan changes need OK. Bug task: never edit the `<KEY>: failing test for …` test — fix the code.

Done → `status: review`; draft the PR description (What / Why / How tested / Risks / ticket link) in the reply. Never push or open a PR without explicit OK. Suggest `/dev:verify` in a fresh session.
