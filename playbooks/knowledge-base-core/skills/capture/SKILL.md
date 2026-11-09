---
name: capture
description: Capture an out-of-scope todo, finding, bug, idea or question into the knowledge-base inbox without acting on it. Use proactively whenever you notice something outside the current task's scope, and when the user says "add to todo", "note this", "запиши", "на потім", "закинь в інбокс".
argument-hint: "<what>"
---
# Capture to inbox

**Locate the KB root:** the nearest `.ai/` folder from the current directory upward (a project knowledge base); if there is none, the personal vault from `~/.claude/CLAUDE.md` (`Personal vault:` line); if neither exists, ask.

1. Duplicate check: grep `<kb>/inbox/` and active tasks for the same subject. Found → append one evidence line to that item and stop.
2. Create `<kb>/inbox/YYYY-MM-DD-<kebab-slug>.md` (≤15 lines):
   ```markdown
   ---
   type: todo | finding | bug | idea | question
   priority: low | normal | high
   source: <task key / session date / conversation>
   created: YYYY-MM-DD
   ---
   # <one-line title>

   **What:** <self-contained description>
   **Where:** <file:line, query, link, person>
   **Why it matters:** <impact>
   **Suggested action:** <task / ticket / knowledge / ask someone>
   ```
   Type guide: `todo` work to do · `finding` fact learned · `bug` defect · `idea` possible improvement · `question` someone must answer.
3. It must be readable in a month without this conversation: include paths, names, links.
4. Reply with one line — `📥 <title>` — and continue the current work. Do not start working on the item.
