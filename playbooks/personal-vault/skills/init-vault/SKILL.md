---
name: init-vault
description: "Create the personal vault (Markdown, Obsidian as the UI), upgrade an older layout, register where it lives. Manual: /me:init-vault."
argument-hint: "[path]"
disable-model-invocation: true
---
# Create or upgrade the personal vault

One vault for all personal knowledge, in a Google Drive folder so every device and every Claude surface reaches it; Obsidian is the main UI.
Templates: `templates/vault/` and `templates/note/` in this plugin (two levels up from this skill's folder).

**Where it lives**
- On the computer: the Google Drive for desktop path, e.g. `G:\My Drive\Vault` (Windows) — used by Claude Code and Cowork.
- In claude.ai chat (no file system): the same folder through the Google Drive connector, found by its name `Vault` at the root of My Drive.

Steps:
1. **Path**: argument, else ask (suggest `G:\My Drive\Vault`). Must be outside any work project.
2. **Create what is missing** (never overwrite a file that exists):
   - `CLAUDE.md` from `templates/vault/CLAUDE.md`; `_tasks.md` from `tasks.md`.
   - Service folders `_inbox/ _ideas/ _daily/ _raw/ _categories/ _templates/ _attachments/`; `_ideas/_ideas.md` from `ideas.md`.
   - Each domain listed in the vault `CLAUDE.md`: folder `<Domain>/` + folder note `<Domain>/<Domain>.md` from `folder-note.md`.
   - `_categories/Recipes.md`, `How-tos.md`, `Prompts.md`, `Notes.md` from `category.md` (`<Category>` = the file's name).
   - `_templates/`: copies of `templates/note/*.md` (refresh them when this plugin's versions differ; tell the user).
3. **Older layout found** (service folders without the `_` prefix, lowercase areas, `index.md` files, type folders like `prompts/` or `howto/`) → show a move plan and apply on OK:
   - service folders → `_` names (`inbox/` → `_inbox/`, `ideas/ideas.md` → `_ideas/_ideas.md`, `tasks.md` → `_tasks.md`, …; Obsidian CLI `move`, else plain moves — links are path-less), then the user updates the Templates, Daily notes, attachments and excluded-files settings per `obsidian-setup.md`;
   - areas → capitalized domains (case-only rename via a temporary name; with the Obsidian CLI use `move`);
   - type folders → notes into their topic domain, the type into `categories`; tags `recipe`/`howto` → `categories`;
   - each `index.md` line → that note's `summary`; then delete root and area `index.md` files.
4. **Register** in `~/.claude/CLAUDE.md` (show the diff, ask first): `Personal vault: <absolute path>` and `Personal vault (Drive): Vault`.
5. **Obsidian**: walk the user through `templates/vault/obsidian-setup.md` (settings, Folder Notes, CLI, phone sync, optional agent skills). Also: mark the Drive folder "Available offline" — search, the CLI and Obsidian need local files.
6. Reply: what was created or moved, in ≤8 lines.
