EOL = "----"
name = 'Pariksheet De'
print(f'Return First Name : {name[0:11]}')
print(f'Return Last Name : {name[-2:]}')

print(EOL * 37)

name = 'Monica Bellucci'
print(f'Name : {name[:]}')

print(EOL * 37)

marks = [10, 20, 30, 40, 50, 60, 70]
print(f'Every 2nd elements from 1st index: {marks[1::2]}')
print(f'Every 2nd elements from 0th index: {marks[0::2]}')

print(EOL * 37)

name = 'Monica Bellucci'
print(f'First Name : {name[0:6]}')
print(f'Last Name : {name[-8:]}')
print(f'Full Name : {name[0:]}')