# Risk classes — what slips past plan and review

<!-- One list for three stages. Analyst turns classes into rules, matrices and edge cases; planner answers each applicable class in plan.md §Cross-cutting; reviewer checks each against the diff. Class numbers are used in review.md. -->

| # | Class | Ask |
|---|---|---|
| 1 | **Collections and batch** | Does every invariant (limit, total, daily cap, uniqueness) hold for all items of one request together, not only per item? Duplicates or swapped values inside one batch? Partial failure — what is saved? |
| 2 | **Fix on fix** | Does the fix interact with the rest of the diff: checks done twice, a retry lost after an error, a race between parallel requests, an existence leak through ordering? |
| 3 | **Permission matrix** | Every role/permission combination (none / read / write / read+write × admin or not, owner or not) × every affected operation and list. Write-only users? Inactive or disabled entities, "show inactive" filters? |
| 4 | **New or changed field** | Every endpoint, DTO and mapping that returns the entity — create, edit, batch, list, search, export — and every client that reads it, in every repo (code-graph `dependencies`: `used` links). |
| 5 | **Client state, cache, time** | Cache: lifetime, invalidation, never cache a failure, refresh when the day/month/period changes. Time: whose time zone (server, browser, business), period boundaries, defaults from "now". |
| 6 | **Placement and design** | Where does the code live; how much does each class grow (past ~300 lines or a second responsibility → a new service, per repo convention)? Named types over bool flags; validation in the layer the repo uses. `<repo>/REVIEW.md` wins. |
| 7 | **Reuse** | Does a service, helper, endpoint or permission check already do this? Search before writing — also for code the diff rewrites, not only new code; never re-implement a check another service owns. |
| 8 | **Cost and frequency** | How often does it run — app start, every page, every item? Same data loaded twice in one request? N+1, unbounded queries, a new query or filter without an index, UI blocked on a non-essential call? |
| 9 | **Error disclosure** | Do "not found" and "forbidden" look the same to a user without access? Do messages, codes or ids reveal data or existence? |
| 10 | **Concurrency** | The same operation started again before the previous one finished (parallel requests, double submit, overlapping async calls): stale reads between check and save, results applied out of order. |
| 11 | **Silent failure** | What happens when each new call fails? Empty or broad catch, log-and-continue, default/null/mock returned on error, `?.`/`??` skipping a step that must run, retries exhausted without a signal — does the failure reach a log with context and the caller or user? |
| 12 | **Rollout** | Old and new versions run side by side during deploy — API clients, queues, caches, stored data still work? DB migration reversible or safe to run twice? Behind a feature flag? How is it rolled back, and what does rollback do to data written meanwhile? |
| 13 | **Rule interaction** | A new rule that restricts, removes or redirects something — re-check every existing rule that selects, routes to or falls back on the same thing. Do they still produce a valid result together? |
| 14 | **Dead ends** | Every state the change can create still has a way forward: someone or something able to move it on, who also learns that they need to. A rule that takes an ability away names who takes it over. Whether anyone can proceed is decided by who has the permission, not by whether a list of assignees happens to be non-empty. |
| 15 | **Tests that can't fail** | Each new or changed test: what change to the code would make it fail? Negative assertions ("nothing matches", "not present") — can the matcher see every form the thing can take? Inputs from the environment (time, randomness, ordering, locale, machine) are fixed, not live — also those read inside dependencies. |

Not a miss: an old bug in shared code the change only calls (capture it); a decision recorded in spec §Decisions.
