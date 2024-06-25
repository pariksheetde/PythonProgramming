# class is the blueprint
# object created form class is called instance
# __init__ is a special method that is used to define the initial state of the object

class Backpack:
    def __init__(self):
        # we are going to create or assign a `price instance attribute` to the instance.
        # all the instances that we create of the backpack class can have an item's attribute.
        self.items = ['Premium', 'Versatile']


american_tourister = Backpack()
print(f'Contents of American Tourister: {american_tourister.items}')

print()

class Backpack:
    def __init__(self, size, color, weight, material, no_of_pockets, number_of_zippers, price):
        self.size = size
        self.color = color
        self.weight = weight
        self.material = material
        self.no_of_pockets = no_of_pockets
        self.number_of_zippers = number_of_zippers
        self.cost = price


duckbag = Backpack('Small',"Red", "1.5 kg", "Fabric", 4, 3, 3500)

print("Details of Duckbag Backpack")
print(f'Price: {duckbag.cost}')
print(f'Color: {duckbag.color}')
print(f'Size: {duckbag.size}')
print(f'Weight: {duckbag.weight}')
print(f'Material: {duckbag.material}')
print(f'Pockets Available: {duckbag.no_of_pockets}')
print(f'Available Zip: {duckbag.number_of_zippers}')

print()


versace = Backpack('Medium',"White", "1.95 kg", "Leather", 4, 6, 10500)

print("Details of versace Backpack")
print(f'Price: {versace.cost}')
print(f'Color: {versace.color}')
print(f'Size: {versace.size}')
print(f'Weight: {versace.weight}')
print(f'Material: {versace.material}')
print(f'Pockets Available: {versace.no_of_pockets}')
print(f'Available Zip: {versace.number_of_zippers}')

print()