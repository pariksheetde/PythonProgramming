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

alphabet = 'abcdefghijklmnopqrstuvwxyz'
# convert the string into tuple
tup = tuple(alphabet)
print(tup)
# convert the string into list
lst = list(alphabet)
print(lst)
print()

alpha = ([10, 15], 30)
beta = alpha * 3
print(beta)

if alpha[0] is beta[0]:
    print(f"alpha[0] is beta[0] objects references are same")

if alpha[0] is beta[2]:
    print(f"alpha[0] is beta[2] objects references are same")

if alpha[0] is beta[4]:
    print(f"alpha[0] is beta[4] objects references are same")
else:
    print(f"Objects references are not same")
print()