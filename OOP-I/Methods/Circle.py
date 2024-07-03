class Circle:

    PI = 3.1416

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def calculate_diameter(self):
        return self.radius * 2
    
    def find_area(self):
        return (self.radius ** 2) * Circle.PI
    
my_circle = Circle(5, "Red")
print(f'Diameter of My Circle: {my_circle.calculate_diameter()}')

print()

blue_circle = Circle(15, "Blue")
area = blue_circle.find_area()
print(f'Area of Blue Circle: {area}')