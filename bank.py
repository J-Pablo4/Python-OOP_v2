class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
        
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient funds or invalid withdrawl amount")
        
    def get_balance(self):
        return self.__balance
    
account = BankAccount("Alice", 1000)
account.deposit(500)

# Accesing a private method incorrectly
# print(account.__balance)

print(account.get_balance())