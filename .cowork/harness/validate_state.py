#!/usr/bin/env python3
"""
Validate a task's STATE.yaml against harness invariants.

Usage:
    python3 .cowork/harness/validate_state.py .cowork/tasks/NNN_name/STATE.yaml

Requires: pip install pyyaml
"""

import sys
import yaml
from pathlib import Path


VALID_STAGES = ["planning", "architecture", "structure", "implementation"]
VALID_STATUSES = ["pending", "in_review", "changes_requested", "approved"]
IMPLEMENTATION_STATUSES = VALID_STATUSES + ["coding", "complete"]
VALID_TASK_STATUSES = ["active", "complete", "verified", "closed"]

# Stage ordering for prerequisite checks
STAGE_ORDER = {stage: i for i, stage in enumerate(VALID_STAGES)}


def validate(state_path: str) -> list[str]:
    """Validate STATE.yaml and return list of errors."""
    errors = []
    path = Path(state_path)

    if not path.exists():
        return [f"File not found: {state_path}"]

    with open(path) as f:
        state = yaml.safe_load(f)

    # --- Required top-level fields ---
    required = ["task", "current_stage", "current_stage_status", "coding_allowed", "stages"]
    for field in required:
        if field not in state:
            errors.append(f"Missing required field: {field}")

    if errors:
        return errors

    stage = state["current_stage"]
    status = state["current_stage_status"]
    coding = state["coding_allowed"]
    stages = state.get("stages", {})

    # --- Validate task_status if present ---
    if "task_status" in state and state["task_status"] not in VALID_TASK_STATUSES:
        errors.append(
            f"Invalid task_status: '{state['task_status']}' "
            f"(valid: {VALID_TASK_STATUSES})"
        )

    # --- Validate current_stage ---
    if stage not in VALID_STAGES:
        errors.append(f"Invalid current_stage: '{stage}'")
        return errors

    # --- Validate current_stage_status ---
    allowed = IMPLEMENTATION_STATUSES if stage == "implementation" else VALID_STATUSES
    if status not in allowed:
        errors.append(
            f"Invalid status '{status}' for stage '{stage}' "
            f"(valid: {allowed})"
        )

    # --- Validate stages block has all 4 stages ---
    for s in VALID_STAGES:
        if s not in stages:
            errors.append(f"Missing stage in stages block: '{s}'")

    if errors:
        return errors

    # --- Validate each stage's status value ---
    for s in VALID_STAGES:
        stage_data = stages[s]
        if "status" not in stage_data:
            errors.append(f"Stage '{s}' missing 'status' field")
            continue
        s_allowed = IMPLEMENTATION_STATUSES if s == "implementation" else VALID_STATUSES
        if stage_data["status"] not in s_allowed:
            errors.append(
                f"Stage '{s}' has invalid status '{stage_data['status']}' "
                f"(valid: {s_allowed})"
            )

    # --- coding_allowed invariant ---
    # coding_allowed must be false unless implementation status is 'coding' or 'complete'
    impl_status = stages.get("implementation", {}).get("status", "pending")
    if coding and impl_status not in ("coding", "complete"):
        errors.append(
            f"coding_allowed is true but implementation status is '{impl_status}' "
            f"(must be 'coding' or 'complete')"
        )
    if not coding and impl_status in ("coding", "complete"):
        errors.append(
            f"coding_allowed is false but implementation status is '{impl_status}' "
            f"(should be true)"
        )

    # --- Stage ordering: no stage can be active past unapproved prerequisites ---
    current_idx = STAGE_ORDER[stage]
    for i in range(current_idx):
        prior = VALID_STAGES[i]
        prior_status = stages[prior].get("status", "pending")
        if prior_status != "approved":
            errors.append(
                f"Current stage is '{stage}' but prerequisite stage "
                f"'{prior}' has status '{prior_status}' (must be 'approved')"
            )

    # --- Review rounds: approved stages must have at least 1 review round ---
    for s in VALID_STAGES:
        stage_data = stages[s]
        if stage_data.get("status") == "approved":
            rounds = stage_data.get("review_rounds", 0)
            if rounds < 1:
                errors.append(
                    f"Stage '{s}' is approved but review_rounds is {rounds} "
                    f"(must be >= 1)"
                )

    # --- Evidence check for closed/verified/complete tasks ---
    task_status = state.get("task_status", "active")
    if task_status in ("complete", "verified", "closed"):
        task_dir = path.parent
        evidence_dir = task_dir / "evidence"
        required_evidence = ["tests.md", "changed_files.md", "verification.md"]
        for ef in required_evidence:
            if not (evidence_dir / ef).exists():
                errors.append(
                    f"task_status is '{task_status}' but evidence file "
                    f"missing: evidence/{ef}"
                )

    return errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <STATE.yaml>")
        sys.exit(1)

    errs = validate(sys.argv[1])
    if errs:
        print("❌ VALIDATION FAILED:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("✅ STATE.yaml is valid")
        sys.exit(0)
