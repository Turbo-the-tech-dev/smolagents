## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Comprehensive Dunder Name Lockdown in LocalPythonExecutor]
**Vulnerability:** Sandbox escapes via dunder name manipulation (e.g., assigning to __builtins__, defining dunder functions/classes, or using dunder names in imports, loop targets, or exception handlers).
**Learning:** Checking only attribute access (obj.__attr__) is insufficient; name-based assignment and definition must be blocked across all AST nodes that introduce names into the scope (Assign, Import, For, With, Try, FunctionDef, ClassDef, Lambda).
**Prevention:** Implement comprehensive is_dunder() checks in set_value, evaluate_import, evaluate_function_def, create_function, evaluate_class_def, evaluate_lambda, evaluate_name, and evaluate_try. Use set_value for target assignment in evaluate_with and evaluate_for to inherit these checks.
