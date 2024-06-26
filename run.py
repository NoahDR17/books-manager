import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('books_manager')


class Book:
    """
    Represents a book with attributes such as name, author, pages, and price.

    Attributes:
        name (str): The title of the book.
        author (str): The author of the book.
        pages (int): The number of pages in the book.
        price (float): The price of the book.
    """

    def __init__(self, name, author, pages, price):
        """
        Initializes a new instance of the Book class.

        Args:
            name (str): The title of the book.
            author (str): The author of the book.
            pages (int): The number of pages in the book.
            price (float): The price of the book.
        """
        self.name = name
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the Book object.

        Returns:
            str: A formatted string containing the book's title, author,
                 number of pages, and price.
        """
        return (
            f"'{self.name}' by {self.author}, "
            f"{self.pages} pages, ${self.price:.2f}"
        )


class Library:
    """
    Represents a library containing a collection of books managed through
    Google Sheets.

    Attributes:
        books (list): A list of Book objects representing the
        library's collection.
        sheet (gspread.Spreadsheet): The Google Sheets spreadsheet
        used to store book data.
    """
    def __init__(self):
        """
        Initializes the library with an empty list of books
        and loads any books from Google Sheets.
        """
        self.books = []
        self.sheet = GSPREAD_CLIENT.open('books_manager').sheet1
        self.load_books_from_google_sheet()

    def update_google_sheet(self):
        """
        Updates the Google Sheet with the current list of books.
        """
        try:
            self.sheet.clear()  # Clear the existing content
            # Add header row
            self.sheet.append_row(['Title', 'Author', 'Pages', 'Price'])
            # Add book data
            for book in self.books:
                self.sheet.append_row([
                    book.name,
                    book.author,
                    book.pages,
                    book.price
                ])
        except Exception as e:
            print(f"An error occurred while updating Google Sheets: {e}")

    def load_books_from_google_sheet(self):
        """
        Loads the books from Google Sheets into the library.
        """
        try:
            rows = self.sheet.get_all_records()
            for row in rows:
                name = row['Title']
                author = row['Author']
                pages = int(row['Pages'])
                price = float(row['Price'])
                book = Book(name, author, pages, price)
                self.books.append(book)
        except Exception as e:
            print("Error occurred loading books from Google Sheets: " f"{e}")

    def add_book(self, book):
        """
        Adds a new book to the library and updates the Google Sheet.
        """
        self.books.append(book)
        self.update_google_sheet()

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
        If no book matches the name inputted then returns
        a message informing the user there is no book by
        that name in the library.
        """
        for book in self.books:
            if book.name.lower() == book_name.lower():
                return (
                    f"Name: {book.name}, "
                    f"Author: {book.author}, "
                    f"Pages: {book.pages}, "
                    f"Price: ${book.price:.2f}"
                )
        return "The book is not in the library."

    def remove_book(self, book_name):
        """
        Removes a book from the library by name and updates the Google Sheet.
        """
        for book in self.books:
            if book.name.lower() == book_name.lower():
                self.books.remove(book)
                self.update_google_sheet()
                return f"'{book_name}' has been removed from the library."
        return "The book is not in the library."


def create_book_for_library(library):
    """
    Prompts the user to enter details for a new book and
    adds it to the library.
    """

    try:
        while True:
            name = input("Enter the name of the book: ")
            if len(name) < 1:
                print("Invalid input. Please enter a name")
                continue
            else:
                break
        while True:
            author = input("Enter the author of the book: ")
            if len(author) < 1:
                print("Invalid input. Please enter an auther")
                continue
            else:
                break
        while True:
            try:
                pages = int(input("Enter the number of pages in the book: "))
            except ValueError:
                print("Invalid input. Please enter a whole number")
                continue
            if pages < 1:
                print("Invalid input. Please enter a number greater than 0")
                continue
            else:
                break
        while True:
            try:
                price = float(input("Enter the price of the book: "))
            except ValueError:
                print("Invalid input. Please enter a number")
                continue
            if price < 1:
                print("Invalid input. Please enter a number greater than 0")
                continue
            else:
                break
        new_book = Book(name, author, pages, price)
        library.add_book(new_book)
        print(f"'{name}' has been added to the library.")
    except ValueError:
        print("Invalid input. Please enter the correct values")


def search_for_book(library):
    """
    Prompts the user to enter a book name to search for and displays
    the search result.
    """
    book_name = input("Enter the name of the book to search for: ")
    result = library.search_for_book(book_name)
    print(result)


def remove_book(library):
    """
    Prompts the user to enter a book name to remove and removes it
    from the library.
    """
    book_name = input("Enter the name of the book to remove: ")
    result = library.remove_book(book_name)
    print(result)


def quit_program():
    """
    Exits the program based on user input.
    """
    while True:
        choice = input("Do you want to quit the program? (y/n): ").lower()
        if choice == 'y':
            print("Quitting the program.")
            exit()
        elif choice == 'n':
            return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def books_manager(library):
    """
    Displays a menu and manages user interaction with the library system.
    """
    while True:
        print("\n------< Books Manager >------")
        print("1. Add a book")
        print("2. Search for a book")
        print("3. View all books")
        print("4. Remove a book")
        print("5. Quit")
        print("-----------------------------\n")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid choice, please enter a number between 1 and 5.")
            continue

        if choice == 1:
            create_book_for_library(library)
        elif choice == 2:
            search_for_book(library)
        elif choice == 3:
            library.display_books()
        elif choice == 4:
            remove_book(library)
        elif choice == 5:
            quit_program()
        else:
            print("Invalid choice, please enter a number between 1 and 5.")


def main():
    """
    Calls all main functions
    """
    library = Library()
    books_manager(library)


main()
