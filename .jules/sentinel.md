## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-24 - [Protecting Interpreter Internal State in Guest Namespace]
**Vulnerability:** Internal state variables used for execution tracking (e.g., `_operations_count`) were stored in the same `state` dictionary as guest variables, allowing guest code to bypass operation limits or manipulate logs.
**Learning:** Security boundaries must extend beyond object attributes (dunders) to the variable namespace itself. Shadows or aliases in imports (e.g., `import math as _operations_count`) can also be used to overwrite protected internal state.
**Prevention:** Centralized identifier validation in `check_protected_name` and applied it to all name-binding and lookup AST nodes: `Name`, `Assign`, `Import`, `FunctionDef`, `ClassDef`, and `Delete`.
