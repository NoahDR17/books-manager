class Book:
    def __init__(self, name, author, pages, price):
        self.name = name
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"'{self.name}' by {self.author}, {self.pages} pages, ${self.price:.2f}"

class Library:
    def __init__(self):
        """
        Initializes the library with an empty list of books.
        """
        self.books = []
    
    def add_book(self, book):
        """
        Adds a new book to the library.
        """
        self.books.append(book)

    def display_books(self):
        """
        Displays all the books currently in the library.
        """
        if not self.books:
            print("The library is empty.")
        else:
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def search_for_book(self, book_name):
        """
        Searches for a book by name in the library.
        If no book matches the name inputted then returns a message informing the user there is no 
        book by that name in the library.
        """
        for book in self.books:
            if book.name.lower() == book_name.lower():
                return f"Name: {book.name}, Author: {book.author}, Pages: {book.pages}, Price: ${book.price:.2f}"
        return "The book is not in the library."

    def remove_book(self, book_name):
        """
        Removes a book from the library by name.
        """
        for book in self.books:
            if book.name.lower() == book_name.lower():
                self.books.remove(book)
                return f"'{book_name}' has been removed from the library."
        return "The book is not in the library."
