import time
import math
from smolagents.local_python_executor import evaluate_python_code, BASE_PYTHON_TOOLS

# Benchmark math.sqrt in a loop
code = """
import math
res = 0
for i in range(100000):
    res += math.sqrt(i)
"""

start = time.time()
evaluate_python_code(code, static_tools=BASE_PYTHON_TOOLS)
duration = time.time() - start
print(f"Duration for 100,000 iterations: {duration:.4f}s")
