"""
This module represents our "Infrastructure Layer".
It connects to a SQLite database. 
In a real application, this could be connecting to PostgreSQL or MongoDB.
Because it talks to a real database, testing it requires Integration Tests.
"""
import sqlite3

class Database:
    def __init__(self, db_name="users.db"):
        self.connection = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self):
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL
            )
            '''
        )
        self.connection.commit()

    def get_user_by_username(self, username: str):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, username, email FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if row:
            return {"id": row[0], "username": row[1], "email": row[2]}
        return None

    def create_user(self, username: str, email: str):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            # E.g., user already exists
            return False
