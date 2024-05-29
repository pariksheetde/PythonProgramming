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

# SORTED & CASEFOLD
names = ['Anna', 'Bob', 'alex', 'monica', 'Thomas', 'peter']
print("Before changes : {}".format(names))
sorted_names = sorted(names)
print("After changes : {}".format(sorted_names))
casefolde_sorted_names = sorted(names, key=str.casefold)
print("After applying casefold {}".format(casefolde_sorted_names))
print()