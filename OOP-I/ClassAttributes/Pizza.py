class Pizza:
    price = 12.99
    def __init__(self, description, toppings, crust):
        self.description = description
        self.toppings = toppings
        self.crust = crust


dominos = Pizza("Margherita", ["Basil", "Mushrooms"], "New York Style")
print(f'Fixed Price: {Pizza.price}: {dominos.description}: {dominos.toppings}: {dominos.crust}')

# Due to economic slowdow, the price has been dropped to 10.49
Pizza.price = 10.49
print(f'Fixed Price: {Pizza.price}: {dominos.description}: {dominos.toppings}: {dominos.crust}')

print()