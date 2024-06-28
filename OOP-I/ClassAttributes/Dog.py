class Dog:
    species = "Golder Retreiver"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self._breed = breed    # _breeed is non-public attribute. non-public attribute shouldn't be accessed outside the class

kite = Dog('Kite', 1.2, 'English')
print(f'Let\'s see the species: {Dog.species}')
print(f'I have {Dog.species} which is {kite._breed} breed. His name is {kite.name} and age is {kite.age}')

kite._breed = 'American'
print(f'After changing the non-public attribute: {kite._breed}')

print()