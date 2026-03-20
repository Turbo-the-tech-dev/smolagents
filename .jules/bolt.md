## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2026-03-02 - Interpreter Dispatch Overhead and Security Checks
**Learning:** Inlining security checks in the most frequently called recursive function (`evaluate_ast`) and using fast-path type checks (isinstance for primitives) provides a measurable speedup (~20% on Fibonacci) by reducing function call overhead and skipping redundant validation.
**Action:** Minimize decorator overhead and function calls in hot paths. Implement fast-paths for common safe cases before performing expensive validation.
