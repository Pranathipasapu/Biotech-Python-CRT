class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added to the library.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"You have borrowed '{book_name}'. Please return it on time.")
        else:
            print(f"Sorry, '{book_name}' is not available in the library.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"Thanks for returning '{book_name}'.")


def main():
    lib = Library()

    while True:
        print("\n====== Library Menu ======")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter book name to add: ")
            lib.add_book(name)
        elif choice == '2':
            lib.display_books()
        elif choice == '3':
            name = input("Enter book name to borrow: ")
            lib.borrow_book(name)
        elif choice == '4':
            name = input("Enter book name to return: ")
            lib.return_book(name)
        elif choice == '5':
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
