class Rectangle:

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def get_length(self):
        return self._length
    
    def set_length(self, new_lenght):
        if isinstance(new_lenght, int) and new_lenght > 0:
            self._length = new_lenght

    def get_width(self):
        return self._width
    
    def set_width(self, new_width):
        if isinstance(new_width, int) and new_width > 0:
            self._width = new_width
        else:
            print("Age should be greater than 0")

    length = property(get_length, set_length)
    width = property(get_width, set_width)

# create a new instance, xmas
xmas = Rectangle(10, 11)
print(f'Original Length & Width: {xmas.get_length()}, {xmas.get_width()}')
xmas.set_length(12)
xmas.set_width(6)
print(f'Updated Length & Width: {xmas.get_length()}, {xmas.get_width()}')

print()

# create a new instance, ymas
ymas = Rectangle(5, 7)
print(f'Original Length & Width: {ymas.length}, {ymas.width}')
ymas.length = 9
ymas.width = 6
print(f'Updated Length: {ymas.length}, {ymas.width}')

print()