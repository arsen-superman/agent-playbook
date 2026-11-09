---
name: ingest
description: Ingest a source (meeting notes, transcript, Confluence/Drive document, Jira epic, article, chat answer) into the knowledge base — split it into facts, decisions, tasks and questions and file each where it belongs. Use when the user pastes or points to material and says ingest, занеси в базу, розклади, save this meeting, process these notes.
argument-hint: "<file | url | pasted text>"
---
# Ingest a source

Principle (from Karpathy's LLM Wiki): sources are immutable raw material; the knowledge base holds compiled, current-truth knowledge with links back to sources.

**Locate the KB root:** the nearest `.ai/` folder from the current directory upward (a project knowledge base); if there is none, the personal vault from `~/.claude/CLAUDE.md` (`Personal vault:` line); if neither exists, ask.

1. **Keep the source.** Save it verbatim to `<kb>/raw/YYYY-MM-DD-<slug>.md` (or note the URL if it lives in Drive/Confluence/Jira — don't copy what has an owner). Never edit raw files later. A web page → `defuddle parse <url> --md` if installed (full clean text); else WebFetch, and mark the raw file `summary, not verbatim`.
2. **Extract** into four lists and show them to the user before writing:
   - **Facts** (how the system/domain/thing is) → which `context/` file (or vault note) each goes to
   - **Decisions** (choice + why + who) → decision records
   - **Actions / todos** → inbox items or tasks
   - **Open questions** → inbox items type `question`, with who should answer
3. After OK: merge facts into existing files in current-truth form (rewrite, don't append "UPDATE"); when a fact contradicts an existing one, show both and ask which is true. Every merged fact gets a source link: `(src: raw/2026-11-02-sync.md)`.
4. Update the KB's index if it has one. Personal vault: no index files — new notes follow `/me:save` rules (domain folder, `categories`, `summary`).
5. Reply: what went where, in ≤8 lines, plus anything that contradicted existing knowledge.
