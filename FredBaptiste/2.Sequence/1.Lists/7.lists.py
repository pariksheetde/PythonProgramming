fruits = [
    'apple',
    'watermelon',
    'guava',
    'blackberry',
]
print(fruits[-1:-3:-1])
print(f'Before change: {fruits}')
fruits[-1:-3:-1] = ['banana', 'grapes']
print(f'After change: {fruits}')
print()

fruits = [
    'apple',
    'strawberry',
    'grapes'
    'watermelon',
    'banana',
    'blackberry',
]
fruits[0:2] = ['pears', 'dragon fruit']
print(f'After Change: {fruits}')
print()