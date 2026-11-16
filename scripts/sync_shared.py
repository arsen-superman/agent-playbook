"""Keep text shared between plugins identical. Source of truth: shared/ (see shared/manifest.json).

  copy   shared/<file> -> playbooks/<plugin>/templates/shared/<file>   (plugins must be self-contained)
  embed  shared/<file> must appear verbatim inside every file matching the glob (agents cannot include files)

Usage: python scripts/sync_shared.py          write the copies, then check
       python scripts/sync_shared.py --check  check only (pre-commit)
"""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
shared = root / "shared"


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    manifest = json.loads(text(shared / "manifest.json"))
    bad = []
    for name, plugins in manifest.get("copy", {}).items():
        source = text(shared / name)
        for plugin in plugins:
            target = root / "playbooks" / plugin / "templates" / "shared" / name
            if target.exists() and text(target) == source:
                continue
            if check_only:
                bad.append(f"{target.relative_to(root).as_posix()}: differs from shared/{name}")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(source, encoding="utf-8", newline="\n")
                print(f"wrote {target.relative_to(root).as_posix()}")
    for name, rule in manifest.get("embed", {}).items():
        block = text(shared / name).strip()
        exempt = set(rule.get("exempt", []))
        for path in sorted(root.glob(rule["glob"])):
            rel = path.relative_to(root).as_posix()
            if rel not in exempt and block not in text(path):
                bad.append(f"{rel}: does not contain shared/{name} verbatim")
    if bad:
        print("shared text out of sync (fix, or run: python scripts/sync_shared.py):\n  " + "\n  ".join(bad))
        return 1
    print("shared OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
