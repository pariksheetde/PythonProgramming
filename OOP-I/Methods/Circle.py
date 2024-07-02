class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_diameter(self):
        return self.radius * 2
    
my_circle = Circle(5)
print(f'Diameter of My_Circle: {my_circle.calculate_diameter()}')

print()

