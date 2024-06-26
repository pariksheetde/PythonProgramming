# When an object is said to immutable, that means it cann't be changed
# The following are immutable types
# 1. int
# 2. str
# 3. bool
# 4. tuple
# 5. frozenset
# 6. bytes

parrot = "Norwegian Blue"
print(f'Length of parrot: {len(parrot)}')
print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(f'Printing the alphabets in reverse order: {alphabet[::-1]}')
print(f'Printing the alphabets in reverse order: {alphabet[:-27:-1]}')
print(f'Printing the alphabets in reverse order: {alphabet[27::-1]}')

print()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(f'Generating "qpo": {alphabet[-10:13:-1]}')
print(f'Generating "edcba": {alphabet[4::-1]}')
print(f'Generating "stuvwxyz": {alphabet[-8:][::-1]}')

print()

print("Hello " * 5)
print("Hello " * (2 + 1))
print("Hello " * (2 + 1), "7")

print()

# format the float value to 50 places of decimal using .50f
print("PI is approximately: {0:5f}".format(22/7))
print(f'PI is approximately: {(22 / 7):12.50}')

print()
