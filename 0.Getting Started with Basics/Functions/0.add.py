from math import *

def add(a, b):
    return (a + b)

print(add(7, -5))

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")


def func_1():
    return func_2()

def func_2():
    return "Executing Func_2 inside Func_1"

func_1()

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")


'''
The below code is intentionally throws error because func_3() is called and func_4() is not yet defined
'''
def func_3():
    return func_4()

func_3()

def func_4():
    return "Executing func_4 inside func_3"


print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")
