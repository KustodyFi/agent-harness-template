---
name: Code Review Skill
description: How to perform structured code and spec reviews.
---

# Code Review Skill

## When to Use
When asked to review a spec, code, or architecture document.

## Process
1. Read the `review.md` in the active stage directory — it contains review instructions
2. Read the corresponding `spec.md`
3. Verify all claims with read-only commands
4. Append findings using the entry format from `ROLE.md`
5. State your verdict

## What to Check
- Are factual claims verifiable? (file paths, line counts, function names)
- Are there internal inconsistencies?
- Are there stale references to moved/deleted files?
- Does the spec match the actual codebase?
- Are there duplicate content across files?
