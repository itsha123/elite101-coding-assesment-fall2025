"""Module that contains all the code for a simple library book management system."""
# Used Ruff docs to figure out how to fix issues found by Ruff
# Used Google AI Overview to find and learn how to use PrettyTable
# Used Google AI Overview to learn how to use timedelta
from datetime import datetime, timedelta, timezone

from prettytable import PrettyTable

from library_books import Book, library_books

# -------- Level 1 --------
# Function that shows all books that are currently available.
# Output includes book ID, title, and author.

def show_available_books() -> None:
    """Display all available books in a table format."""
    # Create table with headers.
    table = PrettyTable()
    table.field_names = ["Book ID", "Title", "Author"]

    # Append row to table for each available book.
    for book in library_books:
        if book["available"]:
            table.add_row([book["id"], book["title"], book["author"]])

    # Show table.
    print(table)

# -------- Level 2 --------
# Function that returns books with same author or genre.
# Search is case-insensitive.
# Returns a list of matching books.

def search_books(query: str) -> list[Book]:
    """Search for books by matching author or genre."""
    # Empty list to hold matching books.
    matching_books: list[Book] = []

    # Check each book for matching author or genre.
    # If matching, append to matching_books list.
    for book in library_books:
        if (query.lower() == book["author"].lower() or query.lower() == book["genre"].lower()):  # noqa: E501
            matching_books.append(book)  # noqa: PERF401

    # Return matching books.
    return matching_books


# -------- Level 3 --------
# Function that checks out a book by its ID.
# If the book is available:
#   - Mark it unavailable.
#   - Set the due_date to 2 weeks from today.
#   - Increment the checkouts counter.
# If it is not available:
#   - Print a message saying it's unavailable.

def checkout_book(book_id: str) -> None:
    """Checkout a book by its ID."""
    # Find the book by its ID.
    for book in library_books:
        if book["id"] == book_id:
            # Check if book is available.
            if not book["available"]:
                # Print unavailable message.
                print("Book is unavailable.")
            else:
                # Set book availability to false.
                # Increment checkouts by 1.
                # Set due date to 2 weeks from now.
                book["available"] = False
                book["checkouts"] += 1
                book["due_date"] = datetime.now(tz=timezone.utc) + timedelta(weeks=2)


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Partial title/author/genre search
# - Save/load catalog to file (CSV or JSON)
# - Number of copies total, available, and unavailable

if __name__ == "__main__":
    checkout_book("B1")
