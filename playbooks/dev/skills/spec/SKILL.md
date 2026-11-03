---
name: spec
description: Analyse a task's requirements against the code and data and write spec.md (AS-IS, rules, acceptance criteria, edge cases, open questions). Use after new-task, or when the user asks to analyse, clarify or scope a ticket. Writes no production code.
argument-hint: "[task-key]"
---
# Write the spec (analyst)

1. Read `task.md`, the Raw requirement in `spec.md`, `.ai/context/glossary.md`. Grep `.ai/decisions/` and `.ai/context/` for the domain terms — the answer may already exist.
2. Explore with a subagent (Explore): entry points, current behaviour with `file:line`, data model, existing tests, other callers. Ask for conclusions, not file dumps. Long reports worth keeping → `research/raw/`.
3. Fill `spec.md`: **AS-IS** (condensed, `file:line`; if two code paths do the same thing, say which is in scope) · **Rules** (numbered, with source) · **Acceptance criteria** (each testable, plus a "no change for unaffected users" AC when touching existing logic) · **Edge cases** · **Out of scope** · **Assumptions**.
4. Unknowns → `task.md §Open questions` with who can answer. Blocking → draft the clarification message (Jira comment / Slack) in the reply; post only on OK.
5. A sub-question that needs real investigation → `/dev:research`, link the result. Keep spec.md ≤250 lines.
6. Out of scope → `/kb:capture`.
7. `task.md` Now: no blockers → `status: planned`, Next `/dev:plan`; else `status: blocked`. Stop. No code.
