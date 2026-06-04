# Library Management System

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
        "issued": False
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

            status = "Issued" if b["issued"] else "Available"

            print("Book ID :", b["id"])
            print("Title :", b["title"])
            print("Author :", b["author"])
            print("Status :", status)
            print()


# Search Book
def search_book():

    title = input("Enter Book Title: ")

    for b in books:

        if b["title"].lower() == title.lower():

            print("\nBook Found")
            print("Book ID :", b["id"])
            print("Author :", b["author"])

            return

    print("Book not found")


# Issue Book
def issue_book():

    book_id = int(input("Enter Book ID: "))

    for b in books:

        if b["id"] == book_id:

            if b["issued"]:
                print("Book already issued")

            else:
                b["issued"] = True
                print("Book issued successfully")

            return

    print("Book not found")


# Return Book
def return_book():

    book_id = int(input("Enter Book ID: "))

    for b in books:

        if b["id"] == book_id:

            if b["issued"]:
                b["issued"] = False
                print("Book returned successfully")

            else:
                print("Book was not issued")

            return

    print("Book not found")


# Delete Book
def delete_book():

    book_id = int(input("Enter Book ID: "))

    for b in books:

        if b["id"] == book_id:

            books.remove(b)

            print("Book deleted successfully")

            return

    print("Book not found")


# Main Program
while True:

    print("\n------ LIBRARY MENU ------")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
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
        delete_book()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")