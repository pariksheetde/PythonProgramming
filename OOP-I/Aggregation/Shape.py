import math

class Shape:

    def __init__(self, color):
        self.color = color

    
class Circle(Shape):

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