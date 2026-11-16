"""Validate YAML frontmatter of every tracked Markdown file (skills, agents, templates, docs)."""
import re
import subprocess
import sys

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("check_frontmatter.py needs PyYAML: python -m pip install pyyaml")

REQUIRED = {"SKILL.md": ("name", "description")}
MAX_DESCRIPTION = 350   # chars; a model-invocable skill's description sits in context on every turn
MAX_AUTO_BODY = 3500    # chars; body of a model-invocable skill, loaded on each use


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
        is_skill = name == "SKILL.md"
        is_agent = "/agents/" in f and f.startswith("playbooks/")
        if (is_skill or is_agent) and isinstance(data, dict):
            # Size is measured in characters: lines can be arbitrarily long, tokens follow characters.
            if not re.search(r'^description: "', m.group(1), re.M):
                print(f"{f}: description must be wrapped in double quotes")
                bad += 1
            desc = data.get("description") or ""
            if len(desc) > MAX_DESCRIPTION:
                print(f"{f}: description is {len(desc)} chars (max {MAX_DESCRIPTION})")
                bad += 1
            body = len(text) - len(m.group(0))
            if is_skill and not data.get("disable-model-invocation") and body > MAX_AUTO_BODY:
                print(f"{f}: body is {body} chars (max {MAX_AUTO_BODY} for a model-invocable skill)")
                bad += 1
    print("frontmatter OK" if not bad else f"{bad} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
