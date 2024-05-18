EOL = "----"
marks = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
grade = marks[0:2]
if marks[0:2] is grade:
    print(f'True')
else:
    print(f'False')

print(EOL * 37)

l1 = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
l2 = l1[0:2]
l2[1] = 100
print(f'After Change l1 : {l1}')
print(f'After Change l2 : {l2}')
if l1[0] is l2[1]:
    print('True')
else:
    print('False')