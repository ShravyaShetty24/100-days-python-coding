# Bank Account Management System

accounts = []


# Create Account
def create_account():

    acc_no = int(input("Enter Account Number: "))
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))

    for a in accounts:
        if a["acc_no"] == acc_no:
            print("Account already exists")
            return

    account = {
        "acc_no": acc_no,
        "name": name,
        "balance": balance
    }

    accounts.append(account)

    print("Account created successfully")


# View Accounts
def view_accounts():

    if len(accounts) == 0:
        print("No accounts found")

    else:

        print("\n------ ACCOUNT LIST ------")

        for a in accounts:

            print("Account No :", a["acc_no"])
            print("Name :", a["name"])
            print("Balance :", a["balance"])
            print()


# Search Account
def search_account():

    acc_no = int(input("Enter Account Number: "))

    for a in accounts:

        if a["acc_no"] == acc_no:

            print("\nAccount Found")
            print("Name :", a["name"])
            print("Balance :", a["balance"])

            return

    print("Account not found")


# Deposit Money
def deposit_money():

    acc_no = int(input("Enter Account Number: "))

    for a in accounts:

        if a["acc_no"] == acc_no:

            amount = float(input("Enter Deposit Amount: "))

            a["balance"] += amount

            print("Amount deposited successfully")
            print("New Balance =", a["balance"])

            return

    print("Account not found")


# Withdraw Money
def withdraw_money():

    acc_no = int(input("Enter Account Number: "))

    for a in accounts:

        if a["acc_no"] == acc_no:

            amount = float(input("Enter Withdrawal Amount: "))

            if amount > a["balance"]:
                print("Insufficient Balance")

            else:
                a["balance"] -= amount

                print("Amount withdrawn successfully")
                print("Remaining Balance =", a["balance"])

            return

    print("Account not found")


# Check Balance
def check_balance():

    acc_no = int(input("Enter Account Number: "))

    for a in accounts:

        if a["acc_no"] == acc_no:

            print("Current Balance =", a["balance"])

            return

    print("Account not found")


# Main Program
while True:

    print("\n------ BANK MENU ------")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Check Balance")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        create_account()

    elif ch == 2:
        view_accounts()

    elif ch == 3:
        search_account()

    elif ch == 4:
        deposit_money()

    elif ch == 5:
        withdraw_money()

    elif ch == 6:
        check_balance()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")