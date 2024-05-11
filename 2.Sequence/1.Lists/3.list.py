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


print(EOL * 37)