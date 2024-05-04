# Create empty tuple
# Tuple are immutable collection of ordered elements
age = ()
print(type(age))

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

age = (10, 15, 20, 25, 30)
print(f'Type : {type(age)}')
print(f'First Element within the tuple : {age[0]}')

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

# create a tuple and convert the tuple into list
age = (10, 11, 20, 22)
age = list(age)
print(f'Converting tuple into list: {type(age)}')
age[1] = 15
print(f'After Change : {age}')

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

# create a list and convert the list into tuple
grade = [10, 11, 20, 22]
grade = tuple(grade)
print(f'Converting list into tuple: : {type(grade)}')
grade[1] = 15
print(f'After Change : {grade}')