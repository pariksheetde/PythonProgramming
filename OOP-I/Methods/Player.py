class Player:

    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def move_up(self, change=5):
        self.y_axis += change

    def move_down(self, change=5):
        self.y_axis -= change

    def move_right(self, change=2):
        self.x_axis += change

    def move_left(self, change=2):
        self.x_axis -= change

# create an instance of class
gary = Player(5, 10)
print(f'Orginal X-Coordinate: {gary.x_axis}, Orginal Y-Coordinate: {gary.y_axis}')

# move_up(), move_down()
gary.move_up(8)
gary.move_down(2)
print(f'Updated X-Coordinate: {gary.x_axis}, Updated Y-Coordinate: {gary.y_axis}')

# print()

# move_right(), move_left()
print("TEST")
print(gary.x_axis, gary.y_axis)
gary.move_right(1.25)
gary.move_left(4.75)
print(f'Updated X-Coordinate: {gary.x_axis}, Updated Y-Coordinate: {gary.y_axis}')