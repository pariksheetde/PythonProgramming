'''
Ternary Operator. Also known as conditional expression
'''
marks = 50

grade = "Grade A" if marks >=45 else "Grade B"
print(grade)

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")


marks = 21

if marks >= 45:
    print("A")
elif marks <= 40 and marks >= 30:
    print("B")
elif marks <= 30 and marks >= 21:
    print("C")
elif marks <= 20:
    print("Fail")
    
print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")


age = 4

if age < 5:
    print(f'{age} is less than 5')
else:
    print(f'{age} is greater than 5')
    
    
print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")

'''
Ternary Operator. Also known as conditional expression
'''

age = 18

status = "Minor" if age < 18 else "Adult"
print(status)

print("-------------------------------------------------------------------------------EOL-----------------------------------------------------------------------------")
