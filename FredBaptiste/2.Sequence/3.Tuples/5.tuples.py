# TUPLE IS A ORDERED SEQUENCE OF ELEMENTS.
# TUPLE IS IMMUTBLE
age = (10, 20, 30)
print(type(age))
print(f'Last Element: {age[len(age) - 1]}')
print()

marks = (74, 87, [True, False], 94)
marks[2][0] = 80
marks[2][1] = 90
print(f'After Change: {marks}')
print()

