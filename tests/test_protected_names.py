import pytest
from smolagents.local_python_executor import evaluate_python_code, InterpreterError, BASE_PYTHON_TOOLS

def test_access_operations_count():
    code = "x = _operations_count"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS)
    assert "Forbidden access to internal state variable: _operations_count" in str(excinfo.value)

def test_assign_print_outputs():
    code = "_print_outputs = 1"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS)
    assert "Forbidden access to internal state variable: _print_outputs" in str(excinfo.value)

def test_delete_operations_count():
    code = "del _operations_count"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS)
    assert "Forbidden access to internal state variable: _operations_count" in str(excinfo.value)

def test_import_as_protected():
    code = "import math as _operations_count"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS, authorized_imports=["math"])
    assert "Forbidden access to internal state variable: _operations_count" in str(excinfo.value)

def test_try_except_as_protected():
    code = """
try:
    raise ValueError("test")
except ValueError as _print_outputs:
    pass
"""
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS)
    assert "Forbidden access to internal state variable: _print_outputs" in str(excinfo.value)

def test_with_as_protected():
    code = """
class MockContext:
    def __enter__(self): return self
    def __exit__(self, *args): pass

# Need to use a tool that returns the context manager to avoid 'A' not defined error
# but simpler is to use a lambda
mock_ctx = MockContext()
with mock_ctx as _operations_count:
    pass
"""
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS)
    assert "Forbidden access to internal state variable: _operations_count" in str(excinfo.value)

def test_define_function_protected():
    code = "def _operations_count(): pass"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS)
    assert "Forbidden access to internal state variable: _operations_count" in str(excinfo.value)

def test_define_class_protected():
    code = "class _operations_count: pass"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS)
    assert "Forbidden access to internal state variable: _operations_count" in str(excinfo.value)

def test_forbidden_dunder():
    code = "x = __forbidden__"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS)
    assert "Forbidden access to dunder attribute: __forbidden__" in str(excinfo.value)

def test_allowed_dunder():
    # Should not raise for allowed dunders
    # Use a builtin type to avoid class definition issues in this test
    code = "x = str(1).__str__()"
    evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS)

def test_call_protected_name():
    code = "_operations_count()"
    with pytest.raises(InterpreterError) as excinfo:
        evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS)
    assert "Forbidden access to internal state variable: _operations_count" in str(excinfo.value)
