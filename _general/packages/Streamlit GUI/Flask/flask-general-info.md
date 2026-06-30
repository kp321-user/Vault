# Flask

Lightweight Python web framework — foundation of HUB. "Lightweight" (micro-framework) means it provides routing, request handling, and templates, leaving database/auth/forms as optional libraries you choose yourself (vs. Django, which bundles more by default).

**Core pieces:** Routes (`@app.route('/path')`) map URLs to Python functions. Request/response cycle: receive request → route function runs → return HTML/JSON/redirect. Templates use Jinja2 to inject Python data into HTML. Static files (JS/CSS/images) served from `static/` by convention.

**Applied in HUB:** Config via `.env` + `load_dotenv()` (e.g. `ROOT_DIR`), replacing an earlier `config.py` approach. No built-in DB layer — uses an ORM on top (e.g. `HistoryPage` model with `is_read` boolean). Synchronous by default, so the media converter's long-running jobs needed `threading` + `uuid` job IDs with frontend polling. Claude Code audit of `app.py` caught an open redirect vulnerability (classic Flask pitfall — unvalidated redirect from a URL parameter).

**Flask vs. MEDIA's stack:** HUB (Flask) = multi-page, route-based, more control/more code. MEDIA (Streamlit) = script-based, reruns top-to-bottom, faster iteration, less control.
