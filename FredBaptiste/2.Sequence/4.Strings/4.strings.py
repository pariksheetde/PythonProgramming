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