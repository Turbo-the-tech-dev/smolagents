## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Hardening Sandbox against Dunder Name Binding and Class Method Leakage]
**Vulnerability:** The executor allowed binding dunder names in the execution scope through variable assignments, function/class definitions, import aliases, and exception handlers (e.g., `__builtins__ = {}` or `import math as __math__`). Additionally, class methods leaked to the global `custom_tools` namespace.
**Learning:** Securing attribute access (`obj.__attr__`) is insufficient if the agent can bind names to the top-level scope. Protecting all identifier binding points in the AST is necessary for a robust sandbox. Class method leakage occurred because method definitions were being evaluated as top-level functions.
**Prevention:** Applied `check_dunder_name` to all name-binding AST nodes (`Assign`, `FunctionDef`, `ClassDef`, `Import`, `Try`, `With`). Fixed method leakage by calling `create_function` directly within `evaluate_class_def` for class methods, ensuring they remain scoped to the class.
