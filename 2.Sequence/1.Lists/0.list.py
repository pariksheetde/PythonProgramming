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

marks.insert(1, 11) # insert element 11 at 2nd index position
print(marks)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

# return those elements which are even number
marks = [10, 20, 15, 25, 30, 35]
for indx in marks:
    if indx % 2 == 0:
        print(indx)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

