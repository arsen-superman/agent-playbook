# Code graph — setup checklist
<!-- Printed by /dev:init-project when the user accepts the code graph. Fill <…> from the scan; drop steps already done. -->

What you get: agents (scout, analyst, planner, reviewer, researcher) answer "who calls this endpoint / uses this field, in which repo" from a graph instead of grepping every repo. Links between repos have `file:line` on both sides; impact = `used` links.

1. **Prerequisites.** Node 22+ (`node --version` → <version>) and uv (`uv --version` → <version or missing>).
   Missing uv: `winget install astral-sh.uv` (Windows) · `brew install uv` · `curl -LsSf https://astral.sh/uv/install.sh | sh`, then open a new terminal.
2. **Install the plugin for this project only**, from the project folder:
   `claude plugin install code-graph@agent-playbook --scope local`
   (already enabled in `.claude/settings.local.json`; never install it for the user — its server starts in every session where it is on).
3. **Restart Claude** in this folder. `/mcp` should list `plugin:code-graph:code-graph`.
4. **First index.** It starts by itself in the background at that session start and takes about <N repos × 10 s × 2 scopes> (Graphify is downloaded once). Want it now and see the result: `/code-graph:reindex`. Log of background runs: `.ai/.index/index.log`.
5. **Branches per scope** (read from git, not from your clones — work on any branch or in worktrees):
   <repo>: dev = <origin/develop>, prod = <origin/master>
   A repo with other branches → `.ai/.index/config.json`: `{ "repos": { "<repo>": { "prod": "release" } } }`.
   Tasks pick the scope from `base:` in `task.md`: `main`/`master` (hotfix) → prod, otherwise dev.
6. **Freshness.** Each session start fetches the scope branches (only `origin/*`, at most every 30 min) and re-indexes what moved. The fetch never asks for a password: it works when git already authenticates on its own (SSH agent, credential manager, `gh` as credential helper); otherwise that repo is indexed from local refs, a warning goes to the log, and the graph is as fresh as your last `git fetch`/`pull`. If your SSH agent asks to approve each use of a key (1Password, KeePassXC, a hardware key), expect that prompt at session start — allow the key for the session, or turn fetching off: `"fetch": false` in `config.json`.
7. **Disk.** About 25 MB per repo for two scopes, in `.ai/.index/` (agents never search it; delete it any time — it is rebuilt).

Turn it off: `claude plugin disable code-graph@agent-playbook --scope local`, `"codeGraph": false` in `.ai/.playbook.json`, delete `.ai/.index/`.
