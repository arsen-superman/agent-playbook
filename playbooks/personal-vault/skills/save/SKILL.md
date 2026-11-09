---
name: save
description: Save something from the conversation (a recipe, a how-to, instructions, a prompt, an explanation, a checklist, a useful answer) as a Markdown note in the personal vault, in the right domain folder, merged with an existing note on the same topic. Use when the user says save this, збережи, запиши в базу, save the recipe, keep this instruction, save this prompt, add to my notes.
argument-hint: "[what] [domain]"
---
# Save to the personal vault

Rules of the vault: its `CLAUDE.md` (domains, categories, frontmatter). Note templates: `templates/note/` in this plugin (same as the vault's `templates/`): **recipe** · **howto** (Check, Rollback, `applies-to`) · **prompt** · **note**.

**Access mode**
- *Files* (Claude Code, Cowork with the folder connected): vault = `Personal vault:` path in `~/.claude/CLAUDE.md`.
- *Drive* (claude.ai chat, or no local path): Google Drive connector, folder `Vault` (or the name given as `Personal vault (Drive):`). Create files with `contentMimeType: text/markdown` and `disableConversionToGoogleType: true` — never as Google Docs. The connector can't edit file content: to update a note, create the new version with the same title in the same folder, then trash the old file.
- Neither available → give the note as Markdown in the reply and say where it should go.

Steps:
1. **What** — the thing meant (usually the last substantial answer). Drop conversation noise; keep exact quantities, commands, values.
2. **Existing note** — search outside `raw/` and `templates/`: file names, `aliases`, `summary`, headings, in both languages. Same subject exists → update that note (merge, current truth, bump `updated`) and skip to step 6.
3. **Domain** = what it is about, from the vault `CLAUDE.md` list. Prompts, how-tos and recipes are categories, never folders. Nothing fits → the closest domain, plus one line proposing a new one; **never create a top-level folder without an explicit OK**. Ambiguous → state the path in one line and go unless the user objects.
4. **Category and shape** — what kind of note: recipe → Recipes; anything that changes a system (BIOS, undervolt, router, OS) → How-tos with Check and Rollback filled and `applies-to` set; a reusable prompt → Prompts; otherwise Notes. Fill `summary` (one line, it is the catalog), `aliases` (the title in the other language, synonyms), `tags` (finer topics, plural), `source:` = `conversation YYYY-MM-DD` or the URL.
5. **Risky numbers** — voltages, doses, temperatures, money/legal figures you're unsure of → mark `⚠️ verify`, never invent precision.
6. **File** — `<Domain>/<kebab-case-title>.md`, unique name, no index to update. Domain past ~50 notes → suggest a topic subfolder (move with the Obsidian CLI as the vault `CLAUDE.md` says).
7. Reply in one line: `💾 <Domain>/<file>.md` (+ "updated existing").
