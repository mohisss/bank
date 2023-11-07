import time
from datetime import datetime

def ensure_balance(func):
    def wrapper(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance.")
        return func(self, amount)
    return wrapper

def measure_time(func):
    def wrapper(self, amount):
        start_time = time.time()
        result = func(self, amount)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transactions = []
        self.is_closed = False

    @measure_time
    def deposit(self, amount):
        if self.is_closed:
            raise ValueError("Account is closed.")
        self.balance += amount
        self.transactions.append({'type': 'Deposit', 'amount': amount, 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

    @ensure_balance
    @measure_time
    def withdraw(self, amount):
        if self.is_closed:
            raise ValueError("Account is closed.")
        self.balance -= amount
        self.transactions.append({'type': 'Withdrawal', 'amount': amount, 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

    def get_balance(self):
        if self.is_closed:
            raise ValueError("Account is closed.")
        return self.balance

    def get_transactions(self):
        if self.is_closed:
            raise ValueError("Account is closed.")
        return self.transactions

    def print_statement(self):
        if self.is_closed:
            raise ValueError("Account is closed.")
        print("Transaction Details:")
        for transaction in self.transactions:
            print(f"{transaction['type']}: {transaction['amount']} at {transaction['timestamp']}")
        print(f"Current Balance: {self.balance}")

    def print_summary(self):
        if self.is_closed:
            raise ValueError("Account is closed.")
        print(f"Account Details:")
        print(f"Current Balance: {self.balance}")
        print(f"Number of Transactions: {len(self.transactions)}")

    def close_account(self):
        self.balance = 0
        self.transactions.clear()
        self.is_closed = True

    def is_account_closed(self):
        return self.is_closed

def menu():
    account = BankAccount()
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transaction History\n5. Print Statement\n6. Print Summary\n7. Close Account\n8. Check if Account is Closed\n9. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
            
        elif choice == 2:
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
            
        elif choice == 3:
            print(f"Current Balance: {account.get_balance()}")
            
        elif choice == 4:
            transactions = account.get_transactions()
            for transaction in transactions:
                print(transaction)
                
        elif choice == 5:
            account.print_statement()
            
        elif choice == 6:
            account.print_summary()
            
        elif choice == 7:
            account.close_account()
            
        elif choice == 8:
            if account.is_account_closed():
                print("The account is closed.")
            else:
                print("The account is open.")
                
        elif choice == 9:
            break
            
if __name__ == "__main__":
    menu()
