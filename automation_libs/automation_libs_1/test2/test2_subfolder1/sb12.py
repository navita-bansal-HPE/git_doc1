class Cuboid:
    """
    A class to represent a cuboid and calculate its volume.
    """

    def __init__(self, length, width, height):
        """
        Initialize the Cuboid with length, width, and height.

        :param length: Length of the cuboid.
        :param width: Width of the cuboid.
        :param height: Height of the cuboid.
        """
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        """
        Calculate the volume of the cuboid.

        :return: The volume of the cuboid.
        """
        return self.length * self.width * self.height


if __name__ == "__main__":
    # Example usage
    length = float(input("Enter the length of the cuboid: "))
    width = float(input("Enter the width of the cuboid: "))
    height = float(input("Enter the height of the cuboid: "))

    cuboid = Cuboid(length, width, height)
    print(f"The volume of the cuboid is: {cuboid.volume()} cubic units.")
