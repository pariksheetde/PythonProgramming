import random
from Move import Move


class Player:

    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, is_human=True):
        self._is_human = is_human

        if is_human:
            self._marker = Player.HUMAN_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human
    
    @property
    def marker(self):
        return self._marker
    
    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
        
    def get_human_move(self):
        while True:
            user_input = int(input("Please enter your move. [1-9] "))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Please enter integer between 1 and 9.")
        return move
    
    def get_computer_move(self):
        random_choice = random.choice(list(range(1, 10)))
        move = Move(random_choice)
        print(f"Computer Move [1-9]: {move.value}")
        return move

# Create an instance for Human Player
"""
dep = Player(is_human=True)
print(dep.is_human)
print(f'Pariksheet\'s Move: {dep.marker}')

print()

mv = dep.get_move()
print(mv.value)
"""
print()

# Create an instance for Computer Player
dell = Player(False)
print(dell.is_human)
print(f'Machine\'s Move: {dell.is_human}')

dell_mv = dell.get_move()
print(dell_mv.value)