# Task: Template Review & Convergence

## Objective
Bring the agent-harness-template to production-ready state through iterative Codex review rounds, fixing all structural inconsistencies, duplication violations, and validator drift.

## Scope
- All files in the template repository
- Structural integrity (cross-references, folder map, pointers)
- One-source-of-truth enforcement
- Validator ↔ state machine ↔ schema alignment
- Bootstrap workflow (GitHub Action + manual setup.sh)
- Documentation (README, getting-started guide)

## Success Criteria
- Codex review returns PASS with zero findings
- Both bootstrap paths produce identical results
- No normative rules duplicated outside canonical files
