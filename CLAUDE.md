# agent-playbook — working on the playbooks themselves

This repo is a Claude Code plugin marketplace. Each folder in `playbooks/` is a plugin; the folder is named after its `displayName`, the slash prefix comes from `name` in `plugin.json` (`kb`, `dev`, `me`, `product`).
Read `docs/design.md` before changing behaviour; README for layout.

## Rules for editing
- A skill = `playbooks/<p>/skills/<name>/SKILL.md` with frontmatter `name` (= folder), `description` (when to use + trigger phrases, EN + UA), optional `argument-hint`. Body ≤40 lines and ≤3500 characters unless the skill has `disable-model-invocation: true` (run by hand only, never preloaded into context — no limit), imperative steps. `description` ≤350 characters. Orchestrators (workflows) are always `disable-model-invocation: true`.
- Frontmatter must be valid YAML: always wrap `description` in double quotes (it contains `: ` in "Triggers:"/"Manual:"); quote any value with `{{…}}`, `: ` or `#`. Run `python scripts/check_frontmatter.py` after editing any `.md` (the pre-commit hook in `.githooks/` runs it too; enable once per clone: `git config core.hooksPath .githooks`).
- Templates: referenced from skills as "`templates/...` in this plugin". Keep them short; comments in `<!-- -->`.
- Cross-plugin references by slash name (`/kb:capture`), never by file path.
- Text several plugins need (orchestration rules, the agent return contract) lives in `shared/`; `shared/manifest.json` says where it is copied (`templates/shared/` of a plugin) or must appear verbatim (agents). Edit the source, then `python scripts/sync_shared.py`; never edit a copy. An orchestrator refers to "`templates/shared/orchestration.md` in this plugin".
- Shared conventions (`.ai/` layout, limits, current-truth rule) live in `playbooks/dev-workflow/templates/project/CLAUDE.md` and `docs/design.md` — change both together.
- Agents: `playbooks/<p>/agents/<name>.md` — set `model`, `effort`, `tools`, `maxTurns`; end with the STATUS return contract (`shared/agent-contract.md`, verbatim). Plugin agents ignore `hooks`, `mcpServers`, `permissionMode`.
- Changing anything that lives inside projects (`.ai/` layout, `templates/project/kb-section.md`, `.ai/.ignore`) → add a migration and bump `migrations/CURRENT`.
- **Keep `docs/COMMANDS.md` current**: any added/removed/renamed skill or agent, changed arguments, trigger (auto vs manual), gates, model or outputs → update it in the same change; run `python scripts/check_commands.py`.
- `me` changed → `python scripts/pack.py me` and re-upload the zip in claude.ai (Customize → Plugins).
- After editing: bump the **patch** number of `version` in that plugin's `plugin.json` (0.1.0 → 0.1.1), also for new skills or agents — minor/major only when I ask. Once per uncommitted change set: already bumped in the working tree → don't bump again. Run `claude plugin validate .`.
- No project or personal data in this repo.
