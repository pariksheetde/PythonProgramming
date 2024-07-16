# data = [
#     4, 5, 104, 110, 120, 130, 150, 160, 170, 
#     183, 185, 187, 188, 191, 350, 360
# ]
data = [
    89, 104, 101, 4, 105, 308, 103, 5,
    107, 100, 306, 106, 102, 108, 17
]
min_valid = 100
max_valid = 200

# process lowest values in the list
stop = 0
for index, value in enumerate(data):
    if (value >= min_valid):
        stop = index
        break 
del data[:stop]
print(data)

# process highest values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break
del data[start:]
print(data)

print()