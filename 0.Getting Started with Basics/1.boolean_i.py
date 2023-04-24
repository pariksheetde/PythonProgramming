age = 30
result = age < 15
print(result)

age = 30
result = age < 15 and age > 12
print(result) # RETURNS FALSE AS 1 OF THE CONDITION IS FALSE

age = 30
result = age < 15 and age < 12
print(result) # RETURNS FALSE AS 1 OF THE CONDITION IS FALSE

age = 30
result = age > 15 and age > 12
print(result) # RETURNS TRUE AS BOTH THE CONDITIONS ARE TRUE

'''
True & False = False
False & True = False
False & False = False
True & True = True
'''