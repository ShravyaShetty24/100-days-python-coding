# Electricity Bill Management System

consumers = []

# Add Consumer
def add_consumer():

    consumer_id = int(input("Enter Consumer ID: "))
    name = input("Enter Consumer Name: ")
    units = int(input("Enter Units Consumed: "))

    for c in consumers:
        if c["id"] == consumer_id:
            print("Consumer ID already exists")
            return

    consumer = {
        "id": consumer_id,
        "name": name,
        "units": units,
        "bill": 0
    }

    consumers.append(consumer)
    print("Consumer added successfully")


# View Consumers
def view_consumers():

    if len(consumers) == 0:
        print("No consumer records found")

    else:
        print("\n------ CONSUMER LIST ------")

        for c in consumers:
            print("Consumer ID :", c["id"])
            print("Name :", c["name"])
            print("Units :", c["units"])
            print("Bill : ₹", c["bill"])
            print()


# Search Consumer
def search_consumer():

    consumer_id = int(input("Enter Consumer ID: "))

    for c in consumers:

        if c["id"] == consumer_id:

            print("\nConsumer Found")
            print("Name :", c["name"])
            print("Units :", c["units"])
            print("Bill : ₹", c["bill"])
            return

    print("Consumer not found")


# Generate Bill
def generate_bill():

    consumer_id = int(input("Enter Consumer ID: "))

    for c in consumers:

        if c["id"] == consumer_id:

            bill = c["units"] * 6
            c["bill"] = bill

            print("Electricity Bill = ₹", bill)
            return

    print("Consumer not found")


# Update Units
def update_units():

    consumer_id = int(input("Enter Consumer ID: "))

    for c in consumers:

        if c["id"] == consumer_id:

            new_units = int(input("Enter New Units: "))
            c["units"] = new_units

            print("Units updated successfully")
            return

    print("Consumer not found")


# Billing Report
def billing_report():

    total_bill = 0

    for c in consumers:
        total_bill += c["bill"]

    print("Total Consumers =", len(consumers))
    print("Total Bill Amount = ₹", total_bill)


# Main Program
while True:

    print("\n------ ELECTRICITY BILL MENU ------")
    print("1. Add Consumer")
    print("2. View Consumers")
    print("3. Search Consumer")
    print("4. Generate Bill")
    print("5. Update Units")
    print("6. Billing Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_consumer()

    elif ch == 2:
        view_consumers()

    elif ch == 3:
        search_consumer()

    elif ch == 4:
        generate_bill()

    elif ch == 5:
        update_units()

    elif ch == 6:
        billing_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")