# 0002 — Test cases per task and a project regression suite
Why: test cases become a persistent artifact (designed at plan time, executed by verify, handed to manual QA) and the reusable ones are kept after a task closes.

## Steps (idempotent)
1. Create `.ai/qa/` if missing.
2. Create `.ai/qa/regression.md` from `templates/project/regression.md` if missing.
3. Refresh the managed KB block in the project CLAUDE.md (done by `/dev:upgrade-project` anyway) — it now lists `test-cases.md` and `qa/regression.md`.

## Check
- `.ai/qa/regression.md` exists; the managed block mentions `qa/regression.md`.

## Manual follow-up
- Active tasks have no `test-cases.md` yet: `/dev:verify` creates one from the AC on its next run; or ask the agent to create them now.
