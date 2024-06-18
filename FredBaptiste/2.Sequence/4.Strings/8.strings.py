matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(matrix[0][0], matrix[1][1], matrix[2][2])
print()

# BELOW CODE IS OBJECT REFERENCE
row_1 = matrix[0]
row_1[0] = 1

row_2 = matrix[1]
row_2[1] = 1

row_3 = matrix[2]
row_3[2] = 1

print(matrix)
print()

matrix_reloaded = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

level_0 = matrix_reloaded[0]
if level_0 is matrix_reloaded[0]:
    print(f"Both the objects references are same")
else:
    print(f"Objects references are not same")