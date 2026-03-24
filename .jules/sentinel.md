## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Blocking Dunder Name Binding in Local Executor]
**Vulnerability:** The executor prevented access to dunder *attributes* but allowed binding unauthorized dunder *names* (e.g., `__builtins__`, `__class__`) via assignments, function/class definitions, and import aliases.
**Learning:** Hardening only attribute access is insufficient if the language allows binding names directly to magic identifiers. Attackers could redefine `__builtins__` or `__init__` at the top level to potentially compromise the sandbox state or behavior.
**Prevention:** Expanded `ALLOWED_DUNDER_METHODS` to 47 standard magic methods and implemented a mandatory `check_dunder_name` validation for all name-binding AST nodes, including `ast.Name` targets, `ast.FunctionDef`, `ast.ClassDef`, `ast.arguments`, `ast.alias` (imports), and `ast.ExceptHandler`.
