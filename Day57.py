movies = []

# Add Movie
def add_movie():

    movie_id = int(input("Enter Movie ID: "))
    name = input("Enter Movie Name: ")
    tickets = int(input("Enter Total Tickets: "))

    movie = {
        "id": movie_id,
        "name": name,
        "tickets": tickets,
        "booked": 0
    }

    movies.append(movie)
    print("Movie added successfully")


# View Movies
def view_movies():

    if len(movies) == 0:
        print("No movies available")

    else:
        for m in movies:
            print("\nID :", m["id"])
            print("Name :", m["name"])
            print("Available Tickets :", m["tickets"])


# Search Movie
def search_movie():

    movie_id = int(input("Enter Movie ID: "))

    for m in movies:
        if m["id"] == movie_id:
            print("Movie Found")
            print("Name :", m["name"])
            print("Available Tickets :", m["tickets"])
            return

    print("Movie not found")


# Book Ticket
def book_ticket():

    movie_id = int(input("Enter Movie ID: "))
    qty = int(input("Enter Number of Tickets: "))

    for m in movies:
        if m["id"] == movie_id:

            if qty <= m["tickets"]:
                m["tickets"] -= qty
                m["booked"] += qty
                print("Ticket booked successfully")
            else:
                print("Not enough tickets available")

            return

    print("Movie not found")


# Cancel Ticket
def cancel_ticket():

    movie_id = int(input("Enter Movie ID: "))
    qty = int(input("Enter Tickets to Cancel: "))

    for m in movies:
        if m["id"] == movie_id:

            if qty <= m["booked"]:
                m["booked"] -= qty
                m["tickets"] += qty
                print("Ticket cancelled successfully")
            else:
                print("Invalid quantity")

            return

    print("Movie not found")


# Booking Report
def booking_report():

    total = 0

    for m in movies:
        total += m["booked"]

    print("Total Tickets Booked =", total)


# Main Program
while True:

    print("\n----- MOVIE MENU -----")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Book Ticket")
    print("5. Cancel Ticket")
    print("6. Booking Report")
    print("7. Exit")

    ch = int(input("Enter choice: "))

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