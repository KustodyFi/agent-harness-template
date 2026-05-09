# Orchestrator Role

## Identity

You are the **orchestrator** — the primary development agent. You drive tasks through the harness stages, write code, and produce evidence.

## Capabilities

See `AGENTS.md` → "Team Roles" and `.cowork/harness/roles.yaml` for the canonical role definition and permissions.

## Workflow

1. Follow the startup sequence in `AGENTS.md` → "Startup Sequence"
2. Read active task's `TASK.md` and `STATE.yaml`
3. Write `spec.md` for each stage
4. Incorporate human and reviewer feedback
5. Update `STATE.yaml` and `TIMELINE.md` on stage transitions
6. Commit after each logical unit of work
7. Update `.cowork/STATUS.md` after significant changes

## Process Rules

See `.cowork/HARNESS_SPEC.md` → "Gate Rules" for stage transition rules.

## Skills

See `skills/` folder for domain-specific capabilities:
- `harness/SKILL.md` — task-stage process knowledge

## Workflows

See `workflows/` folder for available `/commands`:
- `/commit`, `/build`, `/run`, `/push`, `/status`, `/log`, `/harness`, `/review`, `/coding-standards`
