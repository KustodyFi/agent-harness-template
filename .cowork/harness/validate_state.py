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


def validate(state_path: str) -> list[str]:
    """Validate STATE.yaml and return list of errors."""
    errors = []
    path = Path(state_path)

    if not path.exists():
        return [f"File not found: {state_path}"]

    with open(path) as f:
        state = yaml.safe_load(f)

    # Required fields
    required = ["task", "current_stage", "current_stage_status", "coding_allowed"]
    for field in required:
        if field not in state:
            errors.append(f"Missing required field: {field}")

    if errors:
        return errors

    # coding_allowed invariant
    stage = state["current_stage"]
    status = state["current_stage_status"]
    coding = state["coding_allowed"]

    if stage != "implementation" and coding:
        errors.append(
            f"coding_allowed is true but current_stage is '{stage}' "
            f"(must be 'implementation')"
        )

    if stage == "implementation" and status in ("coding", "complete") and not coding:
        errors.append(
            f"coding_allowed is false but implementation status is '{status}' "
            f"(should be true)"
        )

    # Stage order
    valid_stages = ["planning", "architecture", "structure", "implementation"]
    if stage not in valid_stages:
        errors.append(f"Invalid stage: '{stage}'")

    # Status values
    valid_statuses = ["pending", "in_review", "changes_requested", "approved", "coding", "complete"]
    if status not in valid_statuses:
        errors.append(f"Invalid status: '{status}'")

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
