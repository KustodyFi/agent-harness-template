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

**Approval format:**

```markdown
### human: Approve {stage}
**Date:** YYYY-MM-DD
**Status:** APPROVED
**Source:** chat
**Human instruction:** "{exact quote}"
```

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

1. Create folder: `.cowork/tasks/NNN_short_name/`
2. Create `TASK.md` with the task definition
3. Create `STATE.yaml` from the template in `HARNESS_SPEC.md`
4. Create `TIMELINE.md` with the first entry
5. Create stage folders: `01_planning/`, `02_architecture/`, `03_structure/`, `04_implementation/`
6. Create `evidence/` folder
7. Start working on `01_planning/spec.md`

---

## Closing a Task

1. Write `04_implementation/result.md`
2. Fill `evidence/tests.md`, `evidence/changed_files.md`, `evidence/verification.md`
3. Update `STATE.yaml`: `task_status: complete`
4. Human verifies → `task_status: verified`
5. Promote specs to `docs/specs/` if they add permanent knowledge
6. Human closes → `task_status: closed`
