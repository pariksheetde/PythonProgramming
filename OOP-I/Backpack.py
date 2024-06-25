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
    def __init__(self, color, price):
        self.color = color
        self.price = price


duckbag = Backpack("Red", 3500)
print(f'Cost of Duckbag: {duckbag.price} and color will be {duckbag.color}')
