def add(x: float, y: float = 5.33):
    """This Function Is Used To Perform Addition Of 2 Numbers.
    2nd Parameter Has A Default Value Of 5
    """
    result = (x * y)
    return result

print(f'The result of summation: {add(x = 7)}')
print()

for val in range(1,5):
    resultant = add(val, 2)
    print(f'Result: {resultant}')
print()
