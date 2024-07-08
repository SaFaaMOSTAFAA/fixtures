class Bank_Acccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

        return self.balance
