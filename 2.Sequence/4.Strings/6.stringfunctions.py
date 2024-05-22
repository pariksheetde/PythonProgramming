EOL = "----"
stmt = 'To every action there is always an equal and opposite reaction'
print(f'Find the index position of reaction : {stmt.index("reaction")}')
print(f'Find the index position of reaction : {stmt.find("same")}')

print(EOL * 37)

quote = 'To every action there is always an equal and opposite reaction'
print(f'Find the index position of action : {quote.index("reaction") + len("action")}')
print(f'Find the index position of action : {quote.find("same")}')
