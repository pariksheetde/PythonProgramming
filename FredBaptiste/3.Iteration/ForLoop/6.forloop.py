shopping_cart = [
    'milk',
    'pasta',
    'spam',
    'bread',
    'rice'
]
shopping_cart += ['butter']
optimum_cart = []
for cart in shopping_cart:
    optimum_cart.append(cart.upper())
print(optimum_cart)
print(f'Number of items added: {len(optimum_cart)}')
print()

fruits = ['banana', 'apple', 'strawberry', 'watermelon']
a = b = c = fruits
a.append('guava')

print(f'B has the following fruits: {b}')
print(f'C has the following fruits: {c}')
print(f'A has the following fruits: {a}')