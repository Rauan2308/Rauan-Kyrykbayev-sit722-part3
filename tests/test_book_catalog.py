# tests/test_book_catalog.py
import pytest
from fastapi.testclient import TestClient
from book_catalog.app.main import app
from book_catalog.app.db import SessionLocal, engine
from book_catalog.app.models import Base, Book

@pytest.fixture(scope="module")
def client():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    # Drop the database tables
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    # Setup database session
    session = SessionLocal()
    yield session
    session.close()

def test_create_book(client):
    response = client.post("/books/", json={"title": "Test Book", "author": "Test Author", "isbn": "1234567890"})
    assert response.status_code == 200
    assert response.json() == {"title": "Test Book", "author": "Test Author", "isbn": "1234567890"}

def test_read_book(client, db_session):
    # Add a book to the database
    db_session.add(Book(title="Test Book", author="Test Author", isbn="1234567890"))
    db_session.commit()
    
    response = client.get("/books/1/")
    assert response.status_code == 200
    assert response.json() == {"title": "Test Book", "author": "Test Author", "isbn": "1234567890"}
