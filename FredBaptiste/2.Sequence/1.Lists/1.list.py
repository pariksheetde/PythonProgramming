# Create a list og int type.
# This list is homogeneous.
# List can be homogeneous and hetrogeneous
marks = [10, 20, 15, 25, 30, 35]
print(marks)

print(marks[0]) # returns 1st element
print(marks[:]) # returns all the elements
print(marks[:-1]) # returns the elements from 1st index position till 2nd last. -1 ignore the last element
print(marks[-1]) # returns the last element.
print()

grade = ['A', 'B', 'C', 'D', 'F']
grade[1] = 'A+' # Replace 2nd element with A++
print(grade)
print()

grade = [10, 20, 30, 40, 50]
# Return the last element
print(f'Last Element : {grade[-1]}')
print(f'Last Element : {grade[len(grade)- 1]}')
print()

grade = [10, 20, 30, 40, 50]
# Return the fist element
print(f'First Element : {grade[0]}')
print(f'First Element : {grade[len(grade) - len(grade)]}')
print()

item = [10, 20, 30, 40, 0]
print(f'Before Change: {item} has these elements')
item[len(item) - 1] = 50
print(f'After Change: {item} has these elements')
print()
