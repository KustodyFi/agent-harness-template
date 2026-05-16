# Agent Harness Template

> **A structured framework for AI agent development with human-gated workflows.**
> Guides multi-agent collaboration through defined stages with a state machine and Python validator.

[![Use this template](https://img.shields.io/badge/Use%20this%20template-green?style=for-the-badge)](https://github.com/KustodyFi/agent-harness-template/generate)

---

## Why This Exists

AI agents are powerful but need guardrails. Without structure, agents skip planning, hallucinate architecture, overwrite each other's work, and ship code without human review. This template solves that with a **3-layer harness** — a state machine, Python validator, and process rules that guide agent behavior. Deterministic enforcement via hooks is [planned](docs/plans/hooks-layer.md).

---

## Quick Start

### Step 1 — Create your repo

**Option A: GitHub UI**

Click the green **"Use this template"** button at the top of this page → **"Create a new repository"**.

**Option B: CLI**

```bash
gh repo create KustodyFi/your-project \
  --template KustodyFi/agent-harness-template \
  --public \
  --description "Your project description" \
  --clone
```

### Step 2 — Auto-bootstrap

A GitHub Action runs automatically within ~30 seconds:
- Replaces all `{{PLACEHOLDER}}` values using your repo name and description
- Swaps `README.template.md` → `README.md` (your project README)
- Self-destructs after running (one-time use)

> **Branch protection?** Auto-bootstrap cannot push to protected branches. Use `./setup.sh` (manual) instead, or temporarily disable protection for the initial bootstrap.

### Step 3 — Set up your local environment

```bash
# Clone and pull the bootstrap commit
git clone git@github.com:KustodyFi/your-project.git
cd your-project
git pull

# Install harness dependencies
pip install -r requirements.txt

# Create your local agent role copy (gitignored, per-user)
cp -r .agent.default .agent
```

### Step 4 — Configure your project

```bash
# 1. Fill in your project's non-negotiable rules
#    Edit: agent.project.md → replace {{INVARIANT_*}} placeholders

# 2. Set your tech stack
#    Edit: AGENTS.md line 12 → replace "TBD" with your actual stack

# 3. Customize coding standards for your language/framework
#    Edit: docs/standards/coding-standards.md

# 4. Verify — no remaining placeholders
grep -rn '{{PROJECT' . --include='*.md'    # should return nothing
ls .agent/orchestrator/ROLE.md             # should exist
```

### Step 5 — Open in your IDE

Open the project in **Cursor**, **VS Code**, or any AI-enabled IDE. Your AI agent automatically reads `AGENTS.md` from the repo root, which tells it:

1. **Startup sequence** — which files to read and in what order
2. **Role boundaries** — what it can and can't do (orchestrator vs reviewer)
3. **Process rules** — how tasks flow through stages (`.cowork/HARNESS_SPEC.md`)
4. **Task management** — how to create and track tasks (`.cowork/tasks/README.md`)

**The AI is fully onboarded. You're ready to work.**

### Step 6 — Start your first task

Ask your AI agent to create a task:

```
Create a task called "001_my_feature" following .cowork/tasks/README.md
```

The agent will create:
- `.cowork/tasks/001_my_feature/TASK.md` — what you're building
- `.cowork/tasks/001_my_feature/STATE.yaml` — progress tracker (state machine)
- Stage folders for planning → architecture → structure → implementation

> **Note:** All task folders, review logs, and work logs are **local only** (gitignored). They are your development workspace, not project deliverables.

### Manual Bootstrap (fallback)

If the GitHub Action didn't run:

```bash
./setup.sh    # interactive prompts for name, description, tech stack
git add -A && git commit -m "chore: bootstrap harness" && git push
```

---

## Working with Multiple Agents

The harness supports multi-agent review workflows:

| Agent | Role | What it does |
|-------|------|-------------|
| **IDE AI** (Cursor/Copilot) | Orchestrator | Writes specs, code, tests. Drives task stages. |
| **Codex** (CLI) | Reviewer | Reviews specs/code via terminal. Read-only. |
| **GPT / Gemini** (chat) | Reviewer | Reviews via repomix snapshot. Findings pasted back. |

### Coordination flow

1. **Orchestrator** writes spec → logs progress in `.cowork/WORKLOG.md`
2. **Human** sends review prompt to reviewer agent (from `.cowork/prompts/`)
3. **Reviewer** reads files, appends findings to work log
4. **Orchestrator** triages findings: ACCEPTED / REJECTED / DEFERRED
5. **Human** approves triage, orchestrator applies fixes

All coordination happens through local files — no external tools needed.

---

## Architecture

See `AGENTS.md` → "Architecture" for the canonical 3-layer definitions:

| Layer | What | Where |
|-------|------|-------|
| **Policy** | Org-wide rules, project invariants, coding standards | `agent.md`, `agent.project.md`, `docs/` |
| **Roles** | Agent identity, skills, workflows | `.agent.default/`, `.agent/` |
| **Harness** | Process engine, state machine, permissions | `.cowork/` |

## What's Included

```
your-project/
│
├── AGENTS.md                    ← 🚀 AI agent entry point (read first)
├── agent.md                     ← 📜 Org-wide policy (§1-§10)
├── agent.project.md             ← 🏗️ YOUR project invariants
├── requirements.txt             ← 📦 Harness dependencies (PyYAML)
├── setup.sh                     ← ⚙️ Manual bootstrap (fallback)
│
├── .github/workflows/
│   └── bootstrap.yml            ← 🤖 Auto-bootstrap (self-deletes)
│
├── docs/
│   ├── standards/               ← 📏 Coding rules (customize this)
│   ├── specs/                   ← 📋 Verified specs
│   ├── adr/                     ← 📝 Architecture decisions
│   ├── plans/                   ← 🗺️ Roadmap & backlog
│   └── guides/                  ← 📖 Getting started guide
│
├── .agent.default/              ← 👤 Role defaults (tracked)
├── .agent/                      ← 👤 YOUR local roles (gitignored)
│
└── .cowork/                     ← ⚙️ Process harness
    ├── HARNESS_SPEC.md          ← Task stages + gate rules
    ├── ONBOARD.md               ← Role interaction guide
    ├── STATUS.md                ← Project dashboard
    ├── WORKLOG.md               ← Shared agent work log (local)
    ├── harness/                 ← State machine, validator, schema
    ├── prompts/                 ← Agent prompt templates
    ├── tasks/                   ← Task work (local, gitignored)
    └── reviews/                 ← Review logs (local, gitignored)
```

---

## Validation

```bash
# Install dependency (if not already done)
pip install -r requirements.txt

# Validate a task's STATE.yaml
python3 .cowork/harness/validate_state.py .cowork/tasks/NNN_name/STATE.yaml
```

See `.cowork/harness/state_machine.yaml` → `validated_rules` for the full list.

---

## Detailed Guide

**[`docs/guides/getting-started.md`](docs/guides/getting-started.md)** — step-by-step instructions, FAQ, and first-task walkthrough.

---

## License

MIT
