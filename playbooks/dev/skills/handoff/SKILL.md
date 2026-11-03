---
name: handoff
description: End-of-session handoff — save task state so the next session resumes in under a minute, promote decisions and knowledge, clean up. Use when the user says handoff, finish, wrap up, закінчуємо, end session, or before the context gets long.
argument-hint: "[task-key]"
---
# Handoff

Where state goes: **`task.md` (Now/Next, open questions) + `plan.md` (ticks, Next) + `.ai/STATUS.md`**. Nothing else is needed for the next session to resume with `/dev:start`.

**No task in this session** (exploration, a chat-style investigation): don't invent a task — run `/kb:stash` instead; durable findings from it go to `.ai/context/` or `/kb:capture` first.

1. **task.md** — rewrite *Now*: Status (one line), done this session (≤3 bullets), **Next = one concrete action**. Only unresolved open questions. `updated:`.
2. **plan.md** — ticks match reality (with hashes); `**Next:**` current; note reordering.
3. **Decisions** made this session → `spec.md §Decisions`; rewrite what they invalidate. Outlives the task → `.ai/decisions/NNNN-…md` (`templates/doc/decision.md`).
4. **Knowledge about the system/domain** (not the task) → merge into `.ai/context/`; new terms → `glossary.md`.
5. **Uncaptured out-of-scope items** → `/kb:capture`.
6. **Half-formed thinking** that isn't task state (a debugging thread, a hypothesis) → offer `/kb:stash`.
7. **Clean up** — scratch condensed or deleted; long outputs → `raw/`; size limits.
8. **STATUS.md** — task row, Waiting on, inbox count, date.
9. **Self-improvement** — the user corrected the same behaviour twice → propose the exact line for CLAUDE.md or the skill.
10. Reply ≤6 lines: what's saved, Next, and the opening command (`/dev:start <KEY>`).
