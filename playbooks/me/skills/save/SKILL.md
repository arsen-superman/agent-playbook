---
name: save
description: Save something from the conversation (a recipe, a how-to, instructions, an explanation, a checklist, a useful answer) as a Markdown note in the personal vault, in the right folder, merged with an existing note on the same topic. Use when the user says save this, збережи, запиши в базу, save the recipe, keep this instruction, add to my notes.
argument-hint: "[what] [area]"
---
# Save to the personal vault

Note shapes (templates in this plugin, `templates/note/`): **recipe** (ingredients, steps, notes) · **howto** (before you start, steps, Check, Rollback, my settings; `applies-to`) · **note** (TL;DR, details, related). Frontmatter: `tags`, `source`, `created`, `updated` (+ `applies-to`).

**Access mode**
- *Files* (Claude Code, Cowork with the folder connected): vault = `Personal vault:` path in `~/.claude/CLAUDE.md`.
- *Drive* (claude.ai chat, or no local path): Google Drive connector, folder `Vault` (or the name given as `Personal vault (Drive):`). Create files with `contentMimeType: text/markdown` and `disableConversionToGoogleType: true` — never as Google Docs. The connector can't edit file content: to update a note, create the new version with the same title in the same folder, then trash the old file.
- Neither available → give the note as Markdown in the reply and say where it should go.

Steps:
1. **What** — the thing meant (usually the last substantial answer). Drop conversation noise; keep exact quantities, commands, values.
2. **Where** — pick the area from root `index.md` (areas only); find an existing note on the subject by searching file names, `tags` and headings, else `<area>/index.md`. Same subject exists → update that note (merge, current truth, bump `updated`). Ambiguous → state the path in one line and go unless the user objects.
3. **Shape** — recipe → recipe; anything that changes a system (BIOS, undervolt, router, OS) → howto with Check and Rollback filled and `applies-to` set; otherwise note. `source:` = `conversation YYYY-MM-DD` or the URL.
4. **Risky numbers** — voltages, doses, temperatures, money/legal figures you're unsure of → mark `⚠️ verify`, never invent precision.
5. **Index** — add/update `- [[note-name]] — what it is (applies-to)` in `<area>/index.md`. New area → create its index from `templates/vault/area-index.md` in this plugin and add one line to root `index.md`; never list notes in the root.
6. Reply in one line: `💾 <area>/<file>.md` (+ "updated existing").
