import pytest
from smolagents.local_python_executor import evaluate_python_code, BASE_PYTHON_TOOLS, InterpreterError

@pytest.fixture
def static_tools():
    return BASE_PYTHON_TOOLS.copy()

def test_protected_name_read(static_tools):
    code = "x = _operations_count['counter']"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=static_tools)
    assert "Forbidden access to protected name: _operations_count" in str(excinfo.value)

def test_protected_name_write(static_tools):
    code = "_operations_count = {'counter': 0}"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=static_tools)
    assert "Forbidden access to protected name: _operations_count" in str(excinfo.value)

def test_protected_name_delete(static_tools):
    code = "del _operations_count"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=static_tools)
    assert "Forbidden access to protected name: _operations_count" in str(excinfo.value)

def test_protected_name_import_as(static_tools):
    code = "import math as _operations_count"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=static_tools)
    assert "Forbidden access to protected name: _operations_count" in str(excinfo.value)

def test_dunder_import_as(static_tools):
    # Regression test for renamed dunder import
    code = "from math import __doc__ as safe_name"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=static_tools)
    assert "Forbidden access to protected name: __doc__" in str(excinfo.value)

def test_protected_function_definition(static_tools):
    code = "def _operations_count(): pass"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=static_tools)
    assert "Forbidden access to protected name: _operations_count" in str(excinfo.value)

def test_protected_class_definition(static_tools):
    code = "class _operations_count: pass"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=static_tools)
    assert "Forbidden access to protected name: _operations_count" in str(excinfo.value)

def test_allowed_dunder_methods(static_tools):
    # Ensure allowed dunder methods can still be defined in classes
    code = """
class MyClass:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return str(self.x)

obj = MyClass(10)
res = str(obj)
"""
    result, is_final = evaluate_python_code(code, static_tools=static_tools)
    assert result == "10"
