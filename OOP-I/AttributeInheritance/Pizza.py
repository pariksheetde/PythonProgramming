class Pizza:

    def __init__(self, size, toppings, price, rating):
        self.size = size
        self.toppings = toppings
        self.price = price
        self.rating = rating


class Margherita(Pizza):
    
    def __init__(self, size, toppings, price, rating, has_extra_cheese=False):
        
        Pizza.__init__(self, size, toppings, price, rating)
        self.has_extra_cheeze = has_extra_cheese


class Marinara(Pizza):
    
    def __init__(self, size, toppings, price, rating, has_extra_oregano=True):
        
        Pizza.__init__(self, size, toppings, price, rating)
        self.has_extra_oregano = has_extra_oregano


margherita = Margherita("Medium", True, 12.26, 3.5, False)
print(f'{margherita.size} has toppings, {margherita.toppings}. Rating is {margherita.rating} with extra cheeze {margherita.has_extra_cheeze}')

print()

marinara = Marinara("Large", True, 18.99, 3.5, True)
print(f'{marinara.size} has toppings, {marinara.toppings}. Rating is {marinara.rating} with extra cheeze {marinara.has_extra_oregano}')