# Task: Add Hooks Layer (Layer 3) to Template

## Objective
Add deterministic hooks that automatically enforce harness process rules, preventing process violations like the ones that occurred during Task 001.

## Scope
- Create `.hooks/` directory with hook definitions and scripts
- Implement 4 hooks: `session_start`, `pre_write`, `pre_commit`, `post_review`
- Git hooks adapter (universal fallback)
- Update AGENTS.md architecture, folder map, and documentation

## Out of Scope
- Claude Code native hooks adapter (Phase 2)
- Cursor `.cursorrules` adapter (Phase 2)
- Subagent formalization (Task 003)
- Plugin system (future)

## Success Criteria
- `pre-commit` git hook blocks commit when STATE.yaml is invalid
- `session_start` script outputs correct startup context
- All hooks are shell scripts (no Python dependency for hooks)
- Documentation updated to reflect 5-layer architecture
