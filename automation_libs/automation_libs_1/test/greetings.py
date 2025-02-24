class Greeting:
    """
    A class to represent a greeting message.
    """

    def __init__(self, name):
        """
        Initialize the Greeting class with a name.

        :param name: The name of the person to greet.
        """
        self.name = name

    def say_hello(self):
        """
        Prints a greeting message.
        """
        print(f"Hello, {self.name}! Welcome to the world of Python.")

# Example usage
if __name__ == "__main__":
    greeting = Greeting("hello there")
    greeting.say_hello()
