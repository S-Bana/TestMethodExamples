# Usage Manual for `math_operations.py`

This manual provides instructions on how to use the `math_operations.py` script, which contains basic mathematical operations and their corresponding doctests.

## Overview

The `math_operations.py` file includes two functions:

- `add(x, y)`: Adds two numbers together.
- `sub(x, y)`: Subtracts the second number from the first.

Both functions include doctests that verify their correctness through example inputs and expected outputs.

## Prerequisites

Ensure you have Python installed on your machine.
No need to install an external library.

## File Structure

Your directory should look like this:


# Testing Guide for `math_operations.py`

This guide provides a comprehensive manual for testing the `math_operations.py` file, which contains basic arithmetic operations using Python's built-in `doctest` module. The file includes two functions: `add` and `sub`, each equipped with embedded tests in their docstrings.

## File Structure

Ensure your project directory has the following structure:

```
project/
│
├── math_operations.py
└── README.md
```

## Contents of `math_operations.py`

```python
def add(x, y):
    '''
    Adds two numbers together.

    >>> add(4, 5)
    9
    >>> add(-1, 1)
    0
    >>> add(2.5, 2.5)
    5.0
    '''
    return x + y

def sub(x, y):
    '''
    Subtracts the second number from the first.

    >>> sub(6, 4)
    2
    >>> sub(10, 5)
    5
    >>> sub(0, 0)
    0
    '''
    return x - y

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

## How to Test

### Running Tests

1. **Open a terminal** and navigate to the directory containing `math_operations.py`.
2. **Execute the script** by running:

   ```bash
   python math_operations.py
   ```

3. **Check Output**: If all tests pass, you will see no output. If there are any failures, the output will indicate which tests failed and provide details about the expected versus actual results.

### Understanding Doctests

- The tests within the docstrings are examples of how the functions should behave.
- Each example is prefixed with `>>>`, followed by the function call and its expected output on a new line.
- For instance:

   ```python
   >>> add(4, 5)
   9
   ```

   This means calling `add(4, 5)` should return `9`.

### Adding More Tests

To expand your testing framework:

1. **Create a new file** named `test_math_operations.py` in the same directory.
2. **Use the following template** to include additional tests using `unittest`:

```python
import unittest
from math_operations import add, sub

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(2.5, 2.5), 5.0)

    def test_sub(self):
        self.assertEqual(sub(6, 4), 2)
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```

3. **Run your new test suite** by executing:

   ```bash
   python test_math_operations.py
   ```

## Conclusion

This manual provides a straightforward approach to testing your arithmetic functions in Python using both `doctest` and `unittest`. By following these steps, you can ensure that your code behaves as expected and is robust against changes in future development.
