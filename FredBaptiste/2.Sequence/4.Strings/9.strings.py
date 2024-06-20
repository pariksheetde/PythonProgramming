name = "pariksheet de"
title_name = name.title()
upper_name = name.upper()
lower_name = name.lower()
captilize_name = name.capitalize()
casefold_name = name.casefold()
print(f'Name is upper: {title_name}')
print(f'Name is upper: {upper_name}')
print(f'Name is lower: {lower_name}')
print(f'Name is capitalize: {captilize_name}')
print(f'Name is casefold: {casefold_name}')
print()

stmt = "    What\s in a name        "
stripped_stmt = stmt.strip()
left_stripped_stmt = stmt.lstrip()
right_stripped_stmt = stmt.rstrip()
print(f'Both Side stripped: {stripped_stmt}. Length is {len(stripped_stmt)}')
print(f'Left Side stripped: {left_stripped_stmt}. Length is {len(left_stripped_stmt)}')
print(f'Right Side stripped: {right_stripped_stmt}. Length is {len(right_stripped_stmt)}')
print()

f_name = 'Pariksheet'
l_name = 'De'
print('Full Name: {}, {}'.format(f_name, l_name))
print(f'Full Name: {f_name + " " + l_name}')
print()

# split() method is used to convert the STRING into LIST
string = '10, 20, 30, 40'
print(f'String Data after split. String has been converted into List: {string.split(",")}')

# join() method is used to convert the LIST into STRING:
lst = ['10', ' 20', ' 30', ' 40']
print(f'String Data after split. List has been converted into String:{",".join(lst)}')
print()
