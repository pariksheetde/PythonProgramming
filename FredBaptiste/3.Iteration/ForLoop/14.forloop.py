# print the elements from forward staring with 0
marks = [10, 15, 20, 25, 30, 35, 40]
print("print the elements from forward staring with 0")
for index, value in enumerate(marks):
    print(index, value)
print()

# print the elements from backward staring with highest available index value
marks = [10, 15, 20, 25, 30, 35, 40]
print("print the elements from backward staring with highest available index value")
for index in range(len(marks) - 1, -1, -1):
    print(index)
print()