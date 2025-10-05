class BankAccount:
    def __init__(self, account_balance=0.0):
        """Initialize a bank account with an optional starting balance (default = 0.0)."""
        self.account_balance = float(account_balance)

    def deposit(self, amount):
        """Deposit money into the account if the amount is positive."""
        amount = float(amount)
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist."""
        amount = float(amount)
        if amount > self.account_balance:
            print("Insufficient funds.")
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")