# agent-playbook — commands cheat sheet

For you and for any agent. Kept in sync with `playbooks/` (see *Maintenance* at the end).

- Commands are `/<playbook>:<skill>`. Type `/` in Claude Code to see them.
- 🤖 = Claude also starts it by itself when your words match (e.g. "запиши на потім" → `/kb:capture`). ⌨ = only when you type the command (expensive or rare).
- Arguments in `<>` are required, in `[]` optional.

## Typical days

| Situation | Do |
|---|---|
| New project folder | `claude plugin enable dev@agent-playbook --scope local`, then `/dev:init-project` once |
| Continue earlier work | `/dev:start-task [KEY]` (not needed when starting something new) |
| Work with no ticket yet | `/dev:new-task "description"` → `LOCAL-n`, then as usual |
| New ticket, do it all in one go | `/dev:feature-workflow KEY` · `/dev:bugfix-workflow KEY` · `/dev:spike-workflow "question"` |
| New ticket, step by step | `/dev:new-task KEY` → `/dev:spec` → `/dev:plan` → `/dev:implement` → `/dev:verify` → `/dev:close-task` |
| New requirements / clarifications for a task in progress or in review | `/dev:change-request KEY "…"` |
| Reviewers left comments on the PR | `/dev:pr-comments KEY` |
| PR merged | `/dev:close-task KEY` (archive, STATUS, branches and worktrees) |
| End of every session | `/dev:handoff` (no task in the session → `/kb:stash`) |
| Switch to something else for a while | `/kb:stash name` … later `/kb:unstash name` |
| Task blocked for days/weeks | `/dev:pause-task KEY reason` … later `/dev:start-task KEY` |
| Noticed something unrelated | just say "запиши на потім" → `/kb:capture` |
| Free half hour | `/kb:triage` |
| An idea came up (also from the phone) | just say "ідея: …" → `/kb:capture`; later `/kb:brainstorm` |
| Meeting notes / doc / epic to digest | `/kb:ingest <file or paste>` |
| Weekly | `/kb:lint` |
| After changing agent-playbook structure | `/dev:upgrade-project all` |
| Code graph looks stale / after a big merge | `/code-graph:reindex` (normally re-indexed at session start) |
| "Save this recipe / instruction" | `/me:save` |
| "How did I … ?" | `/me:find` |

## dev — software development

