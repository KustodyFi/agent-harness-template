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

See `.cowork/ONBOARD.md` → "Creating a New Task" for step-by-step instructions.
