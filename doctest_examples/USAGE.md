
# Testing Guide for `math_operations.py`

This guide provides a comprehensive manual for testing the `math_operations.py` file, which contains basic arithmetic operations using Python's built-in `doctest` module. The file includes two functions: `add` and `sub`, each equipped with embedded tests in their docstrings.

## Overview

The `math_operations.py` file includes four functions:

- `add(x, y)`: Adds two numbers together.
- `sub(x, y)`: Subtracts the second number from the first.
- `mul(x, y)`: Multiplies two numbers.
- `div(x, y)`: Divides the first number by the second number.

Each one of functions include doctests that verify their correctness through example inputs and expected outputs.

## Prerequisites

Ensure you have Python installed on your machine.
No need to install an external library.

## File Structure

Ensure your project directory has the following structure:

```
project/
│
├── math_operations.py
└── USAGE.md
```

## How to Test

### Running Tests

1. **Open a terminal** and navigate to the directory containing `math_operations.py`.
2. **Execute the script** by running:

   ```bash
   python3 math_operations.py
   # or
   python3 -m doctest -v math_operations.py
   ```

3. **Check Output**: If all tests pass, you will see no output. If there are any failures, the output will indicate which tests failed and provide details about the expected versus actual results. or :
    ```bash
    Trying:
        add(2, 3)
    Expecting:
        5
    ok
    Trying:
        add(-1, 5)
    Expecting:
        4
    ok
    Trying:
        add(0, 10)
    Expecting:
        10
    ok
    Trying:
        add(2.5, 4)
    Expecting:
        6.5
    ok
    Trying:
        div(6, 3)
    Expecting:
        2.0
    ok
    Trying:
        div(5, 2)
    Expecting:
        2.5
    ok
    Trying:
        div(-10, 2)
    Expecting:
        -5.0
    ok
    Trying:
        div(7, 0)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Expecting:
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero
    ok
    Trying:
        mul(2, 3)
    Expecting:
        6
    ok
    Trying:
        mul(-1, 5)
    Expecting:
        -5
    ok
    Trying:
        mul(0, 10)
    Expecting:
        0
    ok
    Trying:
        mul(2.5, 4)
    Expecting:
        10.0
    ok
    Trying:
        sub(5, 3)
    Expecting:
        2
    ok
    Trying:
        sub(10, 15)
    Expecting:
        -5
    ok
    Trying:
        sub(0, 10)
    Expecting:
        -10
    ok
    Trying:
        sub(7.5, 2.5)
    Expecting:
        5.0
    ok
    1 items had no tests:
        math_operations
    4 items passed all tests:
    4 tests in math_operations.add
    4 tests in math_operations.div
    4 tests in math_operations.mul
    4 tests in math_operations.sub
    16 tests in 5 items.
    16 passed and 0 failed.
    Test passed.
    ```

### Understanding Doctests

- The tests within the docstrings are examples of how the functions should behave.
- Each example is prefixed with `>>>`, followed by the function call and its expected output on a new line.
- For instance:

   ```python
   >>> add(4, 5)
   9
   ```

   This means calling `add(4, 5)` should return `9`.

## Conclusion

This manual provides a straightforward approach to testing your arithmetic functions in Python using both `doctest`. By following these steps, you can ensure that your code behaves as expected and is robust against changes in future development.
