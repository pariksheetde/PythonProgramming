# Create empty tuple
# Tuple are immutable collection of ordered elements
age = ()
print(type(age))

print()

age = (10, 15, 20, 25, 30)
print(f'Type : {type(age)}')
print(f'First Element within the tuple : {age[0]}')

print()

# create a tuple and convert the tuple into list
age = (10, 11, 20, 22)
age = list(age)
print(f'Converting tuple into list: {type(age)}')
age[1] = 15
print(f'After Change : {age}')

print()

# create a list and convert the list into tuple
grade = [10, 11, 20, 22]
grade = tuple(grade)
print(f'Converting list into tuple: : {type(grade)}')

print()

alpha = ([1, 2], 30, 40)
print(f'Type of alpha : {type(alpha)}')
beta = list(alpha)
print(f'Type of beta : {type(beta)}')
beta[0][0] = 10
beta[0][1] = 20
print(f'After Change in List : {beta}')
print(f'After Change in Tuple : {alpha}')

print()

data = (10, 15, 20, [True, 'SQL'])
data[len(data) - 1][0] = 30
data[len(data) - 1][1] = 40
print(data)