---
description: Run self-review against docs contracts
---

# /review — Self-Review

## Steps

1. Read `docs/specs/` — verify code matches specs
2. Check for stale cross-references: `grep -rn "old/path"` across docs
3. Verify all test suites pass
4. Report findings

## Checklist

- [ ] Code matches architecture spec?
- [ ] File structure matches file-structure spec?
- [ ] No hardcoded values?
- [ ] No functions > 100 lines?
- [ ] All tests pass?
- [ ] No duplicate content across docs?
