---
name: verify
description: Independently verify a bug fix or feature against its acceptance criteria and neighbouring scenarios (QA). Use when the user asks to test, verify or check a fix, or before a PR/merge. Prefer running it through the verifier agent or a fresh session that did not write the code.
argument-hint: "[task-key]"
---
# Verify (QA)

If this session wrote the code, delegate to the `verifier` agent from this plugin and report its result.

1. Read `spec.md` (AC, rules, edge cases) and `test-cases.md` (`templates/doc/test-cases.md`; missing → create it from the AC first). Test against the spec, not the author's intent.
2. The change: `git diff <base>...<branch>` in each repo from `repos:`.
3. Coverage: every AC has a case; add negatives, edge cases and regression neighbours (other callers of changed code; users the change must NOT affect). Propose automating uncovered ones (implement only on OK).
4. Execute: automated tests via `Automated by`; `manual` cases you can run yourself (API calls, read-only test-DB queries, CLI); UI/human-only → `⏳ for QA` with exact steps, data and environment.
5. Record in `test-cases.md`: Status column, a new line on top of **Runs** (date · verifier · env · counts · commit · failures), mark **Regression candidates**. In `task.md §Verification` keep only: latest verdict, counts, link to `test-cases.md`, what's left for QA.
6. Failures: don't fix here → `status: in-progress`, Next = "fix: TC-…". Unrelated bugs → `/kb:capture` type `bug`.
7. **QA handoff** (if any `⏳ for QA` or the user asks): draft a Jira comment / QA note — environment, build/branch, the TC table, the manual cases in full. Post only on OK.
8. Verdict: pass / fail / pass with notes.
