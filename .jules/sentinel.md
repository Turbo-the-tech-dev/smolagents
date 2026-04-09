## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-06-12 - [Hardening type() and Class Definitions in Local Python Executor]
**Vulnerability:** The `type()` builtin could be used to dynamically create classes with unauthorized dunder names or attributes (e.g., `__getattribute__`), bypassing static dunder checks. Additionally, class methods leaked into the global tool namespace.
**Learning:** Builtins that facilitate dynamic object creation, like `type`, can serve as a conduit for sandbox escapes if they are not explicitly restricted. Internal AST evaluation of function definitions within a class body can also cause scope pollution if not specifically isolated from the global state.
**Prevention:** Replaced the `type` tool with a `nodunder_type` class that intercepts 3-argument calls to validate names and attributes. Modified `evaluate_class_def` to use `create_function` directly for method definitions, preventing accidental registration in the global `custom_tools` dictionary.
