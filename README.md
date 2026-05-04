# Agent Harness Template

> A reusable GitHub template for structured AI agent development.
> Clone this template to get a production-ready 3-layer agent harness in any KustodyFi repo.

[![Use this template](https://img.shields.io/badge/Use%20this%20template-green?style=for-the-badge)](https://github.com/KustodyFi/agent-harness-template/generate)

---

## What This Is

A standardized framework that governs how AI development agents operate in a repository.
See `AGENTS.md` for the full architecture and `agent.md` for operational rules.

---

## 3-Layer Architecture

See `AGENTS.md` → "Architecture" for the canonical 3-layer diagram and layer ownership.

---

## Quick Start

### Option A: Automated (recommended)

1. Click **"Use this template"** on GitHub (or use `gh`):

```bash
gh repo create YourOrg/your-project --template KustodyFi/agent-harness-template --public --clone
```

2. **Done.** A GitHub Action auto-bootstraps the harness on the first push:
   - Replaces `{{PLACEHOLDER}}` values using your repo name and description
   - Swaps `README.template.md` → `README.md`
   - Self-destructs after running once

3. Pull the bootstrapped repo and start working:

```bash
git pull  # get the auto-bootstrap commit
# Read AGENTS.md for the authoritative startup sequence
```

### Option B: Manual

```bash
git clone <your-repo>
cd <your-repo>
./setup.sh    # interactive — prompts for project name, tech stack, etc.
```

### After Setup

1. **`agent.project.md`** — Fill in your architectural invariants
2. **`docs/standards/coding-standards.md`** — Adjust coding rules for your tech stack
3. **Update tech stack** — If auto-bootstrapped, edit `AGENTS.md` to replace "TBD" with your actual stack

---

## What's Included

```
├── AGENTS.md                ← AI agent entry point (read first)
├── agent.md                 ← Org-wide agent policy (§1-§10)
├── agent.project.md         ← Project-specific invariants (you fill in)
├── setup.sh                 ← Manual bootstrap (fallback)
│
├── .github/workflows/
│   └── bootstrap.yml        ← Auto-bootstrap on first push (self-deletes)
│
├── docs/
│   ├── standards/           ← Coding standards (canonical)
│   ├── specs/               ← Verified project specs (anti-hallucination)
│   ├── adr/                 ← Architecture decision records
│   ├── plans/               ← Roadmap & backlog
│   └── guides/              ← How-to guides
│
├── .agent.default/          ← Default role definitions (tracked)
│   ├── orchestrator/        ← Orchestrator role files
│   ├── reviewer/            ← Reviewer role files
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

See `.cowork/HARNESS_SPEC.md` → "Task Stages" and "Gate Rules" for the canonical task flow.

### Team Roles

See `AGENTS.md` → "Team Roles" and `.cowork/harness/roles.yaml` for the canonical role definitions.

---

## Key Design Decisions

- **`AGENTS.md` owns the startup sequence** — all other files point there, never define their own
- **`agent.md` is org-portable** — references only `AGENTS.md` (exists in every repo), zero other paths
- **`.agent.default/` is tracked** (team baseline), **`.agent/` is gitignored** (personal copy)
- **One source of truth** — no duplicated rules, only pointers to canonical files
- **`roles.yaml` is the canonical vocabulary** — `permissions.yaml` uses the same action names

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
