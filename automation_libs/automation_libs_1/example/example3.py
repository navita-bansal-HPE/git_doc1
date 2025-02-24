"""Calculate add sub div mul"""

class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations:
    addition, subtraction, multiplication, and division.
    """

    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Returns the difference of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Returns the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """Returns the quotient of two numbers. Raises ValueError if divisor is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("Addition:", calc.add(10, 5))
    print("Subtraction:", calc.subtract(10, 5))
    print("Multiplication:", calc.multiply(10, 5))
    print("Division:", calc.divide(10, 5))
