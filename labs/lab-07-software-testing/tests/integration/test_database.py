import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from database import Database

@pytest.fixture
def real_db():
    """
    A Pytest fixture that creates a REAL SQLite database in memory.
    Because it uses ':memory:', it doesn't write to the hard drive, making it faster,
    but it IS a real database parsing real SQL syntax.
    """
    db = Database(db_name=":memory:")
    yield db
    # Cleanup after test finishes
    db.connection.close()

def test_database_insert_and_retrieve(real_db):
    """
    INTEGRATION TEST
    This test actually executes the SQL strings in database.py against a real SQLite engine.
    If there was a typo in the SQL (e.g., SELECT * FROMM users), this test would catch it.
    The mocked unit tests would NOT catch a SQL typo, because they bypass the DB entirely.
    """
    # 1. Insert a user
    success = real_db.create_user("bob", "bob@example.com")
    assert success is True

    # 2. Retrieve the user
    user = real_db.get_user_by_username("bob")
    
    # 3. Verify
    assert user is not None
    assert user["username"] == "bob"
    assert user["email"] == "bob@example.com"

def test_database_duplicate_username(real_db):
    """
    Testing that the database correctly enforces the UNIQUE constraint on the username column.
    """
    real_db.create_user("charlie", "charlie@example.com")
    
    # Trying to create the same user again should fail and return False
    success = real_db.create_user("charlie", "other@example.com")
    assert success is False
