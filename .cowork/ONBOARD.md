# Onboarding Guide — Process Interaction

> **Startup:** Read `AGENTS.md` first.
> See `AGENTS.md` for the authoritative startup sequence.
>
> This file describes how each role interacts with the harness process.
> For role identity, skills, and limits, see `.agent/{role}/ROLE.md` (Layer 2).

---

## Quality Standards

See the project's coding standards (referenced in `AGENTS.md` folder map).
See `agent.md` for operational rules.

---

> **Note:** These sections describe how each role interacts with the harness process.
> For role identity, skills, and limits, see `.agent/{role}/ROLE.md` (Layer 2).

## Role: Human (HIL)

**What you do in the harness:**

1. Define tasks by creating `TASK.md`
2. Request reviews by sending prompts to reviewer agents
3. Approve or reject stage deliverables
4. Close tasks after verification

**Entry format:** See "Attribution Format" below.

---

## Role: Orchestrator

**What you do in the harness:**

1. Read the active task: `.cowork/tasks/NNN/TASK.md`
2. Check the gate: `.cowork/tasks/NNN/STATE.yaml`
3. Write `spec.md` for the current stage
4. Prepare reviewer prompts (use `.cowork/prompts/review_stage.md`)
5. Incorporate reviewer feedback into `spec.md`
6. Update `STATE.yaml` when human approves
7. Log events in `TIMELINE.md`
8. At Stage 04, write code and produce evidence

**Entry format:** See "Attribution Format" below.

---

## Role: Reviewer

**What you do in the harness:**

1. Receive context from orchestrator (via human)
2. Read `spec.md` in the active stage
3. Verify claims with read-only commands
4. Append findings to `review.md`
5. State verdict: PASS / PASS WITH NOTES / NEEDS REVISION

**Entry format:** See "Attribution Format" below.

---

## Attribution Format

Every `review.md` entry has attribution:

```markdown
### orchestrator: {title}
**Date:** YYYY-MM-DD
**Agent:** {ide-name} ({model})

### agent: {title}
**Date:** YYYY-MM-DD
**Agent:** codex | gpt | gemini
**Mode:** terminal | chat | deep-research

### human: {title}
**Date:** YYYY-MM-DD
**Status:** APPROVED | CHANGES REQUESTED
**Source:** chat
**Human instruction:** "{exact quote}"
```

---

## Critical Rules

See `.cowork/HARNESS_SPEC.md` → "Gate Rules" for the canonical process rules.
See `agent.md` §1 (human-gated workflow) and §7 (operational process) for operational rules.

---

## Creating a New Task

See `.cowork/tasks/README.md` for the canonical task folder structure.

---

## Closing a Task

See `.cowork/tasks/README.md` → "Closing a Task" for the canonical close procedure.
