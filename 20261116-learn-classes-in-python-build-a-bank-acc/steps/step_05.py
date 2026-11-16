# Step 5: Inheritance
class Account:
    """a bank account: who owns it and how much money it holds"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("the amount must be positive")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("the amount must be positive")
        if amount > self.balance:
            raise ValueError(f"not enough money: {self.owner} has {self.balance}")
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def __str__(self):
        return f"{self.owner}: {self.balance:.2f}"


class SavingsAccount(Account):
    """an account that earns interest"""

    def __init__(self, owner, balance=0, rate=0.02):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = round(self.balance * self.rate, 2)
        self.deposit(interest)
        return interest


ada = Account("Ada", 100)
bob = Account("Bob")
ada.deposit(50)
ada.withdraw(30)
bob.deposit(20)
try:
    bob.withdraw(500)
except ValueError as error:
    print("Could not withdraw:", error)
carla = SavingsAccount("Carla", 1000, rate=0.03)
print("Carla earns", carla.add_interest())
print(ada)
print(bob)
print(carla)
for kind, amount in ada.history:
    print(f"  {kind:<10}{amount:>8.2f}")
