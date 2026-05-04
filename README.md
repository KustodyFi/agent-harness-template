# Agent Harness Template

> **A production-ready framework for structured AI agent development.**
> Every KustodyFi repository uses this template to enforce human-gated, multi-agent workflows.

[![Use this template](https://img.shields.io/badge/Use%20this%20template-green?style=for-the-badge)](https://github.com/KustodyFi/agent-harness-template/generate)

---

## Why This Exists

AI agents are powerful but need guardrails. Without structure, agents:
- Skip planning and jump straight to code
- Hallucinate architecture decisions
- Overwrite each other's work
- Ship code without human review

This template solves that by enforcing a **3-layer harness** that every agent must follow.

---

## 3-Layer Architecture

See `AGENTS.md` → "Architecture" for the canonical layer definitions.

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   LAYER 3: HARNESS                              .cowork/         │
│                                                                  │
│   The process engine. Controls WHAT each role can do             │
│   at each stage. State machine, approval gates, task             │
│   stages, review logs, prompt templates.                         │
│                                                                  │
│   Think: "the rules of the game"                                 │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   LAYER 2: ROLES                                .agent/          │
│                                                                  │
│   Per-role identity. Defines WHO each agent is —                 │
│   their skills, workflows, and limits.                           │
│   Tracked defaults in .agent.default/, personal                  │
│   copy in .agent/ (gitignored).                                  │
│                                                                  │
│   Think: "the players and their abilities"                       │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   LAYER 1: POLICY                               agent.md         │
│                                                                  │
│   Organization-wide rules. Same in every repo.                   │
│   Coding standards, secrets policy, human-gated                  │
│   workflow, evaluation loop.                                     │
│                                                                  │
│   Think: "the law of the land"                                   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**Layer separation is strict:**
- Layer 1 never changes per-project (org-portable)
- Layer 2 defines identity (tracked defaults + personal overrides)
- Layer 3 defines process (what you can do, when you can do it)

---

## How It Works

### Team Roles

See `AGENTS.md` → "Team Roles" and `.cowork/harness/roles.yaml` for the canonical role definitions.

```
     HUMAN (you)
       │
       │  defines tasks, approves stages, closes tasks
       │
       ▼
  ┌─────────────┐         review.md          ┌─────────────┐
  │ ORCHESTRATOR │ ─────────────────────────► │  REVIEWER    │
  │  (IDE AI)    │                            │ (External AI)│
  │              │ ◄───────────────────────── │              │
  │ writes specs │     findings + verdict     │ verifies     │
  │ writes code  │                            │ read-only    │
  │ runs tests   │                            │ never writes │
  └─────────────┘                            └─────────────┘
        │                                          │
        │         human approves/rejects           │
        └──────────────── ▲ ───────────────────────┘
                          │
                       HUMAN
```

See `AGENTS.md` → "Team Roles" and `.cowork/harness/roles.yaml` for the canonical role rules.

### Task Lifecycle

See `.cowork/HARNESS_SPEC.md` → "Task Stages" and "Gate Rules" for the canonical process rules.

```
                        TASK LIFECYCLE
    ┌───────────────────────────────────────────────┐
    │                                               │
    │   01_PLANNING ──► 02_ARCHITECTURE ──►         │
    │                                               │
    │   03_STRUCTURE ──► 04_IMPLEMENTATION           │
    │                                               │
    └───────────────────────────────────────────────┘

    Each stage follows the same cycle:

    ┌──────────┐     ┌──────────┐     ┌──────────┐
    │          │     │          │     │          │
    │  WRITE   │────►│  REVIEW  │────►│ APPROVE  │
    │  spec.md │     │ review.md│     │ (human)  │
    │          │     │          │     │          │
    └──────────┘     └──────────┘     └──────────┘
    orchestrator      reviewer          human
                                          │
                                          ▼
                                    Next stage
                                    (or coding
                                     at stage 04)
```

See `.cowork/HARNESS_SPEC.md` → "Gate Rules" for the canonical stage transition rules.

### State Machine

Each task has a `STATE.yaml` that tracks progress:

```yaml
task: "001_auth_service"
task_status: active
current_stage: planning
current_stage_status: pending
coding_allowed: false        # ← becomes true ONLY at stage 04 coding

stages:
  planning:
    status: pending          # pending → in_review → approved
    review_rounds: 0
  architecture:
    status: pending
    review_rounds: 0
  structure:
    status: pending
    review_rounds: 0
  implementation:
    status: pending          # also supports: coding, complete
    review_rounds: 0
```

The validator (`python3 .cowork/harness/validate_state.py`) enforces all invariants.
See `.cowork/harness/state_machine.yaml` → `validated_rules` for the full list.

---

## Installation

### Flow Diagram

```
    ┌─────────────────────────────────────────────────────────────┐
    │                    OPTION A: AUTOMATED                      │
    │                                                             │
    │  1. "Use this template"     2. GitHub Action runs           │
    │     on GitHub                  automatically                │
    │                                                             │
    │  ┌─────────────┐           ┌──────────────────────┐        │
    │  │  Click      │           │  bootstrap.yml:       │        │
    │  │  "Use this  │──push──►  │  • repo name → vars   │        │
    │  │  template"  │           │  • sed replacements    │        │
    │  │             │           │  • README swap         │        │
    │  │  Fill in:   │           │  • commit              │        │
    │  │  • name     │           │  • self-delete ✂️      │        │
    │  │  • desc     │           └──────────────────────┘        │
    │  └─────────────┘                     │                     │
    │                                      ▼                     │
    │                          3. Clone ready-to-go repo          │
    │                             git clone + git pull            │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────┐
    │                    OPTION B: MANUAL                          │
    │                                                             │
    │  1. Clone          2. Run setup.sh       3. Push            │
    │                                                             │
    │  git clone ──► ./setup.sh ──► git push                     │
    │                 (interactive)                                │
    │                 • project name                               │
    │                 • description                                │
    │                 • tech stack                                  │
    │                 • current phase                               │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

### Option A: Automated (recommended)

1. Click **"Use this template"** on GitHub, or:

```bash
gh repo create KustodyFi/your-project \
  --template KustodyFi/agent-harness-template \
  --public \
  --description "Your project description" \
  --clone
```

2. **Wait ~30 seconds.** A GitHub Action auto-bootstraps:
   - Uses your **repo name** as project name
   - Uses your **repo description** as project description
   - Sets tech stack to "TBD" (you update later)
   - Sets phase to "Phase 1 — Foundation"
   - Swaps `README.template.md` → `README.md`
   - **Self-destructs** after running (one-time use)

3. Pull the bootstrapped repo:

```bash
cd your-project
git pull  # get the auto-bootstrap commit
```

### Option B: Manual

```bash
git clone git@github.com:KustodyFi/your-project.git
cd your-project
./setup.sh    # interactive prompts
git add -A && git commit -m "chore: bootstrap harness" && git push
```

---

## Post-Setup Configuration

After bootstrap (automated or manual), complete these steps:

### 1. Fill in project invariants

**File:** `agent.project.md`

Replace the `{{INVARIANT_*}}` placeholders with your project's non-negotiable rules:

```markdown
* **All API responses use JSON with camelCase keys**
* **PostgreSQL is the only persistence layer**
* **Every service must have health check endpoints**
* **No direct database access from handlers — use repository pattern**
* **All secrets from environment variables, never hardcoded**
```

### 2. Update tech stack

**File:** `AGENTS.md` (line 12)

If auto-bootstrapped, replace "TBD":

```markdown
**Tech stack:** Python 3.11 · FastAPI · PostgreSQL · Redis · Docker
```

### 3. Customize coding standards

**File:** `docs/standards/coding-standards.md`

Adjust for your language, framework, and conventions.

### 4. Set up local agent roles

```bash
# If not already done by setup.sh:
cp -r .agent.default .agent
```

This creates your personal (gitignored) copy of the role definitions.

### 5. Verify

```bash
# No remaining placeholders (INVARIANT_* is OK)
grep -rn '{{PROJECT' . --include='*.md'
# Should return: no results

# .agent/ exists
ls .agent/orchestrator/ROLE.md
# Should exist

# .agent/ is gitignored
git status
# .agent/ should NOT appear
```

---

## What's Included

```
your-project/
│
├── AGENTS.md                    ← 🚀 AI agent entry point (read first)
│                                   Startup sequence, architecture,
│                                   team roles, folder map
│
├── agent.md                     ← 📜 Org-wide policy (§1-§10)
│                                   Same across all KustodyFi repos
│
├── agent.project.md             ← 🏗️ YOUR project invariants
│                                   Non-negotiable architectural rules
│
├── setup.sh                     ← ⚙️ Manual bootstrap (fallback)
│
├── .github/workflows/
│   └── bootstrap.yml            ← 🤖 Auto-bootstrap (self-deletes)
│
├── docs/
│   ├── standards/
│   │   └── coding-standards.md  ← 📏 Coding rules (customize this)
│   ├── specs/                   ← 📋 Verified specs (anti-hallucination)
│   ├── adr/                     ← 📝 Architecture decision records
│   ├── plans/                   ← 🗺️ Roadmap & backlog
│   └── guides/
│       └── getting-started.md   ← 📖 This guide, in detail
│
├── .agent.default/              ← 👤 Role defaults (tracked, shared)
│   ├── orchestrator/
│   │   ├── ROLE.md              ← Orchestrator identity + limits
│   │   ├── skills/              ← Harness skill definitions
│   │   └── workflows/           ← /commit, /build, /run, etc.
│   ├── reviewer/
│   │   ├── ROLE.md              ← Reviewer identity + limits
│   │   └── skills/              ← Code review skill
│   └── shared/
│       └── log.md               ← Change log (append-only)
│
├── .agent/                      ← 👤 YOUR local roles (gitignored)
│                                   Created by setup.sh or manually
│
└── .cowork/                     ← ⚙️ Process harness (Layer 3)
    ├── README.md                ← Harness overview
    ├── HARNESS_SPEC.md          ← Task stages + gate rules
    ├── ONBOARD.md               ← Role interaction guide + attribution
    ├── STATUS.md                ← Project dashboard
    │
    ├── harness/
    │   ├── state_machine.yaml   ← Stage transitions + validated rules
    │   ├── validate_state.py    ← STATE.yaml validator
    │   ├── state.schema.json    ← STATE.yaml JSON schema
    │   ├── roles.yaml           ← Canonical role capabilities
    │   └── permissions.yaml     ← Stage-level permissions
    │
    ├── prompts/
    │   ├── review_stage.md      ← Template: request a review
    │   ├── approve_stage.md     ← Template: approve a stage
    │   └── onboard_agent.md     ← Template: onboard a reviewer
    │
    ├── tasks/
    │   └── README.md            ← Task structure + create/close guide
    │
    └── reviews/
        └── README.md            ← Cross-cutting review logs
```

---

## Agent Startup Sequence

See `AGENTS.md` → "Startup Sequence" for the authoritative boot order.

```
┌─────────────────────────────────────────────────────────────┐
│                    AGENT BOOT SEQUENCE                       │
│                                                             │
│  1. AGENTS.md          ← Entry point, architecture          │
│       │                                                     │
│  2. agent.md           ← Org-wide rules (§1-§10)           │
│       │                                                     │
│  3. agent.project.md   ← Project invariants                 │
│       │                                                     │
│  4. docs/standards/    ← Coding rules                       │
│       │                                                     │
│  5. docs/specs/        ← Ground truth (if populated)        │
│       │                                                     │
│  6. .cowork/STATUS.md  ← Where are we?                     │
│       │                                                     │
│  7. .agent/ROLE.md     ← Who am I? (optional, per-role)     │
│       │                                                     │
│  8. Ready to work      ← Agent is fully onboarded           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| `AGENTS.md` owns the startup sequence | All other files point there — never define their own |
| `agent.md` is org-portable | References only `AGENTS.md` (exists in every repo), zero other paths |
| `.agent.default/` is tracked, `.agent/` is gitignored | Team baseline + personal overrides |
| One source of truth | No duplicated rules — only pointers to canonical files |
| `roles.yaml` is the canonical vocabulary | `permissions.yaml` uses the same action names |
| Validator enforces invariants | `validate_state.py` catches violations before they reach code |
| Bootstrap self-destructs | `bootstrap.yml` deletes itself after first run — clean repo |

---

## Validation

```bash
# Validate a task's STATE.yaml against all harness invariants
# Requires: pip install pyyaml
python3 .cowork/harness/validate_state.py .cowork/tasks/NNN_name/STATE.yaml
```

See `.cowork/harness/state_machine.yaml` → `validated_rules` for the full list of enforced invariants.

---

## Detailed Guide

For step-by-step instructions with verification checklists, FAQ, and first-task walkthrough, see:

**[`docs/guides/getting-started.md`](docs/guides/getting-started.md)**

---

## License

MIT
