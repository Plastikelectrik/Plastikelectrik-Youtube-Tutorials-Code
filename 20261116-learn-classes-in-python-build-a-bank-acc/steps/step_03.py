# Step 3: Rules and Errors
class Account:
    """a bank account: who owns it and how much money it holds"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("the amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("the amount must be positive")
        if amount > self.balance:
            raise ValueError(f"not enough money: {self.owner} has {self.balance}")
        self.balance -= amount


ada = Account("Ada", 100)
bob = Account("Bob")
ada.deposit(50)
ada.withdraw(30)
bob.deposit(20)
try:
    bob.withdraw(500)
except ValueError as error:
    print("Could not withdraw:", error)
print(ada.owner, "has", ada.balance)
print(bob.owner, "has", bob.balance)
