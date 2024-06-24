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
for values in computer_parts:
    print(values)
print(f'Last Item I purchased: {computer_parts[len(computer_parts) - 1]}')
print(f'Items I purchased in reverse order: {computer_parts[::-1]}')

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

# Let's add a new element to the shopping cart
shopping_cart.append("Cookies")
print(shopping_cart)
print(anoher_shopping_cart)

if id(shopping_cart) == id(anoher_shopping_cart):
    print("Woh! The address is same")
else:
    print("Hmm!. The address didn't match")

print()

