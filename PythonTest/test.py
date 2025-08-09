# test.py
# A small script to test your Python environment in Visual Studio Code.

import sys

print("✅ Python environment test starting...")

# Show Python version and executable path
print(f"Python version: {sys.version}")
print(f"Executable path: {sys.executable}\n")

# Test importing a common library
try:
    import numpy as np
    print("✅ Numpy is installed. Version:", np.__version__)
    print("Numpy test array:", np.array([1, 2, 3]))
except ImportError:
    print("⚠️ Numpy is not installed. You can install it with: pip install numpy")

# Simple function test
def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

result = add_numbers(5, 7)
print(f"\nFunction test: 5 + 7 = {result}")

# Interactive test
name = input("\nWhat's your name? ")
print(f"Hello, {name}! Your Python environment is ready to use in VS Code 🚀")
