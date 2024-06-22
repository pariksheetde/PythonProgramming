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