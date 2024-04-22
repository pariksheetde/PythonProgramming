# Create a list og int type.
# This list is homogeneous.
# List can be homogeneous and hetrogeneous
marks = [10, 20, 15, 25, 30, 35]
print(marks)

print(marks[0]) # returns 1st element
print(marks[:]) # returns all the elements
print(marks[:-1]) # returns the elements from 1st index position till 2nd last. -1 ignore the last element
print(marks[-1]) # returns the last element.

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

marks = [10, 20, 15, 25, 30, 35]

marks.insert(1, 11) # insert method adds the element at the specified index position
print(f'After Insert :{marks}')

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

marks = [10, 20, 15, 25, 30, 35]

marks.remove(10) # remove method removes the specified element from the list
print(f'After Remove :{marks}')

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

marks = [10, 20, 15, 25, 30, 35]

print(f'Element Deleted : {marks.pop()}')  # pop method by default removes the last element from the list
print(f'After 2nd Pop : {marks.pop(2)}') # pop method can remove the element by specifying the index position

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

# return those elements which are even number
marks = [10, 20, 15, 25, 30, 35]
for indx in marks:
    if indx % 2 == 0:
        print(indx)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

