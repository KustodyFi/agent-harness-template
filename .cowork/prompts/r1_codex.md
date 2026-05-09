# R1 Prompt — Codex (Structural Integrity Review)

> **How to use:** Send this prompt to Codex. It reads the repo directly.

---

You are a structural integrity reviewer for the `agent-harness-template` repository.

## Your Role

**Structural integrity reviewer.** You enforce the one-source-of-truth rule, verify all cross-references resolve, and ensure the template is clean for cloning.

## Context

This template is being re-architected from 3 layers to 5 layers. A new hooks layer (`.hooks/`) is being added. The structure spec is at `.cowork/tasks/002_hooks_layer/03_structure/spec.md`.

9 prior review rounds (R1-R9) achieved convergence on the existing 3-layer structure. This review validates:
1. The existing structure hasn't regressed
2. The new hooks layer integrates cleanly
3. All documentation reflects the 5-layer architecture

## What to Review

### 1. One Source of Truth (zero tolerance)
Scan every file for ANY restated rule, format, or process detail. Flag if content appears in more than one file (pointers are fine, inline definitions are not).

Canonical sources:
- Attribution format → `.cowork/ONBOARD.md` only
- Gate rules → `.cowork/HARNESS_SPEC.md` only
- Task structure → `.cowork/tasks/README.md` only
- Startup sequence → `AGENTS.md` only
- Validated rules → `.cowork/harness/state_machine.yaml` only
- Hook definitions → `.hooks/hooks.yaml` only (NEW)

### 2. Cross-References
- Every "See X → Y" pointer must resolve to real content
- AGENTS.md folder map must match actual directory structure
- No orphan files, no broken paths

### 3. New Files Integration
- Does `.hooks/` appear in AGENTS.md folder map?
- Does the README reference the hooks layer?
- Does `setup.sh` / `bootstrap.yml` handle `.hooks/install.sh`?
- Is `hooks.yaml` consistent with `state_machine.yaml` terminology?

### 4. Task Structure
- Is `.cowork/tasks/002_hooks_layer/` properly structured per `.cowork/tasks/README.md`?
- Does `STATE.yaml` pass validation?
- Is `TIMELINE.md` up to date?

### 5. Template Hygiene
- Clean for cloning — no project-specific content
- No stale references from R1-R9 fix rounds

### 6. Process Compliance
- Is the review plan at `03_structure/review_plan.md` being followed?
- Are review findings being logged to `review.md` with proper attribution?

## Output Format

Write your findings as an entry appended to:
`.cowork/tasks/002_hooks_layer/03_structure/review.md`

Use this attribution format:

```markdown
### agent: R1 — Structural Integrity Review
**Date:** YYYY-MM-DD
**Agent:** codex (o3)
**Mode:** terminal

## Findings

### N. [SEVERITY]: [Title]
**Location:** [file:line]
**Issue:** [what's wrong]
**Fix:** [suggested fix]

## Verdict
PASS | PASS WITH NOTES | NEEDS REVISION
```

Use HIGH / MEDIUM / LOW severity.
