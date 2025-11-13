# Used Google AI Overview to find and learn how to use PrettyTable
from prettytable import PrettyTable
from library_books import library_books
# Used Google AI Overview to learn how to use timedelta
from datetime import datetime, timedelta

# -------- Level 1 --------
# Function that shows all books that are currently available
# Output includes book ID, title, and author

def show_available_books():
    # Create table with headers
    table = PrettyTable()
    table.field_names = ["Book ID", "Title", "Author"]

    # Append row to table for each available book
    for book in library_books:
        if book["available"]:
            table.add_row([book["id"], book["title"], book["author"]])
    
    # Show table
    print(table)

# -------- Level 2 --------
# Function that returns books with same author or genre
# Search is case-insensitive
# Returns a list of matching books

def search_books(query):
    # Empty list to hold matching books
    matching_books = []

    # Check each book for matching author or genre
    # If matching, append to matching_books list
    for book in library_books:
        if (query.lower() == book["author"].lower() or query.lower() == book["genre"].lower()):
            matching_books.append(book)
    
    # Return matching books
    return matching_books


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout_book(book_id):
    # Find the book by ID
    for book in library_books:
        if book["id"] == book_id:
            # Check if book is available
            if not book["available"]:
                # Print unavailable message
                print("Book is unavailable.")
            else:
                # Set book availability to false, increment checkouts by 1, and set due date to 2 weeks from now
                book["available"] = False
                book["checkouts"] += 1
                book["due_date"] = datetime.now() + timedelta(weeks=2)


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
