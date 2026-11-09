"""Pack playbooks as .zip files for claude.ai / desktop upload (Customize > Plugins > Add > Upload plugin).
Usage: python scripts/pack.py [plugin-name ...]   (default: me)   → dist/<name>-<version>.zip
Plugins are found by the `name` in their plugin.json, not by folder name.
"""
import json, sys, zipfile
from pathlib import Path

root = Path(__file__).resolve().parent.parent
plugins = {json.loads(m.read_text(encoding="utf-8"))["name"]: m.parent.parent
           for m in (root / "playbooks").glob("*/.claude-plugin/plugin.json")}
names = sys.argv[1:] or ["me"]
unknown = [n for n in names if n not in plugins]
if unknown:
    sys.exit(f"unknown plugin(s): {', '.join(unknown)}; known: {', '.join(sorted(plugins))}")
(root / "dist").mkdir(exist_ok=True)
for name in names:
    src = plugins[name]
    version = json.loads((src / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
    out = root / "dist" / f"{name}-{version}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(src.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(src).as_posix())
    print(out)
