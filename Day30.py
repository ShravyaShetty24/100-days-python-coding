# Bus Ticket Booking System

bookings = []


# Function to book ticket
def book_ticket():

    seat_no = int(input("Enter Seat Number: "))
    name = input("Enter Passenger Name: ")
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")

    # Check if seat already booked
    for b in bookings:

        if b["seat_no"] == seat_no:
            print("Seat already booked")
            return

    ticket = {
        "seat_no": seat_no,
        "name": name,
        "source": source,
        "destination": destination
    }

    bookings.append(ticket)

    print("Ticket booked successfully")


# Function to view bookings
def view_bookings():

    if len(bookings) == 0:
        print("No bookings found")

    else:

        print("\n------ BOOKING DETAILS ------")

        for b in bookings:

            print("Seat Number :", b["seat_no"])
            print("Passenger :", b["name"])
            print("Source :", b["source"])
            print("Destination :", b["destination"])
            print()


# Function to search passenger
def search_passenger():

    name = input("Enter passenger name: ")

    for b in bookings:

        if b["name"].lower() == name.lower():

            print("\nPassenger Found")
            print("Seat Number :", b["seat_no"])
            print("Source :", b["source"])
            print("Destination :", b["destination"])

            return

    print("Passenger not found")


# Function to cancel ticket
def cancel_ticket():

    seat_no = int(input("Enter seat number to cancel: "))

    for b in bookings:

        if b["seat_no"] == seat_no:

            bookings.remove(b)

            print("Ticket cancelled successfully")

            return

    print("Booking not found")


# Function to show available seats
def available_seats():

    booked = []

    for b in bookings:
        booked.append(b["seat_no"])

    print("\nAvailable Seats:")

    for seat in range(1, 21):

        if seat not in booked:
            print(seat)


# Main Program
while True:

    print("\n------ BUS BOOKING MENU ------")
    print("1. Book Ticket")
    print("2. View Bookings")
    print("3. Search Passenger")
    print("4. Cancel Ticket")
    print("5. Available Seats")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        book_ticket()

    elif ch == 2:
        view_bookings()

    elif ch == 3:
        search_passenger()

    elif ch == 4:
        cancel_ticket()

    elif ch == 5:
        available_seats()

    elif ch == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")