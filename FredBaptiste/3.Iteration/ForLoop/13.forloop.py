# SEQUENCE IS A ORDERED COLLECTION OF ELEMENTS
# IF THE SEQUENCE ISN'T ORDERED, WE COULDN'T REFER THESE ELEMENTS BY THEIR INDEX POSITION
# STRING, LIST and TUPLES ARE SEQUENCE
# STRINGS ARE IMMUTABLE THAT MEANS THEY CANN'T BE CHANGES
# LISTS ARE MUTABLE, THAT MEANS THE VALUE CAN BE CHANGED

# DELETE THE ELEMENTS THAT ARE GREATER THAN 200
data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200
# processing high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
#     print(index)
    if data[index] <= max_valid:
        start = index + 1 
        break
print(start)
del data[start:]
print(data)