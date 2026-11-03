"""Pack playbooks as .zip files for claude.ai / desktop upload (Customize > Plugins > Add > Upload plugin).
Usage: python scripts/pack.py [playbook ...]   (default: me)   → dist/<name>-<version>.zip
"""
import json, sys, zipfile
from pathlib import Path

root = Path(__file__).resolve().parent.parent
names = sys.argv[1:] or ["me"]
(root / "dist").mkdir(exist_ok=True)
for name in names:
    src = root / "playbooks" / name
    version = json.loads((src / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
    out = root / "dist" / f"{name}-{version}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(src.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(src).as_posix())
    print(out)
