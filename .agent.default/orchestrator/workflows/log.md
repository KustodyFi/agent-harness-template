---
description: Append a new round to the change log
---

# /log — Append Change Log Entry

## Steps

1. Read `.agent/shared/log.md`
2. Determine the next round number
3. Append a new entry with this format:

```markdown
## Round N — YYYY-MM-DD HH:MM TZ

**Status:** ✅ Completed | 🔄 In Progress
**Objective:** {what was accomplished}

**Files Created / Modified:**

- `path/to/file` — description

**Next Steps:**

- {what to do next}
```

## Rules

- Always increment the round number
- Include exact file paths, not vague descriptions
- Record decisions made during the session
