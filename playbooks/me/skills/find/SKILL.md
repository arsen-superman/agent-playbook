---
name: find
description: Find and answer from the personal vault — recipes, how-tos, saved instructions and notes. Use when the user asks "how did I…", "where is my recipe for…", "що я зберігав про…", "find in my notes", or asks something likely already saved.
argument-hint: "<question>"
---
# Find in the personal vault

Access mode as in `/me:save`: local path from `~/.claude/CLAUDE.md`, else the Google Drive connector folder `Vault` (search by title and full text, read with the connector).

1. Read `index.md` first; pick candidates. Then search for key terms, synonyms and the other language (борщ / borscht, undervolt / андервольт).
2. Read only matching notes. Answer from them, citing `[[note-name]]`. If `applies-to` doesn't match the user's situation (other device, version), say so.
3. Nothing found → answer normally, then offer `/me:save`.
4. The answer combined several notes or added something useful → offer to save the synthesis back.
