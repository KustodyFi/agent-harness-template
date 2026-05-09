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
| GPT | Architecture & design soundness | repomix output + prompt | ⬜ Pending |
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
_Paste GPT R1 output here. Orchestrator will triage below._

### Gemini Findings
_Paste Gemini R1 output here. Orchestrator will triage below._

### Codex Findings
_Codex appends findings here directly, or human pastes them._

---

## Orchestrator Triage — R1
_After all 3 reviewers submit, orchestrator consolidates here:_

| # | Finding | Source | Severity | Decision | Notes |
|---|---------|--------|----------|----------|-------|
| | | | | | |

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
| R1 | ⬜ | ⬜ | ⬜ | ⬜ | — |
| R2 | — | — | ⬜ | ⬜ | — |
| R3 | — | — | ⬜ | ⬜ | — |
