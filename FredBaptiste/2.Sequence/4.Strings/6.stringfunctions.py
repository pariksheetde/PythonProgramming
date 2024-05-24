EOL = "----"
stmt = 'To every action there is always an equal and opposite reaction'
print(f'Find the index position of reaction : {stmt.index("reaction")}')
print(f'Find the index position of reaction : {stmt.find("same")}')

print(EOL * 37)

quote = 'To every action there is always an equal and opposite reaction'
print(f'Find the index position of action : {quote.index("reaction") + len("action")}')
print(f'Find the index position of action : {quote.find("same")}')

print(EOL * 37)

# STRING INTERPOLATION using format()
name = 'Pariksheet De'
country = 'Indian'

print('My name is {} and I am an {}'.format(name, country))
print(f'My name is {name} and I am an {country}')

print(EOL * 37)