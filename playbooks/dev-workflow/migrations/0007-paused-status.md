# 0007 — Parked → Paused
Why: `/dev:park` became `/dev:pause-task`; the status, the task block and the STATUS section follow the new name.

## Steps (idempotent)
1. Every `.ai/tasks/*/task.md`: frontmatter `status: parked` → `status: paused`; heading `## Parked` → `## Paused`.
2. `.ai/STATUS.md`: heading `## Parked` → `## Paused` (rows unchanged).

## Check
- `grep -rn "status: parked\|^## Parked" .ai/tasks .ai/STATUS.md` finds nothing.
