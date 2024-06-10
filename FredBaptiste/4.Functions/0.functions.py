def add(x, y):
    result = (x * y)
    return result

print(f'The result of summation: {add(7,5)}')
print()

for val in range(1,5):
    resultant = add(val, 2)
    print(f'Result: {resultant}')
print()