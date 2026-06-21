# Mobile Recharge Management System

customers = []

# Add Customer
def add_customer():

    customer_id = int(input("Enter Customer ID: "))
    name = input("Enter Customer Name: ")
    mobile = input("Enter Mobile Number: ")
    plan = input("Enter Plan (Basic/Standard/Premium): ")

    for c in customers:
        if c["id"] == customer_id:
            print("Customer ID already exists")
            return

    if plan.lower() == "basic":
        amount = 199

    elif plan.lower() == "standard":
        amount = 399

    elif plan.lower() == "premium":
        amount = 699

    else:
        print("Invalid Plan")
        return

    customer = {
        "id": customer_id,
        "name": name,
        "mobile": mobile,
        "plan": plan,
        "amount": amount
    }

    customers.append(customer)

    print("Customer added successfully")


# View Customers
def view_customers():

    if len(customers) == 0:
        print("No records found")

    else:

        print("\n------ CUSTOMER LIST ------")

        for c in customers:

            print("ID :", c["id"])
            print("Name :", c["name"])
            print("Mobile :", c["mobile"])
            print("Plan :", c["plan"])
            print("Amount :", c["amount"])
            print()


# Search Customer
def search_customer():

    customer_id = int(input("Enter Customer ID: "))

    for c in customers:

        if c["id"] == customer_id:

            print("\nCustomer Found")
            print("Name :", c["name"])
            print("Mobile :", c["mobile"])
            print("Plan :", c["plan"])
            print("Amount :", c["amount"])

            return

    print("Customer not found")


# Recharge Number
def recharge_number():

    customer_id = int(input("Enter Customer ID: "))

    for c in customers:

        if c["id"] == customer_id:

            plan = input("Enter New Plan: ")

            if plan.lower() == "basic":
                amount = 199

            elif plan.lower() == "standard":
                amount = 399

            elif plan.lower() == "premium":
                amount = 699

            else:
                print("Invalid Plan")
                return

            c["plan"] = plan
            c["amount"] = amount

            print("Recharge successful")

            return

    print("Customer not found")


# Delete Customer
def delete_customer():

    customer_id = int(input("Enter Customer ID: "))

    for c in customers:

        if c["id"] == customer_id:

            customers.remove(c)

            print("Customer deleted successfully")

            return

    print("Customer not found")


# Recharge Report
def recharge_report():

    total = 0

    for c in customers:
        total += c["amount"]

    print("Total Recharge Collection =", total)


# Main Program
while True:

    print("\n------ MOBILE RECHARGE MENU ------")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Recharge Number")
    print("5. Delete Customer")
    print("6. Recharge Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_customer()

    elif ch == 2:
        view_customers()

    elif ch == 3:
        search_customer()

    elif ch == 4:
        recharge_number()

    elif ch == 5:
        delete_customer()

    elif ch == 6:
        recharge_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")