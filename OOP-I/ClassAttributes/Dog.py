class Dog:
    species = "Golder Retreiver"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

kite = Dog('Kite', 1.2, 'English')
print(f'Let\'s see the species: {Dog.species}')
print(f'I have {Dog.species} which is {kite.breed} breed. His name is {kite.name} and age is {kite.age}')

print()