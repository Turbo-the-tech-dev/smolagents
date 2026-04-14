import unittest
from smolagents.local_python_executor import evaluate_python_code, BASE_PYTHON_TOOLS, InterpreterError

class TestProtectedNames(unittest.TestCase):
    def test_operations_count_protection(self):
        # Test read
        with self.assertRaises(InterpreterError) as cm:
            evaluate_python_code("print(_operations_count)", static_tools=BASE_PYTHON_TOOLS)
        self.assertIn("Forbidden access to internal variable: _operations_count", str(cm.exception))

        # Test write (direct assignment)
        with self.assertRaises(InterpreterError) as cm:
            evaluate_python_code("_operations_count = 0", static_tools=BASE_PYTHON_TOOLS)
        self.assertIn("Forbidden access to internal variable: _operations_count", str(cm.exception))

        # Test write (item assignment)
        with self.assertRaises(InterpreterError) as cm:
            evaluate_python_code("_operations_count['counter'] = 0", static_tools=BASE_PYTHON_TOOLS)
        self.assertIn("Forbidden access to internal variable: _operations_count", str(cm.exception))

        # Test delete
        with self.assertRaises(InterpreterError) as cm:
            evaluate_python_code("del _operations_count", static_tools=BASE_PYTHON_TOOLS)
        self.assertIn("Forbidden access to internal variable: _operations_count", str(cm.exception))

    def test_print_outputs_protection(self):
        # Test read
        with self.assertRaises(InterpreterError) as cm:
            evaluate_python_code("x = _print_outputs", static_tools=BASE_PYTHON_TOOLS)
        self.assertIn("Forbidden access to internal variable: _print_outputs", str(cm.exception))

        # Test write
        with self.assertRaises(InterpreterError) as cm:
            evaluate_python_code("_print_outputs = 'hack'", static_tools=BASE_PYTHON_TOOLS)
        self.assertIn("Forbidden access to internal variable: _print_outputs", str(cm.exception))

    def test_import_alias_protection(self):
        # Test import as
        with self.assertRaises(InterpreterError) as cm:
            evaluate_python_code("import math as _operations_count", static_tools=BASE_PYTHON_TOOLS, authorized_imports=["math"])
        self.assertIn("Forbidden access to internal variable: _operations_count", str(cm.exception))

        # Test from import as
        with self.assertRaises(InterpreterError) as cm:
            evaluate_python_code("from math import sqrt as _operations_count", static_tools=BASE_PYTHON_TOOLS, authorized_imports=["math"])
        self.assertIn("Forbidden access to internal variable: _operations_count", str(cm.exception))

    def test_function_name_protection(self):
        with self.assertRaises(InterpreterError) as cm:
            evaluate_python_code("def _operations_count(): pass", static_tools=BASE_PYTHON_TOOLS)
        self.assertIn("Forbidden access to internal variable: _operations_count", str(cm.exception))

    def test_class_name_protection(self):
        with self.assertRaises(InterpreterError) as cm:
            evaluate_python_code("class _operations_count: pass", static_tools=BASE_PYTHON_TOOLS)
        self.assertIn("Forbidden access to internal variable: _operations_count", str(cm.exception))
