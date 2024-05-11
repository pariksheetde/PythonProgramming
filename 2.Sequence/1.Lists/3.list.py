EOL = "----"
marks = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
grade = marks[0]
print(marks)
print(grade)

print(EOL * 37)

marks = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
grade = marks[0:2]
print(f'Marks : {marks}')
print(f'Grade : {grade}')
grade[1] = [10, 10, 10]
print(f'After Change "Grade" : {grade}')
print(marks is grade)

print(EOL * 37)

alpha = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
beta = marks[0:2]
print(f'Alpha : {alpha}')
print(f'Beta : {beta}')

beta[1] = [0, 1, 0]
print(f'After Change "Beta" : {beta}')

# check to see if alpha is same as beta
print(f'Is Alpha same as Beta : {alpha is beta}')
print(f'Alpha\'s 1st element : {alpha[0]}')
print(f'Beta\'s 1st element : {beta[0]}')
print(f"Is Alpha\'s 1st {alpha[0]} element same as Beta\'s 1st {beta[0]} element? : {alpha[0] is beta[0]}")

print(EOL * 37)