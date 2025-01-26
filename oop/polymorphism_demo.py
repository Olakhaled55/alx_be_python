import math

class Shape:
    def area(self):
        """Raises an error to indicate that this method should be overridden."""
        raise NotImplementedError("Subclasses should implement this method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle (length * width)."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle (π * radius^2)."""
        return math.pi * self.radius ** 2
