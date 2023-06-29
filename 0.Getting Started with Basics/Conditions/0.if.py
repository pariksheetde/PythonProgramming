age = 11

if age < 10:
    print(f'{age} is less than 10')
if age > 10 :
    print(f'{age} is greater than 10')
if age == 10:
    print(f'{age} is same as 10')
    
print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")

    
age = 1

if age < 5:
    print(f'{age} is less than 5')
elif age > 5:
    print(f'{age} is greater than 5')
elif age <= 5:
    print(f'{age} is same as 5')
    
print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")

'''
Ternary Operator. Also known as conditional expression
'''
marks = 50

grade = "A" if marks >=45 else "B"
print(grade)

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")

'''
both age and marks are assigned to same memory address. So same memory address will have 2 objects, 
age and marks. When one of the variable or both the variables are descoped, 
those memory address will be later reused by python programming. 
This is called reference counting. This process is taken care by python.
'''

import sys

age = 10
marks = age
print(id(age))
print(id(marks))

print(sys.getrefcount(age))
print(sys.getrefcount(marks))