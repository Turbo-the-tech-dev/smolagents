## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2026-03-02 - AST Interpreter Safety Check Inlining
**Learning:** Wrapping the recursive `evaluate_ast` in a decorator for safety checks adds significant function call overhead. Additionally, most AST nodes (Constants, BinOps, etc.) do not need safety checks as they cannot return dangerous objects.
**Action:** Inline safety checks into the main evaluation loop and target only "source" nodes (Name, Call, Attribute, Subscript) while skipping primitive types.
