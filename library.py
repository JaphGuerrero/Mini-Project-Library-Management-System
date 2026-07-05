#A simple library management system in Python

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        
    def borrow_book(self):
        """Attempts to borrow the book.

        Returns True if the book was successfully borrowed,
        otherwise returns False if it was already unavailable.
        """
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        """Returns the book to the library.

        Marks the book as available again if it was previously borrowed.
        Returns True if successful, otherwise False.
        """
        if not self.is_available:
            self.is_available = True
            return True
        return False

    def display_info(self):
        """Displays the book's title, author, and availability status."""
        print(f"Title: {self.title}, Author: {self.author}, Available: {self.is_available}")
    

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        """Adds a Book object to the library collection."""
        self.books.append(book)
    
    def show_books(self):
        """Displays all books in the library with their details."""
        for book in self.books:
            print(f"\nTitle: {book.title}, Author: {book.author}, Available: {book.is_available}")
    
    def find_book(self, title):
        """Searches for a book by title and returns it if found."""
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def borrow_book(self, title):
        """Allows the user to borrow a specific book by title."""
        for book in self.books:
            if book.title == title:
                if book.borrow_book():
                    print(f"You have successfully borrowed '{title}'.")
                    return
                else:
                    print(f"Sorry, '{title}' is currently unavailable.")
                    return
                
    
    def return_book(self, title):
        """Allows the user to return a borrowed book by title."""
        for book in self.books:
            if book.title == title:
                if book.return_book():
                    print(f"You have successfully returned '{title}'.")
                    return
                else:
                    print(f"'{title}' was not borrowed.")
                    return


def main():
    pass  # Placeholder for the main function implementation