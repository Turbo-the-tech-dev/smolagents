from smolagents.local_python_executor import evaluate_python_code

def test_code(code, description, authorized_imports=None):
    try:
        evaluate_python_code(code, authorized_imports=authorized_imports)
        print(f"✅ {description}: Successfully (Unexpectedly) executed")
    except Exception as e:
        print(f"❌ {description}: Correctly failed with: {e}")

print("Testing dunder name protections...")

test_code("def __init__(self): pass", "Define __init__ function (allowed)")
test_code("def __forbidden__(): pass", "Define __forbidden__ function")
test_code("class __Forbidden__: pass", "Define __Forbidden__ class")
test_code("try:\n    raise Exception()\nexcept Exception as __e__: pass", "Exception handler with dunder name")
test_code("with open('README.md') as __f__: pass", "With statement with dunder name")
test_code("[x for __x__ in [1, 2]]", "List comprehension with dunder name")
test_code("lambda __x__: __x__", "Lambda with dunder name")
test_code("def func(__x__): pass", "Function with dunder argument")
test_code("import os as __os__", "Import with dunder alias", authorized_imports=["os"])
test_code("from os import name as __name__", "Import from with dunder alias", authorized_imports=["os"])
