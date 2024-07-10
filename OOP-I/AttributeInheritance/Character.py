class Character:

    def __init__(self, x, y, num_lives):
        self.x = x
        self.y = y
        self.num_lives = num_lives

class Player(Character):

    INITIAL_X = 0
    INITIAL_Y = 0
    INITIAL_NUM_LIVES = 10

    def __init__(self, score=0):
        Character.__init__(self, Player.INITIAL_X, Player.INITIAL_Y, Player.INITIAL_NUM_LIVES)
        self.score = score

class Enemy(Character):

    def __init__(self, x=15, y=15, num_lives=8, is_poisonous=False):
        Character.__init__(self, x, y, num_lives)
        self.is_poisonous = is_poisonous

print("Player: IGI")
igi = Player()
print(f'Inital Score: {igi.score}')
print(f'X-Coordinate: {igi.x}')
print(f'Y-Coordinate: {igi.y}')
print(f'Number of Lives: {igi.num_lives}')

print()

print("Level: Easy Enemy")
easy_enemy = Enemy(num_lives=1, is_poisonous=False)
print(f'X-Coordinate: {easy_enemy.x}')
print(f'Y-Coordinate: {easy_enemy.y}')
print(f'Number of Lives: {easy_enemy.num_lives}')
print(f'Is Poisonous: {easy_enemy.is_poisonous}')

print()

print("Level: Hard Enemy")
hard_enemy = Enemy(100, 120, num_lives=20, is_poisonous=True)
print(f'X-Coordinate: {hard_enemy.x}')
print(f'Y-Coordinate: {hard_enemy.y}')
print(f'Number of Lives: {hard_enemy.num_lives}')
print(f'Is Poisonous: {hard_enemy.is_poisonous}')