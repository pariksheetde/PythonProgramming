available_parts = ['computer', 'monitor', 'keyboard', 'mouse', 'mouse mat']
valid_choice = [str(i) for i in range(1, len(available_parts) + 1)]
another_valid_choice = []
for indx in range(1, len(available_parts) + 1):
    another_valid_choice.append(str(indx))
print(another_valid_choice)
current_choice = '-'
computer_parts = []

while current_choice != '0':
    if current_choice in another_valid_choice:
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
            computer_parts.append('hdmi')
    else:
        print("Add option from below list")
        for index, part in enumerate(available_parts):
            print(f'{index + 1}: {part}')
    current_choice = input()
    print(f'{computer_parts} added to your cart')