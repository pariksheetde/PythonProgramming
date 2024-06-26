class Telsa:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

mx = Telsa(10, "Black")
print(f'Current Model MX: {mx.radius} & {mx.color}')

mx.color = "White"
print(f'Current Model MX: {mx.radius} & {mx.color}')

print()