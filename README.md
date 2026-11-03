# agent-playbook

Personal playbooks for working with AI agents (Claude Code first, portable to any agent that reads Markdown).
The repo holds the **method** — skills, templates, rules. The **content** lives elsewhere: a `.ai/` knowledge base inside each project, and a personal vault for everyday knowledge.

```
agent-playbook/                    ← this repo = a Claude Code plugin marketplace
  .claude-plugin/marketplace.json
  playbooks/
    kb/     core for every knowledge base: capture · triage · stash · unstash · ingest · lint
    dev/    software development
            workflows (orchestrators): feature · bugfix · spike
            stages:    init-project · upgrade-project · start · new-task · spec · plan · implement
                       fix-bug · verify · research · handoff · park · resume · close-task
            agents:    analyst · planner · implementer · debugger · reviewer · verifier · researcher
            migrations/  project KB structure changes
    me/     personal vault: init-vault · save · find
  user/CLAUDE.md.example          ← your global ~/.claude/CLAUDE.md
  docs/COMMANDS.md                ← cheat sheet of every command (keep current)
  docs/design.md                  ← principles and why
  scripts/                        ← pack.py (zip for claude.ai), check_commands.py
```

## Install (once per machine)

**Claude Code (CLI / VS Code)** — from GitHub:

```bash
claude plugin marketplace add <github-user>/agent-playbook
claude plugin install kb@agent-playbook
claude plugin install dev@agent-playbook
claude plugin install me@agent-playbook
```

Or clone the repo and add the local folder instead (`claude plugin marketplace add /path/to/agent-playbook`) — then edits apply at the next session start or after `/reload-plugins`, no reinstall.

Optional: copy [`user/CLAUDE.md.example`](user/CLAUDE.md.example) into your `~/.claude/CLAUDE.md` (merge if you have one; you don't need to clone the repo — just copy the text from GitHub) and fill in the `<placeholders>`. The playbooks work without it; `/me:init-vault` adds the vault path for you.

Skills are namespaced by playbook: `/dev:start`, `/kb:capture`, `/me:save`. Most also trigger on their own from what you say.

**Keep [`docs/COMMANDS.md`](docs/COMMANDS.md) handy** — it is the cheat sheet of every command and agent (arguments, triggers, gates, models, outputs). Bookmark it on GitHub or save a copy next to your notes; it is the quickest way to remember what to type.

### Claude Desktop (claude.ai)

Two ways, both under **Customize → Plugins**:

- **From the GitHub repo** — add this repo as a marketplace (`<github-user>/agent-playbook`), then install `kb`, `dev`, `me`.
- **From a zip (`dist`)** — build it yourself and upload:
  ```bash
  python scripts/pack.py me kb dev      # → dist/<name>-<version>.zip (default: me)
  ```
  Then **Customize → Plugins → Add → Upload plugin** and pick a zip. `dist/` is git-ignored, so each person builds their own; re-pack and re-upload after you change a playbook.

`dev` and `kb` lean on file access and subagents, so they are at their best in Claude Code; `me` (personal vault) works well in Desktop.

## Configure the workflow agents

Every agent in the `/dev:feature`, `/dev:bugfix` and `/dev:spike` workflows is one Markdown file in [`playbooks/dev/agents/`](playbooks/dev/agents/). Its frontmatter controls how it runs:

```yaml
model: opus        # opus | sonnet | haiku | a full model ID
effort: high       # low | medium | high | xhigh | max
maxTurns: 60       # turn limit for one run
tools: Read, Grep, Glob, Bash, Write, Edit
```

Defaults: `opus`/`high` for analyst, planner, implementer, debugger and reviewer (the stages where quality matters most); `sonnet` for the lighter ones. Want cheaper or faster runs? Drop a stage to `sonnet`/`medium`. Want deeper analysis? Raise `effort`.

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
/kb:ingest  /kb:lint              meeting notes/docs into the KB · weekly health check
```

**Personal vault**:

```
/me:init-vault ~/Documents/Vault     once
"save this recipe" / /me:save        from any session
"how did I undervolt the CPU?"         /me:find
```

## Workflows — one session, every stage in a subagent

```
/dev:feature IPR-4001   analyst → GATE → planner → GATE → implementer (per phase) → reviewer ⟲ → verifier → GATE (PR)
/dev:bugfix  IPR-4002   debugger (repro, root cause, failing test) → GATE (fix option) → implementer → reviewer → verifier → GATE
/dev:spike   "<question>"  frame → GATE → researcher ×N in parallel → synthesis → GATE (decision record)
```

The session you type in is the orchestrator: it only reads each agent's STATUS block and `task.md`, so its context stays small.
Each agent has its own model, effort, tools and turn limit (`playbooks/dev/agents/*.md`). Single stages stay available as skills (`/dev:spec`, `/dev:plan`, …) for manual work.

## Updating projects after changing this repo

- Skills, agents, rules → nothing to do: every project uses them from the plugin (next session / `/reload-plugins`).
- Project-side structure (`.ai/` layout, the managed KB block in the project CLAUDE.md, `.ai/.ignore`) → `/dev:upgrade-project` (one project) or `/dev:upgrade-project all`. Each project records its schema in `.ai/.playbook.json`; `/dev:start` and `/kb:lint` tell you when it is behind.
- When you change project-side structure: add `playbooks/dev/migrations/NNNN-*.md`, bump `migrations/CURRENT` (see `migrations/README.md`).

## Add a playbook

1. `playbooks/<name>/.claude-plugin/plugin.json` (`name` = folder name).
2. `skills/<skill>/SKILL.md`, templates in `templates/`, agents in `agents/`.
3. Add an entry to `.claude-plugin/marketplace.json`, then `claude plugin install <name>@agent-playbook`.
Reuse `kb` for inbox/stash/ingest/lint instead of copying them.

## Safety

This repo contains no project data and can be pushed anywhere.

## Welcome

Feel free to download, use, and fork this repo — make it yours. If it saves you some time, don't forget to leave a ⭐ on GitHub. Issues and ideas are welcome too.

Happy building, and tokens for everyone! 🚀
