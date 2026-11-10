# Risk classes — what slips past plan and review

<!-- One list for three stages. Analyst turns classes into rules, matrices and edge cases; planner answers each applicable class in plan.md §Cross-cutting; reviewer checks each against the diff. Class numbers are used in review.md. -->

| # | Class | Ask |
|---|---|---|
| 1 | **Collections and batch** | Does every invariant (limit, total, daily cap, uniqueness) hold for all items of one request together, not only per item? Duplicates or swapped values inside one batch? Partial failure — what is saved? |
| 2 | **Fix on fix** | Does the fix interact with the rest of the diff: checks done twice, a retry lost after an error, a race between parallel requests, an existence leak through ordering? |
| 3 | **Permission matrix** | Every role/permission combination (none / read / write / read+write × admin or not, owner or not) × every affected operation and list. Write-only users? Inactive or disabled entities, "show inactive" filters? |
| 4 | **New or changed field** | Every endpoint, DTO and mapping that returns the entity — create, edit, batch, list, search, export — and every client that reads it. |
| 5 | **Client state, cache, time** | Cache: lifetime, invalidation, never cache a failure, refresh when the day/month/period changes. Time: whose time zone (server, browser, business), period boundaries, defaults from "now". |
| 6 | **Placement and design** | Where does the code live; how much does each class grow (past ~300 lines or a second responsibility → a new service, per repo convention)? Named types over bool flags; validation in the layer the repo uses. `<repo>/REVIEW.md` wins. |
| 7 | **Reuse** | Does a service, helper, endpoint or permission check already do this? Search before writing; never re-implement a check another service owns. |
| 8 | **Cost and frequency** | How often does it run — app start, every page, every item? Same data loaded twice in one request? N+1, unbounded queries, UI blocked on a non-essential call? |
| 9 | **Error disclosure** | Do "not found" and "forbidden" look the same to a user without access? Do messages, codes or ids reveal data or existence? |
| 10 | **Concurrency** | Parallel or repeated requests, double submit, stale reads between check and save. |

Not a miss: an old bug in shared code the change only calls (capture it); a decision recorded in spec §Decisions.
