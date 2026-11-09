---
name: park
description: Freeze a task for an unknown time — blocked, missing data, priorities changed — so it can be resumed weeks later without losing context. Use when the user says park, pause, freeze, заморозь, постав на паузу, відкладаємо задачу.
argument-hint: "<task-key> [reason]"
---
# Park a task

A parked task stays in `.ai/tasks/` (paths and links stay valid); only its status changes.

1. Run the `/dev:handoff` steps 1-5 first — the task files must be current truth.
2. **Code**: in each repo from `repos:` — uncommitted changes → ask, then commit `<KEY>: WIP — parked (<reason>)` on the task branch (never `git stash`: it is invisible and easy to lose). Ask whether to push the branch. Record branch + last commit per repo. A worktree for this task can be removed once the branch is committed (ask).
3. Add to the top of `task.md`, set `status: parked`:
   ```markdown
   ## Parked
   - **Since:** YYYY-MM-DD · **Was:** <previous status>
   - **Why:** <blocker / missing data / priority change>
   - **Unblocks when:** <concrete condition> — **owner:** <who>
   - **Code:** <repo>@<branch> <hash> (pushed: yes/no)
   - **Volatile facts to re-check on resume:** <data counts, API behaviour, people's answers, base branch>
   - **Resume with:** <first action once unblocked>
   ```
4. Waiting on a person → draft the follow-up message (Jira comment / Slack) in the reply; post only on OK.
5. `STATUS.md`: move the row from Active to **Parked** (task · since · waiting for).
6. Reply ≤4 lines: parked, why, what unblocks it.
