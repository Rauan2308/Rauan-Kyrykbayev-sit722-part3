# tests/test_inventory_management.py
import pytest
from fastapi.testclient import TestClient
from inventory_management.app.main import app
from inventory_management.app.db import SessionLocal, engine
from inventory_management.app.models import Base, Item
from inventory_management.app.main import app

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

def test_create_item(client):
    response = client.post("/items/", json={"name": "Test Item", "quantity": 10})
    assert response.status_code == 200
    assert response.json() == {"name": "Test Item", "quantity": 10}

def test_read_item(client, db_session):
    # Add an item to the database
    db_session.add(Item(name="Test Item", quantity=10))
    db_session.commit()
    
    response = client.get("/items/1/")
    assert response.status_code == 200
    assert response.json() == {"name": "Test Item", "quantity": 10}
