---
name: pr-comments
description: "Workflow — pull review comments from a task's open PR, triage them with the user, fix through the implementer, draft replies. Triggers: PR comments, review comments, коменти в PR, опрацюй рев'ю."
argument-hint: "[task-key]"
---
# Handle PR review comments — orchestrator

You orchestrate; code changes run in `dev:implementer`, follow the **Orchestration rules** of `/dev:feature-workflow`, with `workflow: pr-comments`. Every comment becomes a row in `<task>/review.md` (`templates/doc/review.md` in this plugin) — the one list that fixes, re-review and replies work from.

1. **Fetch** — PR per repo from `task.md` (Links / `branch:`). Use the repo's tool from the Repositories table (`Host · tool`); GitHub: `gh pr view <n> --json state,reviews,comments` and `gh api repos/{owner}/{repo}/pulls/<n>/comments` (inline threads). Tool missing → give the install/login command, or ask the user to paste the comments. PR merged → offer `/dev:close-task` and stop.
2. **Filter** — unresolved threads and new top-level comments; skip ones whose link already is in `review.md`, bot noise, approvals without text. A follow-up in a thread of an existing row → reopen that row.
3. **Triage** — append one row per comment: Source `PR <link> @author`, Class (risk class number, `convention` for a team rule, `other`), Sev, Where, Finding (≤1 line), proposed Decision:
   - **fix** — code change · **reply** — answer only, no change · **discuss** — you disagree or it's a trade-off: your recommendation in §Notes, the user decides
   - **amend** — a requirement change → `/dev:amend` after this round · **follow-up** — valid but out of scope → `/kb:capture` or a drafted ticket
   Show the new rows as a table. **GATE** — the user confirms or edits in one reply; write the final Decisions.
4. **Plan** — `plan.md`: phase `## PR feedback YYYY-MM-DD` (before the final Verify phase), one step per fix naming its F-IDs: `- [ ] <change> — F-nn — verify: <check>`.
5. **Fix** → `dev:implementer`, that phase only (it sets rows to `fixed <hash>`). Any logic fix (not naming, formatting, docs) → a fresh `dev:reviewer` with the fix commit range and those F-IDs — it re-reads the whole diff around them and marks rows `verified` / `reopened`; reopened → one more fix round, then gate. Then `dev:verifier` on the affected TCs and the automated suite. Trivial fixes → implementer's build + tests are enough; mark them `verified` yourself.
6. **Replies** — draft one per row from its Status: "Fixed in `abc1234`" / the reasoning / the follow-up link; Status → `replied` once posted. **GATE C** — push, post replies, resolve threads only on explicit OK.
7. **Learn** — `convention` rows not yet in `<repo>/REVIEW.md` → draft the lines to add (one rule each, generic, no task details). The repo is shared: a change there is a commit on the user's OK.
8. `task.md` Now: `status: review`, Next = "re-review → `/dev:pr-comments`; merged → `/dev:close-task`". Then `/dev:handoff`.
