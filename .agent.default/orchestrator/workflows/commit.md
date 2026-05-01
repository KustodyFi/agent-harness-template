---
description: Stage all changes and commit with a conventional commit message
---

# /commit — Stage & Commit

## When to use

After completing a unit of work and verifying it locally.

## Steps

1. Check for changes: `git status`
2. Stage everything: `git add -A`
3. Review the diff: `git diff --cached --stat`
4. Construct a conventional commit message:

```
<type>(<scope>): <short summary>

<body — one-line-per-change, bullet list>
```

**Types:** `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `style`, `build`

5. Commit: `git commit -m "<message>"`
6. Confirm: `git log -n 1 --oneline`

## Rules

- Never commit secrets, `.env` files, or API keys
- Always include a meaningful scope
- If partial commit needed, ask the user first
