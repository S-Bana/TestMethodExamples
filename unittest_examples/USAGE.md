This is an instruction on how to use the math_operations module and run unit tests.

---

# Math Operations Module Usage

## Overview

The `math_operations` module provides basic arithmetic functions, including addition, subtraction, multiplication, and division. This module is designed to work with both integers and floating-point numbers.

## Functions

### 1. Addition: `add(x, y)`

Adds two numbers.

**Parameters:**
- `x` (int or float): The first number.
- `y` (int or float): The second number.

**Returns:** 
- int or float: The sum of `x` and `y`.

**Example:**
```python
result = add(3, 5)  # result will be 8
```

---

### 2. Subtraction: `sub(x, y)`

Subtracts the second number from the first number.

**Parameters:**
- `x` (int or float): The minuend.
- `y` (int or float): The subtrahend.

**Returns:** 
- int or float: The result of `x - y`.

**Example:**
```python
result = sub(10, 4)  # result will be 6
```

---

### 3. Multiplication: `mul(x, y)`

Multiplies two numbers.

**Parameters:**
- `x` (int or float): The first number.
- `y` (int or float): The second number.

**Returns:** 
- int or float: The product of `x` and `y`.

**Example:**
```python
result = mul(7, 6)  # result will be 42
```

---

### 4. Division: `div(x, y)`

Divides the first number by the second number.

**Parameters:**
- `x` (int or float): The numerator.
- `y` (int or float): The denominator.

**Returns:** 
- int or float: The result of `x / y`.

**Raises:** 
- `ZeroDivisionError`: If `y` is zero.

**Example:**
```python
result = div(20, 4)  # result will be 5.0
```

## Running Unit Tests

To ensure the correctness of the module, unit tests are provided using the `unittest` framework. Follow these steps to run the tests:

1. **Install Python (if not already installed)**:
   Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a test file**:
   Create a new file named `test_math_operations.py` in the same directory as your `math_operations.py`.

3. **Add the following code to your test file**:
   ```python
   import unittest
   from math_operations import add, sub, mul, div

   class TestMathOperations(unittest.TestCase):

       def test_add(self):
           self.assertEqual(add(1, 2), 3)
           self.assertEqual(add(-1, 1), 0)

       def test_sub(self):
           self.assertEqual(sub(5, 3), 2)
           self.assertEqual(sub(3, 5), -2)

       def test_mul(self):
           self.assertEqual(mul(3, 7), 21)
           self.assertEqual(mul(-1, 5), -5)

       def test_div(self):
           self.assertEqual(div(10, 2), 5)
           with self.assertRaises(ZeroDivisionError):
               div(10, 0)

   if __name__ == '__main__':
       unittest.main()
   ```

4. **Run the tests**:
   Open your terminal or command prompt and navigate to the directory containing your files. Run the following command:

   ```bash
   python -m unittest test_math_operations.py
   ```

5. **Check the output**:
   If all tests pass, you will see an output indicating success. If any tests fail, you will receive details about which tests did not pass.

## Conclusion

You can now use the functions in the `math_operations` module for basic arithmetic operations and verify their correctness using unit tests.


Feel free to customize this file further based on your specific requirements!