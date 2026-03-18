import pytest
from smolagents.local_python_executor import LocalPythonExecutor, InterpreterError

def test_dunder_assignment():
    executor = LocalPythonExecutor(additional_authorized_imports=[])
    with pytest.raises(InterpreterError) as excinfo:
        executor("__builtins__ = 1")
    assert "Forbidden assignment to dunder name: __builtins__" in str(excinfo.value)

def test_dunder_access():
    executor = LocalPythonExecutor(additional_authorized_imports=[])
    # __name__ should be allowed
    result = executor("__name__")
    assert result.output == "__main__"

    # Others should be blocked if they exist in state (though they shouldn't anymore)
    executor.state["__bad__"] = 42
    with pytest.raises(InterpreterError) as excinfo:
        executor("__bad__")
    assert "Forbidden access to dunder name in state: __bad__" in str(excinfo.value)

def test_dunder_function_def():
    executor = LocalPythonExecutor(additional_authorized_imports=[])
    with pytest.raises(InterpreterError) as excinfo:
        executor("def __bad_func__(): pass")
    assert "Forbidden definition of dunder function: __bad_func__" in str(excinfo.value)

    # ALLOWED_DUNDER_METHODS should be allowed
    executor("class A:\n    def __init__(self): self.x = 1")
    result = executor("a = A(); a.x")
    assert result.output == 1

def test_dunder_class_def():
    executor = LocalPythonExecutor(additional_authorized_imports=[])
    with pytest.raises(InterpreterError) as excinfo:
        executor("class __BadClass__: pass")
    assert "Forbidden definition of dunder class: __BadClass__" in str(excinfo.value)

def test_dunder_import_alias():
    executor = LocalPythonExecutor(additional_authorized_imports=["math"])
    with pytest.raises(InterpreterError) as excinfo:
        executor("import math as __math__")
    assert "Forbidden import of dunder name: __math__" in str(excinfo.value)

def test_dunder_from_import():
    executor = LocalPythonExecutor(additional_authorized_imports=["math"])
    with pytest.raises(InterpreterError) as excinfo:
        executor("from math import sqrt as __sqrt__")
    assert "Forbidden import of dunder name: __sqrt__" in str(excinfo.value)

def test_dunder_argument_names():
    executor = LocalPythonExecutor(additional_authorized_imports=[])
    with pytest.raises(InterpreterError) as excinfo:
        executor("def func(__arg__): pass")
    assert "Forbidden dunder name in function arguments: __arg__" in str(excinfo.value)

    with pytest.raises(InterpreterError) as excinfo:
        executor("def func(*__args__): pass")
    assert "Forbidden dunder name in function arguments: __args__" in str(excinfo.value)

    with pytest.raises(InterpreterError) as excinfo:
        executor("def func(**__kwargs__): pass")
    assert "Forbidden dunder name in function arguments: __kwargs__" in str(excinfo.value)

def test_dunder_lambda_arguments():
    executor = LocalPythonExecutor(additional_authorized_imports=[])
    with pytest.raises(InterpreterError) as excinfo:
        executor("lambda __x__: __x__")
    assert "Forbidden dunder name in lambda arguments: __x__" in str(excinfo.value)

def test_dunder_exception_variable():
    executor = LocalPythonExecutor(additional_authorized_imports=[])
    with pytest.raises(InterpreterError) as excinfo:
        executor("try: raise Exception()\nexcept Exception as __e__: pass")
    assert "Forbidden assignment to dunder name: __e__" in str(excinfo.value)

def test_dunder_with_variable():
    from smolagents.local_python_executor import BASE_PYTHON_TOOLS
    executor = LocalPythonExecutor(additional_authorized_imports=["contextlib"])
    executor.send_tools({}) # Initialize static_tools
    # Need a context manager.
    # Use a simple class instead of @contextlib.contextmanager because yield is not supported
    code = """
class Manager:
    def __enter__(self):
        return 1
    def __exit__(self, *args):
        pass

with Manager() as __m__:
    pass
"""
    with pytest.raises(InterpreterError) as excinfo:
        executor(code)
    assert "Forbidden assignment to dunder name: __m__" in str(excinfo.value)

def test_dunder_for_loop_variable():
    from smolagents.local_python_executor import BASE_PYTHON_TOOLS
    executor = LocalPythonExecutor(additional_authorized_imports=[])
    executor.send_tools({}) # Initialize static_tools to have range
    with pytest.raises(InterpreterError) as excinfo:
        executor("for __i__ in range(10): pass")
    assert "Forbidden assignment to dunder name: __i__" in str(excinfo.value)

def test_dunder_comprehension_variable():
    from smolagents.local_python_executor import BASE_PYTHON_TOOLS
    executor = LocalPythonExecutor(additional_authorized_imports=[])
    executor.send_tools({}) # Initialize static_tools to have range
    with pytest.raises(InterpreterError) as excinfo:
        executor("[__x__ for __x__ in range(10)]")
    assert "Forbidden assignment to dunder name: __x__" in str(excinfo.value)

def test_star_import_dunder_filter():
    # math doesn't have dunders in __all__, but let's mock it if possible or use a module that does.
    # Actually, star import from a module should filter dunders.
    executor = LocalPythonExecutor(additional_authorized_imports=["math"])
    executor("from math import *")
    # math.__name__ should not be imported into state
    # Actually, executor.state already has "__name__": "__main__"
    # Let's try to access something like __doc__ from math if it was imported
    import math
    if hasattr(math, "__doc__"):
        with pytest.raises(InterpreterError) as excinfo:
            executor("__doc__")
        assert "The variable `__doc__` is not defined." in str(excinfo.value)
