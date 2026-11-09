# Personal vault

Personal knowledge saved from conversations and sources: recipes, how-tos, instructions, reference answers.
Plain Markdown in a Google Drive folder — readable in Obsidian, any editor, claude.ai chat (Drive connector) or any agent.

## Layout
- `index.md` — list of areas only, one line each. Stays short at any vault size.
- `<area>/index.md` — catalog of that area: one line per note.
- **Looking for something:** search first (file names, `tags`, headings, then full text, in both languages); read an index only when search misses — the root, then just the relevant area's.
- `<area>/` — top-level areas (cooking, tech, home, travel, learning, …). Create a new area only when ≥3 notes would go there; until then use the closest one.
- `<area>/<topic>/` — optional second level once an area has >15 notes.
- `inbox/` — quick captures to sort later (`/kb:triage`).
- `ideas/` — ideas with a status (raw → explored → promoted / shelved), one file each (`/kb:capture`, `/kb:brainstorm`). Project ideas live in that project's `.ai/ideas/`, not here.
- `raw/` — original sources kept verbatim (`/kb:ingest`).

## Notes
- File name: `kebab-case-title.md`, no dates in names.
- Frontmatter: `tags`, `source` (conversation / URL / book), `created`, `updated`, and `applies-to` for anything version- or hardware-specific.
- One subject per note. Same subject again → **update the existing note**, don't create a twin.
- Current truth: rewrite outdated parts; keep a short `## History` only when the old way still matters (e.g. a setting that changed with a BIOS update).
- Instructions that change a system (BIOS, OS, network, car) always have **Check** and **Rollback** sections.
- Link related notes with `[[note-name]]` (works in Obsidian and is greppable).

## Language
Notes in the language the content came in (Ukrainian recipes stay Ukrainian). Titles may be either.
