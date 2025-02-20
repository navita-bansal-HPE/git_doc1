"""To print the message"""

class Printer:
    """
    A simple class to print a message.
    """

    def __init__(self, message):
        """
        Initializes the Printer class with a message.

        :param message: str, the message to be printed
        """
        self.message = message

    def display(self):
        """
        Prints the stored message.
        """
        print(self.message)


# Example usage
if __name__ == "__main__":
    printer = Printer("Hello, this is a Python class with docstrings!")
    printer.display()
