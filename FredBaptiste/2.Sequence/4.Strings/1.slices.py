matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]
sub = matrix[0]
if sub is matrix[0]:
    print('sub & matrix[0] objects are same')
else:
    print('sub & matrix[0] objects are not same. They are different')
print()

matrix_reloaded = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]
sub = matrix_reloaded[0]
sub[1] = 10

sub = matrix_reloaded[1]
sub[1] = 20

sub = matrix_reloaded[2]
sub[1] = 30
print(matrix_reloaded)