# 0004 — Context hygiene, decision frontmatter, repo tags, Obsidian-ready links, per-project dev
Why: `context/` files grew without bound and duplicated repo docs, replaced decisions still read as current rules, multi-repo projects didn't show which repo a file belongs to, and decisions had no properties to filter by.

## Steps (idempotent)
1. Refresh the managed KB block in the project CLAUDE.md (done by `/dev:upgrade-project` anyway) — it now has the context-file limit, the repo-docs rule, the superseded rule, `context/<repo>/`, repo tags and the relative-links rule.
2. `STATUS.md`: add a `Repos` column after `Task` to the Active and Parked tables if missing; fill each row from that task's `repos:`.
3. Each `.ai/decisions/*.md` without frontmatter: move the header bullets into frontmatter per `templates/doc/decision.md` — `Status: accepted` → `status: accepted`; `Status: superseded by NNNN` → `status: superseded` + `superseded-by: NNNN`; `Date` → `date`; `Decided by` → `decided-by`; `Origin` → an `Origin:` line under the title, linking the task folder when it exists in `tasks/` or `archive/`. Add `repos:` inferred from the record and its origin task's `repos:`; can't tell → `[?]`. Keep the body unchanged.
4. Read-only: list `.ai/context/*.md` over 300 lines, and root `context/` files that are about a single repo.
5. Read-only: list decisions without `status`, pairs of `accepted` decisions on the same subject (grep titles and key terms), and links under `.ai/` that point to `tasks/<folder>/` now in `archive/`.
6. Add `"obsidian": false` to `.ai/.playbook.json` if the key is missing.
7. `.claude/settings.local.json`: add `"enabledPlugins": { "dev@agent-playbook": true }` if missing (add-only; `dev` may now be disabled globally).

## Check
- The managed block mentions `context file ≤300`, `superseded-by` and `context/<repo>/`.
- Every decision starts with frontmatter containing `status` and `repos`; STATUS tables have a `Repos` column.

## Manual follow-up
- Decisions with `repos: [?]` → the user names the repos.
- Single-repo context files from step 4 → move to `context/<repo>/` and regroup the Context index by repo (on the user's OK); oversized ones → split by sub-area.
- Decisions from step 5 → the user confirms which one is current; the older gets `status: superseded`, `superseded-by: NNNN`. Stale `tasks/` links → rewrite to `archive/` (on OK).
- `context/` text that repeats a repo's `docs/`/README → replace with a link line in the Context index.
- Want the Obsidian add-on → `/dev:init-project refresh` offers it.
