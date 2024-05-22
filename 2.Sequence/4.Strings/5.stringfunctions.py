EOL = "----"
name = 'Pariksheet De'
print(f'Name :{name}')
print(f'Name is Upper case : {name.upper()}')
print(f'Name is Lower case : {name.lower()}')
print(f'Name is Title case : {name.title()}')

print(f'Using casefold() : {name.casefold() == name.casefold()}')

print(EOL * 37)

model = '   monica bellucci '
print(f'Length : {len(model)}')
print(f'After stripping whitespace : {model.strip().title()}')
print(f'After stripping whitespace, length : {len(model.strip())}')

print(EOL * 37)

stmt = '\tHumpty Dumpty \t sat on a wall'
print(f'Childhood rhyme : {stmt.strip()}')

print(EOL * 37)

f_name = 'Monica'
l_name = 'Bellucci'
print(f'Name : {f_name}  {l_name}')

print(EOL * 37)

full_name = 'Pariksheet, De,depariksheet2@gmail.com'
f_name, last_name, email = full_name.split(',')
print(f'First Name : {f_name}')
print(f'Last Name : {l_name}')
print(f'Email ID : {email}')

print(EOL * 37)

fruits = ['apple', 'orange', 'banana', 'grape', 'watermelon']
fruit_lists = '**'.join(fruits)
print(fruit_lists)

print(EOL * 37)

lang = 'python'.casefold() in 'Python Rocks!. I am learning very fast'.casefold()
print(f'Checking if python is available : {lang}')

print(EOL * 37)

alpha = ['abc', 'def']
print(f'If abc is present is the list : {"abc" in alpha}')
print(f'If a is present is the list : {"a" in alpha}')