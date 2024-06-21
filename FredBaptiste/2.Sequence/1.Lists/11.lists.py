my_lst = range(0,11)
my_lst = list(my_lst)
my_lst = my_lst[2::2]
print(my_lst)
# my_lst[2::2] = [0]  # WILL NOT WORK BECAUSE NUMBER OF SLICES DIFFER FROM SIZE
print(my_lst)
print()


my_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Elements that will be updated, my_lst: {my_lst[2::2]}')
my_lst[2::2] = [100, 200, 300, 400, 500]
print(f'After Change, my_lst: {my_lst}')
print()

delta = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(delta[:-3:-1])
delta[:-3:-1] = [101, 202]
print(f'After Change, delta: {delta}')
print()

llm = [1, 2, 3, 4, 5, 6]
# display only odd elements by deleting unwanted elements
del llm[::2]
print(f'After Removing Odd Elements: {llm}')
print()

# extend() and append()
# append() can take 1 element at a time, whereas extend() can take multiple elements
grades = [1, 2, 3, 4]
grades.extend([5, 6, 7, 8])
print(grades)
print()
