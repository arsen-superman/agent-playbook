---
name: plan
description: Turn an approved spec into plan.md — phased, commit-sized, verifiable steps. Use when the spec has no blocking questions and the user asks for a plan or approach.
argument-hint: "[task-key]"
---
# Write the plan

Template: `templates/doc/plan.md` in this plugin.

1. Read `task.md`, `spec.md`. Blocking open questions → list them and stop.
2. **Approach** (≤10 lines): what changes, what deliberately doesn't, why. ASCII diagram welcome.
3. **Phases**: Phase 0 for changes to existing logic = pin current behaviour (characterisation test / reproduction that must fail once the fix lands). Last phase = verify every AC + regression.
4. **Test design first** — write `test-cases.md` (`templates/doc/test-cases.md`): at least one case per AC, plus negatives, spec edge cases and "unaffected users" regression. Choose the lowest level that proves the behaviour (unit → integration → e2e); `manual` only for what can't be automated here (UI without e2e framework, external systems). Use the repo's existing test frameworks — new ones only with the user's OK.
5. Each step: `- [ ] <one commit-sized action, naming files and repo> — verify: <command or observable check>`. Steps that add tests name the TC IDs they automate.
6. **Follow-ups** — deliberately not done here; each also `/kb:capture`.
7. **Risks** ≤5 bullets. Set `**Next:**` at the top.
8. Ask for approval. On OK: `status: planned`, Next = first step.
