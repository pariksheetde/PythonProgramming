age = 30
result = age < 15
print(result)

age = 30
result = age < 15 or age > 12 # False OR True
print(result) # Returns True as 1 of the condition is True

age = 30
result = age < 15 or age < 12 # False OR False
print(result) # Returns False as both the conditions are False

age = 30
result = age > 15 or age > 12
print(result) # Returns True as both the conditions are True

'''
True & False = False
False & True = False
False & False = False
True & True = True
'''