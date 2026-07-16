# Movie Ticket Booking Management System

movies = []

# Add Movie
def add_movie():

    movie_id = int(input("Enter Movie ID: "))
    movie_name = input("Enter Movie Name: ")
    tickets = int(input("Enter Total Tickets: "))
    price = float(input("Enter Ticket Price: "))

    for m in movies:
        if m["id"] == movie_id:
            print("Movie ID already exists")
            return

    movie = {
        "id": movie_id,
        "movie_name": movie_name,
        "tickets": tickets,
        "booked": 0,
        "price": price
    }

    movies.append(movie)
    print("Movie added successfully")


# View Movies
def view_movies():

    if len(movies) == 0:
        print("No movies available")

    else:
        print("\n------ MOVIE LIST ------")

        for m in movies:
            print("Movie ID :", m["id"])
            print("Movie Name :", m["movie_name"])
            print("Available Tickets :", m["tickets"])
            print("Booked Tickets :", m["booked"])
            print("Ticket Price : ₹", m["price"])
            print()


# Search Movie
def search_movie():

    movie_id = int(input("Enter Movie ID: "))

    for m in movies:

        if m["id"] == movie_id:

            print("\nMovie Found")
            print("Movie Name :", m["movie_name"])
            print("Available Tickets :", m["tickets"])
            print("Ticket Price : ₹", m["price"])
            return

    print("Movie not found")


# Book Ticket
def book_ticket():

    movie_id = int(input("Enter Movie ID: "))
    quantity = int(input("Enter Number of Tickets: "))

    for m in movies:

        if m["id"] == movie_id:

            if quantity <= m["tickets"]:

                m["tickets"] -= quantity
                m["booked"] += quantity

                bill = quantity * m["price"]

                print("Tickets booked successfully")
                print("Total Bill = ₹", bill)

            else:
                print("Tickets not available")

            return

    print("Movie not found")


# Cancel Ticket
def cancel_ticket():

    movie_id = int(input("Enter Movie ID: "))
    quantity = int(input("Enter Number of Tickets to Cancel: "))

    for m in movies:

        if m["id"] == movie_id:

            if quantity <= m["booked"]:

                m["booked"] -= quantity
                m["tickets"] += quantity

                print("Ticket cancelled successfully")

            else:
                print("Invalid ticket count")

            return

    print("Movie not found")


# Booking Report
def booking_report():

    total_booked = 0

    for m in movies:
        total_booked += m["booked"]

    print("Total Movies =", len(movies))
    print("Total Tickets Booked =", total_booked)


# Main Program
while True:

    print("\n------ MOVIE TICKET MENU ------")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Book Ticket")
    print("5. Cancel Ticket")
    print("6. Booking Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_movie()

    elif ch == 2:
        view_movies()

    elif ch == 3:
        search_movie()

    elif ch == 4:
        book_ticket()

    elif ch == 5:
        cancel_ticket()

    elif ch == 6:
        booking_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")