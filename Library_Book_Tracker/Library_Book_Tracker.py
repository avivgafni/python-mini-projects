# Library Book Tracker program
# Author - Aviv Gafni

import os # standard library function used for file existence check

# Create lists for library books - Assuming library only has these books below
available_books =["The Little Prince", "War And Peace", "1984", "Pride And Prejudice", "The Great Gatsby"]
borrowed_books =[]

### Program Functions: ###

# function - Normalise string input - Remove extra whitespaces and capitalise book titles

def tidy(text):
    return text.strip().title()

# Function - View books by status
def view_books():
    print("All books:\n")
    for book in available_books:
        if book in borrowed_books:
            print(book,"- Borrowed")
        else:
            print(book,"- Available")

    # Create numerical summary of library book status
    total = len(available_books) # Total number of books
    borrowed_count = len(borrowed_books) # Number of borrowed books
    available_count = total - borrowed_count  # Number of books available to borrow
    percent_borrowed = (borrowed_count / total) * 100  # Percent of books borrowed
    print("\nTotals: " + str(borrowed_count) + " borrowed, " + str(available_count) + \
    " available (" + str(int(percent_borrowed)) + "% borrowed)") # Summary

# Function - Load borrowed book titles from file -  Allowing to append
def load_data():
    if os.path.isfile("borrowed.txt"):  # File existence check
        with open("borrowed.txt", "a+") as file: # read and append to file, create if missing
            file.seek(0)  # move cursor to beginning of the text file so file will be read from the start
            for line in file:
                title = tidy(line) # removes title whitespace and capitalise first letter in book title
                if title!= "" and title in available_books and title not in borrowed_books: # avoid duplicates & blanks
                    borrowed_books.append(title)
    else:
        with open("borrowed.txt", "w+") as file: # if file does not exist, create a new one
            for line in file:
                title = tidy(line) # removes title whitespace and capitalise first letter in book title
                if title!= "" and title in available_books and title not in borrowed_books: # avoid duplicates & blanks
                    borrowed_books.append(title)


# Function - Save borrowed books to text file
def save_data():
    with open("borrowed.txt", "w") as file: # Save borrowed books to file
        for i in range(len(borrowed_books)): # This loop writes every borrowed title to the file, one per line.
            file.write(borrowed_books[i] + "\n")

# Function - Borrow book
def borrow():
    title = tidy(input("Enter book title to borrow: "))
    if title in available_books and title not in borrowed_books:
        borrowed_books.append(title)
        print("You successfully borrowed the book:", title)
    elif title in borrowed_books and title in available_books:
        print("This book has already been borrowed")
    else:
        print("Sorry, this book is not available in our library")

# Function - Return book
def book_return():
    title = tidy(input("Enter book title to return: "))
    if title in borrowed_books:
        borrowed_books.remove(title)
        print("Book has been successfully returned")
    elif title not in borrowed_books and title in available_books:
        print("This book has not been borrowed")
    else:
        print("Sorry, this book is not available in our library")

load_data() # load/create borrowed file before launching main program


# Main program -  Menu runs in loop until exit
print("Welcome to the Library Book Tracker")
while True:
        print("\nLibrary Menu:")
        print("1. View all books by status")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Save and exit\n")
        selection = input("please select the desired option: ") # Call for relevant function based on input
        if selection == "1":
            view_books()
        elif selection == "2":
            borrow()
        elif selection == "3":
            book_return()
        elif selection == "4":
            save_data()
            print("File saved, existing program")
            break
        else:
            print("please choose a number from the menu below: ") # Deals with invalid/unexpected input
