odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
numbers = (even + odd)
# SORT THE "NUMBERS" ARAAY IN ASCENDING ORDER USING sorted()
print(f'Sorting the numbers in ASC order: {sorted(numbers)}')

print()

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
even.extend(odd)
# SORT THE "NUMBERS" ARAAY IN ASCENDING ORDER USING sort()
even.sort(reverse=True)
print(f'Sorting the numbers in ASC order: {even}')

print()
