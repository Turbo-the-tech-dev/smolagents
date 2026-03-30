from smolagents.local_python_executor import evaluate_python_code

def test_code(code, description):
    print(f"--- Testing: {description} ---")
    try:
        result, is_final_answer = evaluate_python_code(code, static_tools={"final_answer": lambda x: x})
        if hasattr(result, "__next__"):
            list(result)
        print(f"Success! Result: {result}")
    except Exception as e:
        print(f"Caught expected error: {e}")
    print()

test_code("__builtins__ = 1", "Direct assignment to dunder name")
test_code("import math as __builtins__", "Import as dunder name")
test_code("def func(__builtins__): pass", "Function argument as dunder name")
test_code("lambda __builtins__: None", "Lambda argument as dunder name")
test_code("def func(*__builtins__): pass", "Vararg as dunder name")
test_code("def func(**__builtins__): pass", "Kwarg as dunder name")
test_code("def func(*, __builtins__=1): pass", "Keyword-only argument as dunder name")
test_code("for __builtins__ in [1]: pass", "For loop target as dunder name")
test_code("[x for __builtins__ in [1]]", "List comprehension target as dunder name")
test_code("{__builtins__: 1 for __builtins__ in [1]}", "Dict comprehension target as dunder name")
test_code("{__builtins__ for __builtins__ in [1]}", "Set comprehension target as dunder name")
test_code("(x for __builtins__ in [1])", "Generator expression target as dunder name")

test_code("""
class CM:
    def __enter__(self): return self
    def __exit__(self, *args): pass
with CM() as __builtins__:
    pass
""", "With statement target as dunder name")

test_code("def __eq__(self, other): pass", "Defining whitelisted dunder function (allowed)")
test_code("def __forbidden__(self, other): pass", "Defining forbidden dunder function")
