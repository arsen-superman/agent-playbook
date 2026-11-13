---
name: review
description: Review a task's diff against its spec, plan and the risk classes, logging every finding in review.md. Use when the reviewer stage runs, or the user asks to review a task's branch before a PR — "review KEY", "перевір код задачі", "зроби рев'ю".
argument-hint: "[task-key] [fix round: <commit range> <F-IDs>]"
---
# Review a task (reviewer)

Checklist: `templates/checklists/risk-classes.md` in this plugin. Log: `<task>/review.md` (`templates/doc/review.md`; create it if missing).
If this session wrote the code, delegate to the `dev:reviewer` agent and report its result.

1. Read `spec.md` (rules, AC, edge cases, Decisions), `plan.md` (Approach, Cross-cutting, Risks), `review.md`, the project CLAUDE.md, and `<repo>/REVIEW.md` + `<repo>/CLAUDE.md` for each repo in `repos:` — REVIEW.md passes, severities and exclusions win over these defaults.
2. Diff: `git diff <base>...<branch>` per repo. You did not write it; don't trust commit messages or plan ticks.
3. **Conformance** — every rule and AC implemented; a change no plan step covers, or a step done differently without `(changed: …)` → major.
4. **Quality** — the plan is not the reference for correctness. Walk classes 1, 3–15 as questions against the diff; for each changed function read its callers and the whole file at HEAD, not only the hunk. Flaw the plan or spec prescribed, or a case they missed → major, class `plan-level <n>`. Also: injection and auth, secrets in code, path traversal / SSRF, unsafe deserialization; tests assert behaviour, not implementation details (brittle → minor), and pass class 15 (a test guarding an AC that can't fail → major); comments, docstrings and repo docs (README, `docs/`) describing the changed behaviour are still true.
   - Spec-independent pass: read each changed decision point on its own, before the spec's rules — its sibling outcomes (absent/empty, error, repeated or overlapping) and inputs that lead to a dead end (class 14). A gap in the spec is `plan-level`, not "conforms".
   - A risk you judge negligible → name the input or test you checked it against.
5. **Reuse** — for every new or rewritten helper, check or service, grep the repo for an existing one (class 7).
6. **Bug task** — find `<KEY>: failing test for …` (`git log --grep`); `git diff <that commit>..HEAD -- <its test files>` must be empty, else blocker.
7. **Fix round** (prompt names a commit range and F-IDs): review the whole `base...HEAD` diff again, focused on the fix commits and how they interact with the rest (class 2). Each listed row → `verified` (the problem the row describes no longer exists — applying its suggested fix is not enough) or `reopened` (why); new problems → new rows.
8. Write all findings to `review.md` — append rows with the next free F-ID, Source `reviewer R<n>`, Decision empty, Status `open`. No cap on minor rows. Don't duplicate an existing row: reopen it.
9. Never edit code. Verdict: approve (no open blocker/major) / changes required. Reply: counts by severity, the top 5 rows, verdict.
