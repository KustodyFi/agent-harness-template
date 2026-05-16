# Agent Harness Template — Work Log

> **Purpose:** Shared development log for orchestrator (Cursor) and reviewers (Codex, GPT, Gemini).
> This file is tracked so all agents can read it. Remove before releasing the template.

---

## R1 — Full Sweep Review (2026-05-09)

### Reviewers
- **GPT 5.5**: Architecture & design → 6 findings → PASS WITH NOTES
- **Gemini 3.1 Pro**: Implementation correctness → 5 findings → NEEDS REVISION
- **Codex o3**: Structural integrity → 8 findings → NEEDS REVISION

### Orchestrator Triage
**19 total → 16 accepted, 3 deferred**

### Accepted & Fixed (commit 9c4c303)

| # | Finding | Source | Fix |
|---|---------|--------|-----|
| M1 | Validator crashes on empty/malformed YAML | Gemini | try/except + isinstance check |
| M2 | Newlines in repo description break Action | Gemini | Strip newlines before sed |
| M3 | stages=None causes crash | Gemini | `or {}` fallback |
| M5 | Unchecked dict access in validator | Gemini | Safe `.get()` throughout |
| G1 | Layer 1 overloaded with project knowledge | GPT | Clarified Layer 1 scope in AGENTS.md |
| G2 | Bootstrap fails with branch protection | GPT | Added workflow_dispatch trigger |
| G3 | Validator doesn't check review.md existence | GPT | Added file existence check |
| G6 | Hooks roadmap not visible | GPT | Created docs/plans/hooks-layer.md |
| C1 | README duplicates canonical content | Codex | 436→132 lines, pointers only |
| C2 | Role files duplicate capabilities | Codex | Replaced inline rules with pointers |
| C3 | Approval metadata lost after coding | Codex | Enforced for coding/complete |
| C4 | Bootstrap paths differ on .agent/ | Codex | Removed .agent/ from Action |
| C5 | README.template.md has placeholder syntax | Codex | Reworded |
| C6 | Review prompt wrong attribution source | Codex | Points to ONBOARD.md |
| C7 | FX-Town example in setup.sh | Codex | Neutral example |
| C8 | Repomix output not ignored | Codex | Gitignored |

### Deferred

| # | Finding | Source | Reason |
|---|---------|--------|--------|
| G4 | No finding IDs in review process | GPT | Hooks layer scope |
| G5 | Python dependency assumed for validator | GPT | Add Makefile wrapper later |
| M4 | Schema conditional for stage-specific status | Gemini | Complexity vs marginal IDE benefit |

---

## Post-R1 Cleanup (2026-05-09)

- Separated dev tracking from template files (gitignore rules)
- Removed harness_review.md from tracked files
- README rewrite: "How to Use This Template" with 5-step flow
- Enabled as GitHub template (`gh repo edit --template`)
- Renamed 000-template.md → adr-template.md

---

## R2 — Codex Convergence Review (2026-05-15)

### Reviewer
- **Codex o3**: 7 findings — assessed repo as "pre-production, 6/10"

### Orchestrator Triage
**Root cause:** Most findings were valid against the PUSHED code, but R1 fixes existed locally and were never pushed (8 commits ahead of GitHub).

| # | Finding | Severity | Decision | Reason |
|---|---------|----------|----------|--------|
| R2-1 | No requirements.txt for PyYAML | HIGH | ✅ FIXED | Added requirements.txt with pyyaml>=6.0 |
| R2-2 | Validator not crash-safe | HIGH | ❌ REJECTED | Already fixed in R1 (M1,M3,M5). Codex read stale push. |
| R2-3 | "Production-ready" overclaims | HIGH | ✅ FIXED | → "structured framework", linked hooks plan |
| R2-4 | Validator vs state_machine.yaml drift | MEDIUM | ✅ FIXED | Added 2 missing rules to validated_rules |
| R2-5 | Branch protection overclaims | MEDIUM | ✅ FIXED | Documented limitation honestly |
| R2-6 | Local state inconsistent | MEDIUM | ❌ REJECTED | Gitignored dev artifacts, not template content |
| R2-7 | Validator exceeds 100-line limit | LOW | ⏸️ DEFERRED | Refactor separately |

### Lesson Learned
**Push after every fix session.** Codex reads from GitHub, not local disk.

---

## Current State

- **Local HEAD:** Commit with R2 fixes applied
- **GitHub:** Needs push (8+ commits ahead)
- **Template status:** Functional, governance layer complete
- **Hooks layer:** Planned, not implemented (docs/plans/hooks-layer.md)
- **Next:** Push → R3 final review → hooks layer implementation

---

## Codex Instructions

> **Codex:** This is the shared work log. Read it before reviewing.
> After reviewing, append your findings below under a new section heading.
> Use the standard attribution format from `.cowork/ONBOARD.md`.
> The orchestrator will triage your findings and update this log.
