age = [10, 20, 30]
marks = age

print(f'Object Reference of {age}: {id(age)}')
print(f'Object Reference of {marks}: {id(marks)}')

def reference_count(address):
    """This function is used to calculate the number of variables object count"""
    import ctypes
    return ctypes.c_long.from_address(address).value

# since, both the lists, age & marks refer to the same object reference, 
# both age & marks will return 2
print(f'Reference Count of Age: {reference_count(id(age))}')        # 2
print(f'Reference Count of Marks: {reference_count(id(marks))}')    # 2

print()

fruits = ['apple', 'guave', 'banana', 'orange']
shopping_fruits = fruits
available_fruits = shopping_fruits

# since, both the lists, fruits, shopping_fruits & available_fruits refer to the same object reference, 
# both fruits, shopping_fruits & available_fruits will return 2
print(f'Reference Count of Fruits: {reference_count(id(fruits))}')                       # 3
print(f'Reference Count of Shopping_Fruits: {reference_count(id(shopping_fruits))}')     # 3
print(f'Reference Count of Available_Fruits: {reference_count(id(available_fruits))}')    # 3

fruits = None
print(f'Reference Count of Fruits: {reference_count(id(fruits))}') 
print(f'Reference Count of Shopping_Fruits: {reference_count(id(shopping_fruits))}') 
print(f'Reference Count of Available_Fruits: {reference_count(id(available_fruits))}')

print()

