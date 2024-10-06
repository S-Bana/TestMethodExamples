class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        """
        Adds two numbers.

        Args:
            x (int or float): The first number.
            y (int or float): The second number.

        Returns:
            int or float: The sum of x and y.
        """
        return self.x + self.y


    def sub(self):
        """
        Subtracts the second number from the first number.

        Args:
            x (int or float): The minuend.
            y (int or float): The subtrahend.

        Returns:
            int or float: The result of x minus y.
        """
        return self.x - self.y


    def mul(self):
        """
        Multiplies two numbers.

        Args:
            x (int or float): The first number.
            y (int or float): The second number.

        Returns:
            int or float: The product of x and y.
        """
        return self.x * self.y


    def div(self):
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
        if self.y == 0:
            raise ZeroDivisionError("Can't divide by Zero !!!")
        return self.x / self.y