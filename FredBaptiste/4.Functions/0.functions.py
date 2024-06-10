def add(x, y = 5):
    """This Function Is Used To Perform Addition Of 2 Numbers.
    2Nd Parameter Has A Default Value Of 5
    """
    result = (x * y)
    return result

print(f'The result of summation: {add(y = 7,x = 10)}')
print()

for val in range(1,5):
    resultant = add(val, 2)
    print(f'Result: {resultant}')
print()
