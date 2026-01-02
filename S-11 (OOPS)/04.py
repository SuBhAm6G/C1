### Assignment 4: Class with Private Attributes

# Create a class named `BankAccount` with private attributes `account_number` and `balance`. Add methods to deposit and withdraw money, and to check the balance. Create an object of the class and perform some operations.

class BankAccount:
    def __init__(self,account_number,balance):
        self.accout_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited: {amount}. New balance: {self.balance}")
    def withdrawal(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance")
    def check_balance(self):
        print(f"Current balance: {self.balance}")

account1=BankAccount("123456789",1000)
account1.check_balance()
account1.deposit(500)
account1.withdrawal(200)
account1.check_balance()
account1.withdrawal(2000)