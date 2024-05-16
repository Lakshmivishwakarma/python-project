class BankAccount:
    def __init__(self, initBalance=0):
        self.balance = initBalance
    def deposit(self, amount):
        if amount < 0:
            print("The amount should be positive")
        else:
            self.balance= self.balance+amount
            # self.balance=depositAmount
            print("amount deposited: " + str(amount))
    def withdraw(self, amount):
         if amount>=self.balance:
             print("The amount should not be greater than balance")
         elif amount<0:
             print("The amount should be positive")
         else:
             withdraw= self.balance-amount
             self.balance = withdraw
             print("amount withdrawal: ")
    def checkRemainingalance(self):
        print(self.balance)


account = BankAccount(800)
account.checkRemainingalance()
# BankAccount.check_balance(account)
account.deposit(200)
account.checkRemainingalance()
account.withdraw((1000))
account.checkRemainingalance()