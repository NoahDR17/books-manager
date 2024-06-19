### Introduction

**Project Name**: Books Manager

**Description**:
Books Manager is a Python-based command-line terminal application designed to streamline the management of a digital library through integration with Google Sheets. Users can add, search for, view, and remove books from their library directly from the terminal interface.

### Purpose

**Why it exists**:
The project aims to simplify the process of organizing and maintaining a library of books digitally. It leverages Google Sheets for storage, making it accessible and manageable from anywhere with an internet connection.

### Intended Audience

**Who it's intended for**:
Books Manager is primarily targeted at book enthusiasts, librarians, educators, and anyone who manages a collection of books and prefers a digital solution for organization and accessibility.

### Objectives and Benefits

**Project Objectives**:
Books Manager aims to accomplish the following:

- **Efficient Book Management**: Users can easily add new books, search for existing ones, view their entire library, and remove books as needed, all from a straightforward command-line interface.
- **Integration with Google Sheets**: Utilizes Google Sheets API for backend storage, ensuring data is stored securely and accessible across devices.
- **Streamlined User Experience**: Offers a user-friendly experience with intuitive commands and prompts for seamless interaction.

**Benefits to Target Audience**:

- **Simplicity and Accessibility**: Simplifies the process of managing book collections digitally, reducing the overhead associated with manual cataloging.
- **Centralized Management**: Provides a centralized platform (Google Sheets) for storing and accessing book data, promoting efficiency and organization.
- **Flexibility**: Enables users to manage their library from anywhere, whether at home, in a library, or in an educational institution, enhancing accessibility and convenience.

In summary, Books Manager caters to book enthusiasts, librarians, and educators by offering a straightforward, efficient solution for managing digital libraries. By leveraging Google Sheets integration, accessibility, and ease of use, ultimately benefiting users through streamlined book management capabilities.

### Features

#### 1. Adding a Book

- **Feature Description**:
  This feature allows users to add a new book to their library through a prompt-based interface.

- **Code Reference**:
  The code responsible for this feature is located in the `create_book_for_library(library)`. Here’s a breakdown of how it works:

  - **User Input**: Prompts the user to input details such as the book's name, author, number of pages, and price.
  - **Input Validation**: Ensures that inputs for pages (integer) and price (float) are valid numeric values.
  - **Book Creation**: Constructs a `Book` object using the provided details.
  - **Library Interaction**: Calls `library.add_book(new_book)` to add the newly created book to the library instance.
  - **Google Sheets Update**: Automatically updates the associated Google Sheet (`update_google_sheet()` method in `Library` class) to reflect the addition of the new book.

- **Value to the User**:
  Users benefit from a straightforward process to input and catalog new books into their digital library, ensuring that their collection remains organized and accessible.

#### 2. Searching for a Book

- **Feature Description**:
  This feature enables users to search for a specific book by its title within the library.

- **Code Reference**:
  The search functionality is implemented in the `search_for_book(library)` function.

  - **User Input**: Prompts the user to enter the name of the book they wish to search for.
  - **Search Logic**: Iterates through the list of books (`self.books` in `Library` class) and compares each book's title (case-insensitive) with the user input.
  - **Output**: Returns details of the book if found (`__str__` method in `Book` class) or a message indicating the book is not in the library.

- **Value to the User**:
  Users can quickly retrieve information about specific books without manually scanning through their entire collection, enhancing efficiency and usability.

#### 3. Viewing All Books

- **Feature Description**:
  This feature displays all books currently stored in the library.

- **Code Reference**:
  Implemented in the `display_books()` method of the `Library` class.

  - **List Display**: Iterates through `self.books` and prints each book's details using their `__str__` method.
  - **Empty Library Handling**: If there are no books (`self.books` is empty), it notifies the user that the library is empty.

- **Value to the User**:
  Provides users with a comprehensive overview of their entire book collection, facilitating easier management and reference.

#### 4. Removing a Book

- **Feature Description**:
  Allows users to remove a book from their library.

- **Code Reference**:
  The removal functionality is handled in the `remove_book(library)` function.

  - **User Input**: Prompts the user to enter the name of the book they want to remove.
  - **Book Removal**: Finds the book by its title (case-insensitive) in `self.books` and removes it.
  - **Google Sheets Update**: Updates the Google Sheet (`update_google_sheet()` method in `Library` class) to reflect the removal of the book.

- **Value to the User**:
  Enables users to maintain an up-to-date library by removing books they no longer wish to keep, ensuring accurate cataloging and management.

#### 5. Quitting the Program

- **Feature Description**:
  Provides an option for users to exit the program.

