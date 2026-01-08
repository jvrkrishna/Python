balance = 1000
count = 0
KEY = 2024


def Bank():
    global count

    while count < 3:
        password = int(input("Please enter the password to login: "))

        if password == KEY:
            print("Congrats! You successfully logged in...\n")
            break
        else:
            count += 1
            print("Entered password is wrong... Please try again")

    if count == 3:
        print("Sorry! You have entered the wrong password 3 times.")
        print("Please try again after 24 hours.")
        exit(0)

    print("Welcome to the Bank")
    name = input("Enter your name: ")
    print(f"Hi {name}, welcome to the bank...\n")
    ask()


def ask():
    while True:
        print("\nHow may I help you?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            Deposit()

        elif choice == 2:
            Withdraw()

        elif choice == 3:
            Check_Balance()

        elif choice == 4:
            print("Thank you for using the bank service.")
            exit(0)

        else:
            print("Invalid choice. Please try again.")


def Deposit():
    global balance
    amount = int(input("Enter the amount to deposit: "))

    if amount <= 0:
        print("Deposit amount must be positive.")
    else:
        balance += amount
        print("Amount deposited successfully!")
        print("Current balance:", balance)


def Withdraw():
    global balance
    amount = int(input("Enter the amount to withdraw: "))

    if amount <= 0:
        print("Withdrawal amount must be positive.")
    elif amount <= balance:
        balance -= amount
        print("Withdrawal successful!")
        print("Current balance:", balance)
    else:
        print("Insufficient balance.")


def Check_Balance():
    print("Current balance:", balance)


Bank()
