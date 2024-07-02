class Parrot:

    AVAILABLE_COLORS = ["Red", "Yellow", "Green"]
    def __init__(self, color, can_talk):
        self._color = color
        self.can_talk = can_talk

    def get_color(self):
        return self._color
    
    def set_color(self, new_color):
        if new_color in Parrot.AVAILABLE_COLORS:
            self._color = new_color
        else:
            print("Invalid Color option...")

    color = property(get_color, set_color)

tia = Parrot("White", True)
print(f'Original Characteristics: {tia.color}, {tia.can_talk}')

print()

print("Let's update the characteristics of tia................")
tia.color = "Green"
tia.can_talk = False
print(f'Updated Characteristics: {tia.color}, {tia.can_talk}')