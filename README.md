# Elite 101 Coding Assesment - Class of Fall 2025

This is the final coding assesment for the Code2College Fall 2025 Elite 101 interview prep class.

## Disclaimers

This project was made with the assistance of GitHub Copilot autocompletions and next edit suggestions.

Google AI Overview was used to decide on psuedocode conventions, and ChatGPT was used to decide to use Ruff for Python standard conventions.

GitHub Copilot was used to help make the pyproject.toml file, to help fix issues found by Ruff, and to help fix bugs.

## Library Inventory and Checkout Manager

The purpose of this code is to make a Library Inventory and Checkout manager utilizing the list of library books already provided. The functionality is split into multiple levels.

### Level 1

- Create a function that prints all <u>available</u> books.
- Include book ID, title, and author.

### Level 2

- Allow the user to search for books.
- Return books with matching authors or genres.
- Make the search case-insensitive.

### Level 3

- Allow the user to checkout a book using book ID.
- Increment checkouts number when checking out and set as unavailable.
- Set due date two weeks from now using `datetime`.
- If book is already checked out, show a message.

### Level 4

- Write a function to return book by book ID.
- Reset availability and due date.
- Write function to list all overdue books.

### Level 5

- Create a `Book` class
- Make books as objects, not part of a dictionary.
- Create CLI that:
  - Shows available books
  - Allows search
  - Allows checkout
  - Allows return
  - Shows overdue books
  - Shows top 3 most checked out books

### Level 6 (Advanced Features)

- Add new book functionality
- Partial title, author, and genre search
- Save & Load catalog to CSV
- Add multiple copies functionality

### Level 7 (My Addition)

- Use `tkinter` to make full GUI
- Use Sun Valley theme

<sup>A project made for Code2College.</sup>
