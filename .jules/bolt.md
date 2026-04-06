## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2026-03-02 - Inlining Security Checks in Recursion
**Learning:** Removing the '@safer_eval' decorator from 'evaluate_ast' and inlining the 'check_safer_result' logic (with early returns for primitive types) reduces function-call overhead in the recursive evaluation loop, achieving a ~20% performance gain for recursion-heavy code.
**Action:** Minimize decorator use on extremely "hot" recursive entry points to avoid stack frame overhead.
