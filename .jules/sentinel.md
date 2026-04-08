## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-22 - [Protecting Internal State Variables in Local Python Executor]
**Vulnerability:** Guest code could access, modify, and delete internal state variables like `_operations_count` and `_print_outputs` that are injected into the evaluation context.
**Learning:** Even if a sandbox restricts imports and built-ins, internal metadata used for monitoring (like operation counters) or capturing output must be explicitly protected from manipulation within the sandbox state.
**Prevention:** Implemented a centralized `check_protected_name` helper and applied it to all name binding and lookup points (assignments, calls, imports, exception handlers, context managers) in the interpreter.
