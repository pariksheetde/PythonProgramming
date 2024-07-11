# sorted() sorts the sequence, it creates a new variable instead of mutating the original variable
panagram = "The quick brown fox jumps over the lazy dog"

sorted_panagram = sorted(panagram)
print(sorted_panagram)
print(panagram)

print()

# sorted() sorts the sequence, it creates a new list instead of mutating the original list
lst = [10, 12, 9, 1, 14, 12, 7, 15, 19, 21, 20]
sorted_lst = sorted(lst)
print(sorted_lst)
print(lst)
lst.sort()
print(f'Sorted list, using `sort()` method: {lst}')

print()

alphabet = "abcdefghijklmnopqrstuvwxyz"
sorted_alphabet = sorted(alphabet, key=str.casefold)
print(f'Sorted Alphabet: {sorted_alphabet}')

print()

name = "Pariksheet"
sorted_name = sorted(name, key=str.casefold)
print(f'Sorted Name: {sorted_name}')

print()

digits = "432985617"
print(f'Sorted String using `sorted()`{sorted(digits)}')

print()