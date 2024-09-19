from models import Author, Book
from database import SessionLocal, init_db

# Initialize the database
init_db()

# Start a session
session = SessionLocal()

def create_author():
    name = input("Enter the author's name: ")
    new_author = Author(name=name)
    session.add(new_author)
    session.commit()
    print(f"Author {name} added.")

def view_authors():
    authors = session.query(Author).all()
    if not authors:
        print("No authors found.")
    for author in authors:
        print(f"ID: {author.id}, Name: {author.name}")

def create_book():
    title = input("Enter the book title: ")
    view_authors()
    author_id = input("Enter the author ID for this book: ")
    author = session.get(Author, author_id)
    if author:
        new_book = Book(title=title, author=author)
        session.add(new_book)
        session.commit()
        print(f"Book {title} by {author.name} added.")
    else:
        print("Author not found.")

def view_books():
    books = session.query(Book).all()
    if not books:
        print("No books found.")
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author.name}")

def delete_author():
    choices = {
        "1": "name",
        "2": "id"
    }
    choice = input("Do you want to delete by (1) Name or (2) ID? ")
    if choice in choices:
        if choices[choice] == "name":
            name = input("Enter the name of the author to delete: ")
            author = session.query(Author).filter_by(name=name).first()
            if author:
                session.delete(author)
                session.commit()
                print(f"Author '{name}' and all their books have been deleted.")
            else:
                print(f"Author '{name}' not found.")
        elif choices[choice] == "id":
            try:
                author_id = int(input("Enter the ID of the author to delete: "))
                author = session.get(Author, author_id)
                if author:
                    session.delete(author)
                    session.commit()
                    print(f"Author with ID '{author_id}' and all their books have been deleted.")
                else:
                    print(f"Author with ID '{author_id}' not found.")
            except ValueError:
                print("Invalid ID. Please enter a valid number.")
    else:
        print("Invalid choice. Please select 1 for Name or 2 for ID.")
def delete_book():
    choices = {
        "1": "title",
        "2": "id"
    }

    choice = input("Do you want to delete by (1) Title or (2) ID? ")
    if choice in choices:
        if choices[choice] == "title":
            title = input("Enter title of book to be deleted: ")
            book = session.query(Book).filter_by(title=title).first()
            if book:
                session.delete(book)
                session.commit()
                print(f"Book '{title}' has been deleted.")
            else:
                print(f"Book '{title}' not found.")
        elif choices[choice] == "id":
            try:
                book_id = int(input("Enter the ID of the book to delete: "))
                book = session.get(Book, book_id)
                if book:
                    session.delete(book)
                    session.commit()
                    print(f"Book with ID '{book_id}' has been deleted.")
                else:
                    print(f"Book with ID '{book_id}' not found.")
            except ValueError:
                print("Invalid ID. Please enter a valid number.")
    else:
        print("Invalid choice. Please select 1 for Title or 2 for ID.")


def main_menu():
   menu_options= [
          ("1. Add Author", create_author),
        ("2. View Authors", view_authors),
        ("3. Add Book", create_book),
        ("4. View Books", view_books),
        ("5. Delete Author", delete_author),
        ("6. Delete Book", delete_book),
        ("7. Exit", exit)
   ]

   while True:
       print("\nLib_management")
       for option, _ in menu_options:
           print(option)
       
       choice = input("Enter your choice: ")
       for option, action in menu_options:
           if choice == option[0]:
               action()
               break
       else:
           print("Invalid choice. Please try again.")
           

if __name__ == "__main__":
    main_menu()