from models import Author, Book
from database import SessionLocal, init_db

# Initialize the database
init_db()

session = SessionLocal()

# Add initial authors and books
author1 = Author(name="J.K. Rowling")
author2 = Author(name="George R.R. Martin")

book1 = Book(title="Harry Potter and the Sorcerer's Stone", author=author1)
book2 = Book(title="A Game of Thrones", author=author2)

session.add_all([author1, author2, book1, book2])
session.commit()

print("Database seeded with initial authors and books.")