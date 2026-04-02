## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2026-04-02 - [Comprehensive Identifier Hardening in Local Python Executor]
**Vulnerability:** The sandbox allowed binding unauthorized dunder names (e.g., `__builtins__`, `__globals__`) via assignments, imports, function/class definitions, and more.
**Learning:** Protecting attributes alone is insufficient; any mechanism that introduces a name into the local or global scope (like `import as`, `except as`, or function arguments) can be used to shadow or rebind internal dunders.
**Prevention:** Implemented a centralized `check_identifier` helper and applied it to all name-binding points: `set_value`, `evaluate_import`, `evaluate_function_def`, `evaluate_class_def`, `create_function`, `evaluate_lambda`, `evaluate_try`, and `evaluate_with`.
