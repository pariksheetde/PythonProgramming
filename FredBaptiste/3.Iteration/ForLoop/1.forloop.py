# SEQUENCE IS A ORDERED COLLECTION OF ELEMENTS
# IF THE SEQUENCE ISN'T ORDERED, WE COULDN'T REFER THESE ELEMENTS BY THEIR INDEX POSITION
# STRING, LIST and TUPLES ARE SEQUENCE
# STRINGS ARE IMMUTABLE THAT MEANS THEY CANN'T BE CHANGES
# LISTS ARE MUTABLE, THAT MEANS THE VALUE CAN BE CHANGED


for i in [1, 2]:
    i = i
    print(f'i : {i}')
print()

for i in [1, 2]:
    i = i + i
    print(f'i : {i}')
print()

for i in range(0, 10, 2):
    i = i + i
    print(f'i : {i}')
print()

for i in ['a', 'b']:
    j = i + i
    print(f'j : {j}')
print()