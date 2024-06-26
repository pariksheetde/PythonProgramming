class House:
    def __init__(self, price, size):
        self.price = price
        self.area = size


pn = House(15000, '1200 sq ft')
print(f'Total area of the house is {pn.area} and cost is {pn.price} $')

print()