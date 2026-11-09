---
name: amend
description: Workflow — bring new requirements, clarifications or edge cases into a task that already has a spec, plan, code or an open PR — record them, analyse the impact on the current code, plan the delta, then implement, review and verify only that. Use when the user says new requirements, clarification, уточнення, нові вимоги, додай edge case, врахуй ще випадок, for a task past the spec stage.
argument-hint: "<task-key> <clarification text | file | url>"
---
# Amend a task — orchestrator

You orchestrate; stages run in the same agents as `/dev:feature-workflow` and follow its **Orchestration rules** (gates, questions, recording answers in `spec.md §Decisions`), with `workflow: amend`. Never rewrite finished work — add to it.

## Stages
0. **Task** — must have `spec.md` with AC. No AC yet → append to Raw requirement and run `/dev:spec` instead. Note where the task is: workflow stage, PR open or not.
1. **Record** — append verbatim to `spec.md §Raw requirement`: `### Update YYYY-MM-DD — <source>`. Number the items (U1, U2, …) if the source isn't already a list. `task.md` Now: `workflow: amend · stage: 1`.
2. **Impact** → `dev:analyst`, prompt: "amend mode, Update YYYY-MM-DD; AS-IS = task branch". It classifies each item (covered + tested / covered, no test / new behaviour / conflicts with an AC), updates spec in place, estimates S/M/L.
   **GATE A** — show the item table, how the delta fits the current code, conflicts, questions. Everything covered + tested → spec and `test-cases.md` updated explicitly, stop (skip to 6 without code).
3. **Plan** → `dev:planner`, prompt: "amend mode, Update YYYY-MM-DD" + the confirmed item classes. It adds TCs and one phase `Amend YYYY-MM-DD`; done phases stay. **GATE B** — skipped when the phase has ≤3 steps and no high risk.
4. **Implement** → `dev:implementer`, the amend phase only.
5. **Review** → `dev:reviewer` on the whole `base...branch` diff with focus on the amend commits (they interact with earlier code). Max 2 fix rounds.
6. **Verify** → `dev:verifier`: the full `test-cases.md` — new cases plus every earlier AC as regression. Record as in `/dev:feature-workflow` stage 5.
7. **Finish** — draft the PR update: a "Changes since last review" section (items → commits → TCs) and a Jira comment. **GATE C** — push / PR edit / Jira only on OK. `status: review`, then `/dev:handoff`.

Task was mid-workflow (no code for the plan yet) → after stage 3 return to the original workflow at its implement stage instead of 4-7.
Resume: `task.md` says `workflow: amend · stage: N` → continue from N.
