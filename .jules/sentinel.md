## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2026-04-14 - [Internal Sandbox Variable Exposure]
**Vulnerability:** Guest code could directly access or shadow internal state variables like `_operations_count` used for resource limiting.
**Learning:** Sandbox environments often rely on specific keys in the `state` dictionary for metadata. If these keys aren't explicitly protected in the interpreter loop, guest code can bypass security constraints by modifying them.
**Prevention:** Maintain a registry of internal-only names (`INTERNAL_PROTECTED_NAMES`) and enforce rejection in `evaluate_name`, `set_value`, and all binding operations (imports, function/class definitions).
