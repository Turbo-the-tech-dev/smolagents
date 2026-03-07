import sys
import os
sys.path.append(os.path.join(os.getcwd(), "src"))

from smolagents.local_python_executor import evaluate_python_code, BASE_PYTHON_TOOLS

def test_code(code, authorized_imports=None):
    print(f"--- Testing code ---\n{code.strip()}")
    try:
        state = {}
        result, is_final = evaluate_python_code(
            code,
            state=state,
            static_tools=BASE_PYTHON_TOOLS,
            authorized_imports=authorized_imports or []
        )
        print(f"Result: {result}")
        print(f"Logs: {state.get('_print_outputs', '')}")
        print(f"State keys: {[k for k in state.keys() if not k.startswith('_')]}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 20)

# 1. Dunder variable assignment
test_code("__my_dunder__ = 42")

# 2. Dunder import alias
test_code("import math as __math__", authorized_imports=['math'])

# 3. Dunder function name
test_code("def __my_func__(): pass")

# 4. Dunder class name
test_code("class __MyClass__: pass")

# 5. Dunder deletion
test_code("del __builtins__")

# 6. Allowed dunder method in class
test_code("""
class MyClass:
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return f"MyClass({self.val})"
print(str(MyClass(10)))
""")

# 7. Dunder in try/except
test_code("""
try:
    raise ValueError("test")
except ValueError as __err__:
    print(__err__)
""")

# 8. Dunder in with
test_code("""
class MyContext:
    def __enter__(self): return self
    def __exit__(self, *args): pass

with MyContext() as __ctx__:
    print("inside")
""")

# 9. Star import filtering
test_code("from math import *", authorized_imports=['math'])
