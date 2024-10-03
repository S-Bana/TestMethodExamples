# math_operations.py
import doctest


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
    doctest.testmod()