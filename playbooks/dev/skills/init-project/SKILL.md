---
name: init-project
description: Set up (or refresh) the AI infrastructure for a project folder — scan its repositories and stack, create the .ai/ knowledge base, the project CLAUDE.md and local settings, asking the user only what can't be inferred. Use when the user says init project, розгорни базу знань, set up .ai, onboard this project, or points at a project folder; with "refresh" after repos were added or changed.
argument-hint: "[project-folder] [refresh]"
---
# Initialise a project knowledge base

Templates live in this plugin: `templates/project/`, `templates/doc/`, `migrations/CURRENT` (two levels up from this skill's folder).
A project = one folder that contains one or more repositories (e.g. `Repos/SuperProject/`). It is the isolation boundary.

## 1. Scan (read-only, no questions yet)
- Project folder = argument, else the current directory. Confirm it is a project root, not a single repo inside one.
- Is the project folder itself a git repo? (decides step 3)
- Repos: every folder with `.git` up to depth 2, skipping `worktrees/`. For each: remote URL, default branch, last commit date, existing `CLAUDE.md` / `AGENTS.md` / `README`, `git worktree list` (note worktrees outside `<project>/worktrees/`).
- **Git host** per repo from the remote: web URL of the repo and the tool — `github.com`/GHE → `gh`; GitLab → `glab`; `dev.azure.com`/`*.visualstudio.com` → `az repos` (azure-devops extension); Bitbucket or mixed hosts → `gk` (GitKraken CLI/MCP, multi-provider). CLI first (cheaper, scriptable); an MCP server only when no CLI fits. Unknown/self-hosted host → ask.
- Tool check (read-only): installed (`<tool> --version`) and signed in (`gh auth status`, `glab auth status`, `az account show` + `az extension show -n azure-devops`; `gk` → its login status). Missing → recommend the install + login commands; never install yourself.
- Stack per repo: `*.sln`/`*.csproj` (.NET + target framework), `package.json` (Angular/Vue/React, scripts), `angular.json`, `docker-compose*`, `*.bicep`/`*.tf`, test projects, CI files (`.github/workflows`, `azure-pipelines.yml`).
- Build / test commands: from README, CI files, package.json scripts.
- Existing `.ai/` → stop and suggest `/dev:upgrade-project` (structure) or `refresh` (re-scan repos into CLAUDE.md incl. `Host · tool`, create `worktrees/`, add missing tool `ask` rules — nothing else).

## 2. Ask (one batch, only what you couldn't infer)
Show a short scan summary, then ask together:
1. Project name and one-line purpose; your role.
2. Tracker (Jira project key / URL), docs (Confluence / Drive), chat channels.
3. Environments: which databases/services exist (names only), which are allowed (local / test read-only), which are off-limits.
4. Paths or commands the agent must never touch.
5. Discovery-phase project (no code yet)? → add `assumptions.md`.
6. Confirm the detected build/test commands and the git host + tool per repo.

## 3. Create
- `.ai/` with `STATUS.md`, `context/glossary.md`, `decisions/`, `tasks/`, `inbox/`, `stash/`, `raw/`, `archive/`, `qa/regression.md` (from `templates/project/regression.md`), and `.ai/.ignore` from `templates/project/ignore`. Add `.gitkeep` to empty folders only if the project folder is itself a git repo (otherwise nothing tracks them; skills create missing folders on demand).
- Project `CLAUDE.md` from `templates/project/CLAUDE.md`, filled from the scan and answers (≤100 lines). Fill the managed block between `<!-- agent-playbook:kb:begin -->` and `<!-- agent-playbook:kb:end -->` with `templates/project/kb-section.md` verbatim — it is replaced on upgrades, so project-specific text goes outside it.
- `.ai/.playbook.json` from `templates/project/playbook.json`: `schema` = `migrations/CURRENT`, `playbook` = this plugin's version, dates = today.
  - If the project folder **is** a git repo, write it as `CLAUDE.local.md` instead and add `CLAUDE.local.md` and `.ai/` to that repo's `.gitignore` (ask first) — client knowledge must not be committed by accident.
- Repositories table in CLAUDE.md gets each repo's host link and tool.
- `worktrees/` folder at the project root (all task worktrees live there, see the KB rules). Worktrees found elsewhere → list them with the `git worktree move <old> <project>/worktrees/<repo>--<KEY>` command; move only on OK. Project folder is a git repo → add `worktrees/` to its `.gitignore` together with `.ai/`.
- `.claude/settings.local.json` from `templates/project/settings.local.json` + the user's never-touch paths as `deny` rules + `ask` rules for the detected tools' write commands (`glab mr create/merge`, `az repos pr create/update`, `gk` PR create — `gh` is in the template).
- Databases: don't write connection strings anywhere. Suggest the command to register each allowed DB as a local MCP server (`claude mcp add --scope local …`, secrets via env vars or 1Password `op run`) and put only the server names into CLAUDE.md.

## 4. Suggest, don't write
- Repos without their own `CLAUDE.md`: propose a short one (conventions, build/test, structure). Writing into a repo changes the team's code — only on explicit OK, otherwise offer `CLAUDE.local.md`.
- Seed `context/` from what you saw: `architecture.md` (repos and how they talk to each other) — show the draft, write on OK.

## 5. Finish
Print the created tree, the open TODOs left in CLAUDE.md, and how to start: open the project folder in VS Code (the folder itself, so Claude starts there) and run `/dev:start`.
