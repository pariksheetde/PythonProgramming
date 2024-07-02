# There are 3 types of Methods
# 1. Instance Methods
# 2. Class Methods
# 3. Static Methods

class Backpack:

    def __init__(self):
        self._items = []

    
    @property
    def items(self):
        return self._items
    
    def add_items(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Invalid list of Items")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            print(f'{item} is not available in the backpack')
            return 0

    def has_item(self, item):
        # return item in self.items
        if item in self.items:
            print(f"{item} has been added in the campaign")
        else:
            print(f"{item} has not been added in the backpag")

# STEP 1. Create an instance of a class
lv = Backpack()

print(lv.items) # Returns empty list because initial list is empty

# STEP 2. Add some items in the class instance
lv.add_items('Tiffin Box')
print(lv.items)
lv.add_items('Sleeping Bag')
print(lv.items)

# STEP 3. Check if the item is available
lv.has_item('Lunch Box')

# STEP 4. Let's remove some item
lv.remove_item('Cosmetic Box')
print(f'{lv.items} have been loaded in the backpack')

print()