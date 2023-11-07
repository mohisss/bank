This Python code implements a simple banking system with a command-line interface. Here’s a breakdown of its functionality:

BankAccount class: This class represents a bank account. It has methods to deposit and withdraw money, check the balance, view transaction history, print a statement, print a summary, close the account, and check if the account is closed.

ensure_balance decorator: This decorator ensures that there is enough balance in the account before a withdrawal operation.

measure_time decorator: This decorator measures the execution time of deposit and withdrawal operations.

menu function: This function provides a command-line interface for the user to interact with their bank account. It allows the user to choose from various options like depositing money, withdrawing money, checking balance, viewing transaction history, printing a statement, printing a summary, closing the account, and checking if the account is closed.

The program starts by creating a BankAccount object and then enters a loop where it continually asks the user for their choice of operation until they choose to exit. The corresponding methods of the BankAccount class are called based on the user’s choice. If the user chooses to exit, the loop breaks and the program ends.
