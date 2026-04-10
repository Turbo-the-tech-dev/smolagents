## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2026-04-10 - [Protecting Internal State and Dunder Names in Local Executor]
**Vulnerability:** Internal state variables like `_operations_count` and `_print_outputs` were accessible, modifiable, and deletable by guest code in the local Python executor. Additionally, dunder names could be assigned or deleted at the top-level scope.
**Learning:** Preventing attribute-level dunder access (via `nodunder_getattr`) is insufficient if the names themselves can be manipulated in the global/local state. Guests could reset operation counters to bypass execution limits.
**Prevention:** Centralized name validation using `check_protected_name` and integrated it into `evaluate_name`, `set_value`, and `evaluate_delete` to block unauthorized access to internal state and dunder names.
