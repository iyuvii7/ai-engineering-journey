class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit Balance cannot be negative.")
        else:
            self.balance += amount
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal Balance cannot be negative.")
        elif amount > self.balance:
            raise ValueError("Withdrawal Balance cannot be more than the Balance.")
        self.balance -= amount
    def display_balance(self):
        print(f"Balance: ₹{self.balance}")

account = BankAccount("Yuvraj", 1000)

account.deposit(500)
account.withdraw(200)

account.display_balance()