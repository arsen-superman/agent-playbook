# Obsidian setup checklist
<!-- Walked through by /me:init-vault. The user clicks; Claude does not edit .obsidian/ while Obsidian is open. -->

## Settings
- Files & links → New link format: **Shortest path when possible**; Automatically update internal links: **on**; Default location for new attachments: folder `_attachments`.
- Core plugins on: **Templates** (folder `_templates`), **Daily notes** (folder `_daily`, format `YYYY-MM-DD`, template `_templates/daily`), **Bases**.
- General → **Command line interface**: on, then register it (Obsidian 1.12.7+). Restart the terminal so `obsidian` is on PATH.
- Community plugin **Folder Notes**: folder note name `{{folder_name}}`, stored inside the folder; clicking a domain folder opens its Base.
- Excluded files: `_raw/`, `_attachments/` (keeps search and the graph clean).

## Phone (Android)
- Mirror the Drive folder to local storage with **Autosync for Google Drive** (two-way) or **FolderSync**; open that local copy in Obsidian.
- Settings → Files & links → **Override config folder**: `.obsidian-mobile`, so phone and PC never fight over `workspace.json`.

## Agent skills (optional, once per machine)
- `npx skills add kepano/obsidian-skills --skill obsidian-bases -a claude-code` — correct `.base` syntax for folder notes and categories.
- `npx skills add kepano/obsidian-skills --skill defuddle -a claude-code` + `npm i -g defuddle` — clean Markdown from web pages for `/kb:ingest` (applies to every project: it is preferred over WebFetch).
- `json-canvas` from the same repo — only if idea maps on Canvas are wanted.
- Browser: **Obsidian Web Clipper** extension, saving to `_raw/`.
