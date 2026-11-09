## Knowledge base — `.ai/`
Read at session start only: this file → `.ai/STATUS.md` → the task's `task.md` → its `plan.md` up to **Next**.
Everything else on demand.
```
.ai/STATUS.md        active / parked tasks, waiting-on, inbox count (≤30 lines, overwritten)
.ai/context/         durable knowledge: glossary.md, architecture.md, data.md, …   (index below)
.ai/decisions/       NNNN-slug.md — decisions with their why (grep before re-deciding)
.ai/tasks/<KEY-slug>/ task.md · spec.md · plan.md · test-cases.md · research/ (raw/ = dumps)
.ai/qa/regression.md  regression suite promoted from closed tasks (for QA and future changes)
.ai/inbox/           captured, unprocessed items — never read at session start
.ai/ideas/           ideas about this project: raw → explored → promoted / shelved (/kb:capture, /kb:brainstorm)
.ai/stash/           temporary consume-once session context
.ai/raw/             ingested sources, immutable
.ai/archive/         closed tasks — only when asked
worktrees/<repo>--<KEY>/   (project root, not .ai/) git worktrees of tasks
```
Rules:
- **Current truth, not history.** Rewrite in place; no strikethrough, no "UPDATE" paragraphs, no v2 files.
- **One fact, one place.** Link, don't copy. The tracker owns ticket status; files link to it.
- **Decisions keep their why.** Task-only → `spec.md §Decisions`; outlives the task → `.ai/decisions/`.
- **Out of scope → `/kb:capture`**, never a silent fix.
- **No worklogs.** Progress = ticked plan steps with commit hashes.
- **Raw data** (query results, long reports, logs) → `raw/`; conclusions → the md file.
- **Stop on blockers** — write the question in `task.md §Open questions` and ask.
- **Worktrees** only at `<project>/worktrees/<repo>--<KEY>/` (`git -C <repo> worktree add <project>/worktrees/<repo>--<KEY> <branch>`), never inside a repo or elsewhere. Search inside the repo or worktree you work in, not from the project root (worktrees duplicate code).
- **Git host operations** (PR/MR, comments, merge state) with the tool from the Repositories table (`Host · tool`); tool missing or signed out → say so and give the install/login command, don't improvise with another tool.
- Limits: CLAUDE.md ≤100 lines · STATUS ≤30 · task.md ≤40 · spec.md ≤250 · inbox item ≤15 · idea ≤80.
