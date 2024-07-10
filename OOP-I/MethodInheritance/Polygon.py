class Polygon:
    
    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color

    def describe_polygon(self):
        print(f"This polygon has {self.num_sides} sides and it's {self.color}")


class Triangle(Polygon):

    NUM_SIDES = 3

    def __init__(self, base, height, color):
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        self.base = base
        self.height = height

    def calculate_area(self):
        return (self.base * self.height) / 2

class Square(Polygon):

    NUM_SIDES = 4

    def __init__(self, num_sides, color, side_length):
        super().__init__(Square.NUM_SIDES, color)
        self.side_length = side_length

    def calculate_area(self):
        return (self.side_length ** 2)

print("Let's display the properties of Triangle")
triangle = Triangle(4, 6, 'White')
print(f'Base: {triangle.base}')
print(f'Height: {triangle.height}')
print(f'Color: {triangle.color}')
print(triangle.describe_polygon())
print(f'Area of Triangle: {triangle.calculate_area()}')

print()

print("Let's display the properties of Square")
square = Square(4,'Purple', 7)
print(f'Sides: {square.num_sides}')
print(f'Color: {square.color}')
print(f'Side Length: {square.side_length}')
print(square.describe_polygon())
print(f'Area of Square: {square.calculate_area()}')

print()