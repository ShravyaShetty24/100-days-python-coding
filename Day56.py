# Hotel Room Booking Management System

rooms = []

# Add Room
def add_room():

    room_no = int(input("Enter Room Number: "))
    room_type = input("Enter Room Type (Standard/Deluxe/Suite): ")

    for r in rooms:
        if r["room_no"] == room_no:
            print("Room already exists")
            return

    if room_type.lower() == "standard":
        charge = 1000

    elif room_type.lower() == "deluxe":
        charge = 2000

    elif room_type.lower() == "suite":
        charge = 5000

    else:
        print("Invalid Room Type")
        return

    room = {
        "room_no": room_no,
        "type": room_type,
        "charge": charge,
        "booked": False
    }

    rooms.append(room)

    print("Room added successfully")


# View Rooms
def view_rooms():

    if len(rooms) == 0:
        print("No rooms available")

    else:

        print("\n------ ROOM LIST ------")

        for r in rooms:

            status = "Booked" if r["booked"] else "Available"

            print("Room No :", r["room_no"])
            print("Type :", r["type"])
            print("Charge :", r["charge"])
            print("Status :", status)
            print()


# Search Room
def search_room():

    room_no = int(input("Enter Room Number: "))

    for r in rooms:

        if r["room_no"] == room_no:

            print("\nRoom Found")
            print("Type :", r["type"])
            print("Charge :", r["charge"])

            return

    print("Room not found")


# Book Room
def book_room():

    room_no = int(input("Enter Room Number: "))

    for r in rooms:

        if r["room_no"] == room_no:

            if r["booked"]:
                print("Room already booked")

            else:
                r["booked"] = True
                print("Room booked successfully")

            return

    print("Room not found")


# Checkout Room
def checkout_room():

    room_no = int(input("Enter Room Number: "))

    for r in rooms:

        if r["room_no"] == room_no:

            r["booked"] = False
            print("Checkout completed")

            return

    print("Room not found")


# Booking Report
def booking_report():

    booked_rooms = 0

    for r in rooms:

        if r["booked"]:
            booked_rooms += 1

    print("Total Booked Rooms =", booked_rooms)


# Main Program
while True:

    print("\n------ HOTEL MENU ------")
    print("1. Add Room")
    print("2. View Rooms")
    print("3. Search Room")
    print("4. Book Room")
    print("5. Checkout Room")
    print("6. Booking Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_room()

    elif ch == 2:
        view_rooms()

    elif ch == 3:
        search_room()

    elif ch == 4:
        book_room()

    elif ch == 5:
        checkout_room()

    elif ch == 6:
        booking_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")