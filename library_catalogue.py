import os

# Function to add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    with open("library.txt", "a") as f:
        f.write(title + "|" + author + "\n")

    print("Book added successfully!")


# Function to search for books
def search_book():
    search = input("Enter book title or author: ").lower()
    found = False

    if not os.path.exists("library.txt"):
        print("Book not found.")
        return

    with open("library.txt", "r") as f:
        for line in f:
            title, author = line.strip().split("|")

            if search in title.lower() or search in author.lower():
                print("Title:", title, "| Author:", author)
                found = True

    if not found:
        print("Book not found.")


# Function to update a book
def update_book():
    search = input("Enter the title of the book to update: ").lower()
    books = []
    found = False

    if not os.path.exists("library.txt"):
        print("Book not found.")
        return

    with open("library.txt", "r") as f:
        for line in f:
            title, author = line.strip().split("|")

            if title.lower() == search:
                title = input("Enter new book title: ")
                author = input("Enter new author name: ")
                found = True

            books.append(title + "|" + author + "\n")

    if found:
        with open("library.txt", "w") as f:
            f.writelines(books)
        print("Book updated successfully!")
    else:
        print("Book not found.")


# Function to generate reports
def generate_report():
    if not os.path.exists("library.txt"):
        print("Total number of books: 0")
        return

    with open("library.txt", "r") as f:
        books = [
            line.strip().split("|")
            for line in f if line.strip()
        ]

    print("Total number of books:", len(books))

    author_name = input("Enter author name: ").lower()
    count = 0

    print("Books written by", author_name, ":")

    for title, author in books:
        if author.lower() == author_name:
            print(title)
            count += 1

    print("Number of books by this author:", count)


# Function to display all books
def display_books():
    if not os.path.exists("library.txt"):
        print("No books available.")
        return

    with open("library.txt", "r") as f:
        books = f.readlines()

    if not books:
        print("No books available.")
        return

    print("\nLibrary Catalogue")
    for line in books:
        title, author = line.strip().split("|")
        print("Title:", title, "| Author:", author)


# Main menu
while True:
    print("\n===== LIBRARY CATALOGUE =====")
    print("1. Add a book")
    print("2. Search for a book")
    print("3. Update catalogue")
    print("4. Display all books")
    print("5. Generate report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        update_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        generate_report()
    elif choice == "6":
        print("Program stopped.")
        break
    else:
        print("Invalid choice. Try again.")
