---
description: Coding standards for all project code
---

# Coding Standards

Follow these rules for ALL code in this project. No exceptions.

---

## 1. Function Size

- **Max 100 lines per function.** If a function exceeds this, split it.
- Prefer 20-50 line functions. Each function does ONE thing.
- The function name should describe what it does — no `process()` or `handle()`.

---

## 2. No Nested If

Use **guard clauses** (early returns) instead of nested if/else.

```python
# Good: guard clause
def get_item(registry, item_id: str):
    item = registry.lookup(item_id)
    if not item:
        raise ItemNotFoundError(item_id)
    return _to_response(item)
```

---

## 3. No Hardcoded Values

All constants in dedicated config files or module-level constants at the top.

---

## 4. Single Responsibility

Each file/module does ONE thing.

---

## 5. 3-Layer API Architecture

```
Route (thin) → Service (logic) → Data (storage/bus)
```

| Layer | Rules |
|-------|-------|
| **Route** | Only framework imports. Validate → call service → return response. |
| **Service** | No framework imports. Pure logic. No HTTP knowledge. |
| **Data** | Shared tools — bus, registry, storage. |

---

## 6. DRY (Don't Repeat Yourself)

- If two functions share logic, extract a helper with `_` prefix.
- Shared logic goes in a utility function, not copy-pasted.

---

## 7. Error Handling

- Define domain-specific exceptions.
- Raise in service layer. Catch and convert in route layer.
- Never use bare `except:` — always catch specific exceptions.

---

## 8. Naming Conventions

| Item | Convention | Example |
|------|-----------|---------|
| Files | `snake_case.py`, `camelCase.jsx` | `agent_service.py` |
| Functions | `snake_case` | `list_agents()` |
| Private helpers | `_` prefix | `_parse_step()` |
| Classes | `PascalCase` | `AgentResponse` |
| Constants | `UPPER_SNAKE_CASE` | `API_PORT` |

---

## 9. Docstrings

- Every module: top-level docstring explaining purpose.
- Every public function: one-line docstring.
- Private helpers: docstring if non-obvious.

---

## 10. Testing

- Every service gets unit tests.
- Test file naming: `test_{module}.py`.
- Assert exact values, not just `is not None`.

---

## 11. Type Hints

- All functions must have complete type hints.
- Return types are mandatory.

---

## 12. No Ghost Code

- Do not leave `# TODO: implement this` or `pass` in new code.
- If intentionally blank, raise `NotImplementedError` with context.

---

## 13. Immutability

- Treat all function arguments as read-only.
- Return new copies instead of mutating in place.

---

## 14. Specific Exceptions

- Never use bare `except:` or `except Exception: pass`.
- Domain-specific errors include context.

---

## 15. Pure Business Logic

- Keep business logic pure — no I/O inside service functions.
- Services receive data as arguments and return results.

---

## 16. Secrets Safety

- Never embed secrets, keys, or credentials in code, test fixtures, logs, or docs.
- Test fixtures must use obviously fake values.
