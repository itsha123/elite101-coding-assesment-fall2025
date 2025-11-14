"""Module that contains all the code for a simple library book management system."""
# Used Ruff docs to figure out how to fix issues found by Ruff
# Used Google AI Overview to find and learn how to use PrettyTable
# Used Google AI Overview and Python docs to learn how to use timedelta and datetime
# Used GeeksforGeeks and Google AI Overview to learn how to use classes and objects
# Used Google AI Overview to find csv module, and use Python docs to learn how to use it
import csv
from datetime import datetime, timedelta, timezone

from prettytable import PrettyTable

from library_books import library_books


class Book:
    """Class representing each book in the library."""

    # Initialize Book object with its attributes.
    def __init__(
        self,
        book_id: str,
        title: str,
        author: str,
        genre: str,
        checkouts: int) -> None:
        """Initialize a Book object."""
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.copies: list[BookCopy] = []
        self.checkouts = checkouts

    def checkout_book(self) -> None:
        """Checkout a book."""
        # Check each copy.
        for copy in self.copies:
            # If copy is available, checkout the book.
            if copy.available:
                # Set book availability to False.
                # Increment checkouts counter.
                # Set due date to 2 weeks from now.
                copy.available = False
                self.checkouts += 1
                copy.due_date = datetime.now(tz=timezone.utc) + timedelta(weeks=2)

                # Show success message.
                print("Book checked out successfully.")

                # Exit function after checking out one copy.
                return

        # If no copies are available, show message.
        print("No copies available.")

    def return_book(self) -> None:
        """Return a book."""
        # Check each copy.
        for copy in self.copies:
            # If copy is not available, return the book.
            if not copy.available:
                # Set book availability to True.
                # Clear due date.
                copy.available = True
                copy.due_date = None

                # Show success message.
                print("Book returned successfully.")

                # Exit function after returning one copy.
                return

        # If all copies are already available, show message.
        print("All copies are already available.")

    def add_copy(self, available: bool, due_date: datetime | None) -> None:  # noqa: FBT001
        """Add a copy of the book."""
        # Create BookCopy object and append to copies list.
        self.copies.append(BookCopy(available, due_date))

class BookCopy:
    """Class representing each copy of a book in the library."""

    def __init__(
        self,
        available: bool,  # noqa: FBT001
        due_date: datetime | None) -> None:
        """Initialize a BookCopy object."""
        # Set attributes moved from Book class.
        self.available = available
        self.due_date = due_date

books_list: list[Book] = []

# -------- Level 1 - Changed by Level 5 and 6 --------
# Function that shows all books that are currently available.
# Output includes book ID, title, and author.

def show_available_books() -> None:
    """Display all available books in a table format."""
    # Create table with headers.
    table = PrettyTable()
    table.field_names = ["Book ID", "Title", "Author", "Total Copies", "Available Copies"]  # noqa: E501

    # Append row to table for each available book.
    for book in books_list:
        available_copies = 0
        for copy in book.copies:
            if copy.available:
                available_copies += 1
        if available_copies > 0:
            table.add_row([book.book_id, book.title, book.author, len(book.copies), available_copies])  # noqa: E501

    # Show table.
    print(table)

# -------- Level 2 - Changed by Level 5 and 6 --------
# Function that returns books with same author, genre, or title.
# Search is case-insensitive.
# Returns a list of matching books.

def search_books(query: str) -> list[Book]:
    """Search for books by matching author, genre, or title. Return list of matching books."""  # noqa: E501
    # Empty list to hold matching books.
    matching_books: list[Book] = []

    # Check each book for matching author, genre, or title.
    # If matching, append to matching_books list.
    for book in books_list:
        if (query.lower() in book.author.lower() or query.lower() in book.genre.lower() or query.lower() in book.title.lower()):  # noqa: E501
            matching_books.append(book)

    # Return matching books.
    return matching_books


# -------- Level 3 - Changed by Level 5 and 6 --------
# Function that checks out a book by its ID.
# If the book is available:
#   - Mark it unavailable.
#   - Set the due_date to 2 weeks from today.
#   - Increment the checkouts counter.
# If it is not available:
#   - Print a message saying it's unavailable.

# Moved to Book class.


# -------- Level 4 - Changed by Level 5 and 6 --------
# Function that returns a book by its ID.
# Sets the book's availability to True and clears the due date.

# Moved to Book class.

# Function that shows all overdue books.
# A book is overdue if its due_date is before today AND it is still checked out.

