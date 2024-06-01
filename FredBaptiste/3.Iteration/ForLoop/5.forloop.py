# SEQUENCE IS A ORDERED COLLECTION OF ELEMENTS
# STRING, LIST and TUPLES ARE SEQUENCE
# STRINGS ARE IMMUTABLE THAT MEANS THEY CANN'T BE CHANGES
# LISTS ARE MUTABLE, THAT MEANS THE VALUE CAN BE CHANGED

computer_parts = [
    'computer',
    'monitor',
    'keyboard',
    'mouse',
    'mouse mat'
]
for parts in computer_parts:
    print(parts.title())
print()

print(f'First 3 computer parts: {computer_parts[0:3]}')
print(f'Last computer parts: {computer_parts[-1]}')
print()

result = True
anaother_result = result
print(f'Memory address of Result: {id(result)}')
print(f'Memory address of AnotherResult: {id(anaother_result)}')
if id(result) == id(anaother_result):
    print(True)
else:
    print(False)