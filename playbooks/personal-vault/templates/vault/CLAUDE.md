# Personal vault

Personal knowledge saved from conversations and sources: recipes, how-tos, prompts, reference answers, ideas.
Plain Markdown in a Google Drive folder. Obsidian is the main UI; claude.ai chat reaches it through the Drive connector; any agent can read it.

## Two axes — never mix them
- **Folder = what it is about** (domain). Capitalized, one level, from the list below.
- **`categories` = what kind of note it is** (Recipes, How-tos, Prompts, Notes). A link to a note in `categories/`, whose Base lists every note of that kind across all domains.
- Test for a new folder: if the name answers "what is it?" it is a category, not a domain.
- `tags` — finer topics inside a domain (`bios`, `ai`, `ukrainian`), plural, lowercase.

## Domains
- `Cooking/` — recipes, techniques, kitchen gear
- `Tech/` — devices, OS, BIOS, network, software, AI and prompts
- `Home/` — house, repairs, appliances, garden
- `Health/` — doctors, training, nutrition, medicines
- `Money/` — budget, taxes, insurance, purchases
- `Travel/` — trips, checklists, places
- `Learning/` — courses, books, explanations worth keeping

A note fits no domain → put it in the closest one and propose a new domain in one line. **Never create a top-level folder without the user's OK**; a new domain gets a line here and a folder note.
Subfolders (`Tech/network/`) only once a domain passes ~50–100 notes, and only with the user's OK.

## Service folders (lowercase, not domains)
- `inbox/` — captures to sort later (`/kb:triage`)
- `ideas/` — ideas with a status (`/kb:capture`, `/kb:brainstorm`); an idea with material grows into `ideas/<slug>/<slug>.md` + files
- `daily/` — `YYYY-MM-DD.md` daily notes; quick todos are `- [ ]` lines here
- `raw/` — sources kept verbatim (`/kb:ingest`); never edited
- `categories/` — one note per category, each a Base
- `templates/` — note templates (Obsidian Templates syntax)
- `attachments/` — images and files
- `tasks.md` — every open `- [ ]` in the vault

Search skips `raw/`, `templates/`, `attachments/` unless asked.

## Notes
- File name: `kebab-case-title.md`, unique in the vault, no dates (except `daily/` and `raw/`).
- Folder note `<Domain>/<Domain>.md` holds only the Base — no content that exists nowhere else.
- Frontmatter: `categories`, `summary` (one line: what it is — the catalog; there are no index files), `tags`, `aliases` (names in the other language and synonyms), `source`, `created`, `updated`; `applies-to` for anything version- or hardware-specific. Dates `YYYY-MM-DD`.
- One subject per note. Same subject again → **update the existing note**, don't create a twin.
- Current truth: rewrite outdated parts; keep a short `## History` only when the old way still matters.
- Instructions that change a system (BIOS, OS, network, car) always have **Check** and **Rollback**; risks in a `> [!warning]` callout.
- Links: `[[note-name]]` without a path, so moves never break them.

## Obsidian CLI (`obsidian`, needs the app running; always pass `vault=<name>` first)
Use it for anything that touches the link graph: `move`, `rename` (update links), `backlinks`, `unresolved`, `base:query`, `tasks todo`. Read, write and search with plain files.
No CLI → moving is safe with path-less links; renaming → rewrite `[[old-name]]` everywhere with grep.

## Language
Notes in the language the content came in (Ukrainian recipes stay Ukrainian). Titles may be either; put the other language in `aliases`.
