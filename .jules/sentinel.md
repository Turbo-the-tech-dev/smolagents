## 2025-05-22 - [Hardening Local Python Executor against Dunder Attribute Manipulation]
**Vulnerability:** The local Python executor allowed modification and deletion of dunder attributes (e.g., `__init__`, `__class__`) on objects.
**Learning:** While `nodunder_getattr` existed to prevent reading dunder attributes, it didn't prevent assignment or deletion. Attackers could use this to override object methods or change an object's class to escape the sandbox.
**Prevention:** Centralized dunder check in `is_dunder` and applied it to attribute assignment in `set_value` and `evaluate_class_def`, and to attribute deletion in `evaluate_delete`. Also wrapped `setattr` and `delattr` with dunder checks.

## 2025-05-23 - [Sandbox Internal State Tampering via Identifier Access]
**Vulnerability:** Guest code could directly access and modify internal state variables (like `_operations_count` and `_print_outputs`) because they were stored in the same `state` dictionary as user variables. Guest code could also shadow critical names via `import ... as ...` or function definitions using dunder names not in the whitelist.
**Learning:** Preventing access to *attributes* (like `obj.__dict__`) is insufficient if internal accounting variables are exposed as *identifiers* in the evaluation scope. Attackers could reset operation counters to bypass execution limits.
**Prevention:** Implemented a centralized `check_protected_name` and applied it to all identifier entry points: variable lookups, assignments, function/class names, deletions, and import aliases. This ensures internal names are truly "internal" and dunder names are restricted to a safe whitelist for legitimate class behavior.
