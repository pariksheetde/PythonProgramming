class Circle:
    
    VALID_COLORS = ["Red", "Lavender", "Magenta", "Pink"]

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        """This method acts as getter, is used to get the value of the object"""
        return self._radius
    
    def set_radius(self, new_radius):
        """This method acts as setter, is used to modify the value of the object"""
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Invalid Radius.....")

    def get_color(self):
        """This method is used to get the value of the color attribute"""
        return self._color
    
    def set_color(self, new_color):
        """This method is used to modify the value of the color attribute. If the color being modified is not obtained from
        list of available colors, will throw error
        """
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            for available_color in Circle.VALID_COLORS:
                print(f"Invalid Color. Available color option: {available_color}")
    
    radius = property(get_radius, set_radius)
    color = property(get_color, set_color)
    
my_circle = Circle(7, 'Blue')
print(f'Before Change: Radius of My Circle {my_circle.radius} and color is {my_circle.color}')

print()
print("Let's modify the radius and color of My Circle")

my_circle.set_radius(10)
my_circle.set_color("Lavender")
print(f'After Change: Radius of My Circle {my_circle.radius} and color is {my_circle.color}')

print()
