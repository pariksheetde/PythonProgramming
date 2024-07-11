even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9, 11]

# Let's print the max and min from each list
print(f'Max of Even: {max(even)}')
print(f'Min of Even: {min(even)}')
print(f'Max of Odd: {max(odd)}')
print(f'Min of Even: {min(odd)}')

print()

print(f"Lenth of even: {len(even)}")
print(f"Lenth of odd: {len(odd)}")

print()

lst = [8, 9, 11, 4, 6, 3, 2, 10, 1, 7]
print(sorted(lst))

print()

marks = [2, 4, 6, 8, 10]
grades = [1, 3, 5, 7, 9, 11]
empty_lst = []

numbers = marks + grades
numbers.sort()
print(f'Sorted using `sort()`: {numbers}')

print()

