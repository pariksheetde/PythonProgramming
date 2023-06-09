
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

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")

'''
both first_name and last_name are assigned to same memory address. So same memory address will have 2 objects, 
first_name and last_name. When one of the variable or both the variables are descoped, 
those memory address will be later reused by python programming. 
This is called reference counting. This process is taken care by python.
'''

import sys

first_name = "Lara"
last_name = first_name

print(sys.getrefcount(first_name))
print(sys.getrefcount(last_name))

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")

'''
both first_name and last_name are assigned to same memory address. So same memory address will have 2 objects, 
first_name and last_name. When one of the variable or both the variables are descoped, 
those memory address will be later reused by python programming. 
This is called reference counting. This process is taken care by python.
'''

import sys

fruits = ["apple", "banana"]
delicious_fruits = fruits

print(sys.getrefcount(fruits))
print(sys.getrefcount(delicious_fruits))

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")


import ctypes

fruits = ["apple", "banana"]
delicious_fruits = fruits

def ref_count(address):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(fruits)))
print(ref_count(id(delicious_fruits)))

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")
