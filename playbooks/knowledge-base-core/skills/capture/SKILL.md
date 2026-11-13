---
name: capture
description: "Capture an idea, todo, finding, bug or question for later without acting on it — ideas to ideas/, the rest to the inbox. Also proactively for anything outside the current task. Triggers: note this, new idea, запиши, на потім, закинь в інбокс, ідея."
argument-hint: "<what>"
---
# Capture

**Locate the KB root:** the nearest `.ai/` folder from the current directory upward (a project knowledge base); if there is none, the personal vault from `~/.claude/CLAUDE.md` (`Personal vault:` line); no file system (claude.ai) → Drive mode; none of these → ask. The user names another target ("в інбокс проєкту X", "у Vault") → use it. Vault service folders carry a `_` prefix: there `inbox/`, `ideas/`, `raw/`, `stash/` below mean `_inbox/`, `_ideas/`, `_raw/`, `_stash/`.

**Drive mode:** Google Drive connector, folder `Vault` (or the `Personal vault (Drive):` name); search by title and full text. Create files with `contentMimeType: text/markdown` and `disableConversionToGoogleType: true` — never Google Docs. To change a file, create the new version with the same title in the same folder, then trash the old one.

**Where it goes**
- The **user** offers an idea ("ідея: …", "запиши ідею") → `<kb>/ideas/<kebab-slug>.md` from `templates/idea.md` in this plugin, `status: raw`. `## Idea` = the user's words (or a tight summary of the idea discussed in this conversation); fill `## Why / context` only from what was said. Ask at most one question, and only if no title is possible.
- **Personal vault, files mode:** a plain todo from the user that needs no thinking ("купити фільтр") → append `- [ ] <what>` under `## Tasks` in `_daily/YYYY-MM-DD.md` (today; create it from the vault's `_templates/daily.md` if missing), reply `☑️ <what>`. In Drive mode it goes to the inbox (the connector can't append).
- Anything else, and **everything you notice yourself** (incl. improvement ideas during other work) → inbox item below.

**Inbox item** `<kb>/inbox/YYYY-MM-DD-<kebab-slug>.md` from `templates/inbox-item.md` in this plugin (≤20 lines). Every field is filled; no value → `n/a`. `area` is required and never `n/a`: infer it from `Where` or the current task, ask only if impossible.
Type guide: `todo` work to do · `finding` fact learned · `bug` defect · `chore` upkeep, no behaviour change · `idea` possible improvement · `question` someone must answer.
No priority — it is decided at triage. `severity` only for `bug`: `high` data loss, security hole or blocks users · `medium` wrong behaviour with a workaround · `low` cosmetic or rare edge.

Steps:
1. Duplicate check: grep `<kb>/inbox/`, `<kb>/ideas/` (incl. idea folders) and active tasks for the same subject. Found → append one evidence line to that item and stop.
2. Write the file. It must be readable in a month without this conversation: include paths, names, links.
3. Reply with one line — `📥 <title>` (inbox) or `💡 <title>` (idea) — and continue the current work. Do not start working on the item.
