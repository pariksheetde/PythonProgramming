'''
lambda expression
A lambda function is a small anonymous function. Python Lambda Functions are anonymous
function means that the function is without a name.
'''

'''
id() function returns base 13 number, and if you want, use built-in hex() function in python
'''

fn_1 = lambda x: x + 2
print(fn_1)
print(f"The result of lambda expression : {fn_1(7)}")
print(f"Returns Memory Address : {id(fn_1)}")  # id() function returns memory address of a variable
print(f"Returns Hexadecimal Memory Address : {hex(id(fn_1))}")  # hex() function returns hexadecimal memory address of a variable

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")

'''
id() function returns base 13 number, and if you want, use built-in hex() function in python
'''

fn_2 = lambda x, y : x + y
print(f"The result of lambda expression : {fn_2(-7,2)}")
print(f"Returns Memory Address : {id(fn_2)}") # id() function returns memory address of a variable
print(f"Returns Hexadecimal Memory Address : {hex(id(fn_2))}") # hex() function returns hexadecimal memory address of a variable

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")

