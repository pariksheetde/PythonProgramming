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
