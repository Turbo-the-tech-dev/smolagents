## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Comprehensive Hardening of Identifier Binding against Dunder Names]
**Vulnerability:** The local Python executor allowed binding dunder names (e.g., `__builtins__`) as identifiers through imports, function/lambda arguments, class/function names, exception handlers, loop variables, and context managers.
**Learning:** Hardening attribute access is insufficient if an attacker can bind a dunder name to a sensitive object (or vice versa) in the interpreter's state. All binding sites in the AST must be validated.
**Prevention:** Implemented `check_dunder_name` and `check_arguments` helpers to enforce a dunder name policy at all binding points. This includes a whitelist of allowed dunder methods for class definitions while strictly blocking sensitive names like `__builtins__`.
