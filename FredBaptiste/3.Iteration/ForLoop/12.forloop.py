# SEQUENCE IS A ORDERED COLLECTION OF ELEMENTS
# IF THE SEQUENCE ISN'T ORDERED, WE COULDN'T REFER THESE ELEMENTS BY THEIR INDEX POSITION
# STRING, LIST and TUPLES ARE SEQUENCE
# STRINGS ARE IMMUTABLE THAT MEANS THEY CANN'T BE CHANGES
# LISTS ARE MUTABLE, THAT MEANS THE VALUE CAN BE CHANGED

# DELETE THE ELEMENTS THAT ARE LESSER THAN 100 OR GREATER THAN 200
data = [4, 5, 9, 104, 105, 110, 120, 130, 130, 150, 
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200
# processing low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)
del data[:stop]
print(data)