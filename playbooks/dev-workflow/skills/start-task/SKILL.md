---
name: start-task
description: "Start a work session on a task — read the minimum state and say where things stand; a paused task is brought back to active. Use at the beginning of every session, or when the user says start, continue, resume, unpause, where were we, продовжуємо, розморозь, повертаємось до <task>."
argument-hint: "[task-key]"
---
# Start a task session

The project `CLAUDE.md` is already loaded. Knowledge base: `.ai/` next to it. No `.ai/` → suggest `/dev:init-project`.

1. Read `.ai/STATUS.md`.
2. Pick the task: the argument; else the only `in-progress` task; else list Active (and Paused) and ask.
3. Read the task's `task.md`, then `plan.md` from the top through the first unchecked step and the 3 after it. `status: paused` → go to **Paused task** below instead of 4-8.
4. Do **not** read now: `inbox/`, `stash/`, `archive/`, `raw/`, `research/`, `context/`, `decisions/`, the full `spec.md`. Open them later only when a step needs them.
5. Counts only: inbox items, stashes (`ls`). If a stash belongs to this task, mention it (`/kb:unstash <name>`).
6. Staleness: task `updated:` vs recent commits on its branch; Jira status vs `status:` (if a key exists and the connector is available). Mention mismatches. `status: review` with a PR → its state if a tool is available: merged → suggest `/dev:close-task`; unresolved comments → `/dev:pr-comments`.
7. Schema: `.ai/.playbook.json` `schema` below this plugin's `migrations/CURRENT` (or file missing) → one line: "KB structure is outdated — `/dev:upgrade-project`".
8. Reply ≤8 lines: where we are · Next · open questions/blockers · inbox/stash counts. If the user already said what to do, proceed.

## Paused task (`status: paused`)
1. Read the **Paused** block in `task.md` first. **What changed since `Since:`**:
   - Unblock condition — met? (ask the user; check Jira comments/status and linked issues via the connector)
   - Code — per repo: is the task branch still there; how far behind the base branch; would it rebase cleanly (`git merge-tree` / dry run); did files touched by the plan change on the base branch?
   - Volatile facts — re-check each listed one (re-run the query, re-read the code).
   - Decisions/context in `.ai/` updated after `Since:` that touch this task (grep by date and terms).
2. Report a short "while you were away" diff (≤8 lines) and what in spec/plan is now wrong.
3. On OK: update spec/plan to current truth, remove the **Paused** block, restore status (`planned` / `in-progress`), set Next, move the row back to Active in `STATUS.md`. Suggest rebasing the branch before coding. A workflow was mid-stage → it continues at the saved stage.
4. Unblock condition not met → say so, keep it paused, update `Since`-independent notes only.
