---
type: todo           # todo | finding | bug | chore | idea | question
severity: n/a        # bug only: high | medium | low — otherwise n/a
area: <area>         # required, never n/a: one lowercase word — repo or module (project KB), domain folder (vault)
source: <session or conversation, no personal names>
ref: n/a             # ticket / MR key (IPR-1234, LOCAL-2, !401) or n/a
created: YYYY-MM-DD
verified: n/a        # YYYY-MM-DD <what was confirmed> once checked, else n/a
parked: n/a          # set by /kb:triage: YYYY-MM-DD <reason>
---
# <one-line title>

**What:** <self-contained description>
**Where:** <file:line, query, link, person | n/a>
**Why it matters:** <impact | n/a>
**Suggested action:** <task / ticket / knowledge / ask someone | n/a>
<!-- Every field is filled; no value → `n/a`, never empty or removed. Only `area` has no n/a. Strip the comments when writing. ≤20 lines. -->
