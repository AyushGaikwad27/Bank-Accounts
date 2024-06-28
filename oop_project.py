from bank_accounts import *

Ayush = BankAccount(10000, "Ayush")
Ronnie = BankAccount(20000, "Ronnie")

Ayush.getBalance()
Ronnie.getBalance()

Ayush.deposit(1000)

Ronnie.withdraw(30000)
Ronnie.withdraw(5000)

Ayush.transfer(50000, Ronnie)
Ayush.transfer(1000, Ronnie)

Pratik = InterestRewardAcc(10000, "Pratik")

Pratik.getBalance
Pratik.deposit(1000)

Pratik.transfer(1000, Ayush)

Zombie = SavingsAccount(10000, "Zombie")
Zombie.getBalance()
Zombie.deposit(1000)
Zombie.transfer(10000, Ronnie)