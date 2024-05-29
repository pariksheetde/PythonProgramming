# DELETE ANY ELEMENTS WHERE VALUES ARE LESS THAN 100 AND GREATER THAN 200
data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

for index in range(len(data) - 1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        # print(index)
        del data[index]
print("After deletion {}".format(data))

print()