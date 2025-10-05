class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize a bank account with an optional starting balance."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__account_balance = initial_balance  # private attribute

    def deposit(self, amount):
        """Deposit money into the account if the amount is positive."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__account_balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist. Return True if successful, else False."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__account_balance:
            print("Insufficient funds.")
            return False
        self.__account_balance -= amount
        print(f"Withdrew: ${amount:.2f}")
        return True

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

    def get_balance(self):
        """Return the current balance (read-only)."""
        return self.__account_balance
