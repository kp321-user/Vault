# To Do

## Active

- [x] Create `src/core/transcription.py` — move Whisper call logic out of `1_transcribe.py`
- [ ]  Create `src/core/markdown_audio.py` — move edge-tts logic out of `2_md_to_audio.py`
- [x]  Create `src/core/news.py` — move feedparser/NewsAPI logic out of `3_news.py`
- [x]  Update `1_transcribe.py` to import and call `core.transcription` instead of inline logic
- [x]  (repeat for the other two tools files)
- [x]  Decide `0_home.py` role (header vs index) — resolve before or during this pass
- [ ]  Confirm no `st.*` calls remain in any `core/` file

## Backlog
- [ ]

## Done
