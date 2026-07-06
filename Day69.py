# Courier Tracking Management System

couriers = []

# Add Courier
def add_courier():

    courier_id = int(input("Enter Courier ID: "))
    sender = input("Enter Sender Name: ")
    receiver = input("Enter Receiver Name: ")
    destination = input("Enter Destination: ")

    for c in couriers:
        if c["id"] == courier_id:
            print("Courier ID already exists")
            return

    courier = {
        "id": courier_id,
        "sender": sender,
        "receiver": receiver,
        "destination": destination,
        "status": "In Transit"
    }

    couriers.append(courier)
    print("Courier added successfully")


# View Couriers
def view_couriers():

    if len(couriers) == 0:
        print("No courier records found")
    else:
        print("\n------ COURIER LIST ------")

        for c in couriers:
            print("ID :", c["id"])
            print("Sender :", c["sender"])
            print("Receiver :", c["receiver"])
            print("Destination :", c["destination"])
            print("Status :", c["status"])
            print()


# Search Courier
def search_courier():

    courier_id = int(input("Enter Courier ID: "))

    for c in couriers:
        if c["id"] == courier_id:
            print("\nCourier Found")
            print("Sender :", c["sender"])
            print("Receiver :", c["receiver"])
            print("Destination :", c["destination"])
            print("Status :", c["status"])
            return

    print("Courier not found")


# Update Delivery Status
def update_status():

    courier_id = int(input("Enter Courier ID: "))

    for c in couriers:
        if c["id"] == courier_id:

            status = input("Enter New Status (In Transit/Delivered): ")
            c["status"] = status

            print("Status updated successfully")
            return

    print("Courier not found")


# Delete Courier
def delete_courier():

    courier_id = int(input("Enter Courier ID: "))

    for c in couriers:
        if c["id"] == courier_id:
            couriers.remove(c)
            print("Courier deleted successfully")
            return

    print("Courier not found")


# Courier Report
def courier_report():

    delivered = 0

    for c in couriers:
        if c["status"].lower() == "delivered":
            delivered += 1

    print("Total Couriers =", len(couriers))
    print("Delivered Couriers =", delivered)
    print("In Transit =", len(couriers) - delivered)


# Main Program
while True:

    print("\n------ COURIER MENU ------")
    print("1. Add Courier")
    print("2. View Couriers")
    print("3. Search Courier")
    print("4. Update Delivery Status")
    print("5. Delete Courier")
    print("6. Courier Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_courier()

    elif ch == 2:
        view_couriers()

    elif ch == 3:
        search_courier()

    elif ch == 4:
        update_status()

    elif ch == 5:
        delete_courier()

    elif ch == 6:
        courier_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")