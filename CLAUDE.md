# agent-playbook — working on the playbooks themselves

This repo is a Claude Code plugin marketplace. Each folder in `playbooks/` is a plugin.
Read `docs/design.md` before changing behaviour; README for layout.

## Rules for editing
- A skill = `playbooks/<p>/skills/<name>/SKILL.md` with frontmatter `name` (= folder), `description` (when to use + trigger phrases, EN + UA), optional `argument-hint`. Body ≤40 lines, imperative steps.
- Templates: referenced from skills as "`templates/...` in this plugin". Keep them short; comments in `<!-- -->`.
- Cross-plugin references by slash name (`/kb:capture`), never by file path.
- Shared conventions (`.ai/` layout, limits, current-truth rule) live in `playbooks/dev/templates/project/CLAUDE.md` and `docs/design.md` — change both together.
- Agents: `playbooks/<p>/agents/<name>.md` — set `model`, `effort`, `tools`, `maxTurns`; end with the STATUS return contract. Plugin agents ignore `hooks`, `mcpServers`, `permissionMode`.
- Changing anything that lives inside projects (`.ai/` layout, `templates/project/kb-section.md`, `.ai/.ignore`) → add a migration and bump `migrations/CURRENT`.
- **Keep `docs/COMMANDS.md` current**: any added/removed/renamed skill or agent, changed arguments, trigger (auto vs manual), gates, model or outputs → update it in the same change; run `python scripts/check_commands.py`.
- `me` changed → `python scripts/pack.py me` and re-upload the zip in claude.ai (Customize → Plugins).
- After editing: bump `version` in that plugin's `plugin.json`; run `claude plugin validate .`.
- No project or personal data in this repo.
