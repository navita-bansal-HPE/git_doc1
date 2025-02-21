class Greeting:
    """
    A class to generate a greeting message.
    """

    def __init__(self, name):
        """
        Initializes the Greeting class with a name.

        :param name: str, the name of the person to greet
        """
        self.name = name

    def say_hello(self):
        """
        Prints a greeting message with the given name.
        """
        print(f"Hello, {self.name}! Welcome to Python programming.")

# Example usage
if __name__ == "__main__":
    user = Greeting("Navita")
    user.say_hello()
