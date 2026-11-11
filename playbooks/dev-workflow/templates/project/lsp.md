# Language servers by stack
<!-- Used by /dev:init-project. Plugin = <name>@claude-plugins-official. Install commands: the plugin's README. -->

| Stack marker in a repo | Plugin | Binary on PATH | Install binary |
|---|---|---|---|
| `*.sln`, `*.csproj` | `csharp-lsp` | `csharp-ls` | `dotnet tool install -g csharp-ls` |
| `package.json`, `tsconfig.json` | `typescript-lsp` | `typescript-language-server` | `npm i -g typescript-language-server typescript` |
| `pyproject.toml`, `requirements*.txt` | `pyright-lsp` | `pyright-langserver` | `npm i -g pyright` |
| `go.mod` | `gopls-lsp` | `gopls` | `go install golang.org/x/tools/gopls@latest` |
| `pom.xml`, `build.gradle*` (Java) | `jdtls-lsp` | `jdtls` | see plugin README |
| `build.gradle.kts` (Kotlin) | `kotlin-lsp` | `kotlin-lsp` | see plugin README |
| `Cargo.toml` | `rust-analyzer-lsp` | `rust-analyzer` | `rustup component add rust-analyzer` |
| `composer.json` | `php-lsp` | `intelephense` | `npm i -g intelephense` |
| `Gemfile` | `ruby-lsp` | `ruby-lsp` | `gem install ruby-lsp` |
| `CMakeLists.txt`, `*.c*/*.h` | `clangd-lsp` | `clangd` | see plugin README |

Plugin: `claude plugin install <plugin>@claude-plugins-official --scope local` (from the project folder) or an `enabledPlugins` entry in `.claude/settings.local.json` once installed.
Check: `Get-Command <binary>` / `which <binary>`; `claude plugin list`.
