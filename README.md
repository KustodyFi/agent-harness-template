# Agent Harness Template

> **A production-ready framework for structured AI agent development.**
> Every KustodyFi repository uses this template to enforce human-gated, multi-agent workflows.

[![Use this template](https://img.shields.io/badge/Use%20this%20template-green?style=for-the-badge)](https://github.com/KustodyFi/agent-harness-template/generate)

---

## Why This Exists

AI agents are powerful but need guardrails. Without structure, agents skip planning, hallucinate architecture, overwrite each other's work, and ship code without human review. This template solves that with a **3-layer harness** enforced by a state machine and Python validator.

---

## Architecture

See `AGENTS.md` → "Architecture" for the canonical 3-layer definitions (Policy, Roles, Harness).

## Team Roles

See `AGENTS.md` → "Team Roles" and `.cowork/harness/roles.yaml` for the canonical role definitions (Human, Orchestrator, Reviewer).

## Task Lifecycle

See `.cowork/HARNESS_SPEC.md` → "Task Stages" and "Gate Rules" for the canonical 4-stage process (planning → architecture → structure → implementation).

## State Machine

See `.cowork/harness/state_machine.yaml` → `validated_rules` for the full list of enforced invariants. The validator (`python3 .cowork/harness/validate_state.py`) checks all rules at runtime.

---

## How to Use This Template

### Prerequisites (one-time, org admin)

Enable this repo as a GitHub template:

```bash
gh repo edit KustodyFi/agent-harness-template --template
```

Or: GitHub UI → **Settings** → check **Template repository**.

### For Every New Project

**Step 1 — Create your repo from the template:**

Click the green **"Use this template"** button on this repo's GitHub page → **"Create a new repository"**.

Or via CLI:

```bash
gh repo create KustodyFi/your-project \
  --template KustodyFi/agent-harness-template \
  --public \
  --description "Your project description" \
  --clone
```

**Step 2 — Wait ~30 seconds for auto-bootstrap:**

A GitHub Action runs automatically on first push:
- Replaces all `{{PLACEHOLDER}}` values using your repo name and description
- Swaps `README.template.md` → `README.md` (your project README)
- Self-destructs (one-time use)

> **Branch protection?** Use Actions → "Run workflow" (manual dispatch) or fall back to `./setup.sh`.

**Step 3 — Clone and set up locally:**

```bash
git clone git@github.com:KustodyFi/your-project.git
cd your-project
git pull                        # get the bootstrap commit
cp -r .agent.default .agent     # create your local role copy (gitignored)
```

**Step 4 — Open in your IDE and start working:**

Open the project in Cursor, VS Code, or any AI-enabled IDE. Your AI agent automatically reads `AGENTS.md` from the repo root — this tells it:

1. The startup sequence (which files to read and in what order)
2. What it can and can't do (orchestrator vs reviewer roles)
3. Where the process rules live (`.cowork/HARNESS_SPEC.md`)
4. How to create and manage tasks (`.cowork/tasks/README.md`)

**The AI is fully onboarded. You're ready to work.**

### Manual Bootstrap (fallback)

If the GitHub Action didn't run:

```bash
./setup.sh    # interactive prompts for name, description, tech stack
git add -A && git commit -m "chore: bootstrap harness" && git push
```

---

## Post-Setup Configuration

After bootstrap (automated or manual), complete these steps:

### 1. Fill in project invariants

**File:** `agent.project.md` — Replace the `{{INVARIANT_*}}` placeholders with your project's non-negotiable rules.

### 2. Update tech stack

**File:** `AGENTS.md` (line 12) — If auto-bootstrapped, replace "TBD" with your actual stack.

### 3. Customize coding standards

**File:** `docs/standards/coding-standards.md` — Adjust for your language and framework.

### 4. Set up local agent roles

```bash
cp -r .agent.default .agent  # if not already done
```

### 5. Verify

```bash
grep -rn '{{PROJECT' . --include='*.md'  # should return nothing
ls .agent/orchestrator/ROLE.md           # should exist
```

---

## What's Included

```
your-project/
│
├── AGENTS.md                    ← 🚀 AI agent entry point (read first)
├── agent.md                     ← 📜 Org-wide policy (§1-§10)
├── agent.project.md             ← 🏗️ YOUR project invariants
├── setup.sh                     ← ⚙️ Manual bootstrap (fallback)
│
├── .github/workflows/
│   └── bootstrap.yml            ← 🤖 Auto-bootstrap (self-deletes)
│
├── docs/
│   ├── standards/               ← 📏 Coding rules
│   ├── specs/                   ← 📋 Verified specs
│   ├── adr/                     ← 📝 Architecture decisions
│   ├── plans/                   ← 🗺️ Roadmap & backlog
│   └── guides/                  ← 📖 Getting started guide
│
├── .agent.default/              ← 👤 Role defaults (tracked)
├── .agent/                      ← 👤 YOUR local roles (gitignored)
│
└── .cowork/                     ← ⚙️ Process harness (Layer 3)
    ├── HARNESS_SPEC.md          ← Task stages + gate rules
    ├── ONBOARD.md               ← Role interaction guide
    ├── STATUS.md                ← Project dashboard
    ├── harness/                 ← State machine, validator, schema
    ├── prompts/                 ← Agent prompt templates
    ├── tasks/                   ← Task structure guide
    └── reviews/                 ← Cross-cutting review logs
```

---

## Agent Startup Sequence

See `AGENTS.md` → "Startup Sequence" for the authoritative boot order.

---

## Validation

```bash
python3 .cowork/harness/validate_state.py .cowork/tasks/NNN_name/STATE.yaml
```

See `.cowork/harness/state_machine.yaml` → `validated_rules` for the full list.

---

## Detailed Guide

For step-by-step instructions, FAQ, and first-task walkthrough:

**[`docs/guides/getting-started.md`](docs/guides/getting-started.md)**

---

## License

MIT
