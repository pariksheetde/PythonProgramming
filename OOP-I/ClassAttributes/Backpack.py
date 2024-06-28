class Backpack:
    no_of_items = 10
    def __init__(self):
        self.items = ['Leather', 'Premium']

lv = Backpack()
print(f'All the Bagpacks will have {Backpack.no_of_items} items. They are all {lv.items}')