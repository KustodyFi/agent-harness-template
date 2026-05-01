---
description: Show project status and recent activity
---

# /status — Project Status

## Steps

1. Read `.cowork/STATUS.md` — project dashboard
2. Check git status: `git status --short`
3. Show recent commits: `git log -n 5 --oneline`
4. If harness task is active, show `STATE.yaml` current stage

## Output Format

```
Phase: {current phase}
Task: {active task or "none"}
Stage: {current stage} — {status}
Git: {clean | N files modified}
Last commit: {hash} {message}
```
