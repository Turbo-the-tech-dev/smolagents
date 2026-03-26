## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2026-03-02 - Inline Security Checks & Node Targeting
**Learning:** Inlining security logic into the main AST evaluation loop and only targeting high-risk node types (Call, Name, etc.) eliminates massive decorator overhead and redundant checks for safe literal/arithmetic nodes.
**Action:** In high-frequency recursive functions, avoid decorators and target specific cases instead of blanket wrapping.
