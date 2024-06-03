# LIST is an ordered collection of items
# LIST is mutable which can be changed
computer_parts = ['computer', 'monitor', 'keyboard', 'mouse', 'mouse mat']
for parts in computer_parts:
    print(parts.title())
    print(id(parts))

print()

computer_parts = ['computer', 'monitor', 'keyboard', 'mouse', 'mouse mat']
laptop_parts = computer_parts
print(f'ID addres: {id(computer_parts)}')
print(f'ID addres: {id(laptop_parts)}')
print()

shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread']
print(f'Before adding new element, ID : {id(shopping_list)}')
shopping_list += ['curd']
print(f'New shopping cart: {shopping_list}')
print(f'After adding new element, ID : {id(shopping_list)}')
print()

