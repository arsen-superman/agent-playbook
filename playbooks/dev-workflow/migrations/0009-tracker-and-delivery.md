# 0009 — Tracker-neutral tasks, delivery mode, feature specs
Why: a project without a tracker or a review team (own product, personal tool) runs the same workflow; `jira:` in `task.md` becomes `source:` (ticket URL or the `.ai/` file the requirement came from); feature-level rules get a durable home in `.ai/specs/`; the managed KB block gains the Tracker, Delivery and feature-spec rules and the `specs/` and `product/` layout lines.

## Steps (idempotent — skip files that already have `source:`)
1. Every `.ai/tasks/*/task.md` and `.ai/archive/*/task.md`: rename the frontmatter key `jira:` → `source:`; the value stays as it is (an empty value stays empty). Nothing else in the file changes.
2. Create `.ai/specs/` if it is missing (empty; `/dev:requirements` fills it).

## Check
- `grep -rl "^jira:" .ai/tasks .ai/archive` returns nothing.
- The managed block in the project `CLAUDE.md` has the **Tracker**, **Delivery** and **Feature rules** lines (refreshed by this upgrade).

## Manual follow-up
- Project `CLAUDE.md`, outside the managed block (the upgrade never edits it): a project without a tracker → set `- Tracker: none`; a project you merge yourself → add `- Delivery: self-merge` next to it. No `Delivery:` line = PR with team review, as before. Optional: `- Profile: work | tool | product`.
- Inbox `area` may now also be a department (`product`, `design`, `ops`, `growth`, `biz`) for items that are not about a repo; existing items need no change.
