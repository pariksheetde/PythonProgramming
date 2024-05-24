# STRINGS ARE HOMOGENEOUS, IMMUTABLE
EOL = "----"
name = 'pariksheet'
print(f'Length : {len(name)}')

print(EOL * 37)

EOL = "----"
stmt = "What's in a name. This was stated by William Shakesphere"
print(f'Statement : {stmt}')

print(EOL * 37)

EOL = "----"
line = 'What\'s in a name. This was stated by William Shakesphere'
print(f'Line : {line}')

print(EOL * 37)

EOL = "----"
quote = "What\"s in a name. This was stated by William Shakesphere"
print(f'Quote : {quote}')

print(EOL * 37)

EOL = "----"
word = "What\"s in a name. This was stated by William Shakesphere"
print(word.split(" "))
print(f'Type : {type(word.split(" "))}')

print(EOL * 37)
