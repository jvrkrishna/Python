class Bank:
    KEY = 2024

    def __init__(self):
        self.balance = 1000
        self.count = 0

    def login(self):
        while self.count < 3:
            password = int(input("Please enter the password to login: "))

            if password == Bank.KEY:
                print("Congrats! You successfully logged in...\n")
                break
            else:
                self.count += 1
                print("Entered password is wrong... Please try again")

        if self.count == 3:
            print("Sorry! You have entered the wrong password 3 times.")
            print("Please try again after 24 hours.")
            exit(0)

        print("Welcome to the Bank")
        name = input("Enter your name: ")
        print(f"Hi {name}, welcome to the bank...\n")
        self.ask()

    def ask(self):
        while True:
            print("\nHow may I help you?")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.deposit()

            elif choice == 2:
                self.withdraw()

            elif choice == 3:
                self.check_balance()

            elif choice == 4:
                print("Thank you for using the bank service.")
                exit(0)

            else:
                print("Invalid choice. Please try again.")

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))

        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print("Amount deposited successfully!")
            print("Current balance:", self.balance)

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))

        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print("Current balance:", self.balance)


# --------- Run Program ---------
b = Bank()
b.login()
