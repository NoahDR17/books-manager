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
