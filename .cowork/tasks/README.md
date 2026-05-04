# Tasks — All Work Lives Here

> Every task gets its own folder under `.cowork/tasks/`.

## Naming Convention

```
NNN_short_description/
```

Examples:
- `001_auth_service/`
- `002_redis_migration/`
- `003_ui_dashboard/`
- `004_codebase_review/`

## Task Structure

Each task folder contains:

```
NNN_name/
├── TASK.md                    ← What to build (human defines)
├── STATE.yaml                 ← Gate control (copy from HARNESS_SPEC.md)
├── TIMELINE.md                ← Event log (append-only)
│
├── 01_planning/
│   ├── spec.md                ← Scope, schedule, risks
│   └── review.md              ← Review findings
│
├── 02_architecture/
│   ├── spec.md                ← System design, data flow
│   └── review.md
│
├── 03_structure/
│   ├── spec.md                ← Files, classes, functions
│   └── review.md
│
├── 04_implementation/
│   ├── spec.md                ← Code plan
│   ├── review.md
│   └── result.md              ← What was built
│
└── evidence/
    ├── tests.md               ← Raw test output
    ├── changed_files.md       ← Files changed + why
    └── verification.md        ← Final verification
```

## Creating a Task

1. Create folder: `.cowork/tasks/NNN_short_name/`
2. Create `TASK.md` with the task definition
3. Create `STATE.yaml` from the template in `.cowork/HARNESS_SPEC.md`
4. Create `TIMELINE.md` with the first entry
5. Create stage folders: `01_planning/`, `02_architecture/`, `03_structure/`, `04_implementation/`
6. Create `evidence/` folder
7. Start working on `01_planning/spec.md`

## Closing a Task

1. Write `04_implementation/result.md`
2. Fill `evidence/tests.md`, `evidence/changed_files.md`, `evidence/verification.md`
3. Update `STATE.yaml`: `task_status: complete`
4. Human verifies → `task_status: verified`
5. Promote specs to `docs/specs/` if they add permanent knowledge
6. Human closes → `task_status: closed`
