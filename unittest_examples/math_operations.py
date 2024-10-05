# math_operations.py

def add(x, y):
    """
    Adds two numbers.

    Args:
        x (int or float): The first number.
        y (int or float): The second number.

    Returns:
        int or float: The sum of x and y.
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
    """
    return x / y
