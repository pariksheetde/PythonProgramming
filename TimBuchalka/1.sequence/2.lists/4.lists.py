available_parts = [
    'computer', 
    'monitor', 
    'keyboard', 
    'mouse', 
    'mouse mat',
    "DVD drive",
    'hdmi cable'
    ]
current_choice = '-'
computer_parts = []

while current_choice != '0':
    if current_choice in "1234567":
        print(f'Adding {current_choice}')
        if current_choice == '1':
            computer_parts.append('computer')
        elif current_choice == '2':
            computer_parts.append('monitor')
        elif current_choice == '3':
            computer_parts.append('keyboard')
        elif current_choice == '4':
            computer_parts.append('mouse')
        elif current_choice == '5':
            computer_parts.append('mouse mat')
        elif current_choice == '6':
            computer_parts.append('DVD drive')
        elif current_choice == '7':
            computer_parts.append('hdmi cable')
    else:
        print("Add option from below list")
        for index, part in enumerate(available_parts):
            print(f'{index + 1}: {part}')
    current_choice = input()
    print(f'{computer_parts} added to your cart')

print()