# agent-playbook — commands cheat sheet

For you and for any agent. Kept in sync with `playbooks/` (see *Maintenance* at the end).

- Commands are `/<playbook>:<skill>`. Type `/` in Claude Code to see them.
- 🤖 = Claude also starts it by itself when your words match (e.g. "запиши на потім" → `/kb:capture`). ⌨ = only when you type the command (expensive or rare).
- Arguments in `<>` are required, in `[]` optional.

## Typical days

| Situation | Do |
|---|---|
| New project folder | `/dev:init-project` once |
| Continue earlier work | `/dev:start [KEY]` (not needed when starting something new) |
| Work with no ticket yet | `/dev:new-task "description"` → `LOCAL-n`, then as usual |
| New ticket, do it all in one go | `/dev:feature KEY` · `/dev:bugfix KEY` · `/dev:spike "question"` |
| New ticket, step by step | `/dev:new-task KEY` → `/dev:spec` → `/dev:plan` → `/dev:implement` → `/dev:verify` → `/dev:close-task` |
| End of every session | `/dev:handoff` (no task in the session → `/kb:stash`) |
| Switch to something else for a while | `/kb:stash name` … later `/kb:unstash name` |
| Task blocked for days/weeks | `/dev:park KEY reason` … later `/dev:resume KEY` |
| Noticed something unrelated | just say "запиши на потім" → `/kb:capture` |
| Free half hour | `/kb:triage` |
| Meeting notes / doc / epic to digest | `/kb:ingest <file or paste>` |
| Weekly | `/kb:lint` |
| After changing agent-playbook structure | `/dev:upgrade-project all` |
| "Save this recipe / instruction" | `/me:save` |
| "How did I … ?" | `/me:find` |

## dev — software development

### Workflows (one session, each stage in a subagent, you approve at gates)
| Command | When | What happens |
|---|---|---|
| ⌨ `/dev:feature <KEY \| task \| description> [auto]` | a feature end to end | analyst → **GATE A** questions → planner → **GATE B** plan → implementer per phase → reviewer (≤2 fix rounds) → verifier → **GATE C** push/PR. `auto` skips B for small plans. Resumable: `/dev:start` continues at the saved stage |
| ⌨ `/dev:bugfix <KEY \| task \| description>` | a bug end to end | debugger (repro, root cause, failing test) → **GATE A** pick fix → implementer → reviewer → verifier → **GATE C** |
| ⌨ `/dev:spike <question \| KEY> [timebox]` | choose between options before building | frame + sub-questions → **GATE A** → researcher ×N in parallel → synthesis → **GATE B** → decision record in `.ai/decisions/`, follow-ups |

### Project setup and maintenance
| Command | When | What happens |
|---|---|---|
| 🤖 `/dev:init-project [folder] [refresh]` | first time in a project folder; `refresh` after repos change | scans repos and stack, asks what it can't infer, creates `.ai/`, project `CLAUDE.md`, `.claude/settings.local.json`, `.ai/.playbook.json`; suggests (doesn't write) repo CLAUDE.md files and DB MCP setup |
| ⌨ `/dev:upgrade-project [folder \| all] [dry-run]` | after agent-playbook changed project-side structure; when start/lint says "outdated" | applies pending migrations, refreshes the managed KB block in CLAUDE.md, bumps `.ai/.playbook.json` |

### Session and task lifecycle
| Command | When | What happens |
|---|---|---|
| 🤖 `/dev:start [KEY]` | beginning of every session | reads STATUS + task card + plan up to Next; reports where things are, inbox/stash counts, staleness, outdated KB |
| 🤖 `/dev:new-task <KEY \| description> [from LOCAL-n]` | new ticket; work with no ticket yet (→ `LOCAL-n`, tracked like any task); a LOCAL task got a ticket (`IPR-123 from LOCAL-2`) | fetches Jira, creates `.ai/tasks/<KEY-slug>/` with `task.md` and raw requirement, adds to STATUS; on `from` renames the LOCAL task to the ticket key (can draft the Jira ticket for you, created only on OK) |
| 🤖 `/dev:handoff [KEY]` | end of every session, or when context gets long | rewrites task Now/Next, ticks plan, promotes decisions/knowledge, captures leftovers, updates STATUS |
| 🤖 `/dev:park <KEY> [reason]` | blocked / missing data / priorities changed | handoff + WIP commit on the branch + **Parked** block (why, unblocks when, volatile facts) + STATUS → Parked |
| 🤖 `/dev:resume <KEY>` | coming back to a parked task | "while you were away": Jira, branch drift, re-checked facts → updates spec/plan → back to Active |
| 🤖 `/dev:close-task <KEY>` | merged / done / cancelled | promotes decisions, knowledge and regression test cases (→ `.ai/qa/regression.md`), writes Outcome, moves to `.ai/archive/` |

