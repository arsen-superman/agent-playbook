---
name: spec
description: Analyse a task's requirements against the code and data and write spec.md (AS-IS, rules, acceptance criteria, edge cases, open questions). Use after new-task, or when the user asks to analyse, clarify or scope a ticket. Writes no production code.
argument-hint: "[task-key]"
---
# Write the spec (analyst)

1. Read `task.md`, the Raw requirement in `spec.md`, `.ai/context/glossary.md`. Grep `.ai/decisions/` and `.ai/context/` for the domain terms — the answer may already exist.
2. Explore with `dev:scout` subagents in parallel (cheap model; the built-in Explore runs on the caller's model), one narrow question each: entry points, current behaviour with `file:line`, data model, existing tests, other callers. Ask for conclusions, not file dumps. Long reports worth keeping → `research/raw/`.
3. Fill `spec.md`: **AS-IS** (condensed, `file:line`; if two code paths do the same thing, say which is in scope) · **Rules** (numbered, with source) · **Acceptance criteria** (each testable, plus a "no change for unaffected users" AC when touching existing logic) · **Edge cases** · **Out of scope** · **Assumptions**.
4. Unknowns → `task.md §Open questions` with who can answer. Blocking → draft the clarification message (Jira comment / Slack) in the reply; post only on OK.
5. A sub-question that needs real investigation → `/dev:research`, link the result. Keep spec.md ≤250 lines.
6. Out of scope → `/kb:capture`.
**Amend mode** (prompt says amend, or spec already has AC and Raw requirement has a new `### Update`): only the update's items; AS-IS = the task branch. Per item: covered + tested (name the test) / covered, no test / new behaviour / conflicts with ACn. Edit AC and edge cases in place — clarified ones rewritten, new ones appended with the next free ID, never renumber. SUMMARY: item table with class and S/M/L.

7. `task.md` Now: no blockers → `status: planned`, Next `/dev:plan`; else `status: blocked`. Stop. No code.
