---
type: todo           # todo | finding | bug | chore | idea | question
severity: n/a        # bug only: high | medium | low — otherwise n/a
area: <area>         # required, never n/a: project KB — repo name as in the Repositories table, `all` if several; vault — domain folder
source: <ticket/MR key first if any, then session or conversation — no personal names>   # e.g. IPR-4145 MR2 review
created: YYYY-MM-DD
updated: YYYY-MM-DD  # last status change; = created for a new item
status: new          # new | in-progress (triaged, stays in inbox) | done (moved to inbox/_done/)
next: n/a            # in-progress: what is awaited and from whom
resolution: n/a      # done: task <KEY> | ticket <KEY>
---
# <one-line title>

**What:** <self-contained description>
**Where:** <file:line, query, link, person | n/a>
**Why it matters:** <impact | n/a>
**Suggested action:** <task / ticket / knowledge / ask someone | n/a>
<!-- Every field is filled; no value → `n/a`, never empty or removed. Only `area` has no n/a. Strip the comments when writing. ≤20 lines. -->
