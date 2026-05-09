# Structure Spec — Hooks Layer

## File Layout

```
.hooks/
├── hooks.yaml                  ← Hook definitions (what, when, how)
├── install.sh                  ← Installs git hooks adapter
│
├── scripts/                    ← Hook implementation scripts
│   ├── session_start.sh        ← Load context, verify task exists
│   ├── check_coding_allowed.sh ← Block writes when coding_allowed=false
│   ├── validate_and_log.sh     ← Pre-commit: validate STATE.yaml + check review.md
│   └── log_review.sh           ← Append review findings with attribution
│
└── adapters/
    └── git/
        ├── pre-commit           ← Git hook → validate_and_log.sh
        └── README.md            ← How git hooks adapter works
```

## Hook Definitions (hooks.yaml)

```yaml
hooks:
  session_start:
    trigger: "Agent session begins"
    script: scripts/session_start.sh
    enforces: "AGENTS.md startup sequence loaded, active task identified"
    blocking: false

  pre_write:
    trigger: "Before writing code files (non-.md)"
    script: scripts/check_coding_allowed.sh
    enforces: "coding_allowed must be true in active task STATE.yaml"
    blocking: true

  pre_commit:
    trigger: "Before git commit"
    script: scripts/validate_and_log.sh
    enforces: "STATE.yaml valid, review.md has entries for current stage"
    blocking: true

  post_review:
    trigger: "After receiving review findings"
    script: scripts/log_review.sh
    enforces: "Findings logged to review.md with attribution format"
    blocking: false
```

## Script Contracts

### session_start.sh
- **Input:** none
- **Output:** stdout — active task summary, current stage, what to do next
- **Exit:** always 0 (informational)
- **Logic:**
  1. Find active task (grep `task_status: active` in `.cowork/tasks/*/STATE.yaml`)
  2. Print current_stage, current_stage_status, coding_allowed
  3. Print reminder: "Log all review findings to {stage}/review.md"

### check_coding_allowed.sh
- **Input:** file path being written (optional)
- **Output:** stderr if blocked
- **Exit:** 0 = allowed, 1 = blocked
- **Logic:**
  1. Find active task STATE.yaml
  2. If `coding_allowed: false`, exit 1 with message
  3. If `coding_allowed: true`, exit 0

### validate_and_log.sh
- **Input:** none (runs in repo root)
- **Output:** stderr if blocked
- **Exit:** 0 = commit allowed, 1 = blocked
- **Logic:**
  1. Find all modified STATE.yaml files in staging
  2. For each: run `python3 .cowork/harness/validate_state.py` if available
  3. For active task: check current stage has review.md with content
  4. Pass = exit 0, fail = exit 1 with errors

### log_review.sh
- **Input:** agent name, round number, findings file (stdin or arg)
- **Output:** appends to active task's current stage review.md
- **Exit:** always 0
- **Logic:**
  1. Find active task and current stage
  2. Append attribution header (from ONBOARD.md format)
  3. Append findings content

## Git Hooks Adapter

### install.sh
```bash
#!/bin/bash
# Installs git hooks from .hooks/adapters/git/ into .git/hooks/
# Symlinks to keep them in sync with the repo

for hook in .hooks/adapters/git/*; do
  name=$(basename "$hook")
  if [ "$name" != "README.md" ]; then
    ln -sf "../../.hooks/adapters/git/$name" ".git/hooks/$name"
  fi
done
```

### pre-commit hook
Calls `.hooks/scripts/validate_and_log.sh` — blocks commit on failure.

## Changes to Existing Files

### AGENTS.md
- Update architecture diagram from 3-layer to 5-layer
- Add `.hooks/` to folder map
- Update startup sequence to mention hooks

### README.md
- Add hooks layer to architecture section
- Add `install.sh` to Quick Start

### setup.sh
- Add `bash .hooks/install.sh` step after bootstrap
