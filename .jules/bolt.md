## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2026-03-02 - Operator Dispatch and Name Lookup Optimization
**Learning:** Replacing `isinstance` chains with dictionary dispatch tables for binary, unary, and comparison operators improves interpreter speed. Additionally, pre-wrapping static tools with safety decorators instead of wrapping them on every access significantly reduces name lookup overhead.
**Action:** Always pre-wrap fixed toolsets and use O(1) dispatch tables for recursive AST evaluation.
