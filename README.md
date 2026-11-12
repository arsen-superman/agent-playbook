# agent-playbook

Personal playbooks for working with AI agents (Claude Code first, portable to any agent that reads Markdown).
The repo holds the **method** — skills, templates, rules. The **content** lives elsewhere: a `.ai/` knowledge base inside each project, and a personal vault for everyday knowledge.

```
agent-playbook/                    ← this repo = a Claude Code plugin marketplace
  .claude-plugin/marketplace.json
  playbooks/
    knowledge-base-core/  (kb)   core for every knowledge base: capture · brainstorm · triage · stash · unstash · ingest · lint
    dev-workflow/         (dev)  software development
            workflows (orchestrators): feature · bugfix · spike
            stages:    init-project · upgrade-project · start · new-task · spec · plan · implement
                       review · fix-bug · verify · research · handoff · park · resume · close-task
            agents:    analyst · planner · implementer · debugger · reviewer · verifier · researcher · scout
            migrations/  project KB structure changes
    personal-vault/       (me)   personal vault: init-vault · save · find
    code-graph/   (code-graph)   optional: cross-repo code graph MCP server for a project · reindex
  user/CLAUDE.md.example          ← your global ~/.claude/CLAUDE.md
  docs/COMMANDS.md                ← cheat sheet of every command (keep current)
  docs/design.md                  ← principles and why
  scripts/                        ← pack.py (zip for claude.ai), check_commands.py, check_frontmatter.py
```

## Install (once per machine)

**Claude Code (CLI / VS Code)** — from GitHub:

```bash
claude plugin marketplace add <github-user>/agent-playbook
claude plugin install kb@agent-playbook
claude plugin install dev@agent-playbook
claude plugin install me@agent-playbook
```

`dev` is only useful inside project folders, and every enabled skill costs context on each turn — keep it off elsewhere and turn it on per project:

```bash
claude plugin disable dev@agent-playbook --scope user    # once
claude plugin enable dev@agent-playbook --scope local    # in each project folder, before /dev:init-project
```

