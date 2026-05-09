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
| GPT | Architecture & design soundness | repomix output + prompt | ✅ Done |
| Gemini | Implementation correctness & edge cases | repomix output + prompt | ⬜ Pending |
| Codex | Structural integrity & one-source-of-truth | reads repo + this file | ⬜ Pending |

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

**1. [MEDIUM]: Layer 1 overloaded with project knowledge**
Location: AGENTS.md, README.md
Issue: Layer 1 mixes org policy with project-specific invariants (agent.project.md, docs/specs, docs/adr). Weakens "Layer 1 never changes per-project" claim.
Fix: Split or clarify that Layer 1 contains both org policy and project governance.

**2. [HIGH]: Bootstrap flow may fail with branch protection**
Location: .github/workflows/bootstrap.yml, setup.sh
Issue: Auto-bootstrap assumes push to main, write permission, no branch protection. Half-templated repos possible.
Fix: Add workflow_dispatch, document protected-branch behavior, make bootstrap idempotent, add post-bootstrap validation.

**3. [MEDIUM]: Validator doesn't check review entry existence**
Location: state_machine.yaml, validate_state.py
Issue: Validator checks counters/fields but not actual review.md file presence. Approval provenance weakens after coding/complete.
Fix: Validate actual review.md presence, require approval metadata to persist through coding/complete.

**4. [MEDIUM]: No finding IDs or conflict resolution in review process**
Location: ONBOARD.md, harness_review.md
Issue: No finding ID, decision owner, resolution status, or conflict escalation record in the review process.
Fix: Add finding IDs and triage table to the review attribution format.

**5. [LOW]: Python dependency assumed for validator**
Location: validate_state.py, docs/standards/coding-standards.md
Issue: Validator requires Python + PyYAML. Language-specific standards baked in.
Fix: Add `make validate-harness` or containerized fallback. Mark standards as customizable.

**6. [MEDIUM]: Hooks layer roadmap not visible in shipped template**
Location: (planned, not tracked)
Issue: Hooks spec is gitignored. New repos have no visibility into the planned extension.
Fix: Add tracked `docs/plans/hooks-layer.md` with planned extension points and compatibility contract.

**Verdict:** PASS WITH NOTES

---

### Gemini Findings
_Paste Gemini R1 output here. Orchestrator will triage below._

### Codex Findings
_Codex appends findings here directly, or human pastes them._

### codex: R1 — Structural Integrity Review
**Date:** 2026-05-09
**Agent:** codex (o3)
**Mode:** terminal

## Findings

### 1. [HIGH]: README duplicates canonical architecture, role, lifecycle, and startup content
**Location:** README.md:22
**Issue:** README points to canonical sections, then restates the 3-layer architecture, role capabilities, task lifecycle, state shape, and startup sequence inline (`README.md:22`, `README.md:70`, `README.md:97`, `README.md:129`, `README.md:370`). This violates the zero-tolerance one-source-of-truth rule for architecture layers, team roles/capabilities, gate/task process, validated state semantics, and startup sequence.
**Fix:** Keep README as a short template overview with pointers only. Move all normative diagrams/examples for those topics to the canonical files or replace them with links to `AGENTS.md`, `.cowork/HARNESS_SPEC.md`, `.cowork/tasks/README.md`, and `.cowork/harness/state_machine.yaml`.

### 2. [HIGH]: Role capability rules are duplicated in Layer 2 role files
**Location:** .agent.default/orchestrator/ROLE.md:7
**Issue:** `.agent.default/orchestrator/ROLE.md` and `.agent.default/reviewer/ROLE.md` define responsibilities, limits, and can/cannot behavior inline even though role capabilities are canonical in `AGENTS.md` → "Team Roles" and `.cowork/harness/roles.yaml`. Several entries also restate gate rules from `.cowork/HARNESS_SPEC.md`.
**Fix:** Keep Layer 2 role files focused on identity and local workflow pointers. Replace process permissions and can/cannot lists with pointers to `AGENTS.md`, `.cowork/harness/roles.yaml`, and `.cowork/HARNESS_SPEC.md`.

### 3. [HIGH]: Implementation coding approval metadata is not enforced after transition
**Location:** .cowork/harness/validate_state.py:136
**Issue:** `state_machine.yaml` models implementation as `approved → coding`, but the validator only requires `review_rounds`, `approved_by`, and `approved_date` when a stage status is exactly `approved`. Once implementation moves to `coding` or `complete`, approval provenance can disappear while `coding_allowed` is true. The active task demonstrates this: `.cowork/tasks/001_template_review/STATE.yaml:23` has implementation `status: coding` with no `approved_by` or `approved_date`.
**Fix:** Require implementation statuses `coding` and `complete` to retain approval metadata and at least one review round, or introduce explicit `coding_approved_by` / `coding_approved_date` fields and validate them.

