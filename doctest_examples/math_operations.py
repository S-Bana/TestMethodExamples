# math_operations.py
import doctest


def add(x, y):
    """
    Adds two numbers.

    Args:
        x (int or float): The first number.
        y (int or float): The second number.

    Returns:
        int or float: The sum of x and y.

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 5)
        4
        >>> add(0, 10)
        10
        >>> add(2.5, 4)
        6.5
    """
    return x + y


def sub(x, y):
    """
    Subtracts the second number from the first number.

    Args:
        x (int or float): The minuend.
        y (int or float): The subtrahend.

    Returns:
        int or float: The result of x minus y.

    Examples:
        >>> sub(5, 3)
        2
        >>> sub(10, 15)
        -5
        >>> sub(0, 10)
        -10
        >>> sub(7.5, 2.5)
        5.0
    """
    return x - y



def mul(x, y):
    """
    Multiplies two numbers.

    Args:
        x (int or float): The first number.
        y (int or float): The second number.

    Returns:
        int or float: The product of x and y.

    Examples:
        >>> mul(2, 3)
        6
        >>> mul(-1, 5)
        -5
        >>> mul(0, 10)
        0
        >>> mul(2.5, 4)
        10.0
    """
    return x * y

def div(x, y):
    """
    Divides the first number by the second number.

    Args:
        x (int or float): The numerator.
        y (int or float): The denominator.

    Returns:
        int or float: The result of x divided by y.

    Raises:
        ZeroDivisionError: If y is zero.

    Examples:
        >>> div(6, 3)
        2.0
        >>> div(5, 2)
        2.5
        >>> div(-10, 2)
        -5.0
        >>> div(7, 0)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero
    """
    return x / y


if __name__ == "__main__":
    doctest.testmod()