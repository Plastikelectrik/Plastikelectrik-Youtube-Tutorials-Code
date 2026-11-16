# Step 2: Methods
class Account:
    """a bank account: who owns it and how much money it holds"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


ada = Account("Ada", 100)
bob = Account("Bob")
ada.deposit(50)
ada.withdraw(30)
bob.deposit(20)
print(ada.owner, "has", ada.balance)
print(bob.owner, "has", bob.balance)
