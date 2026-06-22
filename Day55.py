# Vehicle Rental Management System

vehicles = []

# Add Vehicle
def add_vehicle():

    vehicle_id = int(input("Enter Vehicle ID: "))
    name = input("Enter Vehicle Name: ")
    vehicle_type = input("Enter Type (Bike/Car/Bus): ")

    for v in vehicles:
        if v["id"] == vehicle_id:
            print("Vehicle ID already exists")
            return

    if vehicle_type.lower() == "bike":
        rent = 500

    elif vehicle_type.lower() == "car":
        rent = 1500

    elif vehicle_type.lower() == "bus":
        rent = 5000

    else:
        print("Invalid Vehicle Type")
        return

    vehicle = {
        "id": vehicle_id,
        "name": name,
        "type": vehicle_type,
        "rent": rent,
        "available": True
    }

    vehicles.append(vehicle)

    print("Vehicle added successfully")


# View Vehicles
def view_vehicles():

    if len(vehicles) == 0:
        print("No vehicles found")

    else:

        print("\n------ VEHICLE LIST ------")

        for v in vehicles:

            status = "Available" if v["available"] else "Rented"

            print("ID :", v["id"])
            print("Name :", v["name"])
            print("Type :", v["type"])
            print("Rent/Day :", v["rent"])
            print("Status :", status)
            print()


# Search Vehicle
def search_vehicle():

    vehicle_id = int(input("Enter Vehicle ID: "))

    for v in vehicles:

        if v["id"] == vehicle_id:

            print("\nVehicle Found")
            print("Name :", v["name"])
            print("Type :", v["type"])
            print("Rent/Day :", v["rent"])

            return

    print("Vehicle not found")


# Rent Vehicle
def rent_vehicle():

    vehicle_id = int(input("Enter Vehicle ID: "))

    for v in vehicles:

        if v["id"] == vehicle_id:

            if v["available"]:
                v["available"] = False
                print("Vehicle rented successfully")
            else:
                print("Vehicle already rented")

            return

    print("Vehicle not found")


# Return Vehicle
def return_vehicle():

    vehicle_id = int(input("Enter Vehicle ID: "))

    for v in vehicles:

        if v["id"] == vehicle_id:

            v["available"] = True
            print("Vehicle returned successfully")

            return

    print("Vehicle not found")


# Rental Report
def rental_report():

    rented = 0

    for v in vehicles:

        if not v["available"]:
            rented += 1

    print("Total Rented Vehicles =", rented)


# Main Program
while True:

    print("\n------ VEHICLE RENTAL MENU ------")
    print("1. Add Vehicle")
    print("2. View Vehicles")
    print("3. Search Vehicle")
    print("4. Rent Vehicle")
    print("5. Return Vehicle")
    print("6. Rental Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_vehicle()

    elif ch == 2:
        view_vehicles()

    elif ch == 3:
        search_vehicle()

    elif ch == 4:
        rent_vehicle()

    elif ch == 5:
        return_vehicle()

    elif ch == 6:
        rental_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")