# Review Log — 001_template_review / 04_implementation

---

### agent: R1 — Initial structural audit
**Date:** 2026-05-01
**Agent:** codex (o3)
**Mode:** terminal

## Findings (10)
1. **HIGH**: validate_state.py doesn't enforce state_machine.yaml invariants
2. **HIGH**: coding_allowed rule inconsistent across files
3. **HIGH**: .gitignore uses evidence/ instead of /evidence/
4. **HIGH**: permissions.yaml vocabulary doesn't match roles.yaml
5. **HIGH**: Duplicated content in .cowork/README.md
6. **MEDIUM**: agent.md doesn't document AGENTS.md exception
7. **MEDIUM**: harness.md wrong skill path
8. **MEDIUM**: setup.sh doesn't escape special chars
9. **LOW**: README.template.md references src/
10. **LOW**: Orchestrator ROLE.md missing /coding-standards

**Verdict:** NEEDS REVISION

---

### orchestrator: R1 fixes applied
**Date:** 2026-05-01
**Agent:** Gemini (Cursor)

All 10 findings fixed. Validator rewritten, permissions normalized, setup.sh escape_sed() added.

---

### agent: R2 — Vocabulary and validator drift
**Date:** 2026-05-03
**Agent:** codex (o3)
**Mode:** terminal

## Findings (7)
1. **HIGH**: permissions.yaml uses actions not in roles.yaml
2. **HIGH**: Validator allows contradictory current_stage_status
3. **HIGH**: Human approval not machine-enforced
4. **MEDIUM**: Attribution format still has multiple sources
5. **MEDIUM**: README defines partial startup sequence
6. **MEDIUM**: AGENTS folder map becomes stale after setup
7. **LOW**: Folder map omits setup.sh and .gitignore

**Verdict:** NEEDS REVISION

---

### orchestrator: R2 fixes applied
**Date:** 2026-05-03
**Agent:** Gemini (Cursor)

All 7 findings fixed. roles.yaml expanded, validator enforces status consistency + approved_by/date.

---

### agent: R3 — Validator completeness
**Date:** 2026-05-03
**Agent:** codex (o3)
**Mode:** terminal

## Findings (4)
1. **HIGH**: Validator doesn't enforce all state machine rules
2. **MEDIUM**: Schema doesn't match validator semantics
3. **MEDIUM**: Gate rules duplicated in README
4. **LOW**: Folder map omits .cowork/README.md

**Verdict:** NEEDS REVISION

---

### orchestrator: R3 fixes applied
**Date:** 2026-05-03
**Agent:** Gemini (Cursor)

Validator: future stages pending check, task lifecycle check. Schema: separate standard/implementation definitions. state_machine.yaml: split validated_rules vs process_rules.

---

### agent: R4 — Final duplication cleanup
**Date:** 2026-05-03
**Agent:** codex (o3)
**Mode:** terminal

## Findings (2)
1. **MEDIUM**: README still restates task flow rules
2. **LOW**: Validator check summaries duplicated and incomplete

**Verdict:** NEEDS REVISION

---

### orchestrator: R4 fixes applied
**Date:** 2026-05-03
**Agent:** Gemini (Cursor)

README task flow → pure pointer. Validator summaries in HARNESS_SPEC.md and .cowork/README.md → pointer to state_machine.yaml validated_rules.

---

### agent: R5 — Zero-tolerance source-of-truth
**Date:** 2026-05-03
**Agent:** codex (o3)
**Mode:** terminal

## Findings (4)
1. **MEDIUM**: Attribution format still has two inline definitions
2. **MEDIUM**: README still restates process and role rules
3. **MEDIUM**: Task deliverables duplicated outside canonical file
4. **LOW**: Schema allows values validator rejects

**Verdict:** NEEDS REVISION

---

### orchestrator: R5 fixes applied
**Date:** 2026-05-03
**Agent:** Gemini (Cursor)

ONBOARD.md: all roles use pointer to Attribution Format. README: inline content → pointers. .cowork/README.md deliverables → pointer to tasks/README.md. Schema: documented semantic-only constraint.

---

### agent: R6 — Convergence attempt
**Date:** 2026-05-04
**Agent:** codex (o3)
**Mode:** terminal

## Findings (5)
1. **HIGH**: README still restates architecture and role details
2. **HIGH**: Task creation/closing pointers are broken (circular)
3. **MEDIUM**: Reviewer onboarding prompt defines own startup sequence
4. **MEDIUM**: Approval prompt restates stage-advance process
5. **MEDIUM**: Task lifecycle semantics differ between state machine and validator

**Verdict:** NEEDS REVISION

---

### orchestrator: R6 fixes applied
**Date:** 2026-05-04
**Agent:** Gemini (Cursor)

README arch → pointer. tasks/README.md now canonical for create+close (broke circular ref). Prompts → pointers. Validator enforces all-stages-done for 'complete'.

---

### agent: R7 — PASS WITH NOTES
**Date:** 2026-05-04
**Agent:** codex (o3)
**Mode:** terminal

## Findings (2)
1. **LOW**: README still repeats role capability summaries
2. **LOW**: State machine repeats two gate-rule statements

**Verdict:** PASS WITH NOTES

---

### orchestrator: R7 notes addressed
**Date:** 2026-05-04
**Agent:** Gemini (Cursor)

README role descriptions neutralized. state_machine.yaml process_rules → pointer to HARNESS_SPEC.md.

---

### agent: R8 — New additions review
**Date:** 2026-05-04
**Agent:** codex (o3)
**Mode:** terminal

## Findings (6)
1. **HIGH**: bootstrap.yml paths filter may not trigger on first push
2. **HIGH**: Repo description injected directly into shell (injection risk)
3. **MEDIUM**: README restates canonical gate rules outside diagrams
4. **MEDIUM**: getting-started.md defines partial startup sequence
5. **MEDIUM**: README.template.md tells bootstrapped repos to run setup.sh
6. **LOW**: First-task example omits required files

**Verdict:** NEEDS REVISION

---

### orchestrator: R8 fixes applied
**Date:** 2026-05-04
**Agent:** Gemini (Cursor)

bootstrap.yml: removed paths filter, env: variables for injection safety. README/guide normative text → pointers. README.template.md rewritten for post-bootstrap. Task example → pointer.

---

### agent: R9 — Bootstrap parity
**Date:** 2026-05-04
**Agent:** codex (o3)
**Mode:** terminal

## Findings (1)
1. **HIGH**: Manual setup.sh leaves bootstrap.yml installed

**Verdict:** NEEDS REVISION

---

### orchestrator: R9 fix applied
**Date:** 2026-05-04
**Agent:** Gemini (Cursor)

setup.sh now removes bootstrap.yml after manual setup, mirroring the Action's self-destruct.

---

### 2026-05-09 — R10 pending
Awaiting final Codex review for PASS confirmation.
