Here's everything in memory related to coding conventions and project decisions:
Project structure & shorthand

CODE = C:\Users\Ken\CODE; HUB = Flask app (formerly Link-DB/KP-Homepage); MEDIA = Streamlit app (formerly MediaDesk); POLITICS = Whisper transcription project; NEWS = folder currently inside HUB; Vault = Obsidian knowledge base inside CODE.
Tools: VS Code (editor), Git Bash (terminal), GitHub (version control).

Environment & path conventions

All virtual environments standardized to .venv naming.
whisper-env virtual environment is at C:\Users\Ken\CODE\POLITICS\whisper-env.
ROOT_DIR defined in .env, read via load_dotenv() + os.getenv() — settled on this after working through a config.py complexity issue.
Prefers os.path.dirname() over pathlib's .parent chain for readability.
Prefers forward slashes via .replace("\\", "/").
VS Code terminal default fixed to Git Bash; has a ~/.bashrc activenv alias and a winpath() bash function for converting Windows paths.

Project scaffolding

Built new_proj_startup.py in CODE/proj_template/ using pathlib, subprocess, and GitHub CLI (gh repo create) for one-command repo creation.

MEDIA-specific

Refactor in progress: separating src/tools/ (Streamlit UI) from src/core/ (pure logic).
Fixed DATA_DIR path miscalculation bug.

HUB-specific

Job-based progress tracking for media converter using threading, uuid, progress_hooks/postprocessor_hooks from yt-dlp, with frontend polling.
Added is_read boolean to HistoryPage model; resolved a PostgreSQL boolean-to-integer migration on Render via TablePlus.
Ran Claude Code to audit app.py; fixed an open redirect vulnerability.
Local database path issue caused by a .env override — resolved.

Documentation hierarchy (most recent, just added)

Three tiers: Git commit history (raw diffs) → <project>/changelog.md (minor/incremental changes, dated one-liners, per-project repo) → Vault/projects/<name>/decisions.md (major architecture decisions only, Vault's own repo).
Vault structure: _inbox/, _general/, projects/ (grouping each project's architecture.md/todo.md/decisions.md).
Vault .gitignore excludes .obsidian/workspace.json, workspace-mobile.json, cache.
Project READMEs may have a local-convenience-only relative link to Vault docs (works in VS Code, not guaranteed on GitHub.com).

Acronym dictionary

ref_dict_acronyms_terms.md moved into Vault/_inbox/, to be sorted later into Vault/_general/acronyms-terms.md.

If you want, I can turn this into an actual CLAUDE.md file for Claude Code to read directly in your repos, since it won't see any of this otherwise.