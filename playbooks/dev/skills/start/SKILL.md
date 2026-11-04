---
name: start
description: Start or resume a work session in a project — read the minimum state and say where things stand. Use at the beginning of every session, or when the user says start, continue, resume, where were we, продовжуємо.
argument-hint: "[task-key]"
---
# Start a session

The project `CLAUDE.md` is already loaded. Knowledge base: `.ai/` next to it. No `.ai/` → suggest `/dev:init-project`.

1. Read `.ai/STATUS.md`.
2. Pick the task: the argument; else the only `in-progress` task; else list Active (and Parked) and ask.
3. Read the task's `task.md`, then `plan.md` from the top through the first unchecked step and the 3 after it.
4. Do **not** read now: `inbox/`, `stash/`, `archive/`, `raw/`, `research/`, `context/`, `decisions/`, the full `spec.md`. Open them later only when a step needs them.
5. Counts only: inbox items, stashes (`ls`). If a stash belongs to this task, mention it (`/kb:unstash <name>`).
6. Staleness: task `updated:` vs recent commits on its branch; Jira status vs `status:` (if a key exists and the connector is available). Mention mismatches. `status: review` with a PR → its state if a tool is available: merged → suggest `/dev:close-task`; unresolved comments → `/dev:pr-comments`.
7. Parked task → run `/dev:resume` instead.
8. Schema: `.ai/.playbook.json` `schema` below this plugin's `migrations/CURRENT` (or file missing) → one line: "KB structure is outdated — `/dev:upgrade-project`".
9. Reply ≤8 lines: where we are · Next · open questions/blockers · inbox/stash counts. If the user already said what to do, proceed.
