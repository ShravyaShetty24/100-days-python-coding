# College Library Book Management System

books = []


# Add Book
def add_book():

    book_id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    for b in books:
        if b["id"] == book_id:
            print("Book ID already exists")
            return

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)

    print("Book added successfully")


# View Books
def view_books():

    if len(books) == 0:
        print("No books available")

    else:
        print("\n------ BOOK LIST ------")

        for b in books:

            status = "Available" if b["available"] else "Issued"

            print("Book ID :", b["id"])
            print("Title :", b["title"])
            print("Author :", b["author"])
            print("Status :", status)
            print()


# Search Book
def search_book():

    book_id = int(input("Enter Book ID: "))

    for b in books:

        if b["id"] == book_id:

            print("\nBook Found")
            print("Title :", b["title"])
            print("Author :", b["author"])
            print("Status :", "Available" if b["available"] else "Issued")

            return

    print("Book not found")


# Issue Book
def issue_book():

    book_id = int(input("Enter Book ID: "))

    for b in books:

        if b["id"] == book_id:

            if b["available"]:
                b["available"] = False
                print("Book issued successfully")
            else:
                print("Book is already issued")

            return

    print("Book not found")


# Return Book
def return_book():

    book_id = int(input("Enter Book ID: "))

    for b in books:

        if b["id"] == book_id:

            if not b["available"]:
                b["available"] = True
                print("Book returned successfully")
            else:
                print("Book is already available")

            return

    print("Book not found")


# Library Report
def library_report():

    issued = 0

    for b in books:
        if not b["available"]:
            issued += 1

    print("Total Books =", len(books))
    print("Books Issued =", issued)
    print("Books Available =", len(books) - issued)


# Main Program
while True:

    print("\n------ LIBRARY MENU ------")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Library Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_book()

    elif ch == 2:
        view_books()

    elif ch == 3:
        search_book()

    elif ch == 4:
        issue_book()

    elif ch == 5:
        return_book()

    elif ch == 6:
        library_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")