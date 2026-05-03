# KustodyFi Agent Policy

> **Organization-wide rules for all AI development agents.**
> This file is the same across all KustodyFi repositories.
> It references only `AGENTS.md` (exists in every repo) — no other path references.
>
> **Startup:** Read `AGENTS.md` first, then this file.
> See `AGENTS.md` for the full startup sequence.

## 1. Human-Gated Design Workflow

For **major changes** (new sprints, architecture changes, multi-file features), follow these four gates in order. Do not self-advance. Wait for explicit human approval at each gate.

1. **Architecture** — Problem, scope, non-goals, affected modules, alternatives, proposed approach, risks.
2. **Data Diagram** — Data/event/state flow, inputs/outputs, schema changes, failure paths, external boundaries.
3. **Function-Level Structure** — Files to create/modify, function signatures, call flow, constants, error plan, test cases.
4. **Coding & Verification** — Implement the smallest correct diff, run tests, report results.

**FAST PATH:** When the human explicitly says "just do it" or the task is trivially small (< 3 files, no architecture change), skip gates 1–3 and go directly to coding.

### Cowork Harness Override

If the repo uses the cowork harness, its rules override FAST PATH:
- Do NOT use FAST PATH for harness tasks.
- Do NOT skip any stage.
- Coding starts ONLY when the harness gate allows it.
- See the harness spec for the full process.

## 2. Turn Budget & Execution Rules

* [DO] When starting a task, issue all `Read` calls for the necessary files in parallel first.
* [DO] Only after all reading and analysis is complete, issue all `Write` calls in parallel.
* [DON'T] Do not mix reading and writing across multiple alternating turns.
* [DO] Search before writing — use `grep` to check if a pattern already exists before creating new utilities.
* [DO] Use surgical edits (SEARCH/REPLACE). NEVER rewrite an entire file if changing a few lines.
* [DON'T] No lazy placeholders like `// ... existing code ...` or `# rest of function`.

## 3. Context Isolation

* [DON'T] Do not read or tail logs/outputs from modules you are not actively working on unless explicitly requested. Prevent context pollution.

## 4. Scope Discipline

* [DON'T] Do not refactor unrelated code without explicit human approval.
* [DON'T] Do not expand scope beyond the approved design.
* [DO] Stay within the current engineering phase/sprint unless the human explicitly expands scope.

## 5. Chain of Thought (CoT)

* [DO] Before making architectural decisions, reason internally.
* [DO] When emitting final code or file writes, output only clean code. No reasoning commentary in source files.
* [DON'T] Do not inject markdown artifacts, analysis blocks, or CoT commentary into source files.

## 6. Evaluation-Driven Loop

* [DO] After writing or modifying code, execute the relevant test suite to verify it works.
* [DO] Report results using explicit states:
  - `VERIFIED` — tests ran and passed.
  - `PARTIALLY VERIFIED` — some tests passed, others could not be run (e.g., external dependency offline).
  - `VERIFICATION IMPOSSIBLE` — environment constraints prevent testing.
* [DON'T] Never falsely claim a test passed, hide failed checks, or manipulate results.
* [DON'T] Never remove assertions to force success.
* [DO] **3-Strike Rule:** If code fails tests 3 times in a row, STOP. Do not blindly guess. Revert the file, state the error, ask the user for guidance.

## 7. Operational Process

* [DO] When blocked by permission, network, or tooling: **STOP immediately.** State the blocker. Ask the human. Do NOT retry with workarounds.
* [DO] When moving or deleting files, update ALL references in the **same commit**. Run `grep -rn "old/path"` to find all references before committing.
* [DO] Commit after each logical unit of work. Push is the human's responsibility — never retry a failed push.
* [DON'T] Never duplicate content across files. One source of truth + pointers everywhere else.
* [DON'T] Never create a new file for content that already exists elsewhere. Search first.

## 8. Logging & Version Control

* [DO] Use conventional commit messages: `type(scope): description` (e.g., `fix(api): handle null response`).
* [DO] One logical change per commit. Do not bundle unrelated changes.
* [DON'T] Never force-push. Never rewrite git history without human approval.
* [DON'T] Never commit generated files, build artifacts, or IDE state.

## 9. Secrets & Security

* [DON'T] Never embed secrets, API keys, or credentials in code, fixtures, logs, or docs.
* [DON'T] Never create or recommend `.env` files.
* [DO] Read credentials from `os.environ` at runtime.
* [DO] Every new runtime capability must either call an existing security hook or document where the hook point will be inserted.

## 10. Standards

For coding rules, see the project's coding standards (referenced in `AGENTS.md`).
