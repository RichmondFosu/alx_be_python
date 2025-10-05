class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Book is available initially

    def check_out(self):
        """Marks the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # checkout successful
        return False  # already checked out

    def return_book(self):
        """Marks the book as returned if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # successfully returned
        return False  # was not checked out

    def is_available(self):
        """Returns True if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # list to store all Book objects

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Tries to check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"'{book.title}' is checked out successfully."
                else:
                    return f"'{book.title}' is already checked out."
        return f"'{title}' not found in library."

    def return_book(self, title):
        """Tries to return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"'{book.title}' has been returned."
                else:
                    return f"'{book.title}' was already available."
        return f"'{title}' not found in library."

    def list_available_books(self):
        """Prints all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available in the library.")
