# Mobile Recharge Management System

customers = []

# Add Customer
def add_customer():

    customer_id = int(input("Enter Customer ID: "))
    name = input("Enter Customer Name: ")
    mobile = input("Enter Mobile Number: ")
    operator = input("Enter Operator (Jio/Airtel/Vi/BSNL): ")

    for c in customers:
        if c["id"] == customer_id:
            print("Customer ID already exists")
            return

    customer = {
        "id": customer_id,
        "name": name,
        "mobile": mobile,
        "operator": operator,
        "last_recharge": 0
    }

    customers.append(customer)
    print("Customer added successfully")


# View Customers
def view_customers():

    if len(customers) == 0:
        print("No customer records found")

    else:
        print("\n------ CUSTOMER LIST ------")

        for c in customers:
            print("Customer ID :", c["id"])
            print("Name :", c["name"])
            print("Mobile :", c["mobile"])
            print("Operator :", c["operator"])
            print("Last Recharge : ₹", c["last_recharge"])
            print()


# Search Customer
def search_customer():

    customer_id = int(input("Enter Customer ID: "))

    for c in customers:

        if c["id"] == customer_id:

            print("\nCustomer Found")
            print("Name :", c["name"])
            print("Mobile :", c["mobile"])
            print("Operator :", c["operator"])
            print("Last Recharge : ₹", c["last_recharge"])
            return

    print("Customer not found")


# Recharge Mobile
def recharge_mobile():

    customer_id = int(input("Enter Customer ID: "))

    for c in customers:

        if c["id"] == customer_id:

            amount = float(input("Enter Recharge Amount: "))
            c["last_recharge"] = amount

            print("Recharge successful")
            return

    print("Customer not found")


# Update Mobile Number
def update_mobile():

    customer_id = int(input("Enter Customer ID: "))

    for c in customers:

        if c["id"] == customer_id:

            new_mobile = input("Enter New Mobile Number: ")
            c["mobile"] = new_mobile

            print("Mobile number updated successfully")
            return

    print("Customer not found")


# Recharge Report
def recharge_report():

    total_recharge = 0

    for c in customers:
        total_recharge += c["last_recharge"]

    print("Total Customers =", len(customers))
    print("Total Recharge Amount = ₹", total_recharge)


# Main Program
while True:

    print("\n------ MOBILE RECHARGE MENU ------")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Recharge Mobile")
    print("5. Update Mobile Number")
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
        recharge_mobile()

    elif ch == 5:
        update_mobile()

    elif ch == 6:
        recharge_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")