## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-22 - [Protecting Internal Interpreter State from Guest Code Manipulation]
**Vulnerability:** Guest code could access and modify internal interpreter state variables like `_operations_count` and `_print_outputs` because they were stored in the same state dictionary as user variables without name protection.
**Learning:** Attackers could reset `_operations_count` to zero or a negative value to bypass the `MAX_OPERATIONS` limit, leading to infinite loops and Denial of Service. They could also modify or clear `_print_outputs` to hide their actions or manipulate logs.
**Prevention:** Implemented `INTERNAL_PROTECTED_NAMES` and a `check_protected_name` helper that is called during name lookup (`evaluate_name`), assignment (`set_value`), definition (`evaluate_function_def`, `evaluate_class_def`), import (`evaluate_import`), and deletion (`evaluate_delete`). This prevents any guest code from binding to, accessing, or unbinding protected internal names.