- **Code Reference**:
  Handled within the `quit_program()` function.

  - **User Confirmation**: Prompts the user to confirm their intention to quit the program (`'y'` for yes, `'n'` for no).
  - **Exit**: Calls `exit()` to terminate the program if the user confirms.

- **Value to the User**:
  Offers a straightforward way to gracefully exit the application once users have completed their tasks, ensuring a user-friendly experience.

Certainly! Here's the complete block of text formatted in Markdown (.md) file format:

### Manual Testing

#### Test Cases

1. Adding a Book

   - **Description**: Test the functionality of adding a new book to the library.
   - **Steps**:
     1. Run the program using `python3 run.py`.
     2. Select option 1. Add a book from the main menu.
     3. Enter the book name when prompted.
     4. Enter the author name when prompted.
     5. Enter the number of pages when prompted.
     6. Enter the price when prompted.
   - **Expected Result**:
     - The book should be added to the library.
     - A message should be displayed: [Book Name] has been added to the library.
     - The book should be visible in the Google Sheet books_manager.
   - **Actual Result**:
     - ![Book Added](./docs/testing/test1.png)
     - ![Book Added to Google Sheet](./docs/testing/test1-google-sheet.png)

2. Searching for a Book

   - **Description**: Test the functionality of searching for an existing book in the library.
   - **Steps**:
     1. Run the program using `python3 run.py`.
     2. Select option 2. Search for a book from the main menu.
     3. Enter the name of an existing book when prompted.
   - **Expected Result**:
     - The details of the book should be displayed: Name: [Book Name], Author: [Author], Pages: [Pages], Price: $[Price].

3. Viewing All Books

   - **Description**: Test the functionality of viewing all books currently in the library.
   - **Steps**:
     1. Run the program using `python3 run.py`.
     2. Select option 3. View all books from the main menu.
   - **Expected Result**:
     - A list of all books currently in the library should be displayed with details: 1. '[Book Name]' by [Author], [Pages] pages, $[Price].

4. Removing a Book

   - **Description**: Test the functionality of removing an existing book from the library.
   - **Steps**:
     1. Run the program using `python3 run.py`.
     2. Select option 4. Remove a book from the main menu.
     3. Enter the name of an existing book to remove when prompted.
   - **Expected Result**:
     - The book should be removed from the library.
     - A message should be displayed: '[Book Name]' has been removed from the library.
     - The book should no longer be visible in the Google Sheet books_manager.

5. Invalid Book Removal

   - **Description**: Test the scenario where an attempt is made to remove a non-existent book from the library.
   - **Steps**:
     1. Run the program using `python3 run.py`.
     2. Select option 4. Remove a book from the main menu.
     3. Enter the name of a non-existent book to remove when prompted.
   - **Expected Result**:
     - A message should be displayed: `The book is not in the library.`
     - No changes should be made to the library or the Google Sheet.

6. Invalid Book Search

   - **Description**: Test the scenario where an attempt is made to search for a non-existent book in the library.
   - **Steps**:
     1. Run the program using `python3 run.py`.
     2. Select option 2. Search for a book from the main menu.
     3. Enter the name of a non-existent book when prompted.
   - **Expected Result**:
     - A message should be displayed: `The book is not in the library.`

7. Exiting the Program

   - **Description**: Test the functionality of exiting the program.
   - **Steps**:
     1. Run the program using `python3 run.py`.
     2. Select option 5. Quit from the main menu.
   - **Expected Result**:
     - The Program should request comfirmation of exit to the user, (y/n) and be (Case Insensitive), it should throw an error if user inputs anything other than (y/Y)/(n/N).
     - The program should exit and the message `Quitting the program.` should be displayed.

8. Invalid Data Type for Pages

   - **Description**: Test the scenario where an invalid data type (non-integer) is entered for the number of pages.
   - **Steps**:
     1. Run the program using `python3 run.py`.
     2. Select option 1. Add a book from the main menu.
     3. Enter the book name when prompted.
     4. Enter the author name when prompted.
     5. Enter a non-integer value (e.g., 'abc') for the number of pages.
     6. Enter the price when prompted.
   - **Expected Result**:
     - The program should display an error message: `Invalid input. Please enter a whole number.`
     - The book should not be added to the library.

9. Invalid Data Type for Price

   - **Description**: Test the scenario where an invalid data type (non-float) is entered for the book price.
   - **Steps**:
     1. Run the program using `python3 run.py`.
     2. Select option 1. Add a book from the main menu.
     3. Enter the book name when prompted.
     4. Enter the author name when prompted.
     5. Enter the number of pages when prompted.
     6. Enter a non-float value (e.g., 'abc') for the price.
   - **Expected Result**:
     - The program should display an error message: `Invalid input. Please enter a number.`
     - The book should not be added to the library.

