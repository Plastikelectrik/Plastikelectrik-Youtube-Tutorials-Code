# Step 1: A Class for Accounts
class Account:
    """a bank account: who owns it and how much money it holds"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


ada = Account("Ada", 100)
bob = Account("Bob")
print(ada.owner, "has", ada.balance)
print(bob.owner, "has", bob.balance)
