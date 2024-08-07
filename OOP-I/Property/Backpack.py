class Backpack:

    def __init__(self):
        self._items = []

    """Define property as getter for item to obtain the values of item attribute"""
    @property
    def items(self):
        print("Calling getter...........")
        return self._items
    
    """Define property as setter for item to modify the values of item attribute"""
    @items.setter
    def items(self, new_item):
        print("Calling setter.........")
        if isinstance(new_item, list):
            self._items = new_item
        else:
            print("Invalid list of Items")

        
lv = Backpack()
print(lv.items)

print("Let's update the list")

lv.items = ["Leather", "Premium"]
print(f'New List of Backpack Items: {lv.items}')

print()