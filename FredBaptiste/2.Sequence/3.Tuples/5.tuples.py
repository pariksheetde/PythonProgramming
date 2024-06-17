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

x = 10.25
y = 12.25

x, y, x + y
print(x, y)
print(type(x))
print()

# create empty tuple
ab = ()
cd = tuple()
print(f'Type of ab: {type(ab)}')
print(f'Type of cd: {type(cd)}')
print()

t = 11, 22, 33
print(t, type(t))
lst = list(t)
print(lst, type(lst))
lst.extend([44, 55])
# DELETE the previosly created Tuple
del t
# Create a new tuple and assign the values from List to Tuple
t = tuple(lst)
print(f'Converting from Tuple to List: {lst}')
print(f'Conents of Tuple: {t}')
print(f"Last Element from Tuple: {t[len(t) - 1]}")
print()
