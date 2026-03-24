## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2026-03-02 - Interpreter Decorator and Introspection Overhead
**Learning:** Inlining security checks in `evaluate_ast` and targeting only `CHECKED_NODES` provided a measured ~29% speedup in recursive execution paths (e.g., Fibonacci). Replacing slow `inspect` calls with `getattr` and `isinstance` further reduced call overhead.
**Action:** Minimize decorator usage in hot recursive paths and prefer direct attribute checks over high-level introspection modules like `inspect`.
