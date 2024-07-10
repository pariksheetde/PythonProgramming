class BankAccount:

    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount

class CheckingAccount(BankAccount):

    def __init__(self, number, balance, fixed_deposit):
        BankAccount.__init__(self, number, balance)
        self.fixed_deposit = fixed_deposit

    def withdraw(self, amount):
        if amount > (self.balance + self.fixed_deposit):
            print(f"Insufficient Balance. Available Balance: {self.balance + self.fixed_deposit}")
        else:
            print(f"You have withdrawn: {amount}")
            available_balance = (self.balance - amount)
            print(f'Available Balance: {available_balance}. FD Balance: {self.fixed_deposit}')

check_account = CheckingAccount("97791", 125000, 45000)
print(f'Account NO: {check_account.number} has balance of {check_account.balance}. FD Balance: {check_account.fixed_deposit}')

check_account.withdraw(75000)