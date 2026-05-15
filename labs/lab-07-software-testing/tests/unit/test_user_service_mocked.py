import pytest
import sys
import os
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from user_service import UserService

def test_register_user_success():
    """
    UNIT TEST WITH MOCKING
    Here we test the UserService. However, UserService requires a Database object.
    Instead of passing a real SQLite database, we pass a "MagicMock".
    A mock is a fake object that we can program to behave exactly how we want.
    """
    # 1. Arrange: Setup the mock
    mock_db = MagicMock()
    # We tell the fake database: "When get_user_by_username is called, return None"
    mock_db.get_user_by_username.return_value = None
    # We tell the fake database: "When create_user is called, return True"
    mock_db.create_user.return_value = True

    # We inject the fake DB into the real service
    service = UserService(database=mock_db)

    # 2. Act
    result = service.register_user("alice", "alice@example.com")

    # 3. Assert
    assert result == "Success: User registered"
    
    # We can also verify that the service actually called the DB correctly!
    mock_db.get_user_by_username.assert_called_once_with("alice")
    mock_db.create_user.assert_called_once_with("alice", "alice@example.com")


def test_register_user_already_exists():
    """Test what happens when the database says the user already exists."""
    mock_db = MagicMock()
    # Program the mock to return a fake user dictionary instead of None
    mock_db.get_user_by_username.return_value = {"id": 1, "username": "alice", "email": "a@b.com"}

    service = UserService(database=mock_db)
    result = service.register_user("alice", "alice@example.com")

    assert result == "Error: User already exists"
    # Ensure it never tried to create the user since it already existed
    mock_db.create_user.assert_not_called()
