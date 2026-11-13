# 0008 — Inbox: one item template, status lifecycle, generated index
Why: inbox items follow one template (`templates/inbox-item.md` in `/kb:capture`): `priority` is dropped (set at triage), `severity` (bugs), `area`, `status`/`next`/`resolution` are added, empty values are `n/a`; `kb` generates `inbox/INDEX.md` for human viewing.

## Steps (idempotent — skip items that already have `status:`)
Every `.ai/inbox/*.md` and `.ai/inbox/_done/*.md`:
1. `priority:` → remove. For `type: bug` it seeds `severity:` — `high` → `high`, `normal`/`medium` → `medium`, `low` → `low`; every other type gets `severity: n/a`.
2. `area:` → the repo name from the Repositories table (project CLAUDE.md) that `Where:` points to, `all` if it spans several. Not inferable → list the item under Manual follow-up and ask; never write `n/a`.
3. `source:` → leave as is (the ticket/MR key stays at its start).
4. Add `updated:` (= `created:`), `status: new`, `next: n/a`, `resolution: n/a` after `created:`. Items in `_done/`: `status: done`.
5. `parked: YYYY-MM-DD <reason>` → remove; `status: in-progress`, `updated:` = that date, `next: <reason>`.
6. `verified: <date> <text>` → remove the field; if the body has no `**Verified` line, add `**Verified (<date>):** <text>` after `Suggested action`.
7. Any other empty frontmatter value → `n/a`.
8. Field order: type, severity, area, source, created, updated, status, next, resolution.
9. `.ai/.ignore`: add the line `inbox/INDEX.md` if missing.

## Check
- `grep -L "^area:" .ai/inbox/*.md` and `grep -L "^status:" .ai/inbox/*.md` find nothing; `grep -l "^priority:\|^parked:\|^verified:\|^ref:" .ai/inbox/*.md` finds nothing.
- `grep -x "inbox/INDEX.md" .ai/.ignore` finds the line.

## Manual follow-up
- Severity of migrated bugs was derived from `priority` and may be off — review them at the next `/kb:triage`.
- Items whose `area` could not be inferred.
- Create the first index: `python <kb plugin>/scripts/inbox_index.py .ai/inbox` (afterwards a hook keeps it current).
