# Hotel Room Booking System

bookings = []
def add_booking():

    room_no = int(input("Enter Room Number: "))
    name = input("Enter Customer Name: ")
    room_type = input("Enter Room Type (Standard/Deluxe/Suite): ")
    days = int(input("Enter Number of Days: "))

    # Room price calculation
    if room_type.lower() == "standard":
        price = 1000

    elif room_type.lower() == "deluxe":
        price = 2000

    elif room_type.lower() == "suite":
        price = 3500

    else:
        print("Invalid Room Type")
        return

    bill = price * days

    booking = {
        "room_no": room_no,
        "name": name,
        "room_type": room_type,
        "days": days,
        "bill": bill
    }

    bookings.append(booking)

    print("Room booked successfully")

def view_bookings():

    if len(bookings) == 0:
        print("No bookings found")

    else:

        print("\n------ BOOKING RECORDS ------")

        for b in bookings:

            print("Room Number :", b["room_no"])
            print("Customer Name :", b["name"])
            print("Room Type :", b["room_type"])
            print("Days :", b["days"])
            print("Bill :", b["bill"])
            print()

def search_booking():

    room_no = int(input("Enter Room Number to search: "))

    for b in bookings:

        if b["room_no"] == room_no:

            print("\nBooking Found")
            print("Customer Name :", b["name"])
            print("Room Type :", b["room_type"])
            print("Days :", b["days"])
            print("Bill :", b["bill"])

            return

    print("Booking not found")

def cancel_booking():

    room_no = int(input("Enter Room Number to cancel booking: "))

    for b in bookings:

        if b["room_no"] == room_no:

            bookings.remove(b)

            print("Booking cancelled successfully")

            return

    print("Booking not found")

def available_rooms():

    booked_rooms = []

    for b in bookings:
        booked_rooms.append(b["room_no"])

    print("\nAvailable Rooms:")

    for room in range(101, 111):

        if room not in booked_rooms:
            print(room)
while True:

    print("\n------ HOTEL MENU ------")
    print("1. Add Booking")
    print("2. View Bookings")
    print("3. Search Booking")
    print("4. Cancel Booking")
    print("5. Available Rooms")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_booking()

    elif ch == 2:
        view_bookings()

    elif ch == 3:
        search_booking()

    elif ch == 4:
        cancel_booking()

    elif ch == 5:
        available_rooms()

    elif ch == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")