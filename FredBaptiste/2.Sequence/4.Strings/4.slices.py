name = 'Pariksheet De'
print(f"First Name : {name.split(' ')[0]}")
print(f"Last Name : {name.split(' ')[1]}")
print()

marks = [10, 15, 20, 25, 30]
grades = marks
cond_one = 'Matched' if marks is grades else 'Mismatched'
cond_two = 'Matched' if marks == grades else 'Mismatched'
print(cond_one)
print(cond_two)
print()

s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(s[-1:4:-1])
print()