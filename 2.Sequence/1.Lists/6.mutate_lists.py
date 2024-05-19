EOL = "----"
# INSERT & DEL
val = [10, 20, 3, 30]
val.insert(2, 30)
val.insert(3, 40)
print(f'After inseting new element : {val}')
del val[-1:-3:-1]
print(f'After deleting new element : {val}')

print(EOL * 37)

# REPLACE
var = [1, 20, 30, 5, 6]
var[1:3] = ['alpha', 'beta', 'gamma', 'delta']
print(f'After change : {var}')

print(EOL * 37)

# EXTEND
debt = [10, 20, 30]
debt.extend([40, 50])
debt.extend((50, 60, 70))
debt.extend(['ab'])
print(f'The value of debt : {debt}')

print(EOL * 37)

# EXTEND
credit = [10, 20, 30]
credit.extend(['a', 'b'])
credit.extend(('a', 'b'))
credit.extend(('ab'))
print(f'The value of credit : {credit}')

print(EOL * 37)

# EXTEND
lst = [10, 20, 30]
lst.extend(['a', 'b', 'c'])
lst.extend(('a', 'b', 'c'))
lst.extend(('abc'))
print(f'The value of lst : {lst}')

print(EOL * 37)

age = [1, 2, 3, 4, 5, 6, 7, 8]
print(f'Before change : {age[1::2]}')
# age[1::2] = [20, 40, 60] # THIS WILL NOT WORK. ValueError: attempt to assign sequence of size 3 to extended slice of size 4 
print(f'After change : {age}')

print(EOL * 37)

dep = [1, 2, 3, 4, 5, 6, 7, 8]
print(f'Before change : {dep[:-3:-1]}')
dep[:-3:-1] = [101, 201]
print(f'After change : {dep}')

print(EOL * 37)

aldo = [10, 20, 30, 40, 50, 60, 70, 80]
aldo[::2]
print(f'Before change : {aldo[::2]}')
aldo[::2] = [1, 3, 5, 7]
print(f'After change : {aldo}')

print(EOL * 37)