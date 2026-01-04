# Create a custom exception named `InsufficientBalanceError`. In the `BankAccount` class, raise this exception when a withdrawal amount is greater than the balance. Handle the exception and print an appropriate message.

class InsufficientBalanceError(Exception):
    pass
class BankAccount:
    def __init__(self,account_id,balance=0):
        self.__account_id=account_id
        self.__balance=balance
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.__balance}")

    def check_balance(self):
        return self.__balance
account = BankAccount("12345", 1001)
try:
    account.withdraw(1002)
except InsufficientBalanceError as e:
    print(e)
    
        