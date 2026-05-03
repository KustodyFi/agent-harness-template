# Cowork Harness — Process Mechanics

> **What this folder is.** `.cowork/` is the multi-agent collaboration harness (Layer 3).
> For the big picture, see `AGENTS.md`.

---

## Purpose

`.cowork/` manages the structured workflow for AI-assisted development:

- **Tasks** — all work units with staged deliverables
- **Reviews** — shared communication between agents
- **Harness** — machine-readable process definitions
- **Prompts** — templates for agent interactions

---

## Deliverables Per Task

| Deliverable | File | What's In It |
|------------|------|-------------|
| **Specs** | `{stage}/spec.md` | Orchestrator-written deliverable |
| **Reviews** | `{stage}/review.md` | Full discussion history with attribution |
| **Results** | `04_implementation/result.md` | What was built, before/after |
| **Evidence** | `evidence/changed_files.md` | Every file changed + why |
| **Tests** | `evidence/tests.md` | Raw test output |

---

## Attribution Format

See `.cowork/ONBOARD.md` → "Attribution Format" for the canonical entry format.

---

## Validation

```bash
# Requires: pip install pyyaml (or activate project venv)
python3 .cowork/harness/validate_state.py .cowork/tasks/NNN_name/STATE.yaml
```

See `.cowork/harness/state_machine.yaml` → `validated_rules` for the full list of enforced invariants.
