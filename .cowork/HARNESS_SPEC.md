# Harness Specification — Task Stage Process

> **Authoritative process rules for task execution.**
> This file defines the stage workflow, gate rules, and evidence requirements.

---

## Task Stages

Every task follows four stages. No stage may be skipped.

```
01_planning → 02_architecture → 03_structure → 04_implementation
```

| Stage | What | Deliverable |
|-------|------|------------|
| **01_planning** | Scope, schedule, risks, non-goals | `spec.md` |
| **02_architecture** | System design, data flow, boundaries | `spec.md` |
| **03_structure** | Files, classes, functions, call flow | `spec.md` |
| **04_implementation** | Code plan, actual code, tests | `spec.md` + `result.md` |

---

## Stage Workflow

```
Orchestrator writes spec.md
       │
       ▼
Human requests review ──► Reviewer reads + appends to review.md
       │
       ▼
Orchestrator revises spec.md based on findings
       │
       ▼
Human: APPROVED ──► advance to next stage
  or: CHANGES REQUESTED ──► repeat review loop
```

---

## Gate Rules

1. **No skipping.** Stages must proceed in order: 01 → 02 → 03 → 04.
2. **No coding before 04.** `coding_allowed` is `false` until Stage 04 is approved and status transitions to `coding`.
3. **Human approval required.** Only the human can advance a stage.
4. **Review before approval.** Each stage must have at least one review round.
5. **Append-only reviews.** Never delete review entries.

---

## STATE.yaml

Each task has a `STATE.yaml` that tracks the current position:

```yaml
task: "NNN_task_name"
task_status: active
current_stage: planning
current_stage_status: pending
coding_allowed: false

stages:
  planning:
    status: pending
    review_rounds: 0
  architecture:
    status: pending
    review_rounds: 0
  structure:
    status: pending
    review_rounds: 0
  implementation:
    status: pending
    review_rounds: 0
```

Valid statuses: `pending` → `in_review` → `changes_requested` → `approved`
Implementation adds: `coding` → `complete`

---

## Evidence Requirements

Before a task can be closed, these files must exist:

```
evidence/
├── tests.md           ← Raw test output
├── changed_files.md   ← Every file changed + why
└── verification.md    ← Final verification summary
```

---

## Validation

```bash
# Requires: pip install pyyaml
python3 .cowork/harness/validate_state.py .cowork/tasks/NNN_name/STATE.yaml
```

The validator checks:
- Required fields present
- `coding_allowed` invariant (false until implementation)
- Valid stage and status values
