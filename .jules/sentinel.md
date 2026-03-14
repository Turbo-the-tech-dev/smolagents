## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Blocking Dunder Name Binding in Local Python Executor]
**Vulnerability:** The executor allowed users to bind values to dunder names (e.g., `__init__ = 1`) or use them as aliases in imports (`import os as __builtins__`). This could be used to shadow critical builtins or manipulate the execution state in ways that could lead to sandbox escapes.
**Learning:** Even if attribute access is protected, name binding (assignment, imports, function/class definitions) can provide alternative ways to inject or overwrite sensitive objects in the local scope.
**Prevention:** Implemented comprehensive dunder name checks at all name binding points: `set_value` for assignments, `evaluate_import` for aliases and star imports, `evaluate_class_def` for class names, `evaluate_function_def` and `create_function` for function names and arguments, `evaluate_try` for exception variables, and `evaluate_with` for context variables.
