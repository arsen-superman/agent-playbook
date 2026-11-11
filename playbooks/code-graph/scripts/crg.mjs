// Launcher for the cross-repo-graph npm package, pinned to one version.
//   node crg.mjs serve --index <dir>                 MCP server over stdio (used by .mcp.json)
//   node crg.mjs index [--project <dir>] [--force]   foreground indexing (used by /code-graph:reindex)
//   node crg.mjs index-background --project <dir>    SessionStart hook: fetch (at most every 30 min) + index, detached; returns at once
// Runs npx through node itself, so it works on Windows without a cmd /c wrapper.
// CRG_PACKAGE overrides the package spec (e.g. a local checkout path while developing).
import { spawn } from "node:child_process";
import { existsSync, mkdirSync, openSync } from "node:fs";
import { dirname, join, resolve } from "node:path";

const PACKAGE = process.env.CRG_PACKAGE || "cross-repo-graph@0.1.1";
const [cmd, ...rest] = process.argv.slice(2);

function npx(args) {
  const bin = dirname(process.execPath);
  const cli = [join(bin, "node_modules", "npm", "bin", "npx-cli.js"), join(bin, "..", "lib", "node_modules", "npm", "bin", "npx-cli.js")].find(existsSync);
  const full = ["--yes", PACKAGE, ...args];
  if (cli) return { command: process.execPath, args: [cli, ...full], shell: false };
  const quote = (a) => (/[\s"]/.test(a) ? `"${a.replace(/"/g, '\\"')}"` : a);
  return process.platform === "win32"
    ? { command: ["npx", ...full].map(quote).join(" "), args: [], shell: true }
    : { command: "npx", args: full, shell: false };
}

function arg(name) {
  const i = rest.indexOf(name);
  return i >= 0 ? rest[i + 1] : undefined;
}

if (cmd === "index-background") {
  const project = resolve(arg("--project") || process.env.CLAUDE_PROJECT_DIR || ".");
  // only projects set up by /dev:init-project; stay silent: hook stdout would land in the session context
  if (!existsSync(join(project, ".ai"))) process.exit(0);
  const indexDir = join(project, ".ai", ".index");
  mkdirSync(indexDir, { recursive: true });
  const log = openSync(join(indexDir, "index.log"), "w");
  const r = npx(["index", "--project", project, "--index", indexDir, "--fetch", "--fetch-min-interval", "30"]);
  const child = spawn(r.command, r.args, { cwd: project, detached: true, stdio: ["ignore", log, log], shell: r.shell, windowsHide: true });
  child.unref();
  process.exit(0);
}

if (cmd === "serve" || cmd === "index") {
  const r = npx([cmd, ...rest]);
  const child = spawn(r.command, r.args, { stdio: "inherit", shell: r.shell, windowsHide: true });
  child.on("exit", (code, signal) => process.exit(code ?? (signal ? 1 : 0)));
  child.on("error", (err) => { console.error(`code-graph: cannot start ${PACKAGE}: ${err.message}`); process.exit(1); });
} else {
  console.error("usage: crg.mjs serve|index|index-background [options]");
  process.exit(2);
}
