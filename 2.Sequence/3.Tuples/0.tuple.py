# Create empty tuple
# Tuple are immutable collection of ordered elements
age = ()
print(type(age))

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

age = (10, 15, 20, 25, 30)
print(f'First Element within the tuple : {age[0]}')

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

# 'tuple' object does not support item assignment
age = (10, 15, 20, 25, 30)
# age[0] = 11
print(age)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

# Tuple are immutable. However, lists within tuple can be modified.
# See below code snippet
marks = (10, 20, 30, [True, False])
print(type(marks))
print(f'Before Changes : {marks}')
print(marks[3][0])
print(marks[3][1])
marks[3][0] = 40
marks[3][1] = 50
print(print(f'After Changes : {marks}'))

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

