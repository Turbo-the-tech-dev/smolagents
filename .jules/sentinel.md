## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Tool Shadowing and Dunder Name Binding]
**Vulnerability:** The local Python executor allowed shadowing `static_tools` (like `print` or `final_answer`) and binding to unauthorized dunder names (like `__builtins__`) via `import as`, `def`, `class`, `with as`, `try ... except ... as`, and function/lambda arguments.
**Learning:** Security checks were only present for direct assignments via `ast.Name` targets in `set_value`. Other ways Python binds identifiers to names were unprotected.
**Prevention:** Implemented centralized `check_can_bind` and `check_dunder_name` helpers and applied them to all AST nodes that bind identifiers.
