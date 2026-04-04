## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Protecting Sandbox Internal State and Blocking Dunder Name Binding]
**Vulnerability:** Sandbox internal variables like `_operations_count` and `_print_outputs` were stored in the same state dictionary as user variables, allowing guest code to access and modify them to bypass resource limits or tamper with logs. Guest code could also bind new values to dunder names (e.g., `__secret__ = 1`).
**Learning:** Security depends not just on blocking attribute access, but also on preventing guest code from interacting with any identifier (variable name, exception alias, or context manager target) that has security implications.
**Prevention:** Defined `INTERNAL_PROTECTED_NAMES` and updated `evaluate_name` and `set_value` (plus `try/except` and `with` handlers) to block both internal state access and dunder name binding.
