import unittest
from smolagents.local_python_executor import LocalPythonExecutor, InterpreterError

class TestProtectedNames(unittest.TestCase):
    def setUp(self):
        self.executor = LocalPythonExecutor(additional_authorized_imports=[])
        self.executor.send_tools({})

    def test_internal_variable_access_blocked(self):
        with self.assertRaisesRegex(InterpreterError, "Forbidden access to internal variable: _operations_count"):
            self.executor("_operations_count['counter'] = 0")

    def test_internal_variable_read_blocked(self):
        with self.assertRaisesRegex(InterpreterError, "Forbidden access to internal variable: _operations_count"):
            self.executor("print(_operations_count)")

    def test_dunder_assignment_blocked(self):
        with self.assertRaisesRegex(InterpreterError, "Forbidden access to dunder name: __my_dunder__"):
            self.executor("__my_dunder__ = 'secret'")

    def test_dunder_import_blocked(self):
        with self.assertRaisesRegex(InterpreterError, "Forbidden access to dunder name: __math__"):
            self.executor("import math as __math__")

    def test_protected_function_blocked(self):
        with self.assertRaisesRegex(InterpreterError, "Forbidden access to internal variable: _print_outputs"):
            self.executor("def _print_outputs(): pass")

    def test_protected_class_blocked(self):
        with self.assertRaisesRegex(InterpreterError, "Forbidden access to internal variable: _print_outputs"):
            self.executor("class _print_outputs: pass")

    def test_protected_deletion_blocked(self):
        with self.assertRaisesRegex(InterpreterError, "Forbidden access to internal variable: _operations_count"):
            self.executor("del _operations_count")

    def test_allowed_dunder_methods_allowed(self):
        # __init__ is allowed
        code = """
class MyClass:
    def __init__(self, x):
        self.x = x
obj = MyClass(10)
final_answer(obj.x)
"""
        # We need final_answer tool
        self.executor.send_tools({"final_answer": lambda x: x})
        result = self.executor(code)
        self.assertEqual(result.output, 10)

if __name__ == "__main__":
    unittest.main()
