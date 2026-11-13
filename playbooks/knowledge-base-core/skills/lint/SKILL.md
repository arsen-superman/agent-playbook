---
name: lint
description: "Health check of a knowledge base — contradictions, oversized or stale files, broken links, forgotten tasks, aging inbox, leftover stashes, secrets. Manual: /kb:lint, weekly."
argument-hint: "[fix]"
disable-model-invocation: true
---
# Lint the knowledge base

**Locate the KB root:** the nearest `.ai/` folder from the current directory upward (a project knowledge base); if there is none, the personal vault from `~/.claude/CLAUDE.md` (`Personal vault:` line); if neither exists, ask. Vault service folders carry a `_` prefix: there `inbox/`, `ideas/`, `raw/`, `stash/` below mean `_inbox/`, `_ideas/`, `_raw/`, `_stash/`.

Check and report as a table (issue · file · suggested fix):

1. **Size limits** — CLAUDE.md ≤100 lines · STATUS.md ≤30 · task.md ≤40 · spec.md ≤250 · context file ≤300 (→ split by sub-area, update the Context index) · inbox item ≤20 · stash ≤40 · idea ≤80.
2. **History instead of truth** — strikethrough, "UPDATE"/"EDIT" paragraphs, `-v2`/`-final` files, chronological research series.
3. **Contradictions and copies** — the same fact stated differently in two files (grep key terms from glossary/context); `context/` text that copies a repo's `docs/`/README instead of linking; two `accepted` decisions that contradict each other (older → `status: superseded`, `superseded-by: NNNN`); `superseded-by` pointing to a missing record; decisions without frontmatter.
   **Repos** (project KB) — decisions without `repos:`, STATUS rows without Repos, `repos:`/`context/<repo>/` names missing from the Repositories table, `context/` root files about a single repo.
4. **Staleness** — `updated:` older than 60 days on active tasks; STATUS rows that disagree with task.md; facts with dates older than 6 months in fast-moving areas.
5. **Broken links** — relative links to files that don't exist (often a task moved to `archive/`); `[[wikilinks]]` in a project KB.
6. **Orphans** — task folders not in STATUS, STATUS rows without folders, decision records nothing links to.
7. **Inbox** — items >60 days, parked twice, `_done/` leftovers; frontmatter off `templates/inbox-item.md` (missing, empty or unknown field, value outside the enum, leftover `priority`, `area` missing or `n/a`, `severity` on a non-bug or missing on a bug).
   **Ideas** — never proposed for deletion by age; `raw` >90 days → suggest `/kb:brainstorm`; `promoted` without `promoted-to`.
8. **Stash** — stashes >14 days (ask: unstash or drop), `.consumed/` >14 days (delete).
9. **Safety** — secrets, connection strings, personal data outside `raw/`.
10. **Structure version** — project KB: `.ai/.playbook.json` missing or `schema` older than the dev playbook's current → suggest `/dev:upgrade-project`; managed block markers in CLAUDE.md missing or hand-edited.
11. **Repetition** — the same instruction repeated across CLAUDE.md files or skills.
12. **Personal vault** — broken links and orphans via the Obsidian CLI (`unresolved`, `backlinks`) when available; notes without `summary` or `categories`; top-level folders missing from the vault `CLAUDE.md` domain list (or type folders like `prompts/`); service folders without the `_` prefix (→ `/me:init-vault`); leftover `index.md` files (→ `/me:init-vault`); a domain past ~100 notes → suggest subfolders.

Default: report only. With `fix`: apply the mechanical fixes (links, purges, STATUS sync) and list the judgement calls for the user.
