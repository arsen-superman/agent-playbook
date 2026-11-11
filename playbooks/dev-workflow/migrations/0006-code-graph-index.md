# 0006 — Code graph index folder
Why: the optional `code-graph` plugin keeps its index in `.ai/.index/` (graph JSON, per-repo work files, a log); agent searches must not wade through it.

## Steps (idempotent)
1. `.ai/.ignore`: add the line `.index/` if missing.
2. `.ai/.playbook.json`: nothing to add — a missing `codeGraph` key makes `/dev:init-project refresh` offer the add-on.

## Check
- `.ai/.ignore` contains `.index/`.

## Manual follow-up
- Projects with 2+ repos: run `/dev:init-project refresh` and accept the code graph, or leave it off.
