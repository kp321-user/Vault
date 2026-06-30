**Protocol: Plan → Implement → Log**

## Phase 1 — Plan
(before touching code) 

Write the actual thinking, not a filled template:
- What's the current problem (e.g. "tools/ mixes [[Streamlit]] calls with logic, can't test or reuse the logic")
- What's the target shape (e.g. "core/ = no `st.*` calls, tools/ = thin wrappers")
- Open questions you haven't resolved yet — write these explicitly as `?` bullets, since these become the actual to-do list of thinking, not coding If the thinking's incomplete, leave the `?` bullets unresolved and move on — don't force answers you don't have.

## Phase 2 — Implement
(while you work) 

Convert the resolved parts of the plan into concrete tasks. As you actually do the refactor:
- Check items off as you go
- If you discover the plan was wrong mid-implementation (very normal), don't go back and edit `architecture.md` to pretend you knew it upfront — just note the deviation here in `todo.md`, e.g. "turns out X also needed to move, wasn't in original plan" This matters because it preserves the actual history of what you learned, rather than a sanitized version.

## Phase 3 — Decisions Log
(after, dated) 

One dated entry, written from the finished state:
- What changed (brief)
- Why (link back to the original problem from Phase 1)
- Any deviation from plan worth remembering (pull from Phase 2's notes)
- Link out to `_general/` if any reusable concept came up (e.g. `[[Pylance refactoring]]`)

**The one rule that makes this not just busywork:** each phase only gets written if it's actually true. If implementation went exactly to plan, Phase 3 can be two lines. If Phase 1 was five minutes of thought, it stays five minutes of writing. The protocol's job is to make sure the right file holds the right kind of note at the right time — not to mandate volume.

We're currently mid-Phase-1 on `architecture.md` — still need the **Problem** section filled in before that file's done.