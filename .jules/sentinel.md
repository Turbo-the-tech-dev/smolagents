## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Blocking Dunder Name Binding in Local Python Executor]
**Vulnerability:** The local Python executor allowed binding dunder names (e.g., `__builtins__`) via assignments, imports, function arguments, and other name-binding points.
**Learning:** Preventing dunder *attribute* access is insufficient if an attacker can shadow or overwrite internal variables like `__builtins__` in the execution state or function scopes. Python's scope resolution means that binding a name like `__builtins__` in a local or module scope can override the real built-ins.
**Prevention:** Centralized identifier validation using `check_dunder_name` and applied it to all name binding points (ast.Assign, ast.Import, ast.FunctionDef, ast.Lambda, ast.Try, ast.With). Expanded the dunder whitelist to support safe magic methods for custom classes.
