---
name: init-vault
description: Create the personal knowledge vault (Markdown, Obsidian-compatible) and register where it lives. Use when the user wants to start a personal knowledge base, second brain or vault, or when save/find finds no vault configured.
argument-hint: "[path]"
---
# Create the personal vault

One vault for all personal knowledge, kept in a Google Drive folder so every device and every Claude surface reaches it.
Templates: `templates/vault/` in this plugin (two levels up from this skill's folder).

**Where it lives**
- On the computer: the Google Drive for desktop path, e.g. `G:\My Drive\Vault` (Windows) — used by Claude Code and Cowork.
- In claude.ai chat (no file system): the same folder through the Google Drive connector, found by its name `Vault` at the root of My Drive.

Steps:
1. Path: argument, else ask (suggest `G:\My Drive\Vault`). Must be outside any work project. Existing folder with notes → add only missing pieces.
2. Create `CLAUDE.md` and root `index.md` (areas only) from `templates/vault/`, folders `inbox/`, `ideas/`, `raw/` and the areas in `index.md`, each with `<area>/index.md` from `area-index.md`. Existing vault whose root `index.md` lists notes → move each area's lines into its `<area>/index.md` and leave only area lines in the root.
3. Add to `~/.claude/CLAUDE.md` (show the diff, ask first): `Personal vault: <absolute path>` and `Personal vault (Drive): Vault`.
4. Tell the user: in Google Drive for desktop, mark the folder "Available offline" (search and Obsidian need local files); open it in Obsidian as a vault if wanted.
