## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-03-05 - [Blocking Dunder Name Manipulation in Local Executor]
**Vulnerability:** The local Python executor allowed the definition and assignment of unauthorized dunder names (e.g., `__builtins__`, `__globals__`) in the execution scope.
**Learning:** Hardening attribute access with `nodunder_getattr` is insufficient if an attacker can bind these names to other values or use them as function arguments, lambda parameters, or import aliases. Legitimate dunder methods (like `__init__`) must be explicitly whitelisted in the definition phase to avoid breaking valid class implementations.
**Prevention:** Strictly block dunder name binding in `set_value`, `evaluate_import`, `create_function`, `evaluate_lambda`, `evaluate_try`, and `evaluate_delete`. Explicitly allow `__name__` and `__class__` for name lookup, and whitelisted magic methods for function definitions.
