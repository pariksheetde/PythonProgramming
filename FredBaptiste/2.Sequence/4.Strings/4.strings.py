pangram = "The quick brown fox jumps over the lazy fox"
print(sorted(pangram))
print()

# SORT() & SORTED()
numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
numbers.sort()
sorted_numbers = sorted(numbers)
print(f'Using Sorted : {sorted(sorted_numbers)}')
print(f'Using Sort : {sorted(numbers)}')
print(f'Using Sort : {numbers}')
print()

letters = "The quick brown fox jumps over the lazy fox"
missing_letter = sorted(letters)
print(missing_letter)
print()

# USE casefold TO SORT THE NAMES IN THE LIST IN ASC OREDR IRRESPECTIVE OF UPPERCASE, LOWERCASE CHARECTERS
name = 'PAriksHEeT'
sorted_name = sorted(name, key = str.casefold)
print(f'Sorted Name: {sorted_name}')
print()
