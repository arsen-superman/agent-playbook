---
name: triage
description: "Process inbox items one by one into tasks, tickets, knowledge, decisions or the bin. Manual: /kb:triage."
argument-hint: "[filter: type | severity | area]"
disable-model-invocation: true
---
# Triage the inbox

**Locate the KB root:** the nearest `.ai/` folder from the current directory upward (a project knowledge base); if there is none, the personal vault from `~/.claude/CLAUDE.md` (`Personal vault:` line); if neither exists, ask. Vault service folders carry a `_` prefix: there `inbox/`, `ideas/`, `raw/`, `stash/` below mean `_inbox/`, `_ideas/`, `_raw/`, `_stash/`.

1. List `<kb>/inbox/*.md` (not the generated `INDEX.md`) as a table — title · type · severity · area · status · source · age — `in-progress` first (show `next`), then `new`; grouped by area, high severity and oldest first within a group.
2. Propose exactly one outcome per item, with a one-line reason:
   - **now** — tiny (<15 min), do it in this session
   - **task** — create a task (`/dev:new-task` in a project KB)
   - **ticket** — draft a tracker ticket (summary, type, description with evidence); create only after explicit OK
   - **checklist** — personal vault only, a plain todo: append `- [ ] <title>` to today's `_daily/YYYY-MM-DD.md`
   - **knowledge** — merge the fact into the right `context/` file (or vault note via `/me:save` rules), current-truth form
   - **decision** — write a decision record
   - **idea** — worth thinking through later: move to `<kb>/ideas/<kebab-slug>.md` from `templates/idea.md` in this plugin, `status: raw`, `## Idea` = the item's What, `source` = the item's source
   - **hold** — cannot decide yet (bug or feature? needs an answer, wait for a date or event); stays in the inbox
   - **drop** — no longer relevant
3. The user confirms or edits the whole batch in one reply. Then apply.
4. Apply per outcome:
   - **task**, **ticket** → `status: done`, `updated` today, `resolution: task <KEY>` / `ticket <KEY>`, move to `<kb>/inbox/_done/` (lint purges it after 90 days).
   - **hold** → `status: in-progress`, `updated` today, `next: <what is awaited, from whom>`.
   - **now**, **checklist**, **knowledge**, **decision**, **idea**, **drop** → delete the file. If deleting is not permitted, move it to `_done/` with `status: done` and `resolution: <outcome>`.
5. `in-progress` for >30 days or any item >60 days old → propose drop.
6. Update the inbox count (new + in-progress) in `<kb>/STATUS.md` if it exists. Project KB: rebuild the index — `python "${CLAUDE_PLUGIN_ROOT}/scripts/inbox_index.py" <kb>/inbox` (moving or deleting files fires no hook).
