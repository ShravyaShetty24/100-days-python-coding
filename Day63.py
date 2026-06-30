# Bus Reservation Management System

buses = []


# Add Bus
def add_bus():

    bus_id = int(input("Enter Bus ID: "))
    bus_name = input("Enter Bus Name: ")
    route = input("Enter Route: ")
    seats = int(input("Enter Total Seats: "))

    for b in buses:
        if b["id"] == bus_id:
            print("Bus ID already exists")
            return

    bus = {
        "id": bus_id,
        "bus_name": bus_name,
        "route": route,
        "total_seats": seats,
        "available_seats": seats
    }

    buses.append(bus)
    print("Bus added successfully")


# View Buses
def view_buses():

    if len(buses) == 0:
        print("No buses available")

    else:
        print("\n------ BUS LIST ------")

        for b in buses:

            print("Bus ID :", b["id"])
            print("Bus Name :", b["bus_name"])
            print("Route :", b["route"])
            print("Total Seats :", b["total_seats"])
            print("Available Seats :", b["available_seats"])
            print()


# Search Bus
def search_bus():

    bus_id = int(input("Enter Bus ID: "))

    for b in buses:

        if b["id"] == bus_id:

            print("\nBus Found")
            print("Bus Name :", b["bus_name"])
            print("Route :", b["route"])
            print("Available Seats :", b["available_seats"])
            return

    print("Bus not found")


# Book Seat
def book_seat():

    bus_id = int(input("Enter Bus ID: "))
    seats = int(input("Enter Number of Seats: "))

    for b in buses:

        if b["id"] == bus_id:

            if seats <= b["available_seats"]:

                b["available_seats"] -= seats
                print("Seat booked successfully")

            else:
                print("Seats not available")

            return

    print("Bus not found")


# Cancel Booking
def cancel_booking():

    bus_id = int(input("Enter Bus ID: "))
    seats = int(input("Enter Number of Seats to Cancel: "))

    for b in buses:

        if b["id"] == bus_id:

            booked = b["total_seats"] - b["available_seats"]

            if seats <= booked:

                b["available_seats"] += seats
                print("Booking cancelled successfully")

            else:
                print("Invalid number of seats")

            return

    print("Bus not found")


# Reservation Report
def reservation_report():

    total_booked = 0

    for b in buses:
        total_booked += (b["total_seats"] - b["available_seats"])

    print("Total Seats Booked =", total_booked)


# Main Program
while True:

    print("\n------ BUS RESERVATION MENU ------")
    print("1. Add Bus")
    print("2. View Buses")
    print("3. Search Bus")
    print("4. Book Seat")
    print("5. Cancel Booking")
    print("6. Reservation Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_bus()

    elif ch == 2:
        view_buses()

    elif ch == 3:
        search_bus()

    elif ch == 4:
        book_seat()

    elif ch == 5:
        cancel_booking()

    elif ch == 6:
        reservation_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")