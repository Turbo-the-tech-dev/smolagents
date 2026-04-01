## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Hardening Dunder Name Binding and Fixing Class Scope Leak]
**Vulnerability:** Unauthorized binding of dunder names (e.g., `__builtins__`) via function/class definitions and imports allowed for potential sandbox escape. Additionally, class methods leaked into the global `custom_tools` scope.
**Learning:** `evaluate_ast` on a `FunctionDef` automatically registers it in `custom_tools`. Within a class definition, this behavior is incorrect as it pollutes the global tool namespace. Binding dunder names in the local state can also bypass attribute-level checks if the interpreter relies on state lookups.
**Prevention:** Strictly block dunder names in all binding points: `set_value` (for Name targets), `evaluate_function_def`, `evaluate_class_def` (for class names), and `evaluate_import` (for names and aliases). In `evaluate_class_def`, call `create_function` directly to avoid global registration. Corrected `evaluate_with` to ensure `__exit__` is called on the context manager itself.