10. Non-Numeric Input for Pages

    - **Description**: Test the scenario where non-numeric input (e.g., 'one hundred') is entered for the number of pages.
    - **Steps**:
      1. Run the program using `python3 run.py`.
      2. Select option 1. Add a book from the main menu.
      3. Enter the book name when prompted.
      4. Enter the author name when prompted.
      5. Enter a non-numeric value (e.g., 'one hundred') for the number of pages.
      6. Enter the price when prompted.
    - **Expected Result**:
      - The program should display an error message: `Invalid input. Please enter a whole number.`
      - The book should not be added to the library.

11. Non-Numeric Input for Price

    - **Description**: Test the scenario where non-numeric input (e.g., 'twenty-nine') is entered for the book price.
    - **Steps**:
      1. Run the program using `python3 run.py`.
      2. Select option 1. Add a book from the main menu.
      3. Enter the book name when prompted.
      4. Enter the author name when prompted.
      5. Enter the number of pages when prompted.
      6. Enter a non-numeric value (e.g., 'twenty-nine') for the price.
    - **Expected Result**:
      - The program should display an error message: `Invalid input. Please enter a number.`
      - The book should not be added to the library.

12. Invalid Menu Choice

    - **Description**: Test the scenario where an invalid menu choice (non-numeric or out-of-range) is entered in the main menu.
    - **Steps**:
      1. Run the program using `python3 run.py`.
      2. Enter a non-numeric or out-of-range value when prompted to enter a menu choice.
    - **Expected Result**:
      - The program should display an error message: `Invalid choice, please enter a number between 1 and 5.`
      - The main menu should be displayed again for valid input.
    - **Actual Result**:
      - When input is a string, test followed the Expected Result.
      - When input is an integer outside of the range of the menu (1-5), throws error `Invalid choice, please try again.`
    - **Fix**:
      - There were two Error cases, one threw the `Invalid choice, please enter a number between 1 and 5.` error if a value that wasnt an integer was given, the other threw `Invalid choice, please try again.`, as an else case in my if/elif statements.
    - **Code Before Fix**:
    - (insert image)
    - **Code After Fix**:
    - (inser image)

13. Adding a Book with Empty Name

    - **Description**: Test the scenario where the user attempts to add a book with an empty name.
    - **Steps**:
      1. Run the program using `python3 run.py`.
      2. Select option 1. Add a book from the main menu.
      3. Enter an empty string ("") when prompted for the book name.
      4. Enter the author name when prompted.
      5. Enter the number of pages.
      6. Enter the price.
    - **Expected Result**:
      - The program should display an error message: `Invalid input. Please enter a name.`
      - The book should not be added to the library.

14. Viewing All Books When Library is Empty

    - **Description**: Test the scenario where the user views all books in the library when the library is empty.
    - **Steps**:
      1. Run the program using `python3 run.py`.
      2. Select option 3. View all books from the main menu.
    - **Expected Result**:
      - The program should display a message: `The library is empty.`

15. Invalid Data Type for Number of Pages (Negative Integer)

    - **Description**: Test the scenario where a negative integer is entered for the number of pages.
    - **Steps**:
      1. Run the program using `python3 run.py`.
      2. Select option 1. Add a book from the main menu.
      3. Enter a negative integer (e.g., -100) for the number of pages.
      4. Enter the book name, author, and price.
    - **Expected Result**:
      - The program should display an error message: `Invalid input. Please enter a positive number for pages.`
      - The book should not be added to the library.

16. Invalid Data Type for Price (Negative Float)

    - **Description**: Test the scenario where a negative float value is entered for the book price.
    - **Steps**:
      1. Run the program using `python3 run.py`.
      2. Select option 1. Add a book from the main menu.
      3. Enter a negative float value (e.g., -29.99) for the price.
      4. Enter the book name, author, and number of pages.
    - **Expected Result**:
      - The program should display an error message: `Invalid input. Please enter a positive number for price.`
      - The book should not be added to the library.

17. Removing a Book with Case Sensitivity

    - **Description**: Test the scenario where the user attempts to remove a book with case sensitivity in the name.
    - **Steps**:
      1. Run the program using `python3 run.py`.
      2. Add a book with a specific name (e.g., "Book").
      3. Select option 4. Remove a book from the main menu.
      4. Enter the name of the book using a different case (e.g., "book") when prompted.
    - **Expected Result**:
      - The program should remove the book from the library and display a message: `'[Book Name]' has been removed from the library.`
      - The book should be removed from the Google Sheet.

18. Viewing All Books After Removal
    - **Description**: Test the scenario where the user views all books after removing all books from the library.
    - **Steps**:
      1. Run the program using `python3 run.py`.
      2. Select option 3. View all books from the main menu.
    - **Expected Result**:
      - The program should display a message: `The library is empty.`
