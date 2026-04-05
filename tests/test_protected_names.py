import pytest

from smolagents.local_python_executor import BASE_PYTHON_TOOLS, InterpreterError, evaluate_python_code


def test_protected_names_access():
    # Test access to _operations_count
    with pytest.raises(InterpreterError) as e:
        evaluate_python_code("x = _operations_count")
    assert "Forbidden access to internal variable: _operations_count" in str(e.value)

    # Test access to _print_outputs
    with pytest.raises(InterpreterError) as e:
        evaluate_python_code("x = _print_outputs")
    assert "Forbidden access to internal variable: _print_outputs" in str(e.value)


def test_protected_names_assignment():
    # Test assignment to _operations_count
    with pytest.raises(InterpreterError) as e:
        evaluate_python_code("_operations_count = 1")
    assert "Forbidden access to internal variable: _operations_count" in str(e.value)

    # Test assignment to _print_outputs
    with pytest.raises(InterpreterError) as e:
        evaluate_python_code("_print_outputs = 1")
    assert "Forbidden access to internal variable: _print_outputs" in str(e.value)


def test_protected_names_import():
    # Test import as protected name
    with pytest.raises(InterpreterError) as e:
        evaluate_python_code("import math as _operations_count")
    assert "Forbidden access to internal variable: _operations_count" in str(e.value)

    # Test from import as protected name
    with pytest.raises(InterpreterError) as e:
        evaluate_python_code("from math import sqrt as _print_outputs")
    assert "Forbidden access to internal variable: _print_outputs" in str(e.value)


def test_protected_names_exception():
    # Test except as protected name
    code = """
try:
    1/0
except Exception as _operations_count:
    pass
"""
    with pytest.raises(InterpreterError) as e:
        evaluate_python_code(code)
    assert "Forbidden access to internal variable: _operations_count" in str(e.value)


def test_protected_names_with():
    # Test with as protected name
    code = """
class SimpleContext:
    def __enter__(self): return self
    def __exit__(self, *args): pass

with SimpleContext() as _print_outputs:
    pass
"""
    with pytest.raises(InterpreterError) as e:
        evaluate_python_code(code)
    assert "Forbidden access to internal variable: _print_outputs" in str(e.value)


def test_allowed_dunder_names():
    # Test access to __name__ and __class__ as names
    code = """
class A:
    def get_class(self):
        return __class__
x = A()
name = __name__
cls = x.get_class()
result = name
"""
    result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={"__name__": "__main__"})
    assert result == "__main__"


def test_forbidden_dunder_attributes():
    # Test that dunder attributes are still forbidden
    with pytest.raises(InterpreterError) as e:
        evaluate_python_code("x = ().__class__")
    assert "Forbidden access to dunder attribute: __class__" in str(e.value)

    with pytest.raises(InterpreterError) as e:
        evaluate_python_code("class A: pass\nx = A().__doc__")
    assert "Forbidden access to dunder attribute: __doc__" in str(e.value)


if __name__ == "__main__":
    pytest.main([__file__])
