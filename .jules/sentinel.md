## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2026-03-11 - [Exhaustive Dunder Name Restriction in Local Python Executor]
**Vulnerability:** The sandbox was vulnerable to several dunder name manipulation vectors beyond direct attribute access, including dunder function/class definitions, dunder argument names, dunder import aliases, and dunder loop/exception/context targets.
**Learning:** Hardening a sandbox requires blocking dunder identifiers not just in `ast.Attribute` but in `ast.Name` nodes across all binding contexts (Assign, For, Try, With, FunctionDef, ClassDef, Import). Merely checking `getattr`/`setattr` is insufficient if the identifier itself can be bound to a value or defined as a function.
**Prevention:** Implemented strict dunder checks in all name-binding AST nodes. Expanded `ALLOWED_DUNDER_METHODS` to support legitimate object-oriented patterns (arithmetic, comparison, iteration) while maintaining a strict "deny-by-default" posture for dangerous internal attributes.
