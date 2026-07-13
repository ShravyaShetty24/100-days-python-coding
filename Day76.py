# Vehicle Rental Management System

vehicles = []

# Add Vehicle
def add_vehicle():

    vehicle_id = int(input("Enter Vehicle ID: "))
    name = input("Enter Vehicle Name: ")
    vehicle_type = input("Enter Vehicle Type (Bike/Car): ")
    rent = float(input("Enter Rent Per Day: "))

    for v in vehicles:
        if v["id"] == vehicle_id:
            print("Vehicle ID already exists")
            return

    vehicle = {
        "id": vehicle_id,
        "name": name,
        "type": vehicle_type,
        "rent_per_day": rent,
        "status": "Available"
    }

    vehicles.append(vehicle)
    print("Vehicle added successfully")


# View Vehicles
def view_vehicles():

    if len(vehicles) == 0:
        print("No vehicles available")

    else:
        print("\n------ VEHICLE LIST ------")

        for v in vehicles:
            print("Vehicle ID :", v["id"])
            print("Name :", v["name"])
            print("Type :", v["type"])
            print("Rent Per Day : ₹", v["rent_per_day"])
            print("Status :", v["status"])
            print()


# Search Vehicle
def search_vehicle():

    vehicle_id = int(input("Enter Vehicle ID: "))

    for v in vehicles:

        if v["id"] == vehicle_id:

            print("\nVehicle Found")
            print("Name :", v["name"])
            print("Type :", v["type"])
            print("Rent Per Day : ₹", v["rent_per_day"])
            print("Status :", v["status"])
            return

    print("Vehicle not found")


# Rent Vehicle
def rent_vehicle():

    vehicle_id = int(input("Enter Vehicle ID: "))

    for v in vehicles:

        if v["id"] == vehicle_id:

            if v["status"] == "Available":
                v["status"] = "Rented"
                print("Vehicle rented successfully")
            else:
                print("Vehicle is already rented")

            return

    print("Vehicle not found")


# Return Vehicle
def return_vehicle():

    vehicle_id = int(input("Enter Vehicle ID: "))

    for v in vehicles:

        if v["id"] == vehicle_id:

            if v["status"] == "Rented":
                v["status"] = "Available"
                print("Vehicle returned successfully")
            else:
                print("Vehicle is already available")

            return

    print("Vehicle not found")


# Rental Report
def rental_report():

    rented = 0

    for v in vehicles:
        if v["status"] == "Rented":
            rented += 1

    print("Total Vehicles =", len(vehicles))
    print("Rented Vehicles =", rented)
    print("Available Vehicles =", len(vehicles) - rented)


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