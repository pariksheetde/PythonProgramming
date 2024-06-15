account_enabled = True
available_balance = 10000
withdraw = 101

if account_enabled:
    if withdraw <= available_balance:
        print(f"You can withdraw the cash. Withdrawl amount {withdraw} INR")
    else:
        print(f"Cash withdrawl has exeeds the available balance by {withdraw - available_balance} INR")
else:
    print("First enable the account!")
print()

account_enabled = False
available_balance = 10000
withdraw = 101000

if account_enabled and withdraw <= available_balance:
    print("Authorized to withdraw cash")
else:
    if not account_enabled:
        print("Not authorized because account is not enabled")
    elif withdraw > available_balance:
        print(f"Withdrawl amaount excceded by {withdraw - available_balance}")
print()
