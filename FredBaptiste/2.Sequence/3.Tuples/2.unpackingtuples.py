details = ('Monica', 'Bellucci', 'Italy', 'Female', 'Model')
print(f'Name: {details[0],details[1]}')
print(f'Profession: {details[4]}')
print("{} belongs from {} and her profession is {}".format(details[0],details[1],details[4]))
print()

rate = 10, 12.25
print(f'Rate: {rate}')
# unpacking tuple
apr, apy = rate
print(f'APR: {apr}')
print(f'APY: {apy}')
print()

# swapping 2 variables using temporary variable
a = 100
b = 200
temp = a
a = b
b = temp
print(f'After Swapping, \'A\': {a}')
print(f'After Swapping, \'B\': {b}')
print()

# swapping 2 variables using unpacking
a = 100
b = 200
tmp = b, a
print(f'After Swapping, \'A\': {a}')
print(f'After Swapping, \'B\': {b}')
print()