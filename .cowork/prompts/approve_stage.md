# Prompt: Approve a Stage (HIL)

Quick-approval template for the human:

---

```markdown
### human: Approve {stage_name}
**Date:** YYYY-MM-DD
**Status:** APPROVED
**Source:** chat
**Human instruction:** "Approved — proceed to next stage"
```

**After approving:**
1. Orchestrator updates `STATE.yaml` to advance the stage
2. Orchestrator logs the transition in `TIMELINE.md`
3. Work begins on the next stage
