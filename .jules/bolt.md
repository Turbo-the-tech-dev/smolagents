## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2025-05-22 - AST Security Check Inlining
**Learning:** Inlining security checks in `evaluate_ast` and restricting them to "producer" nodes (Name, Call, Attribute, Subscript) via a `CHECKED_NODES` set significantly reduces recursion overhead. This resulted in a ~23% speedup for recursive tasks like Fibonacci.
**Action:** Identify hot paths in recursive interpreters and move decorator-based validation inside the main loop to avoid extra function frame overhead.
