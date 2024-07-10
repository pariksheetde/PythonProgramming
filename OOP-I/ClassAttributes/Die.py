import random

class Die:

    def __init__(self, value):
        self.value = value

    def roll_die(self):
        random_choice = random.randint(1, 6)
        self.value = random_choice
        return self.value


roll = Die(4)
print(f"Initial Value: {roll.value}")
roll.roll_die()
print(f'After Roll: {roll.value}')