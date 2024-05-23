EOL = "----"
# Replace any element lesser than 0 with 0 using enumerate() 
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
for indx in suits:
    indx = indx.upper()
    print(f'Suits : {indx}')

print(EOL * 37)

# Replace any element lesser than 0 with 0 using enumerate() 
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
for suit in suits:
    abbr = suit[0]
    print(abbr, suit)

print(EOL * 37)

