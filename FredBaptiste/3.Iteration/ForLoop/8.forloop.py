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
]
cart = []
while current_choice != '0':
    if current_choice in '123456':
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
    else:
        print("Add option from below list")
        print("1. computer")
        print("2. monitor")
        print("3. keyboard")
        print("4. mouse")
        print("5. mouse mat")
        print("6. hdmi cable")
        print("0. to finish")
    current_choice = input()
print(f'{cart} added to your cart')
print()
