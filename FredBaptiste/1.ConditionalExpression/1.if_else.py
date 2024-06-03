account_enabled = True
balance = 1000
withdraw = 1000_00
if account_enabled and withdraw <= balance:
    print(f'You can withdraw {withdraw}')
else:
    print(f'Not authorised to withdraw {withdraw}')
print(f'1st program execution completed')

print('---------------------------------------------------------------------------------------------------------------------------')

account_enabled = True
balance = 1000
withdraw = 1000
if account_enabled and withdraw <= balance:
    print(f'You can withdraw {withdraw}')
else:
    print(f'Not authorised to withdraw {withdraw}')
print(f'2nd program execution completed')

print('---------------------------------------------------------------------------------------------------------------------------')

account_enabled = False
balance = 1000
withdraw = 1000_00
if account_enabled and withdraw <= balance:
    print(f'You can withdraw {withdraw}')
else:
    print(f'Not authorised to withdraw {withdraw}')
print(f'3rd program execution completed')

print('---------------------------------------------------------------------------------------------------------------------------')

account_enabled = True
balance = 1000
withdraw = 1000_00
if account_enabled and withdraw <= balance:
    print(f'You can withdraw {withdraw}')
else:
    if not account_enabled:
        print(f'Account is disabled')
    else:
        print(f'Insufficient Fund')
print(f'4th program execution completed')