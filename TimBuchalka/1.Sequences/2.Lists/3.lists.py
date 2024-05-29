marks = [45, 37, 29, 34, 31]
grade = [15, 36, 9, 48, 30]

# EXTEND & SORT the elements within list
marks.extend(grade)
marks.sort(reverse=True)
print('New Marks {}:'.format(marks))
print()

marks = [45, 37, 29, 34, 31]
grade = [15, 36, 9, 48, 30]

# EXTEND & SORT the elements within list
marks.extend(grade)
marks.sort()
print('New Marks {}:'.format(marks))
print()

marks = [45, 37, 29, 34, 31]
grade = [15, 36, 9, 48, 30]

# EXTEND & SORT the elements within list
marks.extend(grade)
total = 0
for indx in marks:
    total = total + indx
print("Total : {}".format(total))
print()