def show_overdue_books() -> None:
    """Display all overdue books in a table format."""
    # Create table with headers.
    table = PrettyTable()
    table.field_names = ["Book ID", "Title", "Author", "Total Copies", "Overdue Copies"]

    # Append row to table for each overdue book.
    for book in books_list:
        overdue_copies = 0
        for copy in book.copies:
            if not copy.available and copy.due_date is not None:
                # Get time difference between due date and now.
                time_difference: timedelta = copy.due_date.replace(tzinfo=timezone.utc) - datetime.now(tz=timezone.utc)  # noqa: E501
                if time_difference.total_seconds() < 0:
                    overdue_copies += 1

        # If there are any overdue copies, add book to table.
        if overdue_copies > 0:
            table.add_row([book.book_id, book.title, book.author, len(book.copies), overdue_copies])  # noqa: E501
    # Show table.
    print(table)


# -------- Level 5 - Changed by Level 6 --------
# Convert data into Book objects from Book class using books_to_objects function.
# Include child functions of return and checkout in Book class.

# Class is at top of file.

def books_to_objects() -> None:
    """Convert library_books dicts to Book objects and store in books_list."""
    # Iterate through each book in library_books.
    for book in library_books:
        # Convert due_date from str to datetime if necessary.
        if type(book["due_date"]) is str:
            book["due_date"] = datetime.fromisoformat(book["due_date"])
            book["due_date"] = book["due_date"].replace(tzinfo=timezone.utc)

        # Create Book object for each book and append to books_list.
        book_object = Book(
            book_id=book["id"],
            title=book["title"],
            author=book["author"],
            genre=book["genre"],
            checkouts=book["checkouts"],
        )
        book_object.add_copy(book["available"], book["due_date"]) # pyright: ignore[reportArgumentType]
        books_list.append(book_object)

# Implementation of showing top checkouts for CLI.

def show_top_checkouts() -> None:
    """Display the top 3 most checked out books."""
    # Create table with headers.
    table = PrettyTable()
    table.field_names = ["Book ID", "Title", "Author", "Total Checkouts"]

    # Temporary copy of books_list for finding top books.
    temp_books_list = books_list.copy()

    # Iterate through temp_books_list 3 times.
    for _ in range(3):
        # Initialize variables used to find top book.
        max_checkouts = 0
        top_book: Book | None = None

        # Iterate through each book in temp_books_list.
        for book in temp_books_list:
            # Update variables if book is currently the maximum so far.
            # After going through all books, top_book will be the top book.
            if book.checkouts > max_checkouts:
                max_checkouts = book.checkouts
                top_book = book

        # Remove top book from temp_books_list to find next top book in next iteration.
        temp_books_list.remove(top_book) # pyright: ignore[reportArgumentType]

        # Append top book to table.
        table.add_row([top_book.book_id, top_book.title, top_book.author, top_book.checkouts]) # pyright: ignore[reportOptionalMemberAccess]  # noqa: E501

    # Show table.
    print(table)

# Create simple CLI that allows the user to choose different options.
# Allow the user to choose from the following:
# available books, search, checkout, return, overdue books, and top 3 checked out books.

