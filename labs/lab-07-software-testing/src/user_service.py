"""
This module represents our "Business Logic Layer".
It depends on the Database to do its job. 
To unit test this module without touching the real database, we must use MOCKING.
"""

class UserService:
    def __init__(self, database):
        # We inject the database dependency into the service.
        self.db = database

    def register_user(self, username: str, email: str) -> str:
        """
        Registers a new user and returns a status message.
        """
        if not username or not email:
            return "Error: Missing data"

        # Check if user exists
        existing_user = self.db.get_user_by_username(username)
        if existing_user:
            return "Error: User already exists"

        # Create user
        success = self.db.create_user(username, email)
        if success:
            return "Success: User registered"
        else:
            return "Error: Database failure"