`code-graph` (optional, for projects with several repos) is never installed for the user — only per project, from the project folder: `claude plugin install code-graph@agent-playbook --scope local`. `/dev:init-project` prints that command when you accept the code graph. It runs the [`cross-repo-graph`](https://github.com/arsen-superman/cross-repo-graph) MCP server and needs Node 22+ and [uv](https://docs.astral.sh/uv/).

`/dev:init-project` also writes the enablement into the project's `.claude/settings.local.json`, so existing projects get it from `/dev:upgrade-project`.

Or clone the repo and add the local folder instead (`claude plugin marketplace add /path/to/agent-playbook`) — then edits apply at the next session start or after `/reload-plugins`, no reinstall.

Optional: copy [`user/CLAUDE.md.example`](user/CLAUDE.md.example) into your `~/.claude/CLAUDE.md` (merge if you have one; you don't need to clone the repo — just copy the text from GitHub) and fill in the `<placeholders>`. The playbooks work without it; `/me:init-vault` adds the vault path for you.

Skills are namespaced by the plugin's `name`, not its folder or display name: Dev Workflow → `/dev:start`, Knowledge Base Core → `/kb:capture`, Personal Vault → `/me:save`. Most also trigger on their own from what you say; rare, deliberate ones (`init-project`, `upgrade-project`, `init-vault`, `lint`, `triage`, the `*-workflow` orchestrators) are manual-only — type them, their descriptions stay out of the context.

**Keep [`docs/COMMANDS.md`](docs/COMMANDS.md) handy** — it is the cheat sheet of every command and agent (arguments, triggers, gates, models, outputs). Bookmark it on GitHub or save a copy next to your notes; it is the quickest way to remember what to type.

### Claude Desktop (claude.ai)

Two ways, both under **Customize → Plugins**:

- **From the GitHub repo** — add this repo as a marketplace (`<github-user>/agent-playbook`), then install **Knowledge Base Core** (`kb`), **Dev Workflow** (`dev`) and **Personal Vault** (`me`).
- **From a zip (`dist`)** — build it yourself and upload:
  ```bash
  python scripts/pack.py me kb dev      # → dist/<name>-<version>.zip (default: me)
  ```
  Then **Customize → Plugins → Add → Upload plugin** and pick a zip. `dist/` is git-ignored, so each person builds their own; re-pack and re-upload after you change a playbook.

Dev Workflow and Knowledge Base Core lean on file access and subagents, so they are at their best in Claude Code; Personal Vault works well in Desktop.

## Configure the workflow agents

Every agent in the `/dev:feature-workflow`, `/dev:bugfix-workflow` and `/dev:spike-workflow` workflows is one Markdown file in [`playbooks/dev-workflow/agents/`](playbooks/dev-workflow/agents/). Its frontmatter controls how it runs:

```yaml
model: opus        # opus | sonnet | haiku | a full model ID
effort: high       # low | medium | high | xhigh | max
maxTurns: 60       # turn limit for one run
tools: Read, Grep, Glob, Bash, Write, Edit
```

Defaults: judgement on `opus` — analyst and planner at `medium`, reviewer and debugger at `high`; execution and evidence on `sonnet` — implementer and verifier at `medium`, researcher at `high`, scout at `low`. Want cheaper or faster runs? Drop a stage to `sonnet`/`medium`. Want deeper analysis? Raise `effort`.

Where to edit depends on how you installed:

- **Cloned repo / local marketplace** — edit the file in your clone, then `/reload-plugins`.
- **Installed from GitHub** — fork the repo, edit your fork, and install from it. (Edits inside the plugin cache are overwritten on update.)

Bump `version` in the plugin's `plugin.json` after changing agents so installs pick up the update.

## Daily use

**Development project** (e.g. `Repos/SuperProject/` with several repos):

```
open Repos/SuperProject in VS Code → Claude Code or in Claude CLI from project folder
/dev:init-project                 once: scans repos, creates .ai/, CLAUDE.md, local settings
/dev:new-task IPR-4001            → /dev:spec → /dev:plan → /dev:implement → /dev:verify → /dev:close-task
/dev:start IPR-4001               every session        /dev:handoff   end of every session (optional)
/kb:stash  /kb:unstash            switch context for a while (consume-once)
/dev:park  /dev:resume            freeze a task for weeks
/kb:capture  /kb:triage           side findings → inbox → sorted later
/kb:capture  /kb:brainstorm       "ідея: …" → ideas/ → think it through, verdict, promote
/kb:ingest  /kb:lint              meeting notes/docs into the KB · weekly health check
```

**Personal vault**:

```
/me:init-vault ~/Documents/Vault     once; again after a plugin update (refreshes templates, upgrades an older layout)
"save this recipe" / /me:save        from any session
"how did I undervolt the CPU?"         /me:find
"купити фільтр" / /kb:capture         plain todo → today's daily note; _tasks.md collects all open ones
```

The vault is plain Markdown in a Google Drive folder, with [Obsidian](https://obsidian.md) as the main UI: one level of capitalized domain folders (`Tech/`, `Cooking/`, …), each opening as a table (Folder Notes + Bases); `categories` (Recipes, How-tos, Prompts, Notes) cut across domains. `/me:init-vault` walks you through the Obsidian side: settings, the Folder Notes plugin, the Obsidian CLI (keeps links intact when agents move or rename notes), Android sync, and optional [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) (`obsidian-bases`, `defuddle`). Without Obsidian everything still works — agents and claude.ai read the same files.

## Workflows — one session, every stage in a subagent

```
/dev:feature-workflow IPR-4001   analyst → GATE → planner → GATE → implementer (per phase) → reviewer ⟲ → verifier → GATE (PR)
/dev:bugfix-workflow IPR-4002   debugger (repro, root cause, failing test) → GATE (fix option) → implementer → reviewer → verifier → GATE
/dev:spike-workflow  "<question>"  frame → GATE → researcher ×N in parallel → synthesis → GATE (decision record)
```

The session you type in is the orchestrator: it only reads each agent's STATUS block and `task.md`, so its context stays small.
Each agent has its own model, effort, tools and turn limit (`playbooks/dev-workflow/agents/*.md`). Single stages stay available as skills (`/dev:spec`, `/dev:plan`, …) for manual work.

## Code graph — optional, for projects with several repos

The `code-graph` plugin gives agents a graph of every repo in the project: classes, methods and calls, plus the links *between* repos. Those links are HTTP calls from client to endpoint, service addresses from config, and NuGet/npm packages, each with `file:line` on both sides. Scouts and reviewers then answer "who calls this endpoint, who reads this field, in which repo" from the graph instead of grepping every repo. The graph also catches calls grep misses: URLs assembled from config and generated clients. It is the [`cross-repo-graph`](https://github.com/arsen-superman/cross-repo-graph) MCP server, local, with no LLM.

```
/dev:init-project                   say yes to "Code graph" (default with 2+ repos) → it enables the plugin for the project
claude plugin install code-graph@agent-playbook --scope local    once, in the project folder (never --scope user)
restart Claude                      /mcp lists plugin:code-graph:code-graph; the first index builds in the background
/code-graph:reindex                 rebuild now and see the result (normally not needed)
```

- **Requirements.** Node 22+ and [uv](https://docs.astral.sh/uv/) (`winget install astral-sh.uv`). The indexer runs [Graphify](https://github.com/Graphify-Labs/graphify) through `uvx`.
- **What is indexed.** Every repo one or two levels below the project folder, read **from git, not from your clones**, so it doesn't matter which branch you have checked out or whether you work in `worktrees/`. There are two scopes. `dev` is `develop`, used for features, bugs and spikes. `prod` is `main`/`master`, i.e. production, used for hotfixes. A task picks its scope from `base:` in `task.md`. Repos with other branches are set in `.ai/.index/config.json`.
- **Freshness.** Each session start fetches the scope branches (`origin/*` only, at most every 30 min, never asks for a password — a remote that needs one is skipped with a warning and indexed from local refs) and re-indexes in the background only what moved. A first index of ~10 repos takes ~3 min, and an unchanged project re-checks in seconds. Background log: `.ai/.index/index.log`.
- **What it doesn't show.** The task's own branch. Reviewers read the diff for what changed and use the graph for who *outside* the diff depends on it.
- **Turn it off.** `claude plugin disable code-graph@agent-playbook --scope local` and delete `.ai/.index/`, which is derived and rebuilt on demand.

## Updating projects after changing this repo

- Skills, agents, rules → nothing to do: every project uses them from the plugin (next session / `/reload-plugins`).
- Project-side structure (`.ai/` layout, the managed KB block in the project CLAUDE.md, `.ai/.ignore`) → `/dev:upgrade-project` (one project) or `/dev:upgrade-project all`. Each project records its schema in `.ai/.playbook.json`; `/dev:start` and `/kb:lint` tell you when it is behind.
- When you change project-side structure: add `playbooks/dev-workflow/migrations/NNNN-*.md`, bump `migrations/CURRENT` (see `migrations/README.md`).

## Add a playbook

1. `playbooks/<display-name>/.claude-plugin/plugin.json`: the folder is the kebab-case `displayName` (`Personal Vault` → `personal-vault/`); `name` is the short slash prefix (`me`).
2. `skills/<skill>/SKILL.md`, templates in `templates/`, agents in `agents/`.
3. Add an entry to `.claude-plugin/marketplace.json` (`name` + `source` folder), then `claude plugin install <name>@agent-playbook`.
Reuse Knowledge Base Core (`kb`) for inbox/stash/ingest/lint instead of copying them.

## Safety

This repo contains no project data and can be pushed anywhere.

## Welcome

Feel free to download, use, and fork this repo — make it yours. If it saves you some time, don't forget to leave a ⭐ on GitHub. Issues and ideas are welcome too.

Happy building, and tokens for everyone! 🚀
