class Library:

    def __init__(self):
        # Predefined list of books
        self.books = [
            "The Housemaid",
            "Never Lie",
            "The Coworker",
            "Rock Paper Scissors",
            "His & Hers",
            "Sometimes I Lie",
            "Then She Was Gone",
            "The Family Upstairs",
            "None of This Is True",
            "A Good Girl's Guide to Murder",
            "Five Survive",
            "The Reappearance of Rachel Price"
        ]

    # Display all available books
    def display_books(self):
        print("\n========== AVAILABLE BOOKS ==========")

        if len(self.books) == 0:
            print("No books available.")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

        print("=====================================\n")

    # Add a new book
    def add_book(self, book):
        if book in self.books:
            print(f'"{book}" is already in the library.\n')
        else:
            self.books.append(book)
            print(f'"{book}" has been added successfully.\n')

    # Issue a book
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'You have successfully issued "{book}".\n')
        else:
            print(f'Sorry! "{book}" is not available.\n')

    # Return a book
    def return_book(self, book):
        if book in self.books:
            print(f'"{book}" is already available in the library.\n')
        else:
            self.books.append(book)
            print(f'Thank you! "{book}" has been returned.\n')


#Providing choices and calling the functions according to it

library = Library()

while True:

    print("========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        new_book = input("Enter book name to add: ")
        library.add_book(new_book)

    elif choice == "3":
        issue = input("Enter book name to issue: ")
        library.issue_book(issue)

    elif choice == "4":
        returned = input("Enter book name to return: ")
        library.return_book(returned)

    elif choice == "5":
        print("\nThank you for using the Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.\n")