### 4. [MEDIUM]: Manual and GitHub bootstrap paths do not produce identical local results
**Location:** .github/workflows/bootstrap.yml:68
**Issue:** `setup.sh` creates a local `.agent/` copy that persists for the user, while `bootstrap.yml` creates `.agent/` only inside the GitHub runner. Because `.agent/` is ignored, it is not committed and will not exist after a developer clones the bootstrapped repo. The Action still claims to bootstrap `.agent/` in its commit message.
**Fix:** Remove the `.agent/` copy step and claim from `bootstrap.yml`, or make both paths use the same bootstrap script contract and document that `.agent/` is always created locally by the developer after clone.

### 5. [MEDIUM]: Generated README keeps an unreplaced placeholder token
**Location:** README.template.md:21
**Issue:** `README.template.md` contains the literal token `{{PLACEHOLDER}}`, but setup/bootstrap only replace named project placeholders. After bootstrap, the generated project README still contains placeholder syntax while `docs/guides/getting-started.md:46` says all placeholders are replaced.
**Fix:** Reword the note without `{{...}}` syntax, or add an explicit replacement/check for that token and update the getting-started guide to distinguish project placeholders from intentionally user-filled invariants.

### 6. [MEDIUM]: Review prompt points reviewers to a noncanonical attribution source
**Location:** .cowork/prompts/review_stage.md:20
**Issue:** The stage review prompt tells reviewers to use the entry format from `.agent.default/reviewer/ROLE.md` → "Entry Format". The canonical attribution format is `.cowork/ONBOARD.md` → "Attribution Format"; the role file should not be the source for that content.
**Fix:** Point directly to `.cowork/ONBOARD.md` → "Attribution Format" in the prompt and leave `.agent.default/reviewer/ROLE.md` as a pointer only.

### 7. [LOW]: Template contains the explicitly banned FX-Town example
**Location:** setup.sh:13
**Issue:** The review criteria call out project-specific examples such as "FX-Town" as disallowed, but `setup.sh` prompts with `Project name (e.g., FX-Town)`.
**Fix:** Replace with a neutral placeholder such as `your-project` or `Example App`.

### 8. [LOW]: Repomix output is generated but not ignored
**Location:** .gitignore:35
**Issue:** `git status --short` shows `repomix-output.xml` as untracked. This is generated review input and should not be committed into the template, but `.gitignore` only ignores task folders and round prompts under development tracking.
**Fix:** Add `repomix-output.xml` or the chosen Repomix output pattern to `.gitignore`, and remove the local generated artifact if it is not intended to ship.

## Verdict
NEEDS REVISION

---

## Orchestrator Triage — R1

> Triaging GPT findings now. Gemini + Codex pending.

| # | Finding | Source | Severity | Decision | Notes |
|---|---------|--------|----------|----------|-------|
| G1 | Layer 1 overloaded with project knowledge | GPT | MEDIUM | ✅ ACCEPTED | Clarify in AGENTS.md that Layer 1 has both org policy + project governance |
| G2 | Bootstrap fails with branch protection | GPT | HIGH | ✅ ACCEPTED | Add workflow_dispatch trigger + document in README/getting-started |
| G3 | Validator doesn't check review.md existence | GPT | MEDIUM | ✅ ACCEPTED | Add review.md file check for approved stages |
| G4 | No finding IDs in review process | GPT | MEDIUM | ⏸️ DEFERRED | Good for hooks layer — adds complexity to v1 attribution format |
| G5 | Python dependency assumed | GPT | LOW | ⏸️ DEFERRED | Keep Python validator. Add Makefile wrapper in hooks layer phase |
| G6 | Hooks roadmap not visible | GPT | MEDIUM | ✅ ACCEPTED | Create docs/plans/hooks-layer.md with plan stub |

---

## Round 2 Findings
_After R1 fixes, Codex re-reviews._

---

## Codex Instructions

> **Codex:** You are the structural integrity reviewer. Read the entire repository.
> After review, append your findings to this file under "### Codex Findings".
> Use the output format specified in the R1 prompt section below.
> The orchestrator will triage your findings and decide what to fix.

---

## Status

| Round | GPT | Gemini | Codex | Fixes Applied | Next |
|-------|-----|--------|-------|---------------|------|
| R1 | ✅ 6 findings | ⬜ | ⬜ | ⬜ | Waiting for Gemini + Codex |
| R2 | — | — | ⬜ | ⬜ | — |
| R3 | — | — | ⬜ | ⬜ | — |
