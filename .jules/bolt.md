## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2026-03-02 - Nested Interpreter State Management
**Learning:** Pre-computed optimization states (like O(1) tool lookup sets) stored in the shared `state` dictionary can be corrupted by nested interpreter calls (e.g., an agent calling another agent as a tool).
**Action:** Use a save-and-restore pattern with `try...finally` blocks in `evaluate_python_code` to ensure nested executions correctly preserve and restore the outer execution's optimization context.
