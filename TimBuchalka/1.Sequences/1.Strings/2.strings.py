stmt = "What\"s in a name - William Shakespere"
print(stmt)
print()


print('Let\'s try this with separator/sep', 'Ok',sep='\n')
print()


# SEP has been used to break line
print('What\"s in a name - William Shakespere', 'For every action there is an equal or opposite reactions', sep='\n')
print()

parrot = 'Norwegian Blue'
print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

print(f'Display category: {parrot[-1:-5:-1][::-1]}')
print()

# RETURN ELEMENT IN LIST FROM A int type variable
number = "9,123,372:036;775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print()

# DISPLAY THE ALPHABETS IN BACKWARD 
alphabets = 'abcdefghijklmnopqrstuvwxyz'
print(f'Backward alphabets : {alphabets[25::-1]}')
print(f'Backward alphabets : {alphabets[::-1]}')
print(f'Backward alphabets : {alphabets[::-1][::-1]}')
print()

alphabets = 'abcdefghijklmnopqrstuvwxyz'
# PRINT LAST 8 CHARACTERS IN REVERSE ORDER
print(f'Last 8 characters in reverse order : {alphabets[:-9:-1]}')
# PRINT FIRST 5 CHARACTERS IN REVERSE ORDER
print(f'Last 5 characters in reverse order : {alphabets[4::-1]}')