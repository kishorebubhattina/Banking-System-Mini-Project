# Banking System – Mini Project

## Project Overview

This Python mini project simulates basic banking operations through a menu-driven application.

The implementation follows the supplied project brief:

- Create a bank account
- Login using Account Number and PIN
- Check account balance
- Deposit money
- Withdraw money
- Transfer money between accounts
- View transaction history
- Change PIN
- Logout

The project demonstrates variables and data types, conditional statements, loops, functions, lists and dictionaries, string operations, modules, `random`, and `datetime`.

## Project Flow

```text
CREATE ACCOUNT
      ↓
Account Number + PIN
      ↓
LOGIN
      ↓
┌─────────────────────────┐
│      ACCOUNT MENU       │
├─────────────────────────┤
│ 1. Check Balance        │
│ 2. Deposit              │
│ 3. Withdraw             │
│ 4. Transfer             │
│ 5. Transaction History  │
│ 6. Change PIN           │
│ 7. Logout               │
└─────────────────────────┘
      ↓
LOGOUT
      ↓
MAIN MENU
```

## Folder Structure

```text
Banking-System-Mini-Project/
│
├── main.py
├── bank.py
├── account.py
├── storage.py
├── utils.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── data/
│   └── accounts.json
│
└── screenshots/
```

## Python Concepts Used

### Variables and Data Types

Account details, balance, PIN, amounts, names, and phone numbers are stored in variables.

### Conditional Statements

Used for:

- Validating login
- Checking account existence
- Checking balance
- Checking sufficient funds
- Validating PIN
- Handling menu choices

### Loops

The main menu and account menu repeatedly run until the user chooses Exit or Logout.

### Functions

Operations are separated into functions such as:

- `create_account()`
- `login()`
- `deposit()`
- `withdraw()`
- `transfer()`
- `transaction_history()`
- `change_pin()`

### Lists and Dictionaries

Accounts are stored as dictionaries and transaction records are stored as lists of dictionaries.

### String Operations

Input validation and formatted transaction output use string operations.

### Modules

The project is separated into Python modules:

- `main.py`
- `bank.py`
- `account.py`
- `storage.py`
- `utils.py`

### random

`random` generates unique 8-digit account numbers.

### datetime

`datetime` records transaction date and time.

## How to Run

Make sure Python 3.9+ is installed.

Run:

```bash
python main.py
```

No external packages are required.

## Example

```text
================================================
           PYTHON BANKING SYSTEM
================================================
1. Create Account
2. Login
3. Exit
================================================
Enter your choice: 1

--- CREATE BANK ACCOUNT ---
Enter name: Rahul
Enter phone number: 9876543210
Create 4-digit PIN: 1234
Confirm PIN: 1234

Account created successfully!
Account Number: 48372619
Please remember your account number and PIN.
```

Login using the generated account number and PIN.

## Data Storage

Account data is stored locally in:

```text
data/accounts.json
```

The file is ignored by Git so personal/test account data is not accidentally pushed to GitHub.

## GitHub Submission

Create a GitHub repository and push the project:

```bash
git init
git add .
git commit -m "Complete Banking System mini project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Then submit the working GitHub repository link according to the provided project instructions.

## Note

This is an educational banking simulation, not a real banking application. It does not connect to banks, payment networks, or financial accounts.
