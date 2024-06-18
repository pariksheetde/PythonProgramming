# Shallow Copy creates a new sequence
# Not same sequence object as original
# Elements in the new sequence reference the same elements as original


# Deep Copy creates a new sequence
# Not same sequence object as original
# Elements in the new sequence is a deep copy of the original

original = [10, 20, 30, 40]
# create a shallow copy
copy = original[:]
print(f'Before Change, {original, copy}', sep=": ")
if original[0] is copy[0]:
    print(f'Both the object references are same')
else:
    print(f'Both the object references are different')

original[0] = 100
print(f'After Change, {original, copy}', sep=": ")
if original[0] is copy[0]:
    print(f'Both the object references are same')
else:
    print(f'Both the object references are different')
print()
