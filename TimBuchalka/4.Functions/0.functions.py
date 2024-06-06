def multiply():
    result = 10.5 * 4
    return result
print(f'Multiplication of 10.5 and 4: {int(multiply())}')


def multiply2numbers(a, b):
    return (a * b)

print(f'Multiplication: {multiply2numbers(7, 5)}')
print('Multiplication of {} and {}: {}'.format(7,5,multiply2numbers(7,5)))
print()

for value in range(1,5):
    result = multiply2numbers(value, 8)
    print(f'Result: {result}')
print()

