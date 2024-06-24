# shallow copy and original copy are not same containers
# but the elements are referencing to same objects

# Below is the example of shallow copy
marks = [[10, 20], 30]
grades = marks[:]
print(f'Marks: {marks}')
print(f'Grades: {grades}')
# Modifying original list
grades[0][1] = 75.5
grades[-1] = 87
print(f'After changing the original list: {grades}')
print(f'After changing the original list: {marks}')
print()

# Below is the example of shallow copy
original = [[10, 20],[15, 25]]
duplicate = original.copy()
# Let's display the contents
print(f'Original Content Before 1st Change: {original}')
print(f'Original Content After 1st Change: {duplicate}')
# let's modify the original content
original[1][0] = True
original[1][1] = False
print(f'Original Content: {original}')
print(f'Original Content: {duplicate}')
original[0].append([15])
print(f'Original Content Before 2nd Change: {original}')
print(f'Original Content Before 2nd Change: {duplicate}')
print()

actual = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
dup = actual[:]
# Let's display the contents
print(f'Original Content Before 1st Change: {actual}')
print(f'Original Content After 1st Change: {dup}')
actual[0][0] = 1
print(f'Original Content After 1st Change: {actual}')
print(f'Original Content After 1st Change: {dup}')
actual[1][1] = 2
actual[1][1] = 2
print(f'Original Content Before 2nd Change: {actual}')
print(f'Original Content After 2nd Change: {dup}')
actual[2][2] = 3
actual[2][2] = 3
print(f'Original Content Before 2nd Change: {actual}')
print(f'Original Content After 2nd Change: {dup}')
print()

# Below is the example of deepcopy
from copy import deepcopy
actual = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
duplicate = deepcopy(actual)
print("DEEPCOPY")
print(f'Actual: {actual}')
print(f'Duplicate: {duplicate}')
actual[0].append(1)
print(f'After Change: {actual}')
print(f'After Change: {duplicate}')
print()