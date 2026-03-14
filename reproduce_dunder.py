from smolagents.local_python_executor import evaluate_python_code

code = "__init__ = 1"
try:
    evaluate_python_code(code)
    print("Successfully assigned to __init__")
except Exception as e:
    print(f"Failed to assign to __init__: {e}")

code = "import os as __builtins__"
try:
    evaluate_python_code(code, authorized_imports=["os"])
    print("Successfully imported os as __builtins__")
except Exception as e:
    print(f"Failed to import os as __builtins__: {e}")

code = "from os import name as __init__"
try:
    evaluate_python_code(code, authorized_imports=["os"])
    print("Successfully imported name as __init__")
except Exception as e:
    print(f"Failed to import name as __init__: {e}")
