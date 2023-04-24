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
True or False = True
False or True = False
False or False = False
True or True = True
'''