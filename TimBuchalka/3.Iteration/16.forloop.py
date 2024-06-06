prompt = input("Enter 3 numbers separated by comma',': " )
splitted_numbers = prompt.split(",")

int_numbers = []
for value in splitted_numbers:
    int_numbers.append(int(value))

result = int_numbers[0] + int_numbers[1] - int_numbers[2]
print(f'The result: {result}')
print()

