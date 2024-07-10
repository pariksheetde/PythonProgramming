class Backpack:

    def __init__(self):
        self.items = []

    def add_snacks(self, snack):
        print(f"Adding a snack to this Backpack..")
        self.items.append(snack)
        print(f"{snack} was added to backpack")

class SchoolBackpack(Backpack):
    
    def add_snacks(self, snack):
        print("It's time to go to school. Let's add snack")
        Backpack.add_snacks(self, snack)
        print(f"Now backpack has these items. {self.items}")

school = SchoolBackpack()
school.add_snacks(['Bread', 'Egg'])