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



if __name__ == "__main__":
    doctest.testmod()