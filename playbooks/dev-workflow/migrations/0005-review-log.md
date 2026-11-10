# 0005 — Review log per task
Why: review findings (agent rounds and PR comments) had no file, so minor findings were dropped, fix rounds had nothing to check against, and team conventions from PR comments were lost.

## Steps (idempotent)
1. Refresh the managed KB block in the project CLAUDE.md (done by `/dev:upgrade-project` anyway) — the task folder line now lists `review.md`.
2. Nothing to create: `/dev:review` and `/dev:pr-comments` create `review.md` from `templates/doc/review.md` on first use.

## Check
- The managed block lists `review.md` in the `.ai/tasks/<KEY-slug>/` line.

## Manual follow-up
- Tasks in review with PR comments already handled through `plan.md` phases → nothing to move; the next `/dev:pr-comments` starts `review.md` with new comments only.
