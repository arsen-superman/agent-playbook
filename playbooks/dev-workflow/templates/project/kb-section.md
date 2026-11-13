## Knowledge base — `.ai/`
Read at session start only: this file → `.ai/STATUS.md` → the task's `task.md` → its `plan.md` up to **Next**.
Everything else on demand.
```
.ai/STATUS.md        active / paused tasks, waiting-on, inbox count (≤30 lines, overwritten)
.ai/context/         durable cross-repo knowledge: glossary.md, architecture.md, data.md, …   (index below)
.ai/context/<repo>/  knowledge about one repo only (folder name = Repositories table)
.ai/decisions/       NNNN-slug.md — decisions with their why and Repos (grep before re-deciding)
.ai/tasks/<KEY-slug>/ task.md · spec.md · plan.md · test-cases.md · review.md · research/ (raw/ = dumps)
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
- **One fact, one place.** Link, don't copy. The tracker owns ticket status; files link to it. A repo's own docs (`docs/`, README) own what they describe — `.ai/context/` gets one link line in the Context index, not a copy; new knowledge about that code → propose a docs change in the repo. `.ai/context/` holds only what no repo has (cross-repo, domain, data, environments).
- **One area per `context/` file.** About one repo → `context/<repo>/`; spans repos → `context/`. Past the limit → split by sub-area and update the Context index (grouped by repo).
- **Every task, decision and STATUS row names its repos** (`repos:` in task/decision frontmatter · Repos column), using names from the Repositories table or `all`.
- **Decisions keep their why.** Task-only details → `spec.md §Decisions` (archived with the task). `.ai/decisions/` only for what outlives the task *and* someone may want to reverse — usually 0–2 per task.
- **Superseded, not deleted.** A new decision replacing an old one → in the old one set `status: superseded`, `superseded-by: NNNN`. A superseded decision is not a current rule — skip it when grepping.
- **Links are relative Markdown links** (`[spec](spec.md)`, `../tasks/KEY-slug/task.md`), never `[[wikilinks]]`. Link what belongs together — task ↔ research, idea, decisions — so the graph shows it.
- **Out of scope → `/kb:capture`**, never a silent fix.
- **No worklogs.** Progress = ticked plan steps with commit hashes.
- **Raw data** (query results, long reports, logs) → `raw/`; conclusions → the md file.
- **Stop on blockers** — write the question in `task.md §Open questions` and ask.
- **Worktrees** only at `<project>/worktrees/<repo>--<KEY>/` (`git -C <repo> worktree add <project>/worktrees/<repo>--<KEY> <branch>`), never inside a repo or elsewhere. Search inside the repo or worktree you work in, not from the project root (worktrees duplicate code).
- **Git host operations** (PR/MR, comments, merge state) with the tool from the Repositories table (`Host · tool`); tool missing or signed out → say so and give the install/login command, don't improvise with another tool.
- Limits: CLAUDE.md ≤100 lines · STATUS ≤30 · task.md ≤40 · spec.md ≤250 · context file ≤300 · inbox item ≤20 · idea ≤80.
