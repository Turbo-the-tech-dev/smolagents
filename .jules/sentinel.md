## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2026-03-18 - [Hardening Local Python Executor against Dunder Name Manipulation]
**Vulnerability:** The local Python executor allowed the assignment and definition of top-level "dunder" names (e.g., `__builtins__`, `__bad_func__`).
**Learning:** Preventing attribute access (`obj.__class__`) is only one part of sandbox security. If an attacker can bind a name in the execution namespace that overrides internal Python mechanics (like `__builtins__`) or use dunder names in unexpected places (like exception handlers or context managers), they can compromise the integrity of the sandbox.
**Prevention:** Strictly block the assignment, definition, and aliased import of any name matching `is_dunder(name)`, with a granular whitelist for necessary magic methods in classes (`ALLOWED_DUNDER_METHODS`) and a specific exception for `__name__` in the execution state.
