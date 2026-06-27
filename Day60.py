# Bank Loan Management System

loans = []


# Add Loan
def add_loan():

    loan_id = int(input("Enter Loan ID: "))
    name = input("Enter Customer Name: ")
    amount = float(input("Enter Loan Amount: "))
    years = int(input("Enter Loan Period (years): "))

    loan = {
        "id": loan_id,
        "name": name,
        "amount": amount,
        "years": years,
        "status": "Pending"
    }

    loans.append(loan)

    print("Loan added successfully")


# View Loans
def view_loans():

    if len(loans) == 0:
        print("No loan records found")

    else:

        print("\n------ LOAN DETAILS ------")

        for l in loans:

            print("Loan ID :", l["id"])
            print("Name :", l["name"])
            print("Amount :", l["amount"])
            print("Years :", l["years"])
            print("Status :", l["status"])
            print()


# Search Customer
def search_customer():

    loan_id = int(input("Enter Loan ID: "))

    for l in loans:

        if l["id"] == loan_id:

            print("Customer Found")
            print("Name :", l["name"])
            print("Amount :", l["amount"])
            print("Status :", l["status"])

            return

    print("Customer not found")


# Update Loan Status
def update_status():

    loan_id = int(input("Enter Loan ID: "))

    for l in loans:

        if l["id"] == loan_id:

            status = input("Enter Status (Approved/Rejected): ")

            l["status"] = status

            print("Loan status updated")

            return

    print("Loan not found")


# Calculate EMI
def calculate_emi():

    loan_id = int(input("Enter Loan ID: "))

    for l in loans:

        if l["id"] == loan_id:

            emi = l["amount"] / (l["years"] * 12)

            print("Monthly EMI =", emi)

            return

    print("Loan not found")


# Loan Report
def loan_report():

    approved = 0

    for l in loans:

        if l["status"].lower() == "approved":
            approved += 1

    print("Approved Loans =", approved)


# Main Program
while True:

    print("\n------ LOAN MENU ------")
    print("1. Add Loan")
    print("2. View Loans")
    print("3. Search Customer")
    print("4. Update Loan Status")
    print("5. Calculate EMI")
    print("6. Loan Report")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_loan()

    elif ch == 2:
        view_loans()

    elif ch == 3:
        search_customer()

    elif ch == 4:
        update_status()

    elif ch == 5:
        calculate_emi()

    elif ch == 6:
        loan_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")