# 0003 — Worktrees under the project root and a git-host tool per repo
Why: worktrees were placed ad hoc and PR operations guessed the tool; both are now project rules in the managed block.

## Steps (idempotent)
1. Refresh the managed KB block in the project CLAUDE.md (done by `/dev:upgrade-project` anyway) — it now has the Worktrees and Git host rules.
2. Read-only: per repo, `git worktree list`; collect worktrees outside `<project>/worktrees/` or not named `<repo>--<KEY>`.

## Check
- The managed block mentions `worktrees/<repo>--<KEY>` and `Host · tool`.

## Manual follow-up
- Misplaced worktrees from step 2 → `git worktree move <old> <project>/worktrees/<repo>--<KEY>` (on the user's OK; this migration doesn't move them).
- Repositories table has no `Host · tool` column → run `/dev:init-project refresh` to detect hosts, check the CLIs and add `ask` rules for their write commands.
