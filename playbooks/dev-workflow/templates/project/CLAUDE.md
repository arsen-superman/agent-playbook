# Project: <Name>

<!-- 2-3 lines: what the product is, who the client is, your role, current phase. -->

## Repositories
| Folder | What | Stack | Build / test | Host · tool |
|---|---|---|---|---|
| `<repo-a>/` | <purpose> | .NET 8 | `dotnet build X.sln` · `dotnet test` | [GitHub](https://github.com/org/repo-a) · `gh` |

Each repo may have its own `CLAUDE.md` (code conventions) — it loads when you work inside that repo.

## Links
- Tracker: <Jira project URL> (key `ABC`)
- Docs: <Confluence / Drive>
- People: <role → name, only those you need to ask things>

## Environments & data (local only — this file is not in any repo)
- Databases are reached through MCP servers by name, never by connection string: `<db-local>` (local), `<db-test>` (test, read-only).
- Production: **not available to you.** If prod data is needed, write the query and ask me to run it.
- Never read or edit: <paths, e.g. `*/appsettings.Production.json`, `infra/secrets/`>.
- Never run: <commands, e.g. migrations against shared DBs, `terraform apply`>.

## Conventions
- Branch: `feature/<KEY>-<slug>` · commits/PRs in English, prefixed with the ticket key.
- <anything the agent got wrong twice>

## Context index (read on demand)
<!-- One area per file, grouped by repo. Repo docs are linked here, not copied into context/. -->
**Cross-repo**
- `context/glossary.md` — business terms → code

**<repo-a>**
- `<repo-a>/docs/` — <what the repo's own docs cover>
- `context/<repo-a>/<area>.md` — <what only this repo needs, not in its docs>

<!-- agent-playbook:kb:begin -->
<!-- Managed by agent-playbook. Filled from templates/project/kb-section.md by /dev:init-project and replaced by /dev:upgrade-project. Edit outside these markers only. -->
<!-- agent-playbook:kb:end -->
