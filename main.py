from bank import BankingSystem


def main():
    bank = BankingSystem()

    while True:
        print("\n" + "=" * 48)
        print("           PYTHON BANKING SYSTEM")
        print("=" * 48)
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("=" * 48)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.login()
        elif choice == "3":
            print("\nThank you for using Python Banking System!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