### Workflows (one session, each stage in a subagent, you approve at gates)
Diagram of who runs when (models, scouts, reuse, gates): [design.md → Feature workflow — agent map](design.md#feature-workflow--agent-map).

| Command | When | What happens |
|---|---|---|
| ⌨ `/dev:feature-workflow <KEY \| task \| description> [auto]` | a feature end to end | analyst → **GATE A** questions → planner → **GATE B** plan → implementer per phase → reviewer → you pick minors to fix (≤2 fix rounds, logged in `review.md`) → verifier → **GATE C** push/PR. `auto` skips B for small plans. Resumable: `/dev:start-task` continues at the saved stage |
| ⌨ `/dev:bugfix-workflow <KEY \| task \| description>` | a bug end to end | debugger (repro, root cause, failing test) → **GATE A** pick fix → implementer → reviewer → verifier → **GATE C** |
| 🤖 `/dev:change-request <KEY> <text \| file \| url>` | new requirements, clarifications, edge cases after the spec (also with a PR open) | appends a dated Update to Raw requirement → analyst classifies items (covered+tested / no test / new / conflict) and sizes them → **GATE A** → planner adds TCs + one Amend phase (**GATE B** unless ≤3 steps) → implementer → reviewer (whole PR diff, focus on amend) → verifier (full regression) → **GATE C** PR update + Jira |
| 🤖 `/dev:pr-comments [KEY]` | PR has review comments | fetches unresolved threads (`gh` / connector / paste) → one `review.md` row each: fix / reply / discuss / follow-up (requirement-like comments start as discuss; amend only when the user explicitly confirms) → **GATE** → PR-feedback phase by F-ID via implementer (+ reviewer verifying those rows and verifier for logic changes) → drafted replies, one per comment thread → **GATE C** choose push + replies / push only / replies only; resolve on explicit OK → proposed `<repo>/REVIEW.md` lines for team conventions |
| ⌨ `/dev:spike-workflow <question \| KEY> [timebox]` | choose between options before building | frame + sub-questions → **GATE A** → researcher ×N in parallel → synthesis → **GATE B** → decision record in `.ai/decisions/`, follow-ups |

### Project setup and maintenance
| Command | When | What happens |
|---|---|---|
| ⌨ `/dev:init-project [folder] [refresh]` | first time in a project folder; `refresh` after repos change or a playbook update adds project settings (hosts, worktrees) | scans repos, stack and git host per repo (link + tool `gh` / `glab` / `az repos` / `gk`, checks it's installed and signed in, recommends install; also checks Python 3, needed only for the generated inbox index), language server per stack (LSP plugin enabled in `settings.local.json`, install commands for missing binaries/plugins), asks what it can't infer, creates `.ai/`, `worktrees/`, project `CLAUDE.md`, `.claude/settings.local.json`, `.ai/.playbook.json`; optional Obsidian add-on on request (`.ai/views.md` + setup checklist); code graph add-on (default yes with 2+ repos: enables `code-graph` per project); suggests (doesn't write) repo CLAUDE.md files and DB MCP setup |
| ⌨ `/dev:upgrade-project [folder \| all] [dry-run]` | after agent-playbook changed project-side structure; when start/lint says "outdated" | applies pending migrations, refreshes the managed KB block in CLAUDE.md (and `.ai/views.md` if the Obsidian add-on is on), bumps `.ai/.playbook.json` |

### Session and task lifecycle
| Command | When | What happens |
|---|---|---|
| 🤖 `/dev:start-task [KEY]` | beginning of every session | reads STATUS + task card + plan up to Next; reports where things are, inbox/stash counts, staleness, outdated KB; task in review → PR merged / new comments; paused task → "while you were away" (Jira, branch drift, re-checked facts), updates spec/plan, back to Active on OK |
| 🤖 `/dev:new-task <KEY \| description> [from LOCAL-n]` | new ticket; work with no ticket yet (→ `LOCAL-n`, tracked like any task); a LOCAL task got a ticket (`IPR-123 from LOCAL-2`) | fetches Jira, creates `.ai/tasks/<KEY-slug>/` with `task.md` (incl. `branch:` and `base:` — `main`/`master` for a production hotfix) and raw requirement, adds to STATUS; on `from` renames the LOCAL task to the ticket key (can draft the Jira ticket for you, created only on OK) |
| 🤖 `/dev:handoff [KEY]` | end of every session, or when context gets long | rewrites task Now/Next, ticks plan, promotes decisions/knowledge, captures leftovers, updates STATUS |
| 🤖 `/dev:pause-task <KEY> [reason]` | blocked / missing data / priorities changed | handoff + WIP commit on the branch + **Paused** block (why, unblocks when, volatile facts) + STATUS → Paused |
| 🤖 `/dev:close-task <KEY>` | "PR merged" / done / cancelled | confirms the merge, runs handoff (incl. cleanup and self-improvement), promotes decisions, knowledge and regression test cases (→ `.ai/qa/regression.md`), writes Outcome, moves to `.ai/archive/` trimmed to what and why (task Goal/Outcome, spec rules/AC/edge cases/decisions, plan approach), updates STATUS; on one OK removes the task's worktrees (asks before `--force`), local and remote branches |

### Single stages (manual, in this session — the workflows use the same procedures)
| Command | What it produces |
|---|---|
| 🤖 `/dev:spec [KEY]` | `spec.md`: AS-IS with file:line, rules (permission matrix when claims are touched), AC (every endpoint returning a new field), edge cases, open questions. No code |
| 🤖 `/dev:plan [KEY]` | scouts reuse, class sizes, call frequency and the closest existing feature first → `test-cases.md` (cases per AC, level unit/integration/e2e/manual) + `plan.md`: options (only for a real choice), approach, placement, cross-cutting risk classes, phased commit-sized steps each with a verify check, every risk closed by a step or your decision; asks approval |
| 🤖 `/dev:review [KEY]` | `review.md`: every finding (F-ID, risk class, severity, file:line, fix) from a review of the branch diff against spec, plan, risk classes and `<repo>/REVIEW.md`; delegates to `dev:reviewer` if this session wrote the code |
| 🤖 `/dev:implement [KEY] [all \| phase N]` | code + one commit per step, ticks with hashes; one phase per call by default; never pushes |
| 🤖 `/dev:fix-bug [KEY]` | reproduce → root cause → failing test → minimal fix → verification note |
| 🤖 `/dev:verify [KEY]` | executes `test-cases.md` (automated + what it can run itself), adds missing cases, records a run, leaves UI/human cases `⏳ for QA` and drafts a QA handoff (Jira comment on OK); delegates to `dev:verifier` if this session wrote the code |
| 🤖 `/dev:research <question> [KEY]` | `research/<topic>.md`: answer, evidence, confidence, implications |

### Agents (called by workflows; you can also say "use dev:reviewer on IPR-123")
| Agent | Model / effort | Does | Writes |
|---|---|---|---|
| `dev:analyst` | opus / medium | requirements vs code → spec (code reading via scouts) | spec.md |
| `dev:planner` | opus / medium | spec → test design + plan (reuse, class-size, frequency and symbol checks via scouts) | test-cases.md, plan.md |
| `dev:implementer` | sonnet / medium | one phase of the plan | code, commits, plan ticks |
| `dev:debugger` | opus / high | repro, root cause, failing test (no fix); wide searches via scouts | spec AS-IS, test-cases.md TC-01, test commit |
| `dev:reviewer` | opus / high; fix rounds the same, whole diff with focus on fix commits | `/dev:review`: conformance to spec and plan plus independent quality over the risk classes plus a spec-independent pass over each changed decision point (plan/spec-level flaws flagged); reuse search; applies `<repo>/REVIEW.md`; blocks edits to a bug's failing test; no cap on findings | review.md |
| `dev:verifier` | sonnet / medium | executes test cases, proposes missing ones | nothing (orchestrator records the run in test-cases.md) |
| `dev:researcher` | sonnet / high | one research question | research/<topic>.md |
| `dev:scout` | sonnet / low | one narrow read-only question about code, answered with `file:line` facts; called by analyst, planner, debugger, researcher | nothing (returns facts) |
Every agent returns `STATUS / ARTIFACTS / SUMMARY / QUESTIONS / CAPTURED`. Code-reading agents use the `LSP` tool for symbols (definitions, references, callers) when the project has a language server, grep for the rest.

## kb — any knowledge base (project `.ai/` or the personal vault)
| Command | When | What happens |
|---|---|---|
| 🤖 `/kb:capture <what>` | your idea ("ідея: …"); something outside the current task: bug, todo, question, finding | your idea → `ideas/<slug>.md` (`status: raw`), reply `💡 title`; a plain todo in the vault → `- [ ]` in today's `daily/` note, reply `☑️`; anything else (incl. ideas Claude noticed itself) → one small file in `inbox/` from the shared `inbox-item.md` template (type, `severity` for bugs, required `area`; empty = `n/a`; no priority), reply `📥 title` (project KB: a hook then rebuilds the generated `inbox/INDEX.md`); work continues. Works from claude.ai on the phone (vault via Google Drive) |
| 🤖 `/kb:brainstorm [idea]` | time to think an idea through | no argument → lists ideas of the current KB (project `.ai/` or vault, never both) and asks which; dialogue on goal, options, risks, cheapest test → rewrites the idea file: status, verdict, value, effort, next; in the vault an idea with material becomes `ideas/<slug>/` (card + files); offers promote (`/dev:new-task`, new project) on OK. Works from the phone |
| ⌨ `/kb:triage [filter: type / severity / area]` | inbox grew / free time | table of items grouped by area (type, severity, source, age), one proposed outcome each (now / task / ticket / checklist (vault) / knowledge / decision / idea / hold / drop); you confirm in one reply; task and ticket items → `inbox/_done/` with `resolution`, hold → `status: in-progress` + `next`, the rest deleted |
| 🤖 `/kb:stash [name]` | switching context; task-less exploration to continue in a fresh session instead of compacting | ≤40-line snapshot in `stash/` |
| 🤖 `/kb:unstash [name]` | coming back | restores it into the session, reports drift, consumes it (kept 14 days in `.consumed/`) |
| 🤖 `/kb:ingest <file \| url \| text>` | meeting notes, transcript, doc, epic | keeps source in `raw/` (web pages via `defuddle` if installed), proposes facts / decisions / todos / questions, files them on OK |
| ⌨ `/kb:lint [fix]` | weekly | sizes (incl. context files ≤300), history-instead-of-truth, contradictions, copies of repo docs, contradicting or dangling superseded decisions, missing or unknown repo tags, stale/orphan items, old inbox/stash, inbox items off the template (skips generated `INDEX.md`), secrets, outdated KB structure; vault: broken links (Obsidian CLI), notes without `summary`/`categories`, stray folders |

## code-graph — code graph across a project's repos (optional add-on, installed per project: `--scope local`)
The [`cross-repo-graph`](https://github.com/arsen-superman/cross-repo-graph) MCP server: an AST graph of every repo plus cross-repo links (HTTP client → endpoint with `used` / `declared-only`, config addresses per environment, NuGet/npm packages) with `file:line`. Index in `.ai/.index/`, one graph per scope read from git (not from the clones on disk): `dev` = `develop`, `prod` = `main`/`master` — agents use `prod` when the task's `base:` is `main`/`master` (hotfix). At session start, in the background: `git fetch` of the scope branches (only `origin/*`, at most every 30 min, never prompts; a remote that needs a password is skipped and indexed from local refs) and re-indexing of what moved. Branch overrides per repo: `.ai/.index/config.json`. Needs Node 22+ and uv. Agents (scout, analyst, planner, researcher, reviewer) use its tools for cross-repo questions: `dependencies`, `get_neighbors`, `query_graph`, `get_node`, `shortest_path`, `architecture_hubs`, `list_repos`.

| Command | When | What happens |
|---|---|---|
| ⌨ `/code-graph:reindex [force]` | the graph looks stale, after a big merge, or to see indexing errors | fetches the scope branches and rebuilds `.ai/.index/` in the foreground (`force` re-parses every repo); reports fetch, repos per scope, links, failures; the server picks it up without a restart |

## me — personal vault (`G:\My Drive\Vault`; in claude.ai chat via the Drive connector)
| Command | When | What happens |
|---|---|---|
| ⌨ `/me:init-vault [path]` | once; again after a plugin update or to upgrade an older layout | creates capitalized domain folders with folder-note Bases, `_`-prefixed service folders (sorted above domains), `_categories/`, `_tasks.md`, vault `_templates/`; moves an older layout (unprefixed service folders, lowercase areas, index files, type folders) on OK; registers the path in `~/.claude/CLAUDE.md`; walks through Obsidian setup (settings, Folder Notes, CLI, phone sync, optional kepano skills) |
| 🤖 `/me:save [what] [domain]` | "збережи рецепт / інструкцію / промпт / це" | note in its domain folder with a category (Recipes / How-tos with Check+Rollback / Prompts / Notes), `summary`, `aliases`; merged with an existing one; never creates a top-level folder without OK |
| 🤖 `/me:find <question>` | "як я робив…", "де мій рецепт…" | searches names, `aliases`, `summary`, tags, then full text; on a miss scans one domain's `summary` lines; answers with `[[note]]` citations; offers to save new syntheses |

## Command line (outside a session)
```
claude plugin marketplace add <path-to-agent-playbook>   # once, path to your clone of this repo
claude plugin install kb@agent-playbook        # also dev@, me@
claude plugin install code-graph@agent-playbook --scope local   # in a project folder only
claude plugin list                              # what is installed and enabled
claude plugin details dev                       # tokens each plugin costs per session
claude plugin validate .                        # from the repo root
/reload-plugins                                 # inside a session, after editing the repo
python scripts/pack.py me                     # zip for claude.ai upload → dist/
python scripts/check_commands.py                # is this file complete?
```

## Maintenance (rule for whoever edits agent-playbook)
Any change that adds, removes, renames a skill or agent, or changes its arguments, trigger (🤖/⌨), gates, model or outputs **must update this file in the same change**. Then run `python scripts/check_commands.py`. Changes to `me` → also re-pack and re-upload the zip to claude.ai.
