# Copying Sequence
original = [10, 20, 30]
copy = original[:]

print(f'Original : {original}')
print(f'copy : {copy}')
# check to see if the objects are same
if original is copy:
    print(True)
else:
    print(False)
original.append(40)
print()


# Copying Sequence
original = [10, 20, 30]
copy = original.copy()

print(f'Original : {original}')
print(f'copy : {copy}')

# APPEND a element to a lisr
original.append(40)
print(f'Original : {original}')
print(f'copy : {copy}')
print()

mat1 = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [0, 0, 1]]
mat2 = mat1.copy()
mat2.append([11, 22, 33])

print(f'Original copy : {mat1}')
print(f'Duplicate copy : {mat2}')

if mat1[0] is mat2[0]:
    print(True)
else:
    print(False)

# APPEND will effect both the list since the list is a shared reference
mat1[0].append(100)
print(f'After Change : {mat1}')
print(f'After Change : {mat2}')

# import copy library
from copy import deepcopy

set = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [0, 0, 1]]
max = deepcopy(set)

print(f'Set : {set}')
print(f'Max : {max}')
if set[0] is max[0]:
    print(True)
else:
    print(False)

set[0].append(1409)
print(f'After Change SET : {set}')
print(f'After Change MAX : {max}')
print()