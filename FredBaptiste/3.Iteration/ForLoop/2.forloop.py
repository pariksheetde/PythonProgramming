# SEQUENCE IS A ORDERED COLLECTION OF ELEMENTS
# IF THE SEQUENCE ISN'T ORDERED, WE COULDN'T REFER THESE ELEMENTS BY THEIR INDEX POSITION
# STRING, LIST and TUPLES ARE SEQUENCE
# STRINGS ARE IMMUTABLE THAT MEANS THEY CANN'T BE CHANGES
# LISTS ARE MUTABLE, THAT MEANS THE VALUE CAN BE CHANGED


for indx in range(0,5):
    indx = indx * indx
    print(f'Value : {indx}')

print()

for i in range(1, 4):
    for j in range(1, i + 1):
        print(i, j, i * j)

print()

# Replace any element lesser than 0 with 0 
data = [10, 20, 30, -10, 40, -5]
for indx in data:
    if indx < 0:
        indx = 0
    print(indx)
print()

for index, value in enumerate('abcdefghijklmnopqrstuvwxyz'):
    print(index + 1,value)