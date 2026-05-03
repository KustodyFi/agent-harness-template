# Agent Harness Template

> A reusable GitHub template for structured AI agent development.
> Clone this template to get a production-ready 3-layer agent harness in any KustodyFi repo.

[![Use this template](https://img.shields.io/badge/Use%20this%20template-green?style=for-the-badge)](https://github.com/KustodyFi/agent-harness-template/generate)

---

## What This Is

A standardized framework that governs how AI development agents operate in a repository. It enforces:

- **Human-gated workflow** — no code ships without human approval at every stage
- **Multi-agent collaboration** — orchestrator writes, reviewer verifies, human approves
- **Structured task execution** — every task follows 4 stages: planning → architecture → structure → implementation
- **One source of truth** — no duplicated rules, every file has a single canonical home

---

## 3-Layer Architecture

```
┌──────────────────────────────────────────────────────┐
│  LAYER 3: HARNESS                     .cowork/       │
│  Process engine: state machine, task stages,          │
│  review logs, approval gates, prompt templates        │
├──────────────────────────────────────────────────────┤
│  LAYER 2: ROLES                       .agent/        │
│  Per-role identity: orchestrator, reviewer            │
│  Skills, workflows, limits (gitignored, per-user)     │
├──────────────────────────────────────────────────────┤
│  LAYER 1: POLICY                      agent.md       │
│  Org-wide rules: coding standards, secrets,           │
│  human-gated workflow, evaluation loop               │
└──────────────────────────────────────────────────────┘
```

| Layer | What | Where |
|-------|------|-------|
| **1 — Policy** | Org-wide rules (same everywhere) | `agent.md`, `docs/standards/` |
| **2 — Roles** | Agent identity, skills, workflows | `.agent.default/` → `.agent/` |
| **3 — Harness** | Process engine, state machine, tasks | `.cowork/` |

---

## Quick Start

### 1. Create from template

Click **"Use this template"** on GitHub, or:

```bash
gh repo create YourOrg/your-project --template KustodyFi/agent-harness-template --public --clone
cd your-project
```

### 2. Run setup

```bash
./setup.sh
```

This will:
- Replace `{{PLACEHOLDER}}` values with your project info
- Copy `.agent.default/` → `.agent/` (your local, gitignored working copy)
- Set the initial project date

### 3. Start development

```bash
# Read AGENTS.md for the authoritative startup sequence
```

---

## What's Included

```
├── AGENTS.md                ← AI agent entry point (read first)
├── agent.md                 ← Org-wide agent policy (§1-§10)
├── agent.project.md         ← Project-specific invariants (you fill in)
├── setup.sh                 ← First-run bootstrap script
│
├── docs/
│   ├── standards/           ← Coding standards (canonical)
│   ├── specs/               ← Verified project specs (anti-hallucination)
│   ├── adr/                 ← Architecture decision records
│   ├── plans/               ← Roadmap & backlog
│   └── guides/              ← How-to guides
│
├── .agent.default/          ← Default role definitions (tracked)
│   ├── orchestrator/        ← Primary AI: writes specs, code, tests
│   ├── reviewer/            ← Secondary AI: reviews, verifies claims
│   └── shared/              ← Shared resources (change log)
│
└── .cowork/                 ← Process harness (Layer 3)
    ├── HARNESS_SPEC.md      ← Task-stage process rules
    ├── ONBOARD.md           ← Role interaction guide
    ├── STATUS.md            ← Project dashboard
    ├── harness/             ← State machine, validator, schemas
    ├── prompts/             ← Templates for review/approve/onboard
    ├── tasks/               ← All task work (staged deliverables)
    └── reviews/             ← Cross-cutting review logs
```

---

## How It Works

### Task Flow

Every task follows 4 stages. No stage may be skipped.

```
01_planning → 02_architecture → 03_structure → 04_implementation
```

At each stage:
1. **Orchestrator** writes `spec.md`
2. **Reviewer** verifies and appends to `review.md`
3. **Human** approves or requests changes
4. Advance to next stage

Coding only begins at Stage 04 after human approval.

### Team Roles

| Role | Agent | Can Do | Cannot Do |
|------|-------|--------|-----------|
| **Human** | You | Approve, reject, close | — |
| **Orchestrator** | IDE AI | Write specs, code, tests | Approve, skip stages |
| **Reviewer** | External AI | Review, verify claims | Write code, approve |

---

## Key Design Decisions

- **`AGENTS.md` owns the startup sequence** — all other files point there, never define their own
- **`agent.md` is org-portable** — references only `AGENTS.md` (exists in every repo), zero other paths
- **`.agent.default/` is tracked** (team baseline), **`.agent/` is gitignored** (personal copy)
- **One source of truth** — no duplicated rules, only pointers to canonical files
- **`roles.yaml` is the canonical vocabulary** — `permissions.yaml` uses the same action names

---

## Customization

After running `setup.sh`:

1. **`agent.project.md`** — Fill in your architectural invariants
2. **`docs/standards/coding-standards.md`** — Adjust coding rules for your tech stack
3. **`.agent.default/orchestrator/workflows/`** — Customize `/build`, `/run` for your project
4. **`.cowork/STATUS.md`** — Update as your project progresses

---

## Validation

```bash
# Validate a task's state against harness invariants
# Requires: pip install pyyaml
python3 .cowork/harness/validate_state.py .cowork/tasks/NNN_name/STATE.yaml
```

---

## License

MIT

