# {{PROJECT_NAME}} — AI Agent Development

> How AI development agents operate in this repository.
> Read this file first. It governs all AI agent behavior.

---

## Project

{{PROJECT_NAME}} — {{PROJECT_DESCRIPTION}}

**Tech stack:** {{TECH_STACK}}

**Current phase:** {{CURRENT_PHASE}}

---

## Architecture (3-Layer Agent Engineering)

```
┌──────────────────────────────────────────────────────┐
│  LAYER 3: HARNESS                     .cowork/       │
│  Multi-agent collaboration: process, state machine,  │
│  review logs, task tracking, approval gates,          │
│  process permissions (who can do what per stage)      │
├──────────────────────────────────────────────────────┤
│  LAYER 2: ROLES                       .agent/        │
│  Per-role identity: who you are, your skills,         │
│  your limits, your workflows (gitignored, per-user)   │
├──────────────────────────────────────────────────────┤
│  LAYER 1: POLICY                      agent.md       │
│  Org-wide rules: coding standards, logging, secrets, │
│  human-gated workflow, evaluation loop               │
└──────────────────────────────────────────────────────┘
```

> **This file (`AGENTS.md`) is the entry point.** It is not a layer —
> it is the overview that tells agents where to find each layer.
>
> **Layer ownership:**
> - Layer 2 (`.agent/`) owns role **identity** — who you are, your skills, your limits
> - Layer 3 (`.cowork/`) owns **process permissions** — what each role can do per stage
> - Layer 3 also provides process guides (ONBOARD.md) for how roles interact with the harness

---

## Startup Sequence (Authoritative)

```
1. Read AGENTS.md                           ← This file (overview)
2. Read agent.md                            ← Org policy (rules §1-§10)
3. Read agent.project.md                    ← Project invariants
4. Read docs/standards/coding-standards.md  ← Coding rules
5. Read docs/specs/ (if populated)          ← Ground truth
6. Read .cowork/STATUS.md                   ← Where are we?
7. If .agent/{your-role}/ROLE.md exists, read it  ← Optional, local
8. Ready to work.
```

> Step 7 is optional. `.agent/` is gitignored and per-user.
> If absent, use the role descriptions in `.cowork/ONBOARD.md`.

> All other files that reference a startup sequence MUST point here.

---

## Team Roles

| Role | Agent | Can Do | Cannot Do |
|------|-------|--------|-----------|
| **Human (HIL)** | You | Approve, reject, close, set direction | — |
| **Orchestrator** | Primary IDE AI | Write specs, code, tests, commit | Approve stages, skip stages |
| **Reviewer** | Secondary AI(s) | Review specs/code, verify claims | Write code, approve, commit |

### Coordination Protocol

```
     HUMAN
       │ chat
       ▼
  ORCHESTRATOR ──── review.md ────► REVIEWER
  (writes specs)                    (appends findings)
  (writes code)                     (read-only commands)
  (commits)                         (never commits)
```

- Orchestrator prepares reviewer prompts → human delivers to reviewer agent
- `review.md` is the shared communication channel (files = how agents talk)

---

## Commands

| Command | Description |
|---------|-------------|
| `/commit` | Stage all changes and commit with conventional message |
| `/push` | Push current branch to origin |
| `/build` | Build the project |
| `/run` | Build and run locally |
| `/status` | Show project status and recent activity |
| `/log` | Append a new round to the change log |
| `/harness` | Load harness rules before starting any task |
| `/review` | Run self-review against docs contracts |
| `/coding-standards` | Show coding standards |

---

## Folder Map

| Path | What | Layer |
|------|------|-------|
| `AGENTS.md` | This file — agent entry point | — |
| `agent.md` | Org-wide operational rules | 1 |
| `agent.project.md` | Project-specific invariants | 1 |
| `docs/standards/` | Coding standards (canonical, tracked) | 1 |
| `docs/specs/` | Verified project specs (ground truth) | 1 |
| `docs/adr/` | Architecture decision records | 1 |
| `docs/plans/` | Roadmap, backlog, schedule | 1 |
| `docs/guides/` | How-to guides (demo, run, deploy) | 1 |
| `.agent.default/` | Default role definitions (tracked baseline) | 2 |
| `.agent/` | Active role copy (gitignored, per-user) | 2 |
| `.cowork/STATUS.md` | Live project dashboard | 3 |
| `.cowork/README.md` | Harness overview (Layer 3 entry point) | 3 |
| `.cowork/HARNESS_SPEC.md` | Task-stage process rules | 3 |
| `.cowork/ONBOARD.md` | Process guide for all roles | 3 |
| `.cowork/harness/` | State machine, validator, permissions | 3 |
| `.cowork/prompts/` | Prompt templates for review/approve | 3 |
| `.cowork/tasks/` | All task work (stages, specs, reviews) | 3 |
| `.cowork/reviews/` | Shared review logs | 3 |
| `README.md` | Template overview (before setup) / Project README (after setup) | — |
| `README.template.md` | Project README with placeholders (consumed by `setup.sh`) | — |
| `setup.sh` | First-run bootstrap script (manual fallback) | — |
| `.github/workflows/bootstrap.yml` | Auto-bootstrap on first push (self-deletes) | — |
| `.gitignore` | Git ignore rules (`.agent/`, secrets, build artifacts) | — |

---

## Expectations

1. **Read before writing.** Always read the startup sequence files before any work.
2. **No code before approval.** Coding starts only after harness approval.
3. **One source of truth.** Never duplicate content. One canonical file + pointers.
4. **Commit after each unit.** Push is human's responsibility.
5. **Follow agent.md.** All operational rules (stop-when-blocked, scope discipline, etc.) are in `agent.md`.
