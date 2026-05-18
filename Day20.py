balance=1000
while True:
    print("\n------ATM MENU-------\n")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. withdraw")
    print("4. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        print("Balance: ",balance)
    elif choice==2:
        amount=int(input("Enter amount: "))
        balance +=amount
        print("Deposited Successfully")
    elif choice==3:
        amount=int(input("Enter amount: "))
        if amount<=balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insuffient balance")
    elif choice==4:
        print("Thank you")
        break
    else:
        print("Invalid Choice")