### Single stages (manual, in this session — the workflows use the same procedures)
| Command | What it produces |
|---|---|
| 🤖 `/dev:spec [KEY]` | `spec.md`: AS-IS with file:line, rules, AC, edge cases, open questions. No code |
| 🤖 `/dev:plan [KEY]` | `test-cases.md` (cases per AC, level unit/integration/e2e/manual) + `plan.md`: phased, commit-sized steps each with a verify check; asks approval |
| 🤖 `/dev:implement [KEY] [all \| phase N]` | code + one commit per step, ticks with hashes; one phase per call by default; never pushes |
| 🤖 `/dev:fix-bug [KEY]` | reproduce → root cause → failing test → minimal fix → verification note |
| 🤖 `/dev:verify [KEY]` | executes `test-cases.md` (automated + what it can run itself), adds missing cases, records a run, leaves UI/human cases `⏳ for QA` and drafts a QA handoff (Jira comment on OK); delegates to `dev:verifier` if this session wrote the code |
| 🤖 `/dev:research <question> [KEY]` | `research/<topic>.md`: answer, evidence, confidence, implications |

### Agents (called by workflows; you can also say "use dev:reviewer on IPR-123")
| Agent | Model / effort | Does | Writes |
|---|---|---|---|
| `dev:analyst` | opus / high | requirements vs code → spec | spec.md |
| `dev:planner` | opus / high | spec → test design + plan | test-cases.md, plan.md |
| `dev:implementer` | sonnet / medium | one phase of the plan | code, commits, plan ticks |
| `dev:debugger` | opus / high | repro, root cause, failing test (no fix) | spec AS-IS, test-cases.md TC-01, test commit |
| `dev:reviewer` | opus / high | code review of the diff | nothing (returns findings) |
| `dev:verifier` | sonnet / high | executes test cases, proposes missing ones | nothing (orchestrator records the run in test-cases.md) |
| `dev:researcher` | opus / high | one research question | research/<topic>.md |
Every agent returns `STATUS / ARTIFACTS / SUMMARY / QUESTIONS / CAPTURED`.

## kb — any knowledge base (project `.ai/` or the personal vault)
| Command | When | What happens |
|---|---|---|
| 🤖 `/kb:capture <what>` | something outside the current task: bug, idea, todo, question, finding | one small file in `inbox/`; reply `📥 title`; work continues |
| 🤖 `/kb:triage [filter]` | inbox grew / free time | table of items, one proposed outcome each (now / task / ticket / knowledge / decision / ask / park / drop); you confirm in one reply |
| 🤖 `/kb:stash [name]` | switching context; task-less exploration to continue in a fresh session instead of compacting | ≤40-line snapshot in `stash/` |
| 🤖 `/kb:unstash [name]` | coming back | restores it into the session, reports drift, consumes it (kept 14 days in `.consumed/`) |
| 🤖 `/kb:ingest <file \| url \| text>` | meeting notes, transcript, doc, epic | keeps source in `raw/`, proposes facts / decisions / todos / questions, files them on OK |
| 🤖 `/kb:lint [fix]` | weekly | sizes, history-instead-of-truth, contradictions, stale/orphan items, old inbox/stash, secrets, outdated KB structure |

## me — personal vault (`G:\My Drive\Vault`; in claude.ai chat via the Drive connector)
| Command | When | What happens |
|---|---|---|
| 🤖 `/me:init-vault [path]` | once | creates vault structure, registers the path in `~/.claude/CLAUDE.md` |
| 🤖 `/me:save [what] [area]` | "збережи рецепт / інструкцію / це" | note (recipe / howto with Check+Rollback / note) in the right folder, merged with an existing one, index updated |
| 🤖 `/me:find <question>` | "як я робив…", "де мій рецепт…" | answers from the vault with `[[note]]` citations; offers to save new syntheses |

## Command line (outside a session)
```
claude plugin marketplace add C:\Users\user\Documents\Repos\personal\agent-playbook   # once
claude plugin install kb@agent-playbook        # also dev@, me@
claude plugin list                              # what is installed and enabled
claude plugin details dev                       # tokens each plugin costs per session
claude plugin validate C:\Users\user\Documents\Repos\personal\agent-playbook
/reload-plugins                                 # inside a session, after editing the repo
python scripts/pack.py me                     # zip for claude.ai upload → dist/
python scripts/check_commands.py                # is this file complete?
```

## Maintenance (rule for whoever edits agent-playbook)
Any change that adds, removes, renames a skill or agent, or changes its arguments, trigger (🤖/⌨), gates, model or outputs **must update this file in the same change**. Then run `python scripts/check_commands.py`. Changes to `me` → also re-pack and re-upload the zip to claude.ai.
