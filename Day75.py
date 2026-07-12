# Hotel Room Booking Management System

rooms = []

# Add Room
def add_room():

    room_id = int(input("Enter Room ID: "))
    room_type = input("Enter Room Type (Standard/Deluxe/Suite): ")
    price = float(input("Enter Room Price: "))

    for r in rooms:
        if r["id"] == room_id:
            print("Room ID already exists")
            return

    room = {
        "id": room_id,
        "type": room_type,
        "price": price,
        "status": "Available"
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
            print("Room ID :", r["id"])
            print("Room Type :", r["type"])
            print("Price : ₹", r["price"])
            print("Status :", r["status"])
            print()


# Search Room
def search_room():

    room_id = int(input("Enter Room ID: "))

    for r in rooms:

        if r["id"] == room_id:

            print("\nRoom Found")
            print("Room Type :", r["type"])
            print("Price : ₹", r["price"])
            print("Status :", r["status"])
            return

    print("Room not found")


# Book Room
def book_room():

    room_id = int(input("Enter Room ID: "))

    for r in rooms:

        if r["id"] == room_id:

            if r["status"] == "Available":
                r["status"] = "Booked"
                print("Room booked successfully")
            else:
                print("Room is already booked")

            return

    print("Room not found")


# Cancel Booking
def cancel_booking():

    room_id = int(input("Enter Room ID: "))

    for r in rooms:

        if r["id"] == room_id:

            if r["status"] == "Booked":
                r["status"] = "Available"
                print("Booking cancelled successfully")
            else:
                print("Room is already available")

            return

    print("Room not found")


# Hotel Report
def hotel_report():

    booked = 0

    for r in rooms:
        if r["status"] == "Booked":
            booked += 1

    print("Total Rooms =", len(rooms))
    print("Booked Rooms =", booked)
    print("Available Rooms =", len(rooms) - booked)


# Main Program
while True:

    print("\n------ HOTEL MENU ------")
    print("1. Add Room")
    print("2. View Rooms")
    print("3. Search Room")
    print("4. Book Room")
    print("5. Cancel Booking")
    print("6. Hotel Report")
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
        cancel_booking()

    elif ch == 6:
        hotel_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")