# SEQUENCE IS A ORDERED COLLECTION OF ELEMENTS
# IF THE SEQUENCE ISN'T ORDERED, WE COULDN'T REFER THESE ELEMENTS BY THEIR INDEX POSITION
# STRING, LIST and TUPLES ARE SEQUENCE
# STRINGS ARE IMMUTABLE THAT MEANS THEY CANN'T BE CHANGES
# LISTS ARE MUTABLE, THAT MEANS THE VALUE CAN BE CHANGED


# Replace any element lesser than 0 with 0 using enumerate() 
data = [10, 20, 30, -10, 40, -5]
for t in enumerate(data):
    index, element = t
    if element <= 0:
        data[index] = 0
print(f'After change : {data}')

print()

data = [10, 20, 30, -10, 40, -5]
for indx in data:
    if indx <= 0:
        indx = 0
    print(indx)

print()

# Replace any element lesser than 0 with 0 using enumerate() 
data = [10, 20, 30, -10, 40, -5]
for index, element in enumerate(data):
    if element<=0:
        data[index] = 0
print(data)