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

lang = 'python rocks!'
print(lang[0:6])

range = range(1, 11)
tup = tuple(range)
# display alternate elements from tuple
alt_tuple = tup[::2]
print(type(alt_tuple), alt_tuple)
print()

grades = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
# every element from backward  
print(f'Test: {grades[-9::1]}')
print()
