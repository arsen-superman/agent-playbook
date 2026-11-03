---
name: close-task
description: Close a finished or cancelled task — promote lasting decisions and knowledge to the project, record the outcome, archive the folder. Use when a task is merged, done, released or cancelled.
argument-hint: "<task-key>"
---
# Close a task

1. Confirm done: PR merged / Jira status (connector) / the user says so.
2. **Promote** what outlives the task: `test-cases.md` regression candidates → append to `.ai/qa/regression.md` under the feature area (ID → `<KEY>/TC-nn`, keep steps, data and `Automated by`); decisions → `.ai/decisions/`; facts about code, data, domain → `.ai/context/`; terms → `glossary.md`; untracked follow-ups → `/kb:capture` or drafted tickets.
3. `## Outcome` at the top of `task.md` (≤10 lines): what shipped, PR, release, what was deferred (links), lessons that changed a skill or CLAUDE.md. `status: done`.
4. Move the folder to `.ai/archive/`. Ask whether to delete `research/raw/` (may contain client data).
5. `STATUS.md`: remove from Active, add to Recently closed (keep 5).
6. Worktrees for this task → suggest `git worktree remove`.
