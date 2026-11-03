"""Fail if docs/COMMANDS.md doesn't mention every skill and agent as /<plugin>:<name> or <plugin>:<name>.
Usage: python scripts/check_commands.py
"""
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
doc = (root / "docs" / "COMMANDS.md").read_text(encoding="utf-8")
missing = []
for p in sorted((root / "playbooks").iterdir()):
    for s in sorted((p / "skills").glob("*/SKILL.md")) if (p / "skills").exists() else []:
        if f"/{p.name}:{s.parent.name}" not in doc:
            missing.append(f"/{p.name}:{s.parent.name}")
    for a in sorted((p / "agents").glob("*.md")) if (p / "agents").exists() else []:
        if f"{p.name}:{a.stem}" not in doc:
            missing.append(f"{p.name}:{a.stem} (agent)")
if missing:
    print("docs/COMMANDS.md is missing:\n  " + "\n  ".join(missing)); sys.exit(1)
print("docs/COMMANDS.md covers all skills and agents")
