---
name: pr-comments
description: Workflow — pull review comments from a task's open PR, triage them with the user, fix through the implementer, draft replies. Triggers: PR comments, review comments, коменти в PR, опрацюй рев'ю.
argument-hint: "[task-key]"
---
# Handle PR review comments — orchestrator

You orchestrate; code changes run in `dev:implementer`, follow the **Orchestration rules** of `/dev:feature-workflow`, with `workflow: pr-comments`.

1. **Fetch** — PR per repo from `task.md` (Links / `branch:`). Use the repo's tool from the Repositories table (`Host · tool`); GitHub: `gh pr view <n> --json state,reviews,comments` and `gh api repos/{owner}/{repo}/pulls/<n>/comments` (inline threads). Tool missing → give the install/login command, or ask the user to paste the comments. PR merged → offer `/dev:close-task` and stop.
2. **Filter** — unresolved threads and new top-level comments; skip ones whose link already appears in `plan.md`, bot noise, approvals without text.
3. **Triage** — table `# · author · file:line · comment (≤1 line) · proposal`, proposal one of:
   - **fix** — code change · **reply** — answer only, no change · **discuss** — you disagree or it's a trade-off: give your recommendation, the user decides
   - **amend** — a requirement change → `/dev:amend` after this round · **follow-up** — valid but out of scope → `/kb:capture` or a drafted ticket
   **GATE** — the user confirms or edits the table in one reply.
4. **Plan** — `plan.md`: phase `## PR feedback YYYY-MM-DD` (before the final Verify phase), one step per fix: `- [ ] <change> — <comment link> — verify: <check>`.
5. **Fix** → `dev:implementer`, that phase only. A fix changing logic (not naming, formatting, docs) → `dev:reviewer` on those commits only, max 1 round; then `dev:verifier` on the affected TCs and the automated suite. Trivial fixes → implementer's build + tests are enough.
6. **Replies** — draft one per thread: "Fixed in `abc1234`" / the reasoning / the follow-up link. **GATE C** — push, post replies, resolve threads only on explicit OK.
7. `task.md` Now: `status: review`, Next = "re-review → `/dev:pr-comments`; merged → `/dev:close-task`". Then `/dev:handoff`.
