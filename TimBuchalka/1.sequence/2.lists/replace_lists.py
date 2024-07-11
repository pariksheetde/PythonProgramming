computer_parts = [
    'Computer', 
    'Monitor', 
    'Keyboard', 
    'Mouse', 
    'Mouse Mat', 
    'DVD Drive',
    'HDMI Cable']

print(computer_parts)

computer_parts[4] = "External Hard Disk"
print(computer_parts)

print()

fruits = [
    "Apple",
    "Banana",
    "Strawberry",
    "Watermelon",
    "Pineapple",
    "Dragon Fruit"
]

print(fruits)
fruits[2:4] = ["Guava"]
print(f'After replacing `fruits[] using slicing`: {fruits}')