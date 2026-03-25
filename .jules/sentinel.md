## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Blocking Dunder Name Manipulation in Local Python Executor]
**Vulnerability:** The local Python executor allowed the definition and assignment of unauthorized dunder names (e.g., `__builtins__`, `__globals__`) in the interpreter's state via various AST nodes, including direct assignment, function/lambda definitions, and import aliases.
**Learning:** Security checks on attributes (`obj.__class__`) were present, but the interpreter lacked validation for identifiers in the local `state`. This allowed attackers to overwrite critical dunder names or bind them to malicious objects.
**Prevention:** Centralized identifier validation in `check_dunder_name` (against a whitelist of safe magic methods) and applied it to `set_value` (for `ast.Name`), function/class/lambda definitions, `try-except` handlers, and `import` aliases. Used `check_arguments` to validate all function argument names at definition time.
