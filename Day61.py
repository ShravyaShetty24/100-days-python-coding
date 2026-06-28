# Flight Reservation Management System

flights = []


# Add Flight
def add_flight():

    flight_id = int(input("Enter Flight ID: "))
    flight_name = input("Enter Flight Name: ")
    destination = input("Enter Destination: ")
    seats = int(input("Enter Total Seats: "))

    for f in flights:
        if f["id"] == flight_id:
            print("Flight ID already exists")
            return

    flight = {
        "id": flight_id,
        "flight_name": flight_name,
        "destination": destination,
        "seats": seats,
        "booked": 0
    }

    flights.append(flight)

    print("Flight added successfully")


# View Flights
def view_flights():

    if len(flights) == 0:
        print("No flights available")

    else:
        print("\n------ FLIGHT LIST ------")

        for f in flights:
            print("Flight ID :", f["id"])
            print("Flight Name :", f["flight_name"])
            print("Destination :", f["destination"])
            print("Available Seats :", f["seats"])
            print()


# Search Flight
def search_flight():

    flight_id = int(input("Enter Flight ID: "))

    for f in flights:

        if f["id"] == flight_id:

            print("\nFlight Found")
            print("Flight Name :", f["flight_name"])
            print("Destination :", f["destination"])
            print("Available Seats :", f["seats"])

            return

    print("Flight not found")


# Book Ticket
def book_ticket():

    flight_id = int(input("Enter Flight ID: "))
    qty = int(input("Enter Number of Seats: "))

    for f in flights:

        if f["id"] == flight_id:

            if qty <= f["seats"]:

                f["seats"] -= qty
                f["booked"] += qty

                print("Ticket booked successfully")

            else:
                print("Seats not available")

            return

    print("Flight not found")


# Cancel Ticket
def cancel_ticket():

    flight_id = int(input("Enter Flight ID: "))
    qty = int(input("Enter Seats to Cancel: "))

    for f in flights:

        if f["id"] == flight_id:

            if qty <= f["booked"]:

                f["booked"] -= qty
                f["seats"] += qty

                print("Ticket cancelled successfully")

            else:
                print("Invalid number of seats")

            return

    print("Flight not found")


# Reservation Report
def reservation_report():

    total_booked = 0

    for f in flights:
        total_booked += f["booked"]

    print("Total Booked Seats =", total_booked)


# Main Program
while True:

    print("\n------ FLIGHT MENU ------")
    print("1. Add Flight")
    print("2. View Flights")
    print("3. Search Flight")
    print("4. Book Ticket")
    print("5. Cancel Ticket")
    print("6. Reservation Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_flight()

    elif ch == 2:
        view_flights()

    elif ch == 3:
        search_flight()

    elif ch == 4:
        book_ticket()

    elif ch == 5:
        cancel_ticket()

    elif ch == 6:
        reservation_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")