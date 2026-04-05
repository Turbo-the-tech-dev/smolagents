## 2025-05-15 - Centralized Identifier Validation in LocalPythonExecutor
**Vulnerability:** Internal interpreter state variables (`_operations_count`, `_print_outputs`) were accessible and modifiable by guest code, potentially allowing sandbox escapes (e.g. infinite loops by resetting counter) or data tampering.
**Learning:** In AST-based interpreters, name binding happens at multiple points (assignments, imports, exception handlers, context managers). Relying on disparate checks at each point is error-prone.
**Prevention:** Implement a centralized `check_dunder_name` helper that is called at all name-binding and name-lookup nodes in the AST to enforce a uniform security policy across the sandbox.
