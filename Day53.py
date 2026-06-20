# Electricity Bill Management System

consumers = []

# Add Consumer
def add_consumer():

    consumer_id = int(input("Enter Consumer ID: "))
    name = input("Enter Consumer Name: ")
    units = int(input("Enter Units Consumed: "))

    if units <= 100:
        bill = units * 2

    elif units <= 300:
        bill = units * 4

    else:
        bill = units * 6

    consumer = {
        "id": consumer_id,
        "name": name,
        "units": units,
        "bill": bill
    }

    consumers.append(consumer)

    print("Consumer added successfully")


# View Consumers
def view_consumers():

    if len(consumers) == 0:
        print("No records found")

    else:

        print("\n------ CONSUMER LIST ------")

        for c in consumers:

            print("ID :", c["id"])
            print("Name :", c["name"])
            print("Units :", c["units"])
            print("Bill :", c["bill"])
            print()


# Search Consumer
def search_consumer():

    consumer_id = int(input("Enter Consumer ID: "))

    for c in consumers:

        if c["id"] == consumer_id:

            print("\nConsumer Found")
            print("Name :", c["name"])
            print("Units :", c["units"])
            print("Bill :", c["bill"])

            return

    print("Consumer not found")


# Update Units
def update_units():

    consumer_id = int(input("Enter Consumer ID: "))

    for c in consumers:

        if c["id"] == consumer_id:

            units = int(input("Enter New Units: "))

            if units <= 100:
                bill = units * 2

            elif units <= 300:
                bill = units * 4

            else:
                bill = units * 6

            c["units"] = units
            c["bill"] = bill

            print("Units updated successfully")

            return

    print("Consumer not found")


# Delete Consumer
def delete_consumer():

    consumer_id = int(input("Enter Consumer ID: "))

    for c in consumers:

        if c["id"] == consumer_id:

            consumers.remove(c)

            print("Consumer deleted successfully")

            return

    print("Consumer not found")


# Bill Report
def bill_report():

    total_bill = 0

    for c in consumers:
        total_bill += c["bill"]

    print("Total Bill Collection =", total_bill)


# Main Program
while True:

    print("\n------ ELECTRICITY BILL MENU ------")
    print("1. Add Consumer")
    print("2. View Consumers")
    print("3. Search Consumer")
    print("4. Update Units")
    print("5. Delete Consumer")
    print("6. Bill Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_consumer()

    elif ch == 2:
        view_consumers()

    elif ch == 3:
        search_consumer()

    elif ch == 4:
        update_units()

    elif ch == 5:
        delete_consumer()

    elif ch == 6:
        bill_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")