# Getting Started — New Repository Setup

> **Audience:** Any developer creating a new KustodyFi repository.
> This guide walks you through creating a repo with the agent harness from scratch.

---

## Prerequisites

- GitHub account with access to the [KustodyFi](https://github.com/KustodyFi) organization
- Git installed locally
- (Optional) [GitHub CLI](https://cli.github.com/) installed for command-line setup

---

## Step 1: Create Your Repository

### Via GitHub UI (recommended)

1. Go to **[agent-harness-template](https://github.com/KustodyFi/agent-harness-template)**
2. Click the green **"Use this template"** → **"Create a new repository"**
3. Fill in:
   - **Owner:** `KustodyFi`
   - **Repository name:** your project name (e.g., `fx-town`, `invoice-engine`)
   - **Description:** one-line project description
   - **Visibility:** Public or Private
4. Click **"Create repository"**

### Via GitHub CLI

```bash
gh repo create KustodyFi/your-project-name \
  --template KustodyFi/agent-harness-template \
  --public \
  --description "Your project description" \
  --clone
cd your-project-name
```

---

## Step 2: Wait for Auto-Bootstrap (≈30 seconds)

A GitHub Action automatically runs on the first push and:

- ✅ Replaces all `{{PLACEHOLDER}}` values using your repo name and description
- ✅ Swaps `README.template.md` → `README.md` (your project README)
- ✅ Commits the changes
- ✅ Deletes itself (one-time use)

**How to verify it ran:**

1. Go to your repo on GitHub → **Actions** tab
2. You should see a completed **"Bootstrap Harness"** workflow run
3. Check the commit history — you should see a commit from `github-actions[bot]`

> **⚠️ If the Action didn't run:** You can bootstrap manually instead (see Step 2b below).

---

## Step 2b: Manual Bootstrap (fallback)

Only use this if the GitHub Action did not run:

```bash
git clone git@github.com:KustodyFi/your-project-name.git
cd your-project-name
./setup.sh
```

The script will prompt you for:
- Project name
- Project description
- Tech stack
- Current phase

Then commit and push:

```bash
git add -A
git commit -m "chore: bootstrap harness"
git push
```

---

## Step 3: Clone and Configure

```bash
# If you haven't already cloned
git clone git@github.com:KustodyFi/your-project-name.git
cd your-project-name

# Pull the bootstrap commit (if created via GitHub UI)
git pull
```

### 3a. Set up local agent roles

```bash
# Copy default roles to your local (gitignored) working copy
# Skip this if setup.sh already ran locally
cp -r .agent.default .agent
```

### 3b. Fill in project invariants

Open `agent.project.md` and replace the `{{INVARIANT_*}}` placeholders with your project's architectural rules. Examples:

```markdown
* **All API responses use JSON with camelCase keys**
* **PostgreSQL is the only persistence layer**
* **Every service must have health check endpoints**
* **No direct database access from API handlers — use repository pattern**
* **All secrets come from environment variables, never hardcoded**
```

### 3c. Update tech stack

If auto-bootstrapped, the tech stack will say "TBD". Update it in `AGENTS.md`:

```markdown
**Tech stack:** Python 3.11 · FastAPI · PostgreSQL · Redis · Docker
```

### 3d. Customize coding standards

Review and adjust `docs/standards/coding-standards.md` for your project's language and framework.

---

## Step 4: Verify Your Setup

Run through this checklist:

| Check | How | Expected |
|-------|-----|----------|
| README has project name | Open `README.md` | Your project name, not `{{PROJECT_NAME}}` |
| AGENTS.md has project name | Open `AGENTS.md` | Your project name in header |
| STATUS.md has date | Open `.cowork/STATUS.md` | Today's date |
| `.agent/` exists locally | `ls .agent/` | `orchestrator/`, `reviewer/`, `shared/` |
| `.agent/` is gitignored | `git status` | `.agent/` should NOT appear |
| No remaining placeholders | `grep -rn '{{PROJECT' .` | No results (only `{{INVARIANT_*}}` is OK) |

---

## Step 5: Start Working

Your AI agent (Cursor, Copilot, Gemini, etc.) reads files in this order on startup:

```
AGENTS.md → agent.md → agent.project.md → docs/standards/ → .cowork/STATUS.md
```

> See `AGENTS.md` → "Startup Sequence" for the authoritative boot order.

### Creating your first task

See `.cowork/tasks/README.md` for the canonical task folder structure.

Quick version:

```bash
mkdir -p .cowork/tasks/001_your_first_task/{01_planning,02_architecture,03_structure,04_implementation,evidence}

# Create the required files
cat > .cowork/tasks/001_your_first_task/TASK.md << 'EOF'
# Task: Your First Task

## Objective
What you want to build.

## Scope
What's in and out of scope.

## Success Criteria
How you know it's done.
EOF

cat > .cowork/tasks/001_your_first_task/STATE.yaml << 'EOF'
task: "001_your_first_task"
task_status: active
current_stage: planning
current_stage_status: pending
coding_allowed: false

stages:
  planning:
    status: pending
    review_rounds: 0
  architecture:
    status: pending
    review_rounds: 0
  structure:
    status: pending
    review_rounds: 0
  implementation:
    status: pending
    review_rounds: 0
EOF
```

---

## Repo Structure After Setup

```
your-project/
├── AGENTS.md                ← AI agent entry point (read first)
├── agent.md                 ← Org-wide rules (§1-§10)
├── agent.project.md         ← YOUR project invariants
├── README.md                ← Project README
│
├── docs/
│   ├── standards/           ← Coding standards
│   ├── specs/               ← Verified specs (anti-hallucination)
│   ├── adr/                 ← Architecture decision records
│   ├── plans/               ← Roadmap & backlog
│   └── guides/              ← How-to guides
│
├── .agent.default/          ← Role defaults (tracked, shared)
├── .agent/                  ← Your local roles (gitignored)
│
└── .cowork/                 ← Process harness
    ├── HARNESS_SPEC.md      ← Task-stage rules
    ├── ONBOARD.md           ← Role interaction guide
    ├── STATUS.md            ← Project dashboard
    ├── harness/             ← State machine, validator
    ├── prompts/             ← Agent prompt templates
    ├── tasks/               ← All task work
    └── reviews/             ← Cross-cutting reviews
```

---

## FAQ

### Q: What if I need to change the project name later?

Run `grep -rn 'OldName' .` to find all occurrences, then find-and-replace. The name appears in `AGENTS.md`, `README.md`, `.cowork/STATUS.md`, and `.agent.default/shared/log.md`.

### Q: Can I add custom workflows?

Yes. Add new `.md` files to `.agent.default/orchestrator/workflows/`. After adding, run `cp -r .agent.default .agent` to refresh your local copy (or just copy the new file to `.agent/orchestrator/workflows/`).

### Q: What if I want to skip the harness for a quick prototype?

You don't have to use tasks. The harness is there when you need structured multi-stage work. For quick prototyping, just write code normally — the `agent.md` rules and `docs/standards/` still apply.

### Q: How do I onboard a reviewer agent?

Use the prompt template in `.cowork/prompts/onboard_agent.md`. Copy it and send to your reviewer (Codex, GPT, Gemini).

### Q: Where do I report issues with the template?

Open an issue on [KustodyFi/agent-harness-template](https://github.com/KustodyFi/agent-harness-template/issues).
