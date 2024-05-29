# DELETE ANY ELEMENTS WHERE VALUES ARE LESS THAN 100 AND GREATER THAN 200
# DEL to remove the unwanted elements
data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

for index in range(len(data) - 1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        # print(index)
        del data[index]
print("After deletion Data {}".format(data))
print()

# DELETE ANY ELEMENTS WHERE VALUES ARE LESS THAN 100 AND GREATER THAN 200
# REVERSED() to reverse the elements within the list
marks = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

top_index = len(marks) - 1
for index, value in enumerate(reversed(marks)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del marks[top_index - index]
print('After deletion Marks {}'.format(marks))
print()