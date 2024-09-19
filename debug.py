from models import Author
from database import SessionLocal

# Example: print all authors
session = SessionLocal()
authors = session.query(Author).all()
print(authors)