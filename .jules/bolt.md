## 2026-03-02 - AST Interpreter Dispatch Table
**Learning:** Replacing a large if-elif chain (40+ branches) with a dictionary dispatch table for AST nodes significantly reduces lookup overhead in tight evaluation loops.
**Action:** Always prefer O(1) dispatch tables over O(N) chains for recursive evaluation logic.

## 2026-03-02 - Import Tree Caching
**Learning:** Redundant construction of the import authorization tree (splitting strings, building dicts) was a major bottleneck in every module/attribute access.
**Action:** Use lru_cache for authorization checks, ensuring arguments are converted to hashable types (tuples) when necessary.

## 2026-03-02 - Interpreter Loop De-decoration
**Learning:** In-lining security checks and eliminating high-frequency decorators (like @safer_eval) in the primary recursive interpreter loop (evaluate_ast) significantly reduces function call overhead.
**Action:** For performance-critical recursive functions, manual in-lining of validation logic is often more efficient than generic decorators.

## 2026-03-02 - Built-in Introspection Bottleneck
**Learning:** Using 'inspect.getmodule' and 'inspect.isbuiltin' in a hot execution path is prohibitively slow due to module resolution overhead.
**Action:** Replace expensive 'inspect' calls with direct attribute and type checks (e.g., func.__module__ == 'builtins') for 2-3x faster validation.
