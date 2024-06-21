# Shallow Copy creates a new sequence
# Not same sequence object as original
# Elements in the new sequence reference the same elements as original


# Deep Copy creates a new sequence
# Not same sequence object as original
# Elements in the new sequence is a deep copy of the original

# SHALLOW COPY
original = [
    [1, 0, 0], 
    [0, 1, 0],
    [0, 0, 1]
    ]
# create a shallow copy
copy = original.copy()
print(f'Before Change, {original[0], copy[0]}', sep=": ")
if original[0] is copy[0]:
    print(f'1st STATEMENT: Both the object references are same')
else:
    print(f'1st STATEMENT: Both the object references are different')

print(f'After Modifying Original List')
original[0].append(100)
if original[0] is copy[0]:
    print(f'1st STATEMENT: Both the object references are same')
else:
    print(f'1st STATEMENT: Both the object references are different')

# original[0] = [1, 1, 1]
print(original)
print(copy)
print()