def show_cli() -> None:  # noqa: C901, PLR0912, PLR0915
    """Run the user-interactable command line interface."""
    while True:
        # Show all the options.
        print("Please select one of the following options:")
        print("1. Show available books.")
        print("2. Search for book.")
        print("3. Checkout book.")
        print("4. Return book.")
        print("5. Show overdue books.")
        print("6. Show top 3 most checked out books.")
        print("7. Add new book.")
        print("8. Export to CSV.")
        print("9. Exit")
        # Ask user for numerical menu option, raise error if they don't give a number.
        try:
            menu_option = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Run code based on user input.
        if menu_option == 1:
            # Show available books.
            show_available_books()
        elif menu_option == 2:
            # Create table with headers.
            table = PrettyTable()
            table.field_names = ["Book ID", "Title", "Author", "Total Copies", "Available Copies"]  # noqa: E501

            # Ask user for search query.
            user_query = input("Enter your search query: ")

            # Append row to table for each matching book.
            for book in search_books(user_query):
                available_copies = 0
                for copy in book.copies:
                    if copy.available:
                        available_copies += 1
                table.add_row([book.book_id, book.title, book.author, len(book.copies), available_copies])  # noqa: E501

            # Show table.
            print(table)
        elif menu_option == 3:
            # Ask user for book ID to checkout book.
            user_query = input("Enter the ID of the book you want to checkout: ")

            # Iterate through books to find matching ID.
            for book in books_list:
                if book.book_id == user_query:
                    # Checkout book.
                    book.checkout_book()
                    break
            else:
                # Print message if no matching book ID.
                print("No matching book ID.")
        elif menu_option == 4:
            # Ask user for book ID to return book.
            user_query = input("Enter the ID of the book you want to return: ")

            # Iterate through books to find matching ID.
            for book in books_list:
                if book.book_id == user_query:
                    # Return book.
                    book.return_book()
                    break
            else:
                # Print message if no matching book ID.
                print("No matching book ID.")
        elif menu_option == 5:
            # Show overdue books.
            show_overdue_books()
        elif menu_option == 6:
            # Show top 3 most checked out books.
            show_top_checkouts()
        elif menu_option == 7:
            # Add new book via user input.
            # Gather user input for book attributes.
            user_input: list[str | int] = []
            user_input.append(input("Enter the book ID: "))
            user_input.append(input("Enter the title: "))
            user_input.append(input("Enter the author: "))
            user_input.append(input("Enter the genre: "))
            user_input.append(int(input("Enter the number of checkouts: ")))
            # Create Book object based on user input.
            new_book = Book(
                user_input[0], # pyright: ignore[reportArgumentType]
                user_input[1], # pyright: ignore[reportArgumentType]
                user_input[2], # pyright: ignore[reportArgumentType]
                user_input[3], # pyright: ignore[reportArgumentType]
                user_input[4], # pyright: ignore[reportArgumentType]
            )

            # Ask user for number of total and available copies.
            user_total_copies = int(input("Enter the total copies: "))
            user_available_copies = int(input("Enter the number of available copies: "))
            # Add copies to new book based on user input.
            for _ in range(user_available_copies):
                new_book.add_copy(available=True, due_date=None)
            for _ in range(user_total_copies - user_available_copies):
                new_book.add_copy(available=False, due_date=None)

            # Add new book to books_list.
            books_list.append(new_book)

            # Show success message.
            print("Book added successfully.")
        elif menu_option == 8:
            # Export current catalog to catalog.csv.
            with open("catalog.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                # Iterate through each book in books_list.
                for book in books_list:
                    # Add book attributes to list.
                    book_info: list[str | int] = [
                        book.book_id,
                        book.title,
                        book.author,
                        book.genre,
                        book.checkouts,
                        len(book.copies)]

                    # Count available copies.
                    available_copies = 0
                    for copy in book.copies:
                        if copy.available:
                            available_copies += 1

                    # Add available copies to book attributes list.
                    book_info.append(available_copies)

                    # Write book attributes to CSV file.
                    writer.writerow(book_info)

            # Show success message.
            print("Exported successfully.")
        elif menu_option == 9:
            # Show goodbye message.
            print("Thanks for using the Library Management System. Goodbye!")
            # Exit program.
            break
        else:
            # Print message if menu option is invalid.
            # Split into two lines to reduce line length.
            print("Please enter a valid menu option.", end=" ")
            print("Valid options are (1, 2, 3, 4, 5, 6, 7).")

# -------- Level 6 (Optional Advanced Features) --------
# - Add a new book (via input) to the catalog
# - Partial title/author/genre search
# - Save/load catalog to file (CSV or JSON)
# - Number of copies total, available, and unavailable

# Main function to run the program.
if __name__ == "__main__":
    # Show welcome message.
    print("Welcome to the Library Management System!\n")

    # Ask user to load default catalog or import from file.
    while True:
        # Spliti into multiple lines to reduce line length.
        print("Would you like to load the default catalog", end=" ")
        print("or import from file at 'catalog.csv'? (default/file)", end=" ")
        user_query = input()

        if user_query == "default":
            # Load existing library_books catalog and continue to CLI.
            books_to_objects()
            break
        elif user_query == "file":
            # Load catalog from catalog.csv and continue to CLI.
            with open("catalog.csv", newline="") as csvfile:
                book_reader = csv.reader(csvfile)
                # Iterate through each row in the CSV file.
                for row in book_reader:
                    # Create Book object for each row.
                    file_book = Book(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        int(row[4]))

                    # Add copies based on total and available counts.
                    for _ in range(int(row[6])):
                        file_book.add_copy(available=True, due_date=None)
                    for _ in range(int(row[5]) - int(row[6])):
                        file_book.add_copy(available=False, due_date=None)

                    # Append new book to books_list.
                    books_list.append(file_book)

            # Continue to CLI.
            break
        else:
            # Print message if input is invalid.
            print("Invalid input. Please enter 'default' or 'file'.")

    # Show CLI to user.
    show_cli()
