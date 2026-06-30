Here's the three-tier hierarchy, from most granular to most abstracted:

**1. Git commit history (most minute)**  
The raw, unfiltered record of every single change — every save point, every line diff, including small or messy commits (typo fixes, WIP, etc.). This is the ground truth if you ever need the _exact_ code-level diff or need to revert something. Viewed via `git log` or the GitHub.com commits tab — functional but not meant for casual reading.

**2. `changelog.md` (project folder, mid-level)**  
Lives inside each project (`HUB/`, `MEDIA/`, etc.), backed up by that project's own repo — independent of Vault. This is where I document the **minor/incremental changes** as they happen: bug fixes, small additions, tweaks — dated, terse, one-liner-per-entry. It's a curated summary layer above raw commits: groups related changes into readable entries, skippable in a glance, no need to dig through Git history for the small stuff.

**3. `Vault/projects/<name>/decisions.md` (most abstracted)**  
The planning layer — reserved for **major decisions**: architecture choices, why one approach was picked over another, tradeoffs considered. This is the "why" record, not the "what." Lower frequency, higher significance, and lives in Vault's own separate repo as part of your broader project planning/documentation system.

**The logic of the hierarchy:** as you move up (commits → changelog → decisions), the entries get less frequent, more curated, and shift from _what exactly changed_ → _what changed in summary_ → _why something significant changed_. Each layer also happens to be backed up independently (project repo for commits + changelog, Vault repo for decisions), so no single point of failure documents everything.