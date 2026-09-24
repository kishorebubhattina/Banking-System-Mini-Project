import random
from datetime import datetime

from account import Account
from storage import load_accounts, save_accounts
from utils import (
    is_valid_amount,
    is_valid_name,
    is_valid_phone,
    is_valid_pin,
)


class BankingSystem:
    """Controls account creation, login, and authenticated account operations."""

    def __init__(self):
        self.accounts = load_accounts()

    def _save(self):
        save_accounts(self.accounts)

    def _generate_account_number(self):
        while True:
            account_number = str(random.randint(10000000, 99999999))
            if account_number not in self.accounts:
                return account_number

    def create_account(self):
        print("\n--- CREATE BANK ACCOUNT ---")

        name = input("Enter name: ").strip()
        if not is_valid_name(name):
            print("Invalid name. Use letters and spaces only.")
            return

        phone = input("Enter phone number: ").strip()
        if not is_valid_phone(phone):
            print("Invalid phone number. Enter a 10-digit number.")
            return

        pin = input("Create 4-digit PIN: ").strip()
        if not is_valid_pin(pin):
            print("PIN must contain exactly 4 digits.")
            return

        confirm_pin = input("Confirm PIN: ").strip()
        if pin != confirm_pin:
            print("PINs do not match.")
            return

        account_number = self._generate_account_number()

        account = Account(
            account_number=account_number,
            name=name,
            phone=phone,
            pin=pin,
            balance=0.0,
            transactions=[],
        )

        self.accounts[account_number] = account.to_dict()
        self._save()

        print("\nAccount created successfully!")
        print(f"Account Number: {account_number}")
        print("Please remember your account number and PIN.")

    def login(self):
        print("\n--- LOGIN ---")

        account_number = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()

        account_data = self.accounts.get(account_number)

        if account_data is None:
            print("Account not found.")
            return

        if account_data["pin"] != pin:
            print("Incorrect PIN.")
            return

        account = Account.from_dict(account_data)
        print(f"\nWelcome, {account.name}!")
        self.account_menu(account)

    def account_menu(self, account):
        while True:
            print("\n" + "-" * 42)
            print("              ACCOUNT MENU")
            print("-" * 42)
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Transaction History")
            print("6. Change PIN")
            print("7. Logout")
            print("-" * 42)

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.check_balance(account)
            elif choice == "2":
                self.deposit(account)
            elif choice == "3":
                self.withdraw(account)
            elif choice == "4":
                self.transfer(account)
            elif choice == "5":
                self.transaction_history(account)
            elif choice == "6":
                self.change_pin(account)
            elif choice == "7":
                self._save_account(account)
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice. Please select 1-7.")

    def check_balance(self, account):
        print(f"\nCurrent Balance: ₹{account.balance:.2f}")

    def deposit(self, account):
        print("\n--- DEPOSIT MONEY ---")

        amount_text = input("Enter amount to deposit: ").strip()

        if not is_valid_amount(amount_text):
            print("Enter a valid positive amount.")
            return

        amount = float(amount_text)
        account.balance += amount

        account.add_transaction(
            "Deposit",
            amount,
            f"Cash deposit of ₹{amount:.2f}"
        )

        self._save_account(account)
        print(f"₹{amount:.2f} deposited successfully.")
        print(f"New Balance: ₹{account.balance:.2f}")

    def withdraw(self, account):
        print("\n--- WITHDRAW MONEY ---")

        amount_text = input("Enter amount to withdraw: ").strip()

        if not is_valid_amount(amount_text):
            print("Enter a valid positive amount.")
            return

        amount = float(amount_text)

        if amount > account.balance:
            print("Insufficient balance.")
            return

        account.balance -= amount

        account.add_transaction(
            "Withdrawal",
            amount,
            f"Cash withdrawal of ₹{amount:.2f}"
        )

        self._save_account(account)
        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Remaining Balance: ₹{account.balance:.2f}")

    def transfer(self, sender):
        print("\n--- TRANSFER MONEY ---")

        receiver_number = input("Enter receiver account number: ").strip()

        if receiver_number == sender.account_number:
            print("You cannot transfer money to your own account.")
            return

        receiver_data = self.accounts.get(receiver_number)

        if receiver_data is None:
            print("Receiver account not found.")
            return

        amount_text = input("Enter amount to transfer: ").strip()

        if not is_valid_amount(amount_text):
            print("Enter a valid positive amount.")
            return

        amount = float(amount_text)

        if amount > sender.balance:
            print("Insufficient balance.")
            return

        receiver = Account.from_dict(receiver_data)

        sender.balance -= amount
        receiver.balance += amount

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sender.add_transaction(
            "Transfer Sent",
            amount,
            f"Transferred to account {receiver.account_number}",
            timestamp,
        )

        receiver.add_transaction(
            "Transfer Received",
            amount,
            f"Received from account {sender.account_number}",
            timestamp,
        )

        self.accounts[sender.account_number] = sender.to_dict()
        self.accounts[receiver.account_number] = receiver.to_dict()
        self._save()

        print(f"₹{amount:.2f} transferred successfully.")
        print(f"New Balance: ₹{sender.balance:.2f}")

    def transaction_history(self, account):
        print("\n--- TRANSACTION HISTORY ---")

        if not account.transactions:
            print("No transactions found.")
            return

        print("-" * 86)
        print(f"{'Date & Time':20} {'Type':20} {'Amount':14} Description")
        print("-" * 86)

        for transaction in account.transactions:
            print(
                f"{transaction['timestamp']:20} "
                f"{transaction['type']:20} "
                f"₹{transaction['amount']:10.2f}   "
                f"{transaction['description']}"
            )

        print("-" * 86)

    def change_pin(self, account):
        print("\n--- CHANGE PIN ---")

        old_pin = input("Enter old PIN: ").strip()

        if old_pin != account.pin:
            print("Incorrect old PIN.")
            return

        new_pin = input("Enter new 4-digit PIN: ").strip()

        if not is_valid_pin(new_pin):
            print("PIN must contain exactly 4 digits.")
            return

        confirm_pin = input("Confirm new PIN: ").strip()

        if new_pin != confirm_pin:
            print("PINs do not match.")
            return

        account.pin = new_pin
        self._save_account(account)

        print("PIN changed successfully.")

    def _save_account(self, account):
        self.accounts[account.account_number] = account.to_dict()
        self._save()
