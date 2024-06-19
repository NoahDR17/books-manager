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

