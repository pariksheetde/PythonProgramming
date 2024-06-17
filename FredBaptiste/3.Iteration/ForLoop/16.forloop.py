# SEQUENCE IS A ORDERED COLLECTION OF ELEMENTS
# IF THE SEQUENCE ISN'T ORDERED, WE COULDN'T REFER THESE ELEMENTS BY THEIR INDEX POSITION
# STRING, LIST and TUPLES ARE SEQUENCE
# STRINGS ARE IMMUTABLE THAT MEANS THEY CANN'T BE CHANGES
# LISTS ARE MUTABLE, THAT MEANS THE VALUE CAN BE CHANGED

# DELETE THE ELEMENTS THAT ARE GREATER THAN 200 OR LESSER THAN 100
data = [1, 7, 104, 101, 4, 105, 308, 103, 5,
        107, 100, 12, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        del data[top_index - index]
        print(top_index - index, value)
print(f'Data after deletion: {data}')
print()

