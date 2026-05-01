---
description: Push current branch to origin
---

# /push — Push to Remote

## Steps

1. Check current branch: `git branch --show-current`
2. Push: `git push origin <branch>`
3. If push fails: **STOP.** Tell the user the error. Do NOT retry.

## Rules

- Push is the human's responsibility — suggest the command, let them run it
- Never force-push without explicit human approval
- Never push to main without review
