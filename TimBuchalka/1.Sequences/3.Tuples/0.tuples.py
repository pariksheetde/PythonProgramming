# TUPLE IS A MATHEMATICAL NAME FOR OREDRED SET OF ELEMENTS. OREDERED IS A REQUIREMENT FOR PYTHON SEQUENCE
# TUPLES DIFFER FROM LISTS, BECAUSE TUPLES ARE IMMUTABLE. THE ELEMENTS CANN'T BE CHANGED AFTER THEY ARE CREATED JUST LIKE STRINGS
# TUPLES CAN BE CREATED WITHIN PARENTHESIS, aka ROUND BRACKET

fruits = "Apple", "Banana", "Grapes"
print(f'Type : {type(fruits)}')
print(fruits)
print()

welcome = 'Welcome to my Nightmare', "Allice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(f'The album : \"{metallica[0]}\" was released by artist \"{metallica[1]}\" in the year {metallica[2]}')
print()

alpha = "abcdefg"
for index, value in enumerate(alpha):
    print(f'Unpacking : {index}, {value}')
print()

beta = "abcdefg"
for index in enumerate(beta):
    print(f'Packing : {index}')
print()

# UNPACKING A TUPLE
student = ("Monica", 75, 41, 85)
print(f'{student[0]} scored {student[1]} in Physics, {student[2]} in Chemistry, {student[3]} in Maths')
print()

# UNPACKING A TUPLE
name, physics, chemistry, maths = ("Monica", 71, 65, 63)
print(f'{name} scored {physics} in Physics, {chemistry} in Chemistry, {maths} in Maths')
print()