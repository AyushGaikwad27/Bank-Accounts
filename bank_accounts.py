class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name} created.\nBalance = ₹{self.balance:.2f}")
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ₹ {self.balance:.2f}")
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete. ")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ₹{self.balance:.2f}"
            )
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw Interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer.. 🚀🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!✅\n\n**********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌ {error}')
class InterestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self .balance + (amount * 1.5)
        print("\nDeposit Complete.")
        self.getBalance()

class SavingsAccount(InterestRewardAcc):
    def __init__(self, initialAmount, accountName):
        super().__init__(initialAmount, accountName)
        self.fee = 5
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

