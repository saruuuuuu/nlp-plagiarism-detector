class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")

def main():
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")
    account = BankAccount(account_number, account_holder)

    while True:
        print("\nBanking Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Current balance: ${account.balance}.")
        elif choice == '4':
            print("Exiting banking system.")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
