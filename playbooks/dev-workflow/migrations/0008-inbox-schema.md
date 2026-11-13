# 0008 — Inbox item schema: severity, area, ref, n/a
Why: inbox items follow one template (`templates/inbox-item.md` in `/kb:capture`); `priority` is dropped (set at triage), `severity` (bugs), `area`, `ref`, `verified`, `parked` are added, empty values are `n/a`.

## Steps (idempotent — skip items that already have `area:`)
Every `.ai/inbox/*.md` (not `_done/`):
1. `priority:` → remove. For `type: bug` it seeds `severity:` — `high` → `high`, `normal`/`medium` → `medium`, `low` → `low`; every other type gets `severity: n/a`.
2. `area:` → one lowercase word, the repo or module from `Where:` (or the slug prefix). Not inferable → list the item under Manual follow-up and ask; never write `n/a`.
3. `ref:` → the first ticket/MR key in `source:` (`ABC-123`, `LOCAL-2`, `!401`), else `n/a`. Leave `source:` as is.
4. `verified:` and `parked:` → keep when present, else add `n/a`.
5. Any other empty frontmatter value → `n/a`.
6. Field order: type, severity, area, source, ref, created, verified, parked.

## Check
- `grep -L "^area:" .ai/inbox/*.md` finds nothing; `grep -l "^priority:" .ai/inbox/*.md` finds nothing.

## Manual follow-up
- Severity of migrated bugs was derived from `priority` and may be off — review them at the next `/kb:triage`.
- Items whose `area` could not be inferred.
