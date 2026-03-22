## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Blocking Dunder Name Bindings in Local Python Executor]
**Vulnerability:** The local Python executor allowed binding values to dunder names (e.g., `__builtins__`, `__init__`) via imports, assignments, function/class definitions, and argument names.
**Learning:** While attribute access was protected, name bindings in the interpreter's state were not. Attackers could overwrite critical dunder names in the local scope or use them in imports (aliasing) to potentially access forbidden builtins or manipulate execution state.
**Prevention:** Implemented strict dunder name checks in `evaluate_import`, `set_value`, `evaluate_function_def`, `create_function`, `evaluate_lambda`, `evaluate_class_def`, `evaluate_try`, and `evaluate_with`. Whitelisted safe magic methods in `ALLOWED_DUNDER_METHODS` to maintain functionality.
