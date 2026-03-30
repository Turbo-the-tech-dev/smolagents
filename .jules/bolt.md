## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2026-03-02 - Builtin Function Check Optimization
**Learning:** Replacing `inspect.getmodule(func) == builtins` and `inspect.isbuiltin(func)` with `getattr(func, "__module__", None) == "builtins"` and `isinstance(func, BuiltinFunctionType)` in the interpreter's hot path (evaluate_call) significantly reduces overhead per tool call.
**Action:** Avoid slow `inspect` module calls in high-frequency evaluation loops; prefer faster type and attribute checks.

## 2026-03-02 - Dispatch Table Anti-pattern for Simple Ops
**Learning:** Replacing an `if-elif` chain with a dictionary-based dispatch using `lambda` functions for simple binary operations (arithmetic) in Python is often a performance regression. The overhead of a Python function call (lambda) exceeds the cost of a few `isinstance` checks and an inline operation.
**Action:** Only use dispatch tables when the number of branches is large (>20-30) or when the work inside the branches is significant enough to dwarf the function call overhead.
