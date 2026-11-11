---
name: reindex
description: Fetch the scope branches and rebuild the project's code graph (.ai/.index) now; report repos, cross-repo links, errors. Manual: /code-graph:reindex [force]; normally the SessionStart hook keeps it fresh.
argument-hint: "[force]"
disable-model-invocation: true
---
# Rebuild the code graph

The index lives in `<project>/.ai/.index/` and is built by the `cross-repo-graph` package that this plugin pins. One graph per scope, read from git, not from the clones on disk: `dev` = `develop`, `prod` = `main`/`master` (production, for hotfixes). Different branches per repo or other scopes → `.ai/.index/config.json` (see the package README).

1. Project folder = the current directory; it must contain `.ai/` (else: suggest `/dev:init-project` and stop).
2. Check prerequisites: `node --version` (22+) and `uv --version`. Missing uv → print `winget install astral-sh.uv` (Windows) / `brew install uv` / `curl -LsSf https://astral.sh/uv/install.sh | sh` and stop.
3. Run in the foreground (first run downloads Graphify, can take a few minutes):
   `node "${CLAUDE_PLUGIN_ROOT}/scripts/crg.mjs" index --project . --index .ai/.index --fetch` — add `--force` when the argument is `force` (re-parses every repo). The fetch only updates `origin/*` refs, never prompts, 20 s per repo; a repo whose remote needs a password or is unreachable is indexed from its local refs, with a warning in the log.
4. Read the JSON log lines it prints and report in ≤8 lines: fetch ok/failed, per scope repos reused / rebuilt / failed (with the error's first line), cross-repo links (used / declared-only), seconds. Exit code 2 = published without the failed repos.
5. A failed background run leaves its log in `.ai/.index/index.log` — show its last lines when the user asks why the graph is stale.
6. The MCP server picks up the new graph by itself; no restart needed. If the `code-graph` tools are missing in this session, tell the user to restart Claude (the server starts with the session).
