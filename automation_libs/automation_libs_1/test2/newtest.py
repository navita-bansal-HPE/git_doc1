class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    def __init__(self, a, b):
        """
        Initializes the calculator with two numbers.

        :param a: First number
        :param b: Second number
        """
        self.a = a
        self.b = b

    def add(self):
        """
        Returns the sum of two numbers.
        """
        return self.a + self.b

    def multiply(self):
        """
        Returns the product of two numbers.
        """
        return self.a * self.b

# Example usage
if __name__ == "__main__":
    calc = Calculator(5, 3)
    print(f"Addition: {calc.add()}")
    print(f"Multiplication: {calc.multiply()}")
