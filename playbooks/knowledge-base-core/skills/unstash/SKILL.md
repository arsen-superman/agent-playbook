---
name: unstash
description: Restore a previously stashed working context into the current session and consume it (remove the stash). Use when the user says unstash, поверни контекст, restore context, "повертаюсь до …", or names a stash.
argument-hint: "[short-name]"
---
# Restore a stash

**Locate the KB root:** the nearest `.ai/` folder from the current directory upward (a project knowledge base); if there is none, the personal vault from `~/.claude/CLAUDE.md` (`Personal vault:` line); if neither exists, ask. Vault service folders carry a `_` prefix: there `inbox/`, `ideas/`, `raw/`, `stash/` below mean `_inbox/`, `_ideas/`, `_raw/`, `_stash/`.

1. No name given → list `<kb>/stash/*.md` (name · created · task · first line) and ask which one.
2. Read the stash (and its `.raw.md` only if the next step needs it). If it references a task, read that task's `task.md` too.
3. Check drift since `created:` — branch moved, files changed, ticket updated. Mention what changed.
4. Restate it to the user in ≤6 lines: goal, where we were, next step. From now on it lives in this session.
5. **Consume it**: move the stash (and its `.raw.md`) to `<kb>/stash/.consumed/` — a short safety net; `/kb:lint` deletes consumed stashes older than 14 days. If moving is impossible, delete.
6. Anything in it that turns out to be durable (a decision, a fact) → write it to the proper file during this session; the stash will not be there next time.
