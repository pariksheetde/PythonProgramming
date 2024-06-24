odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
numbers = (even + odd)
# SORT THE "NUMBERS" ARAAY IN ASCENDING ORDER USING sorted()
print(f'Sorting the numbers in ASC order: {sorted(numbers)}')
print()

digits = '432985617'
print(f'Digits are sorted in ASC order: {sorted(digits)}')
print()

digits = list('432985617')
print(f'Digits are sorted in ASC order in the List: {sorted(digits)}')
print()

days = [1, 2, 3, 4, 5]
new_days = days
stmt = True if new_days == days else False
id = stmt = True if new_days is days else False
print(stmt)
print(id)
print()