# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.balance = initial_balance
#     def deposit(self, amount):
#         if amount < 0:
#             print("The amount should be positive")
#         else:
#             self.balance= self.balance+amount
#             # self.balance=depositAmount
#             print(str(amount)+" Rupees deposited " )
#     def withdraw(self, amount):
#          if amount >= self.balance:
#              print("The amount should not be greater than balance")
#          elif amount<0:
#              print("The amount should be positive")
#          else:
#              withdraw= self.balance-amount
#              self.balance = withdraw
#              print("amount withdrawal: ")
#     def check_balance(self):
#         print(self.balance)
#
#
# account = BankAccount(800)
# account.check_balance()
# account.deposit(200)
# account.check_balance()
# account.withdraw((1000))
# account.check_balance()

