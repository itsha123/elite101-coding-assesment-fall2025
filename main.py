from prettytable import PrettyTable
from library_books import library_books
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
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


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
    show_available_books()
