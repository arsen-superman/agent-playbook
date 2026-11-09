---
name: upgrade-project
description: Bring a project's .ai/ knowledge base and project CLAUDE.md up to date with the current agent-playbook version — apply pending migrations and refresh the managed CLAUDE.md block. Use when the user says upgrade project, онови структуру, sync with playbook, or when start/lint reports an outdated KB schema.
argument-hint: "[project-folder | all] [dry-run]"
disable-model-invocation: true
---
# Upgrade a project knowledge base

Plugin files (two levels up from this skill's folder): `migrations/CURRENT`, `migrations/NNNN-*.md`, `templates/project/kb-section.md`.

1. **Targets** — argument folder; `all` → every folder listed under `Projects:` in `~/.claude/CLAUDE.md` (or scan that parent folder for `*/.ai/.playbook.json`); none → the current project.
2. **Read state** — `.ai/.playbook.json` (`schema`). Missing file → schema 0: the KB predates versioning; treat as needing the baseline (create the file, managed block markers if absent).
3. **Plan** (always shown, per project): pending migrations `schema+1 … CURRENT` with their one-line "what changes"; whether the managed CLAUDE.md block differs from `kb-section.md` (show a short diff). `dry-run` → stop here.
4. **Apply** on OK, per project:
   - each migration in order, following its Steps; run its Check; on failure stop that project and report — no partial schema bump.
   - replace everything between `<!-- agent-playbook:kb:begin -->` and `<!-- agent-playbook:kb:end -->` with `kb-section.md`. Markers missing → insert the block at the end and tell the user to delete the old hand-written KB section if there is one (show it; don't delete yourself).
   - `.ai/.ignore`, `settings.local.json`: add missing entries from `templates/project/`, never remove the user's.
   - update `.ai/.playbook.json`: `schema`, `playbook` (from the dev plugin.json version), `upgraded`.
5. **Report** ≤8 lines per project: from → to schema, what changed, manual follow-ups.
Never touch repositories, task content, context, or decisions beyond what a migration explicitly says.
