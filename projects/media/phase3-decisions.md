# MEDIA — Decisions Log

## 2026-06-26
Initiated Phase 3 refactor — extracted tools/core separation that was absent from the original codebase.

## 2026-06-28
Added four tools to the Streamlit app:
- YT Converter — download YouTube video as MP3 or MP4
- Transcription — transcribe audio to text via Whisper
- Markdown to Audio — convert Markdown file to MP3 via text-to-speech
- News Feed — search recent articles via NewsAPI

## 2026-06-29 — Path resolution & config
**Problem:** Each tool in `src/tools/` independently computed paths to `data/` using `os.path.dirname(__file__)`, which was fragile and caused at least one `DATA_DIR` miscalculation bug.

**Attempted:** A shared `config.py` (tried at both `MEDIA/src/config.py` and `MEDIA/config.py`) to compute `ROOT_DIR`, `DATA_DIR`, etc. once and import everywhere. Failed — Streamlit's page-loading doesn't add the project root to Python's import path, causing `ModuleNotFoundError` regardless of placement.

**Decided:** Abandoned shared `config.py` for path resolution. Added `ROOT_DIR` to `.env` as the fallback plan — but it was never wired up in the code.

**Resolved:** Claude Code audit found `ROOT_DIR` was dead config. Hardcoded `C:\Users\Ken\Downloads` in two tool files replaced with `Path.home() / "Downloads"` — cross-platform, no `.env` needed. `ROOT_DIR` removed from `.env`.

**Current state:**
- Data file paths — `os.path.dirname(__file__)` relative resolution per file
- Default download folder — `Path.home() / "Downloads"`
- `config.py` — JSON-backed settings store for user preferences (e.g. save folder override), unrelated to path resolution

**Note:** `os.path.dirname(__file__)` for internal data files is intentional and correct — it anchors each file to its own location in the repo, which is stable. Not a problem to solve unless files are moved.
