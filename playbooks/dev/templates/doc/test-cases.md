# Test cases — KEY-123 Short title

Designed from `spec.md` before coding; automated where possible; the rest is ready for manual QA.
Levels: **unit** (logic) · **integration** (DB, API, other services) · **e2e/UI** · **manual** (needs a human or an environment we can't reach).

| ID | AC | Title | Level | Automated by | Status |
|---|---|---|---|---|---|
| TC-01 | AC1 | <behaviour in one line> | unit | `Tests/FooTests.cs::Should_…` | ✅ |
| TC-02 | AC2 | | manual | — | ⏳ for QA |

Status: ⏳ not run · ✅ pass · ❌ fail · ⏭ n/a (why).

## Cases

### TC-01 — <title>
- **Covers:** AC1 · rule R2
- **Preconditions / data:** <user, role, records, config, environment>
- **Steps:**
  1. 
- **Expected:** <observable result>

### TC-02 — <title>
…

## Runs
<!-- Newest first. One line per run; details only for failures. -->
- YYYY-MM-DD · <who: verifier / QA name> · <env> · 5 ✅ 1 ❌ (TC-03: <actual>) · <commit>

## Regression candidates
<!-- TC IDs worth keeping after the task closes → promoted to .ai/qa/regression.md by /dev:close-task -->
