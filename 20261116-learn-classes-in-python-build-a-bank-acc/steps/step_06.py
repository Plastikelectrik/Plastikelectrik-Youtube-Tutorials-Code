# Step 6: A Bank
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


class Bank:
    """all the accounts, found by the name of their owner"""

    def __init__(self):
        self.accounts = {}

    def open(self, owner, savings=False):
        if owner in self.accounts:
            raise ValueError(f"{owner} already has an account")
        account = SavingsAccount(owner) if savings else Account(owner)
        self.accounts[owner] = account
        return account

    def get(self, owner):
        if owner not in self.accounts:
            raise ValueError(f"there is no account for {owner}")
        return self.accounts[owner]

    def transfer(self, source, target, amount):
        self.get(target)
        self.get(source).withdraw(amount)
        self.get(target).deposit(amount)


bank = Bank()
bank.open("Ada").deposit(100)
bank.open("Bob")
bank.transfer("Ada", "Bob", 40)
try:
    bank.transfer("Bob", "Ada", 1000)
except ValueError as error:
    print("Transfer failed:", error)
for account in bank.accounts.values():
    print(account)
