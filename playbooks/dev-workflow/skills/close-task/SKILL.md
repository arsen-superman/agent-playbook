---
name: close-task
description: Close a finished or cancelled task — confirm the PR is merged, promote lasting decisions and knowledge to the project, record the outcome, archive the folder, update STATUS and clean up branches and worktrees. Use when a task is merged, done, released or cancelled — "PR merged", "змерджено", "закрий задачу".
argument-hint: "<task-key>"
---
# Close a task

1. **Confirm done** per repo: PR state via the repo's tool from the Repositories table (e.g. `gh pr view <n> --json state,mergedAt`), Jira status (connector), or the user says so. Some PR still open → stop, offer `/dev:pr-comments`. Cancelled → skip regression promotion, keep the rest.
2. **Handoff first** — `/dev:handoff` steps 1-5, 7 and 9, so the task files are current truth before promotion.
3. **Promote** what outlives the task: `test-cases.md` regression candidates → append to `.ai/qa/regression.md` under the feature area (ID → `<KEY>/TC-nn`, keep steps, data and `Automated by`); decisions that may be reversed later → `.ai/decisions/` (usually 0–2; any they replace → `status: superseded`, `superseded-by: NNNN`), the rest stay in `spec.md §Decisions`; facts about code, data, domain → `.ai/context/`, or a docs change in the repo when it has `docs/` on that subject; terms → `glossary.md`; `review.md` rows with class `convention` not yet in `<repo>/REVIEW.md` → draft the rules (commit on OK); untracked follow-ups → `/kb:capture` or drafted tickets. Promoted text stands on its own: it links the task only via `task.md`, never its research, review or test files.
4. `## Outcome` at the top of `task.md` (≤10 lines): what shipped, PR, release, what was deferred or not done and why (incl. `review.md` rows decided `follow-up` / `won't fix`, with links), lessons that changed a skill or CLAUDE.md. `status: done` (or `cancelled`).
5. **Archive** — move the folder to `.ai/archive/`; rewrite links to it across `.ai/` (`tasks/<KEY-slug>/` → `archive/<KEY-slug>/`). Trim it to what explains what was done and why — never without asking: list what goes (file or section, one line each) and let the user pick what to keep (AskUserQuestion multiSelect when available; `.ai/` is not versioned, deletion is final). Kept items stay as they are:
   - keep `task.md` (frontmatter, Goal, Outcome, Links), `spec.md` (Rules, AC, Edge cases, Out of scope, Decisions, Rejected, Assumptions), `plan.md` (Options, Approach, `accepted:` risks);
   - drop the other sections (Raw requirement is in Jira, AS-IS is stale after merge, steps and fix phases are in git and the PR) and delete `test-cases.md`, `review.md`, `research/` incl. `raw/`, scratch;
   - links across `.ai/` into deleted files → point them at `task.md` or the PR.
6. `STATUS.md`: remove from Active, add to Recently closed (keep 5).
7. **Git cleanup** — per repo in `repos:`, show the list and ask once:
   - worktree `worktrees/<repo>--<KEY>` → `git worktree remove <path>`. Refused → AskUserQuestion with the reason (uncommitted changes: show `git status --short`; locked or open in an editor/terminal) and options: force (`--force`; locked → `--force --force`; lists what is lost) · I closed it, retry · keep it. Windows file locks survive `--force` — then only close-and-retry helps.
   - main checkout on the task branch → switch to the base branch, `git pull --ff-only`.
   - local branch → `git branch -d`; refused because the PR was squash/rebase-merged → `-D` only when step 1 confirmed the merge.
   - remote branch still there → `git push origin --delete <branch>`; then `git fetch --prune`.
8. Reply ≤5 lines: outcome, what was promoted, what was cleaned up.
