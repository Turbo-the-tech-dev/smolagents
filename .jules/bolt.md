## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2026-03-24 - Evaluation Loop Inlining
**Learning:** Inlining security checks in the AST evaluation loop and restricting them to nodes that actually resolve new references (Call, Name, Attribute, Subscript) significantly reduces overhead. Using try-except for hot-path counter initialization also improves performance in tight recursion.
**Action:** Minimize decorator usage and conditional branching in core recursive functions.
