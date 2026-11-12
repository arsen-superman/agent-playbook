"""Validate YAML frontmatter of every tracked Markdown file (skills, agents, templates, docs)."""
import re
import subprocess
import sys

import yaml

REQUIRED = {"SKILL.md": ("name", "description")}


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    files = subprocess.check_output(["git", "ls-files", "*.md"], text=True, encoding="utf-8").split("\n")
    bad = 0
    for f in filter(None, files):
        text = open(f, encoding="utf-8").read()
        if not text.startswith("---"):
            if f.endswith("SKILL.md"):
                print(f"{f}: missing frontmatter")
                bad += 1
            continue
        m = re.match(r"---\r?\n(.*?)\r?\n---", text, re.S)
        if not m:
            print(f"{f}: unclosed frontmatter")
            bad += 1
            continue
        try:
            data = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            print(f"{f}: invalid YAML: {str(e).splitlines()[0]} ({getattr(e, 'problem_mark', '')})")
            bad += 1
            continue
        name = f.rsplit("/", 1)[-1]
        for key in REQUIRED.get(name, ()):
            if not isinstance(data, dict) or not isinstance(data.get(key), str) or not data[key].strip():
                print(f"{f}: missing or non-string '{key}'")
                bad += 1
        if name == "SKILL.md" and isinstance(data, dict) and data.get("name") != f.split("/")[-2]:
            print(f"{f}: name does not match folder")
            bad += 1
    print("frontmatter OK" if not bad else f"{bad} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
