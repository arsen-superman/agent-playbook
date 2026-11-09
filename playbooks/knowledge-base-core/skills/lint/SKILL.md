---
name: lint
description: Health check of a knowledge base — contradictions, stale or oversized files, broken links, forgotten tasks, aging inbox, leftover stashes, sensitive data in the wrong place. Use when the user says lint, health check, перевір базу, прибери базу, or periodically (e.g. weekly).
argument-hint: "[fix]"
---
# Lint the knowledge base

**Locate the KB root:** the nearest `.ai/` folder from the current directory upward (a project knowledge base); if there is none, the personal vault from `~/.claude/CLAUDE.md` (`Personal vault:` line); if neither exists, ask.

Check and report as a table (issue · file · suggested fix):

1. **Size limits** — CLAUDE.md ≤100 lines · STATUS.md ≤30 · task.md ≤40 · spec.md ≤250 · inbox item ≤15 · stash ≤40 · idea ≤80.
2. **History instead of truth** — strikethrough, "UPDATE"/"EDIT" paragraphs, `-v2`/`-final` files, chronological research series.
3. **Contradictions** — the same fact stated differently in two files (grep key terms from glossary/context).
4. **Staleness** — `updated:` older than 60 days on active tasks; STATUS rows that disagree with task.md; facts with dates older than 6 months in fast-moving areas.
5. **Broken links** — relative links to files that don't exist.
6. **Orphans** — task folders not in STATUS, STATUS rows without folders, decision records nothing links to.
7. **Inbox** — items >60 days, parked twice, `_done/` leftovers.
   **Ideas** — never proposed for deletion by age; `raw` >90 days → suggest `/kb:brainstorm`; `promoted` without `promoted-to`.
8. **Stash** — stashes >14 days (ask: unstash or drop), `.consumed/` >14 days (delete).
9. **Safety** — secrets, connection strings, personal data outside `raw/`.
10. **Structure version** — project KB: `.ai/.playbook.json` missing or `schema` older than the dev playbook's current → suggest `/dev:upgrade-project`; managed block markers in CLAUDE.md missing or hand-edited.
11. **Repetition** — the same instruction repeated across CLAUDE.md files or skills.

Default: report only. With `fix`: apply the mechanical fixes (links, purges, STATUS sync) and list the judgement calls for the user.
