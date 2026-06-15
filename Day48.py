class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}")
        print("Available" if self.available else "Issued")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book Issued Successfully")
                else:
                    print("Book Already Issued")
                return
        print("Book Not Found")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print("Book Returned Successfully")
                return
        print("Book Not Found")

    def display_books(self):
        for book in self.books:
            book.display()
            print("-" * 20)


# Driver Program
lib = Library()

b1 = Book(101, "Python Programming", "Guido")
b2 = Book(102, "Data Structures", "Mark")

lib.add_book(b1)
lib.add_book(b2)

print("Available Books:")
lib.display_books()

lib.issue_book(101)

print("\nAfter Issuing Book:")
lib.display_books()

lib.return_book(101)

print("\nAfter Returning Book:")
lib.display_books()