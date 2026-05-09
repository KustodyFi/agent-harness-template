# Review Plan — Task 002: Hooks Layer + Full Harness Audit

## Objective

Multi-agent review of the entire agent-harness-template, including the proposed 5-layer re-architecture with hooks. Three reviewers provide independent perspectives, findings are consolidated into `review.md`.

---

## Reviewers

| Reviewer | Interface | Input Method | Focus Area |
|----------|-----------|-------------|------------|
| **GPT** | Chat UI | `npx repomix` output pasted | Architecture & design soundness |
| **Gemini** | Chat UI | `npx repomix` output pasted | Implementation correctness & gaps |
| **Codex** | Terminal | Reads repo directly | Structural integrity & one-source-of-truth |

---

## Review Rounds

### Round 1: Full Harness Audit (all 3 reviewers)

**Goal:** Independent review of the entire template — current state + proposed hooks layer.

Each reviewer gets:
1. The same base context (repomix output or repo access)
2. A role-specific prompt (see below)
3. Same output format for easy consolidation

**Process:**
1. Run `npx repomix` to generate repo snapshot
2. Send R1 prompt to GPT (chat UI)
3. Send R1 prompt to Gemini (chat UI)
4. Send R1 prompt to Codex (terminal)
5. Orchestrator consolidates findings into `03_structure/review.md`
6. Fix all findings
7. Proceed to R2

### Round 2: Convergence (Codex only)

**Goal:** Verify R1 fixes. Codex re-reads all files.

### Round 3: Final PASS (Codex only)

**Goal:** Confirm PASS. If R2 was clean, skip R3.

---

## Input Preparation

```bash
# Generate repo snapshot for chat-based reviewers
cd ~/Desktop/Github/agent-harness-template
npx repomix
```

This produces a single file with all repo contents that can be pasted into GPT/Gemini chat.

---

## Output Format (all reviewers must use this)

```markdown
### {reviewer}: R1 — {title}
**Date:** YYYY-MM-DD
**Agent:** gpt | gemini | codex
**Mode:** chat | terminal

## Findings

### N. [SEVERITY]: [Title]
**Location:** [file:line]
**Issue:** [what's wrong]
**Fix:** [suggested fix]

## Verdict
PASS | PASS WITH NOTES | NEEDS REVISION
```

---

## Consolidation

After all R1 responses are collected:
1. Orchestrator appends all three reviews to `03_structure/review.md`
2. Deduplicate overlapping findings
3. Prioritize: findings flagged by 2+ reviewers are HIGH priority
4. Fix all findings
5. Commit with attribution
