"""simple interest program"""

def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculates the Simple Interest.

    :param principal: The principal amount (Initial investment or loan amount)
    :param rate: The annual interest rate (in percentage)
    :param time: The time period (in years)
    :return: The simple interest calculated using the formula (P * R * T) / 100
    """
    return (principal * rate * time) / 100


# Example usage
if __name__ == "__main__":
    principal_amount = 1000  # Initial amount
    annual_rate = 5  # 5% per annum
    time_period = 2  # 2 years

    interest = calculate_simple_interest(principal_amount, annual_rate, time_period)
    print(f"Simple Interest: {interest}")
