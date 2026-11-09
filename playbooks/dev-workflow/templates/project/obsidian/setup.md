# Obsidian add-on for a project KB — setup checklist
<!-- Shown by /dev:init-project when the user opts in. The user clicks; Claude does not edit .obsidian/. -->

## Open
- Open **`.ai/` itself** as a vault, not the project folder: Obsidian hides dot-folders, and the repos would flood search and the graph.

## Settings
- Files & links → Use [[Wikilinks]]: **off**; New link format: **Relative path to file**; Automatically update internal links: **on**.
- Core plugins on: **Bases**, **Graph view**, **Backlinks**.
- Excluded files: `raw/`, `stash/.consumed/`, `inbox/_done/`.
- Graph view → Groups (colour by): `path:tasks`, `path:archive`, `path:decisions`, `path:ideas`, `path:context`. Many files are named `task`/`spec`/`plan` — use the **local graph** of a `task.md` to see one task with its research, idea and decisions.

## Use
- `views.md` — tasks by status and by repo, archive, current and superseded decisions, ideas.
- Search: `path:archive <term>`, `[repos:billing-api]`, `[status:superseded]`.

## Drop it
- Delete `.ai/.obsidian/` and `.ai/views.md`. Nothing else depends on Obsidian.
