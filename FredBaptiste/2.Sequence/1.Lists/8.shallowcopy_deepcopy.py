# Shallow Copy creates a new sequence
# Not same sequence object as original
# Elements in the new sequence reference the same elements as original


# Deep Copy creates a new sequence
# Not same sequence object as original
# Elements in the new sequence is a deep copy of the original

# SHALLOW COPY
original = [10, 20, 30, 40]
# create a shallow copy
copy = original[:]
print(f'Before Change, {original, copy}', sep=": ")
if original[0] is copy[0]:
    print(f'1st STATEMENT: Both the object references\'SHALLOW COPY \' are same')
else:
    print(f'1st STATEMENT: Both the object references\'SHALLOW COPY \' are different')

original[0] = 100
print(f'After Change, {original, copy}', sep=": ")
if original[0] is copy[0]:
    print(f'2nd STATEMENT: Both the object references\'SHALLOW COPY \' are same')
else:
    print(f'2nd STATEMENT: Both the object references\'SHALLOW COPY \' are different')
print()

original = [11, 22, 33, 44]
# create a shallow copy
copy = original.copy()
print(f'Before Change, {original, copy}', sep=": ")
if original[0] is copy[0]:
    print(f'3rd STATEMENT: Both the object references\'SHALLOW COPY \' are same')
else:
    print(f'3rd STATEMENT: Both the object references\'SHALLOW COPY \' are different')

original[0] = 100
print(f'After Change, {original, copy}', sep=": ")
if original[0] is copy[0]:
    print(f'3rd STATEMENT: Both the object references are same')
else:
    print(f'3rd STATEMENT: Both the object references are different')
print()

# DEEP COPY
from copy import deepcopy
original = [
    [1, 0, 0], 
    [0, 1, 0],
    [0, 0, 1]
    ]
copy = deepcopy(original)
print(f'4th STATEMENT: Before Change, {original[0], copy[0]}', sep=": ")
if original[0] is copy[0]:
    print(f'4th STATEMENT: Both the object references \'DEEP COPY \'are same')
else:
    print(f'Both the object references \'DEEP COPY \' are different')