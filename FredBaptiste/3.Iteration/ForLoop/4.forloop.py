# SEQUENCE IS A ORDERED COLLECTION OF ELEMENTS
# STRING, LIST and TUPLES ARE SEQUENCE
# STRINGS ARE IMMUTABLE THAT MEANS THEY CANN'T BE CHANGES
# LISTS ARE MUTABLE, THAT MEANS THE VALUE CAN BE CHANGED


# Replace any element lesser than 0 with 0 using enumerate() 
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
for indx in suits:
    indx = indx.upper()
    print(f'Suits : {indx}')

print()

# Replace any element lesser than 0 with 0 using enumerate() 
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
for suit in suits:
    abbr = suit[0]
    print(abbr, suit)

print()

