# Project KB migrations

Skills, agents and rules update by themselves (they live in the plugin). Migrations are only for what lives **inside projects**:
`.ai/` layout, the managed block in the project `CLAUDE.md`, `.ai/.ignore`, `.claude/settings.local.json` defaults.

- `CURRENT` — the schema number new projects get. Bump it only when project-side structure changes.
- Each project records its schema in `.ai/.playbook.json`.
- `/dev:upgrade-project` applies `NNNN-*.md` files with a number above the project's schema, in order, then refreshes the managed CLAUDE.md block from `templates/project/kb-section.md` (this happens on every upgrade, even with no migrations).

## Writing a migration — `NNNN-short-slug.md` (NNNN = new schema number)
```markdown
# NNNN — <what changes>
Why: <one line>
## Steps (idempotent — safe to run twice)
1. <create / move / rename, with exact paths under .ai/>
## Check
- <how to confirm it applied>
## Manual follow-up (if any)
- <what the user must decide>
```
Rules: never delete user content — move it and report; never touch anything outside `.ai/`, the managed block, `.ai/.ignore`, `.claude/settings.local.json` (add-only).
