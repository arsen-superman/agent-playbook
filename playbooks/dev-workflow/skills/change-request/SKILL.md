---
name: change-request
description: "Workflow — bring new requirements or edge cases into a task past the spec stage: record, analyse impact, plan and deliver only the delta. Manual: /dev:change-request KEY, then text, file or url."
argument-hint: "<task-key> <clarification text | file | url>"
disable-model-invocation: true
---
# Change request — orchestrator

You orchestrate; stages run in the same agents as `/dev:feature-workflow` and follow `templates/shared/orchestration.md` in this plugin (two levels up from this skill's folder; read it first) (gates, questions, recording answers in `spec.md §Decisions`), with `workflow: amend`. Never rewrite finished work — add to it.

## Stages
0. **Task** — must have `spec.md` with AC. No AC yet → append to Raw requirement and run `/dev:spec` instead. Note where the task is: workflow stage, PR open or not.
1. **Record** — append verbatim to `spec.md §Raw requirement`: `### Update YYYY-MM-DD — <source>`. Number the items (U1, U2, …) if the source isn't already a list. `task.md` Now: `workflow: amend · stage: 1`.
2. **Impact** → `dev:analyst`, prompt: "amend mode, Update YYYY-MM-DD; AS-IS = task branch". It classifies each item (covered + tested / covered, no test / new behaviour / conflicts with an AC), updates spec in place, estimates S/M/L.
   **GATE A** — show the item table, how the delta fits the current code, conflicts, questions. Everything covered + tested → spec and `test-cases.md` updated explicitly, stop (skip to 6 without code).
3. **Plan** → `dev:planner`, prompt: "amend mode, Update YYYY-MM-DD" + the confirmed item classes. It adds TCs and one phase `Amend YYYY-MM-DD`; done phases stay. **GATE B** — skipped when the phase has ≤3 steps and no high risk.
4. **Implement** → `dev:implementer`, the amend phase only.
5. **Review** → `dev:reviewer` on the whole `base...branch` diff with focus on the amend commits (they interact with earlier code). Max 2 fix rounds, then gate: the user decides each remaining row (fix / follow-up / won't fix + why); running out of rounds is never the reason for `won't fix`.
6. **Verify** → `dev:verifier`: the full `test-cases.md` — new cases plus every earlier AC as regression. Record as in `/dev:feature-workflow` stage 5.
7. **Finish** — draft the PR update: a "Changes since last review" section (items → commits → TCs) and a tracker comment. **GATE C** — push / PR edit / tracker only on OK (`Delivery: self-merge` → the merge gate from the KB rules instead, then `/dev:close-task`). `status: review`, then `/dev:handoff`.

Task was mid-workflow (no code for the plan yet) → after stage 3 return to the original workflow at its implement stage instead of 4-7.
Resume: `task.md` says `workflow: amend · stage: N` → continue from N.
