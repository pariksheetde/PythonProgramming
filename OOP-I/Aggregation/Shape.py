import math

class Shape:
    """A class that represents a Shape."""

    def __init__(self, color):
        self.color = color

    
class Circle(Shape):
    """A class that represents a Crcle. Inherits from Shape.
    
    Methods:
        calculate_area(self):
            Returns math.pi with radius exponential 2
    """

    def __init__(self, color, radius):
        Shape.__init__(self, color)
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
my_circle = Circle("Purple", 12)
print(f"Color: {my_circle.color}")
print(f"Radius: {my_circle.radius}")

print()

print(f"Area of My Circle: {my_circle.calculate_area()}")
# print(my_circle.calculate_area.__doc__)