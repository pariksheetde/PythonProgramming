import random

class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value

"""
Test Die class to check the logic works
# die = Die()
# print(die.value)
# die.roll(6)
# print(die.value)
"""

class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()

"""
# Test Player class to check the logic works
die = Die()             ## Initiate the class die
print(die.value)        ## Initial value of die
die.roll()              ## assign a new value for roll() for Die method
print(die.value)        ## will print the value for die.value

dep = Player(die, is_computer=False)
print(f'Player Object: {dep}')
print(f'Die Object: {die}')
print(f'Die Object called from Player object, dep{dep.die}')
print(f'Player is {dep.is_computer}')

print()

print(f'Initial Value of counter: {dep.counter}')
dep.increment_counter()
print(f'After increment, value of counter: {dep.counter}')

print()

print(f'Initial Value of counter: {dep.counter}')
dep.decrement_counter()
print(f'After decrement, value of counter: {dep.counter}')

print()

print(f'Initial Value: {die.value}')                  ## Initial value of die
dep.roll_die()                                        ## invoke roll_die()
print(f'After Die is rolled: {die.value}')            ## check the value
"""


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("Welcome to Roll the Dice!")
        print("Let's start the Game")
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break 

    def play_round(self):
        self.welcome()
        # Roll the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        self.show_dice(player_value, computer_value)

        # Determine the winner & loser
        if player_value > computer_value:
            print("You won the round")
            self.update_counters(winner=self._player, losser=self._computer)
        elif computer_value > player_value:
            print("Computer won this round. Please try again")
            self.update_counters(winner=self._computer, losser=self._player)
        elif player_value == computer_value:
            print("It's a tie")

        # Show counters
        print(f"Your Counter: {self._player.counter}")
        print(f"Computer Counter: {self._computer.counter}")

    def welcome(self):
        print("\n----- New Round -----")
        input("Press any key to roll the dice! ")

    def show_dice(self, player_value, computer_value):
        # show the values
        print(f"Player's Die: {player_value}")
        print(f"Computer's Die: {computer_value}")

    def update_counters(self, winner, losser):
        winner.decrement_counter()
        losser.increment_counter()

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False
        
    def show_game_over(self, winner):
        if winner.is_computer:
            print(f"\n------------------------------------")
            print("GAME OVER")
            print("Computer Won the Game")
        else:
            print(f"\n------------------------------------")
            print("GAME OVER")
            print("You Won the Game. Congrats..........")


pariksheet_die = Die()
dell_die = Die()

my_player = Player(pariksheet_die, is_computer=False)
laptop_player = Player(dell_die, is_computer=True)

game = DiceGame(my_player, laptop_player)

# Start the Game
game.play()