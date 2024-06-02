# SEQUENCE IS A ORDERED COLLECTION OF ELEMENTS
# IF THE SEQUENCE ISN'T ORDERED, WE COULDN'T REFER THESE ELEMENTS BY THEIR INDEX POSITION
# STRING, LIST and TUPLES ARE SEQUENCE
# STRINGS ARE IMMUTABLE THAT MEANS THEY CANN'T BE CHANGES
# LISTS ARE MUTABLE, THAT MEANS THE VALUE CAN BE CHANGED


shopping_cart = [
    'milk',
    'pasta',
    'spam',
    'bread',
    'rice'
]

shopping_cart += ['butter']
fav_shopping_cart = shopping_cart
fav_shopping_cart.append('cherry')
print(f'Shopping Cart has: {shopping_cart}')
print(f'Favourite Shopping Cart has: {fav_shopping_cart}')
print()

# count number of "e" appears in the string "pariksheet"
# casefold() and count() method
name = 'parikshEet'
wify = 'DeEpSi'
print(f'Number of \'e\' appears in {name}: {name.casefold().count("e")}')
print(f'Number of \'e\' appears in {wify}: {wify.casefold().count("e")}')