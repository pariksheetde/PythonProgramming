odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8]
# Below code will create Nested List
lst = [odd, even]
print('New List : {}'.format(lst))
print()

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8]
# Below code will break nested list into individual elements
lst = [odd, even]
for number in lst:
    for value in number:
        print(value)
print()

