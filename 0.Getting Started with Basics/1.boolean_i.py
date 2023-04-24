age = 30
result = age < 15
print(result)

age = 30
result = age < 15 and age > 12
print(result) # Returns False as of the condition is False

age = 30
result = age < 15 and age < 12
print(result) # Returns False as of both the condition are False

age = 30
result = age > 15 and age > 12
print(result) # Returns True as of the condition are True

'''
True & False = False
False & True = False
False & False = False
True & True = True
'''