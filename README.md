# python-mini-projects
Small Python programs as part of my learning journey
# Library Book Tracker

A simple Python command-line application for managing a small library system.
The program allows users to view, borrow, and return books while maintaining data persistence through file storage.

---

## Features

* View all books with current status (Available / Borrowed)
* Borrow and return books with validation checks
* Prevents duplicate or invalid entries
* Automatically saves borrowed books to a file
* Loads previous session data on startup

---

## Skills Demonstrated

* Python fundamentals (variables, lists, functions)
* Control flow (`if/elif/else`, loops)
* File handling (read/write, persistence)
* Input validation and error handling
* Data normalisation (cleaning and formatting user input)
* Basic data integrity practices

---

## Project Structure

```text
library-book-tracker/
├── library_tracker.py
└── borrowed.txt (auto-created on first run)
```

---

## How to Run

### Option 1. Command Line

```bash
python library_tracker.py
# or (Windows alternative)
py library_tracker.py
```

### Option 2. IDE

Open the file in an IDE (e.g. VS Code) and click **Run**.

---

## Example Usage

```text
Welcome to the Library Book Tracker

Library Menu:
1. View all books by status
2. Borrow a book
3. Return a book
4. Save and exit

please select the desired option: 1

All books:
The Little Prince - Available
War And Peace - Borrowed
1984 - Available

Totals: 1 borrowed, 4 available (20% borrowed)
```

---

## How It Works

* A predefined list of books represents the library catalogue
* Borrowed books are stored in `borrowed.txt`
* Data is loaded at startup and saved on exit
* Input is normalised to ensure consistency (e.g. spacing and capitalisation)

---

## Purpose

This project was developed as part of building foundational Python and problem-solving skills, with a focus on writing clean, structured code and handling real-world scenarios such as persistent data storage and user input validation.

---

## Future Improvements

* Add ability to dynamically add/remove books
* Implement user accounts for tracking borrowers
* Improve error handling and edge case coverage
* Add a graphical user interface (GUI)
* Convert to a database-backed system (e.g. SQLite)

---

## Author

Aviv Gafni
Aspiring Cybersecurity Professional | Background in biotechnology and research
