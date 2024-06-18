# display only the 2nd occurance of the element
marks = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
print(marks[2::2])
print()

# display only the 2nd occurance of the element from backward
marks = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
print(marks[::-2])
print()

# display only the 3rd occurance of the element from backward
marks = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
print(marks[::-3])
print()

# display last 2 characters
name = "Pariksheet De"
surname = name[-2:]
last_name = name[11:]
reversed_name = name[::-1]
print(surname)
print(last_name)
print(reversed_name)
print()
