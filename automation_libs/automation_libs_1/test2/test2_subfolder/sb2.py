class TemperatureConverter:
    """
    A class to convert temperature from Fahrenheit to Celsius.
    """

    def __init__(self, fahrenheit):
        """
        Initialize with temperature in Fahrenheit.

        :param fahrenheit: Temperature value in Fahrenheit.
        """
        self.fahrenheit = fahrenheit

    def to_celsius(self):
        """
        Convert the Fahrenheit temperature to Celsius.

        :return: Temperature in Celsius.
        """
        return (self.fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    try:
        fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
        converter = TemperatureConverter(fahrenheit_value)
        celsius_value = converter.to_celsius()
        print(f"{fahrenheit_value}°F is equal to {celsius_value:.2f}°C")
    except ValueError:
        print("Please enter a valid number.")
