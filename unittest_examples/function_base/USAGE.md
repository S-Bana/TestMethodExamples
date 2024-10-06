### This is an instruction on how to use the math_operations module and run unittests.

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
   Ensure you have Python installed on your system.

2. **test file**:
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

3. **Run the tests**:
   Open your terminal or command prompt and navigate to the directory containing your files. Run the following command:

   ```bash
   python3 -m unittest test_math_operations.py
   # or
   python3 -m unittest -v test_math_operations.py
   ```

4. **Check the output**:
   If all tests pass, you will see an output indicating success. If any tests fail, you will receive details about which tests did not pass.
   
   ====================================================================================
    test_add (unittest_examples.test_math_operations.TestMathOperations) ... ok
    test_div (unittest_examples.test_math_operations.TestMathOperations) ... ok
    test_mul (unittest_examples.test_math_operations.TestMathOperations) ... ok
    test_sub (unittest_examples.test_math_operations.TestMathOperations) ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 0.000s

    OK

## Conclusion

You can now use the functions in the `math_operations` module for basic arithmetic operations and verify their correctness using unit tests.


Feel free to customize this file further based on your specific requirements!

## Here’s a comprehensive list of methods available in the `unittest` module, specifically focusing on the assertion methods provided by the `TestCase` class:

| Method                           | Description                                      |
|----------------------------------|--------------------------------------------------|
| `assertEqual(a, b)`             | Checks if `a` is equal to `b`.                  |
| `assertNotEqual(a, b)`          | Checks if `a` is not equal to `b`.              |
| `assertTrue(x)`                 | Checks if `x` is `True`.                        |
| `assertFalse(x)`                | Checks if `x` is `False`.                       |
| `assertIs(a, b)`                | Checks if `a` is `b`.                           |
| `assertIsNot(a, b)`             | Checks if `a` is not `b`.                       |
| `assertIsNone(x)`               | Checks if `x` is `None`.                        |
| `assertIsNotNone(x)`            | Checks if `x` is not `None`.                    |
| `assertIn(a, b)`                | Checks if `a` is in container `b`.              |
| `assertNotIn(a, b)`             | Checks if `a` is not in container `b`.          |
| `assertIsInstance(a, b)`        | Checks if `a` is an instance of class/type `b`. |
| `assertNotIsInstance(a, b)`     | Checks if `a` is not an instance of class/type `b`.|
| `assertRaises(exc, func, *args, **kwargs)` | Checks that an exception is raised.  |
| `assertAlmostEqual(a, b, places=7)` | Checks that two values are almost equal.  |
| `assertNotAlmostEqual(a, b, places=7)` | Checks that two values are not almost equal.|
| `assertGreater(a, b)`           | Checks that `a` is greater than `b`.            |
| `assertGreaterEqual(a, b)`      | Checks that `a` is greater than or equal to `b`.|
| `assertLess(a, b)`              | Checks that `a` is less than `b`.               |
| `assertLessEqual(a, b)`         | Checks that `a` is less than or equal to `b`.   |
| `assertRegex(text, regex)`      | Checks that the regex matches the text.         |
| `assertNotRegex(text, regex)`   | Checks that the regex does not match the text.  |
| `assertCountEqual(a, b)`        | Checks that two sequences have the same elements in any order.|
| `assertDictEqual(d1, d2)`       | Checks that two dictionaries are equal.          |
| `assertListEqual(l1, l2)`       | Checks that two lists are equal.                 |
| `assertTupleEqual(t1, t2)`      | Checks that two tuples are equal.                |
| `assertSetEqual(s1, s2)`        | Checks that two sets are equal.                  |

### Additional Notes:
- The methods prefixed with "assert" are used to verify expected outcomes in your tests.
- You can also use setup and teardown methods like:
  - **setUp()**: Called before every test method.
  - **tearDown()**: Called after every test method.


