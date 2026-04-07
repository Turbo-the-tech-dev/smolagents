## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2026-03-02 - Inlining Security Checks in evaluate_ast
**Learning:** Removing the `@safer_eval` decorator from `evaluate_ast` and inlining the security check logic (with early returns for primitive types) significantly reduces function-call overhead in the recursive evaluation loop. This provided a measured speedup of ~18% for Fibonacci(20).
**Action:** In high-frequency recursive functions, inline logic from decorators to save call stack overhead when possible, especially for early-exit conditions.
