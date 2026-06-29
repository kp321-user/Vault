```
Vault/
├── _general/              # cross-project reference, not tied to one codebase
│   ├── acronyms-terms.md  # your existing ref_dict file, moved/linked here
│   ├── python-concepts.md
│   ├── workflows.md       # e.g. "how I set up a new venv", git workflow notes
│   └── tools.md           # VS Code tricks, bashrc aliases, etc.
├── HUB/
│   ├── architecture.md
│   ├── decisions.md       # why you made certain calls (e.g. DATABASE_URL fix)
│   └── todo.md
├── MEDIA/
│   ├── architecture.md
│   ├── decisions.md
│   └── todo.md
├── POLITICS/
│   ├── architecture.md
│   ├── decisions.md
│   └── todo.md
└── _inbox.md              # quick capture, unsorted — sort later

```

## Notes
- \_general/ with a leading underscore sorts it to the top of the folder list visually — a small Obsidian convention so reference material doesn't get buried alphabetically between HUB and MEDIA.
- decisions.md per project: "why did I structure it this way?" and exactly what you'd want six months from now when you've forgotten the reasoning. Just dated bullet entries.
- \_inbox: "where does this go" drop-box. (weekly review, or whenever).
- Cross-project stuff can still link both ways — e.g. a note in MEDIA/architecture.md can link to \_general/python-concepts.md with [[python-concepts]] even though they're in different folders. Obsidian doesn't care about folder structure for linking.