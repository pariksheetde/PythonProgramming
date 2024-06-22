splittedline = "This senetence has been \nover several line \tto demonstrate how \nsepecial characters work \tin python"
print(splittedline)
print()

stmt = "Pet owner said \"No, no, \'e \'s uh,...he\'s is resting"
print(stmt)
print()

stmt = 'Pet owner said \"No, no, \"e \"s uh,...he\'s is resting'
print(stmt)

sentence = """This line is written over several lines. \
However, while reading this line, the sentence would appear \
in a single line.
"""
print(sentence)

stmt = 'Pet owner said \"No, no, \"e \\\
\"s uh,...he\'s is resting'
print(stmt)

drive = r"D:\Finance\code"
print(f'Drive: {drive}')

name = "Pariksheet"
age = 20
print(name + " is " + str(age) + " " + "years old")
print(f"{name} is {age} years old")
print()

# numeric operator
a = 12
b = 3

print(f'Addition of {a} + {b}: {a + b}')                # 15
print(f'Subtraction of {a} - {b}: {a - b}')             # 9
print(f'Multiplication of {a} * {b}: {a * b}')          # 36
print(f'Division of {a} / {b}: {a / b}')                # 4.0
print(f'Integer Division of {a} // {b}: {a // b}')      # 4
print(f'Modulus of {a} % {b}: {a % b}')                 # 0
print(f'BOSMAS Expression: {(a + b) * (a - b)}')        # 135
print()

# Applying BODMAS
print(f'The Result of Operator Precedence: {a + b / 3 - 4 * 12}')   # (12 + 1 - 48) = -35
print(f'The Result of Operator Precedence: {a + (b / 3) - (4 * 12)}')   # (12 + 1 - 48) = -35
print()