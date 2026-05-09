# Hooks Layer — Planned Extension

> **Status:** Planned (not yet implemented)
> **Target:** Template v2

---

## Purpose

Add deterministic guardrails (Layer 3 in a future 5-layer architecture) that automatically enforce harness process rules. Think "git hooks for AI agents."

## Planned Hooks

| Hook | Trigger | What It Enforces |
|------|---------|-----------------|
| `session_start` | Agent session begins | Startup sequence loaded, active task identified |
| `pre_write` | Before writing code files | `coding_allowed` must be true in STATE.yaml |
| `pre_commit` | Before git commit | STATE.yaml valid, review.md has entries |
| `post_review` | After review findings received | Findings logged to review.md with attribution |

## Architecture

```
.hooks/
├── hooks.yaml              ← Hook definitions (agent-agnostic)
├── install.sh              ← Installs git hooks adapter
├── scripts/                ← Hook implementation (shell)
└── adapters/
    └── git/                ← Git hooks (universal fallback)
```

## Design Principles

- **Deterministic, not AI** — hooks are shell scripts, not LLM calls
- **Agent-agnostic** — git hooks as universal adapter
- **Non-blocking by default** — informational hooks don't stop work
- **Blocking where critical** — pre_commit validates STATE.yaml

## Non-Goals (v1)

- Claude Code native hooks (future adapter)
- Cursor `.cursorrules` integration (future adapter)
- Plugin marketplace / distribution system

## Compatibility

Hooks will not break existing harness functionality. They add enforcement on top of the existing state machine + validator.
