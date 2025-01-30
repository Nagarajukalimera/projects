class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

    def display_account(self):
        return f"Account Number: {self.account_number} | Name: {self.name} | Balance: {self.balance}"

class BankManagementSystem:
    def __init__(self):
        self.accounts = []
        self.next_account_number = 1000  # Starting account number
    
    def create_account(self):
        name = input("Enter your name: ")
        initial_deposit = float(input("Enter initial deposit: "))
        account = BankAccount(self.next_account_number, name, initial_deposit)
        self.accounts.append(account)
        print(f"Account created successfully! Your account number is {self.next_account_number}")
        self.next_account_number += 1
    
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def deposit(self):
        account_number = int(input("Enter account number to deposit to: "))
        account = self.find_account(account_number)
        if account:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        else:
            print("Account not found.")
    
    def withdraw(self):
        account_number = int(input("Enter account number to withdraw from: "))
        account = self.find_account(account_number)
        if account:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        else:
            print("Account not found.")
    
    def view_balance(self):
        account_number = int(input("Enter account number to view balance: "))
        account = self.find_account(account_number)
        if account:
            print(f"Your balance is {account.get_balance()}")
        else:
            print("Account not found.")

    def view_account_details(self):
        account_number = int(input("Enter account number to view details: "))
        account = self.find_account(account_number)
        if account:
            print(account.display_account())
        else:
            print("Account not found.")
    
    def close_account(self):
        account_number = int(input("Enter account number to close: "))
        account = self.find_account(account_number)
        if account:
            self.accounts.remove(account)
            print(f"Account {account_number} closed successfully.")
        else:
            print("Account not found.")
    
    def show_menu(self):
        print("\n===== Bank Management System =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. View Account Details")
        print("6. Close Account")
        print("7. Exit")
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.view_balance()
            elif choice == "5":
                self.view_account_details()
            elif choice == "6":
                self.close_account()
            elif choice == "7":
                print("Exiting Bank Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select again.")

if __name__ == "__main__":
    system = BankManagementSystem()
    system.run()
