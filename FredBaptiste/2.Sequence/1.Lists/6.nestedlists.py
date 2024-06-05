# CREATE A NESTED LIST
odd = [1, 2, 3, 4, 5, 7, 9]
even = [2, 4, 6, 8]
print([odd], [even] )
print()

# CREATE A NESTED LIST
odd = [1, 2, 3, 4, 5, 7, 9]
even = [2, 4, 6, 8]
numbers = [odd, even]
print(numbers)
for number in numbers:
    for sub_number in number:
        print(sub_number)