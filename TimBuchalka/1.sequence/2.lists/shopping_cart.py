# Mutable object is one that can be changed
# Following is an example of Mutable objects
# 1. list
# 2. dictionary
# 3. set
# 4. bytearray

computer_parts = [
    "Computer",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Mouse Mat"
]

for value in computer_parts:
    print(value)
    
print(f'Last product I purchased: {computer_parts[-1]}')
print(f'Last product I purchased: {computer_parts[len(computer_parts) - 1]}')
print(f'First 3 products I purchased: {computer_parts[0:3]}')
print(f'Products I purchased from backward: {computer_parts[::-1]}')

print()

shopping_cart = [
    "Milk",
    "Pasta",
    "Eggs",
    "Spam",
    "Bread",
    "Rice"
]

anoher_shopping_cart = shopping_cart
print(f'ID of "Shopping Cart": {id(shopping_cart)}')
print(f'ID of "Another Shopping Cart": {id(anoher_shopping_cart)}')

if id(shopping_cart) == id(anoher_shopping_cart):
    print("Woh! The address is same")
else:
    print("Hmm!. The address didn't match")

print()

# Let's add a new element to the shopping cart
shopping_cart.append("Cookies")
shopping_cart += ["Butter"]

print(shopping_cart)
print(anoher_shopping_cart)

if id(shopping_cart) == id(anoher_shopping_cart):
    print("Woh! The address is same")
else:
    print("Hmm!. The address didn't match")

print()

my_fav = wife_fav = kid_fav = shopping_cart

anoher_shopping_cart.append("Ice-Cream")
print(f'My Fav: {my_fav}')
print(f'My Wife\'s Fav: {wife_fav}')
print(f'My Kid\'s Fav: {kid_fav}')
print(f'Actual Shooping Cart: {shopping_cart}')

print()