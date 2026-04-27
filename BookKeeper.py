import os

class Library:
    def __init__(self):
        self.books = []
        self.issued_books = {}  # book: user
        self.load_data()

    def load_data(self):
        # Load books
        if os.path.exists("books.txt"):
            with open("books.txt", "r") as f:
                self.books = [line.strip() for line in f]

        # Load issued books
        if os.path.exists("issued.txt"):
            with open("issued.txt", "r") as f:
                for line in f:
                    book, user = line.strip().split(",")
                    self.issued_books[book] = user

    def save_data(self):
        # Save books
        with open("books.txt", "w") as f:
            for b in self.books:
                f.write(b + "\n")

        # Save issued books
        with open("issued.txt", "w") as f:
            for book, user in self.issued_books.items():
                f.write(f"{book},{user}\n")

    def add_book(self):
        name = input("Enter book name: ")
        self.books.append(name)
        self.save_data()
        print(name, "added successfully")

    def show_books(self):
        if not self.books:
            print("No books available")
        else:
            print("\nAvailable Books:")
            for b in self.books:
                print("-", b)

    def borrow_book(self):
        name = input("Enter book name: ")
        if name in self.books:
            user = input("Enter your name: ")
            self.books.remove(name)
            self.issued_books[name] = user
            self.save_data()
            print(f"{name} issued to {user}")
        else:
            print("Book not available")

    def return_book(self):
        name = input("Enter book name: ")
        if name in self.issued_books:
            self.books.append(name)
            user = self.issued_books.pop(name)
            self.save_data()
            print(f"{name} returned by {user}")
        else:
            print("This book was not issued")

    def search_book(self):
        name = input("Enter book name to search: ")
        if name in self.books:
            print(name, "is available")
        elif name in self.issued_books:
            print(name, "is issued to", self.issued_books[name])
        else:
            print("Book not found")

    def show_issued_books(self):
        if not self.issued_books:
            print("No books are issued")
        else:
            print("\nIssued Books:")
            for book, user in self.issued_books.items():
                print(f"{book} --> {user}")

    def menu(self):
        while True:
            print("\n" + "="*30)
            print(" LIBRARY MANAGEMENT SYSTEM ")
            print("="*30)
            print("1. Add Book")
            print("2. Show Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Search Book")
            print("6. Show Issued Books")
            print("7. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a number")
                continue

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.show_books()
            elif choice == 3:
                self.borrow_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5:
                self.search_book()
            elif choice == 6:
                self.show_issued_books()
            elif choice == 7:
                print("Thank you, visit again")
                break
            else:
                print("Invalid choice")


# Run the program
lib = Library()
lib.menu()
