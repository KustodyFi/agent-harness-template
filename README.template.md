# {{PROJECT_NAME}}

{{PROJECT_DESCRIPTION}}

## Quick Start

```bash
# Clone the repo
git clone <repo-url>
cd {{PROJECT_NAME_LOWER}}

# Pull latest (in case auto-bootstrap ran)
git pull

# Set up local agent roles (if not already present)
cp -r .agent.default .agent

# Read AGENTS.md for the full startup sequence
```

> **Note:** If `{{PLACEHOLDER}}` values remain in any files, run `./setup.sh` as a fallback.

## Tech Stack

{{TECH_STACK}}

## Project Structure

```
├── AGENTS.md                ← AI agent entry point
├── agent.md                 ← Org-wide agent policy
├── agent.project.md         ← Project-specific rules
├── docs/                    ← Documentation
│   ├── standards/           ← Coding standards
│   ├── specs/               ← Verified project specs
│   ├── adr/                 ← Architecture decisions
│   ├── plans/               ← Roadmap & backlog
│   └── guides/              ← How-to guides
├── .agent.default/          ← Default AI role definitions
└── .cowork/                 ← Multi-agent harness
```

## AI Agent Harness

This project uses the [KustodyFi Agent Harness](https://github.com/KustodyFi/agent-harness-template) for structured AI-assisted development. See `AGENTS.md` for details.

## License

<!-- Add your license here -->
