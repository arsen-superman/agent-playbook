---
name: requirements
description: "Specify a feature before it becomes tasks (business analyst): actors, scenarios, business rules, scope, open questions — written to .ai/specs/FEATURE.md, no code. Triggers: requirements, feature spec, business analysis, вимоги, специфікація фічі, опиши бізнес-правила, побудь аналітиком."
argument-hint: "<feature | idea | ticket | file>"
---
# Feature requirements (business analyst)

A feature spec is the durable, current-truth description of a feature: what it does and why, in business terms. It outlives tasks — `/dev:spec` maps one task onto code and takes its rules from here. Template: `templates/doc/feature-spec.md` in this plugin. Writes no code and no task files.

1. **Find it.** Grep `.ai/specs/`, `.ai/context/`, `.ai/decisions/` and the glossary for the feature — an existing spec is updated in place, never duplicated. A repo's `docs/` or the team wiki already owns this spec → link it and work on a draft for that page (KB rule: link, don't copy).
2. **Sources.** Read what the user gave: idea file, ticket or epic (tracker connector), notes; long material → `/kb:ingest` first. Existing behaviour matters → `dev:scout` for facts with `file:line`; don't read code yourself.
3. **Ask**, a few questions at a time, your recommendation first: who the actors are and what each wants; the main scenario and its alternatives; what must never happen; what is out of scope; how success is measured. Push back on vague answers ("fast", "as usual") until they are testable.
4. **Write** `.ai/specs/<kebab-feature>.md` (≤250 lines): Purpose · Actors · Scenarios (numbered steps, alternatives, failures) · Rules (R-IDs, each with its source) · Data and states · Out of scope · Open questions (who answers). Walk risk classes 1, 3, 5, 9, 13, 14, 16 (`templates/checklists/risk-classes.md` in this plugin) for rules: a permission matrix when roles differ, rules that must hold across a batch, every state with a way forward.
5. **Check** before showing: every scenario step is covered by a rule or needs none; no two rules contradict; each rule is testable; terms match the glossary (new ones → `glossary.md`).
6. **Slice** — propose tasks: thin end-to-end slices, each naming the rules it delivers and what it depends on. On OK create them with `/dev:new-task` (`source:` = this spec), or draft tracker tickets — created only on explicit OK.
7. A blocking question for someone else → draft the message; post only on OK. Publishing the spec to the team wiki → draft the page; publish only on OK, then keep a link line here instead of the text.
8. Reply ≤8 lines: file, rule count, open questions, proposed slices.

**Update mode** (the spec exists): change rules in place — current truth, R-IDs never renumbered, a removed rule → one line under *Removed* with why; list the open tasks that cite a changed rule.
