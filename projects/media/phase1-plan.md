# Architecture

Current problem: 
- Programming logic is a combination of user-interface and application code, which makes  knowledge gaps difficult to locate when troubleshooting the program
- Questions about the functionality and capabilities of the user-interface ([[Streamlit]]) are muddled with the functionality and capabilities of the API calls and internal processing of the program
Goal:
- distinguish "core" functions from the so-called "tools"
- "tools" are the user-facing objects that call the useful "core" programs to do something useful, like a format conversion or internet query.  In other words "tools" presentation/UI layer layer.
- "core" objects are the APIs and processing operations that are hidden from the user and could be used by any other program, but are independent of UI (no [[Streamlit]] `st.*` calls). In other words "core" is the business logic/domain layer.
Open questions:
- ?  [[0_home.py]] - either a header displayed at the top of each page or an index for the other pages

High-level overview of how this project is structured.
```
MEDIA/
└── src/
    ├── tools/          ← stays: anything with st. calls (UI/pages)
    │   ├── 0_home.py
    │   ├── 1_transcribe.py
    │   ├── 2_md_to_audio.py
    │   └── 3_news.py
    └── core/           ← new: pure logic, no st. calls
        ├── transcription.py   (Whisper calls, etc.)
        ├── markdown_audio.py  (edge-tts conversion logic)
        └── news.py            (RSS/feedparser logic)
```

## Components
- [[0_home.py]] - TBD see open questions
- [[1_transcribe.py]] - UI for [[transcription.py]]
- [[2_md_to_audio.py]] - UI for [[markdown_audio.py]]
- [[3_news.py]] - UI for [[news.py]]
- [[transcription.py]] - conversion of audio to text using [[Whisper]] 
- [[markdown_audio.py]] - conversion of text to audio using [[edge TTS]]
- [[news.py]] - [[NewsAPI.org]] calls (experimental)

## Notes
- This is an extract refactor of the original programs where the tools/core distinction was not included in the program (check terminology here)
- This is also a test-case for using Obsidian to plan, implement and document programming work
