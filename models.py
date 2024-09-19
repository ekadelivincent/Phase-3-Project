from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from database import Base, SessionLocal


class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author(name={self.name})>"
    
    def add(self):
        session = SessionLocal()
        try:
            session.add(self)  # Adds the current instance (self) to the session
            session.commit()   # Commits the transaction
        except Exception as e:
            session.rollback()  # Roll back if there’s an error
            raise e
        finally:
            session.close()     # Close the session to free up resources
    
    def delete(self):
        session = SessionLocal()
        try:
            session.delete(self)  # Deletes the current instance (self)
            session.commit()      # Commits the transaction
        except Exception as e:
            session.rollback()    # Roll back if there’s an error
            raise e
        finally:
            session.close()       # Close the session to free up resources
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author.name})>"
    
    def add(self):
        session = SessionLocal()
        try:
            session.add(self)  # Adds the current instance (self) to the session
            session.commit()   # Commits the transaction
        except Exception as e:
            session.rollback()  # Rollback if there's an error
            raise e
        finally:
            session.close()     # Close the session to free up resources

    def delete(self):
        session = SessionLocal()
        try:
            session.delete(self)  # Deletes the current instance (self)
            session.commit()      # Commits the transaction
        except Exception as e:
            session.rollback()    # Rollback if there's an error
            raise e
        finally:
            session.close()   