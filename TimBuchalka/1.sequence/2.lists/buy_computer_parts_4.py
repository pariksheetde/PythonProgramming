available_parts = [
    'Computer', 
    'Monitor', 
    'Keyboard', 
    'Mouse', 
    'Mouse Mat', 
    'DVD Drive',
    'HDMI Cable']
# valid_choice = [str(i) for i in range(1, len(available_parts) + 1)]
another_valid_choice = []
for indx in range(1, len(available_parts) + 1):
    another_valid_choice.append(str(indx))
print(another_valid_choice)
current_choice = '-'
computer_parts = []

while current_choice != '0':
    if current_choice in another_valid_choice:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print(f'Removing: {current_choice}')
            computer_parts.remove(chosen_part)
        else:
            print(f'Adding {current_choice}')
            computer_parts.append(chosen_part)
        print(f"Your cart now contains: {chosen_part}")
    else:
        print("Add option from below list")
        for index, part in enumerate(available_parts):
            print(f'{index + 1}: {part}')
    current_choice = input()
    print(f'{computer_parts} added to your cart')

print()