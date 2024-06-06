user_text = input("Enter 3 numbers separated by comma',': " )
numbers_splitted = user_text.split(",")

numbers = []
for value in numbers_splitted:
    numbers.append(int(value))

a, b, c = numbers
result = a + b - c
print(f'The result: {result}')
print()