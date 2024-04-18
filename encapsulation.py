class BankAccount:
    def __init__(self):
        self.__balance = 0    # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

my_account = BankAccount()
my_account.deposit(1000)
print(my_account.get_balance())  # Output: 1000
# Attempting to access the private attribute directly will result in an AttributeError
# print(my_account.__balance)  # Error: 'BankAccount' object has no attribute '__balance'
