age = 11

if age < 10:
    print(f'{age} is less than 10')
if age > 10 :
    print(f'{age} is greater than 10')
if age == 10:
    print(f'{age} is same as 10')
    
print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")

    
age = 1

if age < 5:
    print(f'{age} is less than 5')
elif age > 5:
    print(f'{age} is greater than 5')
elif age <= 5:
    print(f'{age} is same as 5')
    
print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")

'''
Ternary Operator. Also known as conditional expression
'''
marks = 50

grade = "A" if marks >=45 else "B"
print(grade)

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")
