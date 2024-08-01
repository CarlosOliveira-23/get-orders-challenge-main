import sqlite3
from src.settings.db_connection_handler import get_db_connection


class OrderRepository:
    @staticmethod
    def create_order(user_id: int, description: str) -> int:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (user_id, description) VALUES (?, ?)", (user_id, description))
        conn.commit()
        order_id = cursor.lastrowid
        conn.close()
        return order_id

    @staticmethod
    def get_orders_by_user_id(user_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        orders = cursor.fetchall()
        conn.close()
        return orders
