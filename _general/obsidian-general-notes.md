**The core split to keep in your head**

Obsidian holds _thinking and documentation_, not the code itself. So:

- `CODE/HUB/`, `CODE/MEDIA/`, `CODE/POLITICS/` — actual code, stays exactly where it is, untouched by any of this.
- [[Vault/HUB]]/, `Vault/MEDIA/`, `Vault/POLITICS/` — your _notes about_ that code (decisions, architecture, todos) — separate, parallel structure.

You're not moving code into Obsidian. You're building a documentation layer next to it.

**How a project note should actually get used, concretely**

Right now `HUB/decisions.md` is just an empty template. The intended use, based on stuff you've already done (DATABASE_URL override bug, open redirect fix, path traversal fix) — each of those deserved a dated entry:

markdown

```markdown
## 2026-05-12
Fixed DATABASE_URL override of BASE_DIR causing wrong SQLite path.
Root cause: .env DATABASE_URL took precedence over the BASE_DIR fix.
See: [[SQLite]] [[python-dotenv]]
```

That's it — a log entry, with optional links out to general concepts if they're reusable elsewhere.

**Where general notes plug in**

`_general/` is for things that don't belong to one project — a concept, a tool, a workflow. The link is the bridge: a project decision can reference `[[CUDA]]` or `[[Whisper setup]]` living in `_general/`, so the general note accumulates context from every project that touched it (this is the backlink payoff from a few messages ago, now actually doing real work instead of a glossary stub).

**A realistic day-to-day loop**, not a big upfront reorg:

1. You fix a bug / make an architecture decision in HUB → open `Vault/HUB/decisions.md` → add a dated entry, right then, while it's fresh.
2. You learn something generally reusable (a Python concept, a CLI trick) → it goes in `_general/`, not buried inside a project file.
3. Quick thought mid-work, unsure where it belongs → `_inbox.md`, sort later.
4. Weekly-ish: skim `_inbox.md`, file things into the right project or `_general/`.

**What I'd avoid**

Don't try to retroactively document everything you've ever built in one sitting — that's the kind of upfront-perfection trap that kills a system before it's used. Start documenting _forward_ from today (new decisions, new learning), and only backfill old stuff if it's actively useful to recall later (e.g. the DATABASE_URL bug is worth backfilling since it's the kind of thing you could hit again).

Does that loop — log decisions as you make them, link out to general concepts, dump uncertain stuff in inbox — feel workable as your actual habit, or does part of it feel like friction you'd skip?