---
name: triage
description: "Process inbox items one by one into tasks, tickets, knowledge, decisions or the bin. Manual: /kb:triage."
argument-hint: "[filter: type | priority]"
disable-model-invocation: true
---
# Triage the inbox

**Locate the KB root:** the nearest `.ai/` folder from the current directory upward (a project knowledge base); if there is none, the personal vault from `~/.claude/CLAUDE.md` (`Personal vault:` line); if neither exists, ask. Vault service folders carry a `_` prefix: there `inbox/`, `ideas/`, `raw/`, `stash/` below mean `_inbox/`, `_ideas/`, `_raw/`, `_stash/`.

1. List `<kb>/inbox/*.md` as a table — title · type · priority · age · source — high priority and oldest first.
2. Propose exactly one outcome per item, with a one-line reason:
   - **now** — tiny (<15 min), do it in this session
   - **task** — create a task (`/dev:new-task` in a project KB)
   - **ticket** — draft a tracker ticket (summary, type, description with evidence); create only after explicit OK
   - **checklist** — personal vault only, a plain todo: append `- [ ] <title>` to today's `_daily/YYYY-MM-DD.md`
   - **knowledge** — merge the fact into the right `context/` file (or vault note via `/me:save` rules), current-truth form
   - **decision** — write a decision record
   - **idea** — worth thinking through later: move to `<kb>/ideas/<kebab-slug>.md` from `templates/idea.md` in this plugin, `status: raw`, `## Idea` = the item's What, `source` = the item's source
   - **ask** — draft the question for the person who knows
   - **park** — keep; add `parked: YYYY-MM-DD <reason>` to frontmatter
   - **drop** — no longer relevant
3. The user confirms or edits the whole batch in one reply. Then apply.
4. Processed items: delete the file. If deleting is not permitted, move it to `<kb>/inbox/_done/` (lint purges it later).
5. Items parked twice or older than 60 days → propose drop.
6. Update the inbox count in `<kb>/STATUS.md` if it exists.
