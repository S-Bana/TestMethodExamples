
Here’s a `usage.md` file that provides clear instructions and information about how to use the `Math` class and its associated unit tests.

# Usage Guide for Math Operations

## Overview

This document provides guidance on how to use the `Math` class and the associated unit tests implemented using Python's `unittest` framework. The `Math` class supports basic arithmetic operations: addition, subtraction, multiplication, and division.

## Math Class

### Initialization

To create an instance of the `Math` class, you need to provide two numbers as arguments:

```python
from math_operations_class import Math

# Example
math_instance = Math(5, 6)


### Methods

The `Math` class includes the following methods:

- **Addition (`add`)**
  
  ```python
  result = math_instance.add()
  ```

- **Subtraction (`sub`)**
  
  ```python
  result = math_instance.sub()
  ```

- **Multiplication (`mul`)**
  
  ```python
  result = math_instance.mul()
  ```

- **Division (`div`)**
  
  ```python
  result = math_instance.div()
  ```

### Example Usage

Here is an example of how to use the `Math` class:

```python
from math_operations_class import Math

# Create instances of Math
m1 = Math(5, 6)
m2 = Math(9, 3)

# Perform operations
print("Addition:", m1.add())         # Output: 11
print("Subtraction:", m1.sub())      # Output: -1
print("Multiplication:", m1.mul())   # Output: 30
print("Division:", round(m1.div(), 3)) # Output: 0.833
```

## Running Unit Tests

To ensure that the `Math` class works as expected, you can run the unit tests provided in the `TestMathOperations` class.

### Requirements

Make sure you have Python installed on your machine. You can run the tests using the built-in `unittest` framework.

### Running Tests

To run the tests, execute the following command in your terminal:

```bash
python3 -m unittest test_math_operations_class.py
# or
python3 -m unittest test_math_operations_class_setUp_tearDown.py
```

Replace `test_math_operations_class.py` with the name of your test file if it's different.

### Test Cases Included

The following operations are tested:

- **Addition**: Validates that the sum of two numbers is correct.
- **Subtraction**: Validates that the difference between two numbers is correct.
- **Multiplication**: Validates that the product of two numbers is correct.
- **Division**: Validates that the quotient of two numbers is correct and rounded to three decimal places.

## Conclusion

This guide provides a comprehensive overview of how to use the `Math` class and run its associated unit tests. For any further questions or issues, please refer to the documentation or reach out for support.

- Feel free to modify any sections according to your specific needs or additional features!


