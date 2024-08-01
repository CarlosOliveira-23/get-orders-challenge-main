import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from src.settings.db_connection_handler import get_db_connection


class UserRepository:
    @staticmethod
    def create_user(username: str, password: str) -> int:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, generate_password_hash(password)))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id

    @staticmethod
    def find_user_by_username(username: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        return user

    @staticmethod
    def verify_password(stored_password: str, provided_password: str) -> bool:
        return check_password_hash(stored_password, provided_password)
