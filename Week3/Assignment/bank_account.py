class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")


account = BankAccount("Ankita", 5000)

account.deposit(2000)

account.withdraw(1000)

account.display_balance()