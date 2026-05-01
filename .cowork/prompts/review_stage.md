# Prompt: Review a Stage

Send this to a reviewer agent to review the current stage:

---

**Goal:** Review the {STAGE_NAME} spec for task {TASK_NAME}.

**Read these files:**
1. `.cowork/tasks/{TASK_ID}/TASK.md` — what we're building
2. `.cowork/tasks/{TASK_ID}/{STAGE_FOLDER}/spec.md` — the spec to review
3. `.cowork/tasks/{TASK_ID}/{STAGE_FOLDER}/review.md` — previous review rounds (if any)

**Check:**
- Are all claims verifiable? Use read-only commands to verify.
- Are there internal inconsistencies?
- Are there stale references?
- Is anything missing?

**Write findings** into `.cowork/tasks/{TASK_ID}/{STAGE_FOLDER}/review.md` using this format:

```markdown
### agent: {stage} R{N} Review
**Date:** YYYY-MM-DD
**Agent:** {your-name} ({model})
**Mode:** terminal

## Findings
### 1. [SEVERITY]: [Title]
**Location:** [file:line]
**Issue:** [description]
**Fix:** [suggestion]

## Verdict
PASS | PASS WITH NOTES | NEEDS REVISION
```

Do NOT modify any other file.
