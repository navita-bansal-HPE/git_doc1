class Rectangle:
    """
    A class to represent a rectangle.
    """

    def __init__(self, length, width):
        """
        Initializes the Rectangle with length and width.

        :param length: float, the length of the rectangle
        :param width: float, the width of the rectangle
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        :return: float, the area of the rectangle
        """
        return self.length * self.width

    def display(self):
        """
        Prints the details of the rectangle including its length, width, and area.
        """
        print(f"Rectangle with length {self.length} and width {self.width} has an area of {self.area()}.")


# Example usage
if __name__ == "__main__":
    rect = Rectangle(5, 3)
    rect.display()
