# Harness Template Review — Multi-Agent Review Tracker

> **Orchestrator:** Gemini (Cursor IDE)
> **Reviewers:** GPT (chat), Gemini (chat), Codex (terminal)
> **Scope:** Full agent-harness-template — architecture, file structure, implementation, documentation

---

## Review Plan

### Round 1 — Full Sweep
All 3 reviewers audit the entire template independently.

| Reviewer | Focus | Input | Status |
|----------|-------|-------|--------|
| GPT | Architecture & design soundness | repomix output + prompt | ✅ Done — 6 findings |
| Gemini | Implementation correctness & edge cases | repomix output + prompt | ✅ Done — 5 findings |
| Codex | Structural integrity & one-source-of-truth | reads repo + this file | ✅ Done — 8 findings |

### Round 2 — Convergence
Codex verifies all R1 fixes. GPT/Gemini only if R1 had architecture-level findings.

### Round 3+ — Final PASS
If needed. Goal is PASS from all reviewers.

---

## Orchestrator Decisions

> I (orchestrator) triage all findings here. Each finding gets:
> - ✅ ACCEPTED — will fix
> - ❌ REJECTED — reason documented
> - ⏸️ DEFERRED — tracked for future task

---

## Round 1 Findings

### GPT Findings

#### gpt: R1 — Architecture & Design Review
**Date:** 2026-05-09
**Agent:** GPT-5.5 Thinking
**Mode:** chat

**G1. [MEDIUM]: Layer 1 overloaded with project knowledge**
**G2. [HIGH]: Bootstrap flow may fail with branch protection**
**G3. [MEDIUM]: Validator doesn't check review entry existence**
**G4. [MEDIUM]: No finding IDs or conflict resolution in review process**
**G5. [LOW]: Python dependency assumed for validator**
**G6. [MEDIUM]: Hooks layer roadmap not visible in shipped template**

**Verdict:** PASS WITH NOTES

---

### Gemini Findings

#### gemini: R1 — Implementation Correctness Review
**Date:** 2026-05-09
**Agent:** Gemini 3.1 Pro
**Mode:** chat

**M1. [HIGH]: Validator crashes on empty/malformed YAML**
Location: validate_state.py:35
Issue: No try/except around yaml.safe_load(). Empty file → None → TypeError. Malformed → unhandled YAMLError.

**M2. [MEDIUM]: Newlines in repo description break GitHub Action**
Location: bootstrap.yml:50
Issue: escape_sed() doesn't strip newlines. Multi-line description → "unterminated s command".

**M3. [MEDIUM]: stages parsed as None causes crash**
Location: validate_state.py:46
Issue: `state.get("stages", {})` returns None if key exists but value is null. Crash at line 68.

**M4. [LOW]: Schema permits invalid status for non-implementation stages**
Location: state.schema.json:11
Issue: JSON Schema unconditionally allows "coding"/"complete" for any stage. IDE autocomplete misleading.

**M5. [LOW]: Unchecked dictionary access in verification logic**
Location: validate_state.py:102
Issue: stages[stage].get("status") can KeyError if stage missing from stages block.

**Verdict:** NEEDS REVISION

---

### Codex Findings

#### codex: R1 — Structural Integrity Review
**Date:** 2026-05-09
**Agent:** codex (o3)
**Mode:** terminal

**C1. [HIGH]: README duplicates canonical architecture, role, lifecycle, startup content**
Location: README.md:22, 70, 97, 129, 370

**C2. [HIGH]: Role capability rules duplicated in Layer 2 role files**
Location: .agent.default/orchestrator/ROLE.md:7, .agent.default/reviewer/ROLE.md

**C3. [HIGH]: Implementation approval metadata not enforced after transition**
Location: validate_state.py:136

**C4. [MEDIUM]: Bootstrap paths don't produce identical local results**
Location: bootstrap.yml:68

**C5. [MEDIUM]: Generated README keeps unreplaced placeholder token**
Location: README.template.md:21

**C6. [MEDIUM]: Review prompt points to noncanonical attribution source**
Location: .cowork/prompts/review_stage.md:20

**C7. [LOW]: Template contains FX-Town example**
Location: setup.sh:13

**C8. [LOW]: Repomix output not ignored**
Location: .gitignore:35

**Verdict:** NEEDS REVISION

---

## Orchestrator Triage — R1 (consolidated)

### ✅ ACCEPTED — Will Fix

| # | Finding | Source | Severity | Fix Plan |
|---|---------|--------|----------|----------|
| M1 | Validator crashes on empty/malformed YAML | Gemini | HIGH | Add try/except + isinstance check |
| G2 | Bootstrap fails with branch protection | GPT | HIGH | Add workflow_dispatch trigger + docs |
| C1 | README duplicates canonical content | Codex | HIGH | Strip inline diagrams, keep pointers only |
| C2 | Role files duplicate capabilities | Codex | HIGH | Replace inline rules with pointers |
| C3 | Approval metadata lost after coding transition | Codex+GPT | HIGH | Enforce approved_by/date for coding/complete |
| M2 | Newlines in description break Action | Gemini | MEDIUM | Strip newlines before sed |
| M3 | stages=None causes crash | Gemini | MEDIUM | Use `or {}` fallback |
| M5 | Unchecked dict access in validator | Gemini | LOW→MED | Use .get() safely |
| G1 | Layer 1 overloaded | GPT | MEDIUM | Clarify Layer 1 scope in AGENTS.md |
| G3 | Validator doesn't check review.md | GPT | MEDIUM | Add file existence check |
| C4 | Bootstrap paths differ on .agent/ | Codex | MEDIUM | Remove .agent/ from Action, document |
| C5 | README.template.md has {{PLACEHOLDER}} | Codex | MEDIUM | Reword without placeholder syntax |
| C6 | Review prompt wrong attribution source | Codex | MEDIUM | Point to ONBOARD.md |
| G6 | Hooks roadmap not visible | GPT | MEDIUM | Create docs/plans/hooks-layer.md |
| C7 | FX-Town example in setup.sh | Codex | LOW | Replace with neutral example |
| C8 | Repomix output not ignored | Codex | LOW | Already fixed |

### ⏸️ DEFERRED — Future Task

| # | Finding | Source | Severity | Reason |
|---|---------|--------|----------|--------|
| G4 | No finding IDs in review process | GPT | MEDIUM | Hooks layer scope |
| G5 | Python dependency assumed | GPT | LOW | Keep Python validator, add Makefile wrapper later |
| M4 | Schema conditional for stage-specific status | Gemini | LOW | Complexity vs marginal IDE benefit |

---

## Status

| Round | GPT | Gemini | Codex | Fixes Applied | Next |
|-------|-----|--------|-------|---------------|------|
| R1 | ✅ 6 findings | ✅ 5 findings | ✅ 8 findings | ⬜ | Applying 16 fixes |
| R2 | — | — | ⬜ | ⬜ | — |
| R3 | — | — | ⬜ | ⬜ | — |
