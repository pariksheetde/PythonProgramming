class Circle:
    def __init__(self, radius, color = "Blue"):
        self.radius = radius
        self.color = color

my_circle = Circle(10)
print(f'Radius of my circle: {my_circle.radius} and initial color was {my_circle.color}')

print()

print(f'Changing Color')
my_circle.color = 'Magenta'
print(f'New color of the My Circle: {my_circle.color} and radius: {my_circle.radius}')

print()

wife_circle = Circle(15)
wife_circle.color = "Purple"
print(f'New color of the My Circle belonging to my wife: {wife_circle.color} and radius: {wife_circle.radius}')

print()