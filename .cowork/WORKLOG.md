# Work Log

> **Purpose:** Shared development log for orchestrator and reviewer agents.
> All agents read this file for context before starting work.
> Orchestrator triages findings and updates this log.

---

## How to Use

1. **Orchestrator** appends entries as work progresses
2. **Reviewer agents** read this log before reviewing, then append findings
3. **Orchestrator** triages findings: ACCEPTED / REJECTED / DEFERRED
4. **Human** approves or rejects the orchestrator's triage decisions

### Entry Format

```markdown
## Round N — [Review Type] (YYYY-MM-DD)

### Reviewer
- **[Agent Name]**: [Focus area] → [N] findings → [VERDICT]

### Findings
| # | Finding | Severity | Decision | Reason |
|---|---------|----------|----------|--------|
| N-1 | Description | HIGH/MEDIUM/LOW | ✅/❌/⏸️ | Reason |
```

---

<!-- Append new entries below this line -->
