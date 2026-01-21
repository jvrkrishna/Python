"""
🏦 Bank Management System (OOP)
----------------------------------------
This program allows:
✔ Create account
✔ Login with PIN
✔ Deposit / Withdraw
✔ Check balance
✔ Transaction History
✔ Auto-save to JSON file
----------------------------------------
Author: RK
"""

import json
import os
import time
from datetime import datetime
from getpass import getpass


DATA_FILE = "bank_data.json"   # File to store account data


# ============================================================
# 📌 ACCOUNT CLASS
# ============================================================
class Account:
    """
    Represents a single bank account.
    Holds: Name, Account No, PIN, Balance, Transactions.
    """

    def __init__(self, acc_no, name, pin, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transactions = []
        self.failed_attempts = 0
        self.locked_until = 0  # time until locked

    def check_pin(self, pin):
        """Check PIN with 3-attempt lock system."""

        # If account is locked
        now = time.time()
        if now < self.locked_until:
            print("⛔ Account temporarily locked! Try again later.")
            return False

        # PIN correct
        if pin == self.pin:
            self.failed_attempts = 0
            return True

        # PIN incorrect
        self.failed_attempts += 1
        print("❌ Incorrect PIN!")

        if self.failed_attempts == 3:
            self.locked_until = now + 30  # lock 30 seconds
            print("⛔ Account locked for 30 seconds.")

        return False

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(
            {"type": "DEPOSIT", "amount": amount, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance!")

        self.balance -= amount
        self.transactions.append(
            {"type": "WITHDRAW", "amount": amount, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )

    def to_dict(self):
        """Convert object to dictionary to store in JSON."""
        return {
            "acc_no": self.acc_no,
            "name": self.name,
            "pin": self.pin,
            "balance": self.balance,
            "transactions": self.transactions,
            "failed_attempts": self.failed_attempts,
            "locked_until": self.locked_until,
        }

    @staticmethod
    def from_dict(data):
        """Convert JSON dict back to Account object."""
        acc = Account(data["acc_no"], data["name"], data["pin"], data["balance"])
        acc.transactions = data["transactions"]
        acc.failed_attempts = data.get("failed_attempts", 0)
        acc.locked_until = data.get("locked_until", 0)
        return acc


# ============================================================
# 📌 BANK CLASS
# ============================================================
class Bank:
    """Manages all accounts."""

    def __init__(self):
        self.accounts = {}
        self.load_data()

    def load_data(self):
        """Load account data from JSON file."""
        if not os.path.exists(DATA_FILE):
            return

        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        for acc_no, acc_data in data.items():
            self.accounts[int(acc_no)] = Account.from_dict(acc_data)

    def save_data(self):
        """Save all account data to JSON file."""
        data = {acc_no: acc.to_dict() for acc_no, acc in self.accounts.items()}
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def create_account(self, name, pin, balance=0):
        """Create new account."""
        acc_no = max(self.accounts.keys(), default=1000) + 1
        acc = Account(acc_no, name, pin, balance)
        self.accounts[acc_no] = acc
        self.save_data()
        return acc

    def authenticate(self, acc_no, pin):
        """Verify account number & PIN."""
        acc = self.accounts.get(acc_no)
        if not acc:
            print("❌ Account not found!")
            return None

        if acc.check_pin(pin):
            return acc

        return None


# ============================================================
# 📌 MENU / PROGRAM INTERFACE
# ============================================================
def main_menu():
    print("\n------------------------------")
    print("🏦 WELCOME TO RK BANK SYSTEM")
    print("------------------------------")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")


def account_menu(name):
    print(f"\n--- Welcome {name} ---")
    print("1. Balance Enquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Logout")


# ============================================================
# 📌 MAIN APPLICATION LOOP
# ============================================================
def run_bank():
    bank = Bank()

    while True:
        main_menu()

        choice = input("Choose option: ")

        # ----------------------------------------------------
        # Create New Account
        # ----------------------------------------------------
        if choice == "1":
            name = input("Enter your name: ")
            pin = input("Set 4-digit PIN: ")
            initial = int(input("Initial deposit: "))
            acc = bank.create_account(name, pin, initial)
            print(f"🎉 Account created! Your Account Number: {acc.acc_no}")

        # ----------------------------------------------------
        # Login
        # ----------------------------------------------------
        elif choice == "2":
            acc_no = int(input("Enter Account Number: "))
            pin = input("Enter PIN: ")
            acc = bank.authenticate(acc_no, pin)

            if not acc:
                continue

            print(f"🎉 Login Successful! Welcome {acc.name}")

            # -------------------------
            # Logged-in Menu
            # -------------------------
            while True:
                account_menu(acc.name)
                ch = input("Choose: ")

                if ch == "1":
                    print(f"💰 Current Balance: ₹{acc.balance}")

                elif ch == "2":
                    amt = int(input("Enter deposit amount: "))
                    acc.deposit(amt)
                    bank.save_data()
                    print("✔ Deposit Successful!")

                elif ch == "3":
                    amt = int(input("Enter withdraw amount: "))
                    try:
                        acc.withdraw(amt)
                        bank.save_data()
                        print("✔ Withdrawal Successful!")
                    except Exception as e:
                        print("❌", e)

                elif ch == "4":
                    print("\n📜 Transaction History:")
                    for t in acc.transactions:
                        print(f"{t['time']}  | {t['type']} | ₹{t['amount']}")

                elif ch == "5":
                    print("🔒 Logged out.")
                    break
                else:
                    print("❌ Invalid choice")

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------
        elif choice == "3":
            print("👋 Thank you for visiting RK Bank!")
            break

        else:
            print("❌ Invalid choice. Try again.")


# Run the program
run_bank()





























