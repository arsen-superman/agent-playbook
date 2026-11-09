---
name: find
description: Find and answer from the personal vault — recipes, how-tos, prompts, saved instructions and notes. Use when the user asks "how did I…", "where is my recipe for…", "що я зберігав про…", "find in my notes", or asks something likely already saved.
argument-hint: "<question>"
---
# Find in the personal vault

Access mode as in `/me:save`: local path from `~/.claude/CLAUDE.md`, else the Google Drive connector folder `Vault` (search by title and full text, read with the connector).

1. **Search** outside `raw/`, `templates/`, `attachments/`: key terms, synonyms and the other language (борщ / borscht, undervolt / андервольт) — file names, frontmatter `aliases`, `summary`, `tags`, headings, then full text. Files mode: Grep; Drive mode: connector search.
2. **On a miss** (no or too many hits): pick the domain from the vault `CLAUDE.md` list and scan that folder's `summary:` lines (`grep -r "^summary:" <Domain>/`). Kind-of-note questions ("all my prompts") → grep `categories` for that category across domains. There are no index files.
3. Read only matching notes. Answer from them, citing `[[note-name]]`. If `applies-to` doesn't match the user's situation (other device, version), say so.
4. Nothing found → answer normally, then offer `/me:save`.
5. The answer combined several notes or added something useful → offer to save the synthesis back.
