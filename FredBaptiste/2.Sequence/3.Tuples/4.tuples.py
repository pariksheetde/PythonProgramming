# Tuple are immutable. However, lists within tuple can be modified.
# See below code snippet
marks = (10, 20, 30, [True, False])
print(type(marks))
print(f'Before Changes : {marks}')
print(f'1st Change: {marks[3][0]}')
print(f'2nd Change: {marks[3][1]}')
marks[3][0] = 40
marks[3][1] = 50
print(print(f'After Changes : {marks}'))
print()

age = tuple()
print(f'Type: {age}')
print()

delta = (10, 15, ['SQL', 'Python'])
delta[2][1] = 'NoSQL'
print(delta)