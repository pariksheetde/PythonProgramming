class Polygon:

    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color

class Triangle(Polygon):

    NUM_SIDES = 3
    
    def __init__(self, base, height, color):
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        self.base = base
        self.height = height


class Square(Polygon):
    pass

mt = Triangle(5, 4, "White")

print()
print("Triangle has inherited below properties from Polygon")
print(f'Sides: {mt.num_sides}')
print(f'Color: {mt.color}')

print()

print(f'Base: {mt.base}')
print(f'Height: {mt.height}')