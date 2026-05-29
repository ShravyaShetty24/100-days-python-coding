#Movie ticket booking system
bookings=[]
def book_ticket():
    seat_no=int(input("Enter the seat no.:"))
    name=input("Enter the name:")
    movie=input("Enter the movie name:")
    seat_type=input("Enter the seat type:")
    tickets=int(input("Enter the no. of tickets"))
    for b in bookings:
        if b[seat_no]==seat_no:
            print("seat already booked")
            return
    if seat_type.lower()=="silver":
        price=150
    elif seat_type.lower()=="gold":
        price=250
    elif seat_type.lower()=="platinum":
        price=400
    else:
        print("Invalid seat type")
        return
    amount=price*tickets
    booking={"seat_no":seat_no,
              "name":name,
              "movie":movie,
              "seat_type":seat_type,
              "tickets":tickets,
              "price":price,
              "amount":amount
              }
    bookings.append(booking)
    print("Ticket booked succesfully")

def view_bookings():
    if len(bookings)==0:
        print("no booking found")
    else:
        print("\n---BOOKING DETAILS----\n")
        for b in bookings:
            print("seat_no:",b["seat_no"])
            print("name:",b["name"])
            print("movie:",b["movie"])
            print("seat_type:",b["seat_type"])
            print("tickets:",b["tickets"])
            print("price:",b["price"])
            print("amount:",b["amount"])
            print()
def search_customer():
    name=input("ENter customer name:")
    for b in bookings:
        if b["name"].lower()==name.lower():
            print("customer found")
            print("movie:",b["movie"])
            print("seat_no:",b["seat_no"])
            print("amount:",b["amount"])
            return
    print("customer not found")
def cancel_bookings():
    seat_no=int(input("Enter seat number to cancel:"))
    for b in bookings:
        if b["seat_no"]==seat_no:
            bookings.remove(b)
            print("Booking cancelled successfully")
            return
    print("Booking not found")
def availabel_seat():
    booked=[]
    for b in bookings:
        booked.append(b["seat_no"])
    print("\nAvailable seat:")
    for seat in range(1,31):
        if seat not in booked:
            print(seat)
while True:
    print("\n------ BUS BOOKING MENU ------")
    print("1. Book Ticket")
    print("2. View Bookings")
    print("3. Search customer")
    print("4. Cancel booking")
    print("5. Available Seats")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        book_ticket()

    elif ch == 2:
        view_bookings()

    elif ch == 3:
        search_customer()

    elif ch == 4:
        cancel_bookings()

    elif ch == 5:
        availabel_seat()

    elif ch == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")