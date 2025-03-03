class CompoundInterestCalculator:
    """
    A class to calculate compound interest.

    Attributes:
        principal (float): The initial amount of money.
        rate (float): The annual interest rate (in percentage).
        time (float): The time in years.
        n (int): Number of times interest is compounded per year.
    """

    def __init__(self, principal, rate, time, n):
        """
        Initializes the CompoundInterestCalculator with the provided values.

        Args:
            principal (float): The initial amount of money.
            rate (float): The annual interest rate (in percentage).
            time (float): The time in years.
            n (int): Number of times interest is compounded per year.
        """
        self.principal = principal
        self.rate = rate
        self.time = time
        self.n = n

    def calculate(self):
        """
        Calculates the compound interest and final amount.

        Returns:
            tuple: Compound interest and total amount.
        """
        amount = self.principal * (1 + (self.rate / (100 * self.n))) ** (self.n * self.time)
        compound_interest = amount - self.principal
        return compound_interest, amount


# Example usage:
if __name__ == "__main__":
    principal = 10000  # Initial investment
    rate = 5           # Interest rate in %
    time = 3           # Time period in years
    n = 4              # Compounded quarterly

    calculator = CompoundInterestCalculator(principal, rate, time, n)
    ci, total = calculator.calculate()

    print(f"Compound Interest: ₹{ci:.2f}")
    print(f"Total Amount: ₹{total:.2f}")
