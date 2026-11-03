---
name: resume
description: Resume a parked task — re-read its frozen state, detect what changed while it was parked, and bring it back to active. Use when the user says resume, unpark, розморозь, повертаємось до <task>, or when start picks a parked task.
argument-hint: "<task-key>"
---
# Resume a parked task

1. Read `task.md` (the **Parked** block first), then `plan.md` up to Next.
2. **What changed since `Since:`**:
   - Unblock condition — met? (ask the user; check Jira comments/status and linked issues via the connector)
   - Code — per repo: is the task branch still there; how far behind the base branch; would it rebase cleanly (`git merge-tree` / dry run); did files touched by the plan change on the base branch?
   - Volatile facts — re-check each listed one (re-run the query, re-read the code).
   - Decisions/context in `.ai/` updated after `Since:` that touch this task (grep by date and terms).
3. Report a short "while you were away" diff (≤8 lines) and what in spec/plan is now wrong.
4. On OK: update spec/plan to current truth, remove the **Parked** block, restore status (`planned` / `in-progress`), set Next, move the row back to Active in `STATUS.md`. Suggest rebasing the branch before coding.
5. Unblock condition not met → say so, keep it parked, update `Since`-independent notes only.
