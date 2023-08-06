class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

class User:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.borrowed_books = []

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def add_user(self, name, student_id):
        user = User(name, student_id)
        self.users.append(user)
        print(f"User '{name}' with ID {student_id} added to the library.")

    def search_book(self, keyword):
        matching_books = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                matching_books.append(book)
        return matching_books

    def check_out(self, user, book):
        if book.checked_out:
            return "Book is already checked out."
        book.checked_out = True
        user.borrowed_books.append(book)
        return "Book checked out successfully."

    def check_in(self, user, book):
        if not book.checked_out:
            return "Book is already checked in."
        book.checked_out = False
        user.borrowed_books.remove(book)
        return "Book checked in successfully."

def main():
    john_harris_library = Library("John Harris Library")

    while True:
        print("\nLibrary Management System - John Harris Library")
        print("1. Add Book")
        print("2. Add User")
        print("3. Search Book")
        print("4. Check Out Book")
        print("5. Check In Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            john_harris_library.add_book(title, author, isbn)
        elif choice == "2":
            name = input("Enter user name: ")
            student_id = input("Enter student ID: ")
            john_harris_library.add_user(name, student_id)
        elif choice == "3":
            keyword = input("Enter search keyword: ")
            search_result = john_harris_library.search_book(keyword)
            for book in search_result:
                print(f"Found: {book.title} by {book.author}")
        elif choice == "4":
            user_id = input("Enter user's student ID: ")
            book_title = input("Enter book title: ")
            user = next((u for u in john_harris_library.users if u.student_id == user_id), None)
            book = next((b for b in john_harris_library.books if b.title.lower() == book_title.lower()), None)
            if user and book:
                print(john_harris_library.check_out(user, book))
            else:
                print("User or book not found.")
        elif choice == "5":
            user_id = input("Enter user's student ID: ")
            book_title = input("Enter book title: ")
            user = next((u for u in john_harris_library.users if u.student_id == user_id), None)
            book = next((b for b in john_harris_library.books if b.title.lower() == book_title.lower()), None)
            if user and book:
                print(john_harris_library.check_in(user, book))
            else:
                print("User or book not found.")
        elif choice == "6":
            print("Exiting the library management system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
