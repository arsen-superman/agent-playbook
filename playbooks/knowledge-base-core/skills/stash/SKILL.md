---
name: stash
description: Save the current session's working context into a temporary, consume-once stash so the user can switch to something else and later restore it with unstash. Use when the user says stash, відклади контекст, збережи контекст, switch task, "переключаюсь", or before abandoning a half-finished line of thought.
argument-hint: "[short-name]"
---
# Stash the working context

A stash is **ephemeral session memory** — also the way to carry a task-less exploration or chat into a fresh session instead of compacting: what is in your head right now that is not yet worth writing into task files. It is consumed once by `unstash` and then removed. Durable task state belongs in `task.md` (`/dev:handoff`, `/dev:park`), not here.

**Locate the KB root:** the nearest `.ai/` folder from the current directory upward (a project knowledge base); if there is none, the personal vault from `~/.claude/CLAUDE.md` (`Personal vault:` line); if neither exists, ask. Vault service folders carry a `_` prefix: there `inbox/`, `ideas/`, `raw/`, `stash/` below mean `_inbox/`, `_ideas/`, `_raw/`, `_stash/`.

1. Write `<kb>/stash/YYYY-MM-DD-HHMM-<short-name>.md` (≤40 lines):
   ```markdown
   ---
   created: YYYY-MM-DD HH:MM
   task: <task key or none>
   ---
   # <short-name> — <one-line what I was doing>

   ## Goal
   ## Where I am
   ## Facts established (with file:line / links)
   ## Hypotheses / open threads
   ## Files and state touched (branch, uncommitted changes, running processes)
   ## Next step
   ```
2. Write what a fresh agent needs to continue — not a transcript. Long outputs → save next to it as `<same-name>.raw.md` and link.
3. Uncommitted code: say so in the stash and ask whether to commit a WIP commit on the task branch first. Never `git stash` silently — it is easy to lose.
4. Reply: `🗂 stashed: <short-name> — restore with /kb:unstash <short-name>`.
