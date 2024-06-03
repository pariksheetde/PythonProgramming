# SEQUENCE IS A ORDERED COLLECTION OF ELEMENTS
# IF THE SEQUENCE ISN'T ORDERED, WE COULDN'T REFER THESE ELEMENTS BY THEIR INDEX POSITION
# STRING, LIST and TUPLES ARE SEQUENCE
# STRINGS ARE IMMUTABLE THAT MEANS THEY CANN'T BE CHANGES
# LISTS ARE MUTABLE, THAT MEANS THE VALUE CAN BE CHANGED

current_choice = '-'
computer_parts = [
    'computer',
    'monitor',
    'keyboard',
    'mouse',
    'mouse mat',
    'hdmi cable',
    'DVD drive',
]
cart = []
# valid_choice = [str(i) for i in range(1, len(computer_parts) + 1)]
# print('Valid Choice {}'.format(valid_choice))
valid_choice = []
for i in range(1, len(computer_parts) + 1):
    valid_choice.append(str(i))
print('Valid Choice {}'.format(valid_choice))
while current_choice != '0':
    if current_choice in valid_choice:
        print('Adding {}'.format(current_choice))
        if current_choice == '1':
            cart.append('computer')
        if current_choice == '2':
            cart.append('monitor')
        if current_choice == '3':
            cart.append('keyboard')
        if current_choice == '4':
            cart.append('mouse')
        if current_choice == '5':
            cart.append('mouse mat')
        if current_choice == '6':
            cart.append('hdmi cable')
        if current_choice == '7':
            cart.append('DVD drive')
    else:
        print("Add option from below list")
        for index, value in enumerate(computer_parts):
            print("{0}: {1}".format(index + 1, value)) # THIS LINE OF CODE has been modified USING ENUMERATE FUNCTION 
    current_choice = input()
print(f'{cart} added to your cart')
print()
