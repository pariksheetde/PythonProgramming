class Player:

    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def move_up(self, change=5):
        self.y_axis += change

    def move_down(self, change=5):
        if not change <= 0:
            self.y_axis -= change
        else:
            print('Cann\'t be less than 0')

    def move_right(self, change=2):
        self.x_axis += change

    def move_left(self, change=2):
        if change <= 0:
            print('Cann\'t be less than 0')
        else:
            self.x_axis -= change

# create an instance of class
gary = Player(5, 10)
print("-------------------------------------------------------------------------")
print(f'Orginal X-Coordinate: {gary.x_axis}, Orginal Y-Coordinate: {gary.y_axis}')
print("-------------------------------------------------------------------------")


print("Modifying Y-Coordinate")
gary.move_up(8)
print("After Change(+) in Y-Corodinate")
print(f'Updated Y-Coordinate: {gary.x_axis}, Updated Y-Coordinate: {gary.y_axis}')
print("After Change(-) in Y-Corodinate")
gary.move_down(2)
print(f'Updated Y-Coordinate: {gary.x_axis}, Updated Y-Coordinate: {gary.y_axis}')

print("-------------------------------------------------------------------------")

print(f'Orginal X-Coordinate: {gary.x_axis}, Orginal Y-Coordinate: {gary.y_axis}')
print("Modifying X-Coordinate")
gary.move_right(1.25)
print(f'Updated X-Coordinate: {gary.x_axis}, Updated Y-Coordinate: {gary.y_axis}')
gary.move_left(4.75)
print(f'Updated X-Coordinate: {gary.x_axis}, Updated Y-Coordinate: {gary.y_axis}')

print()