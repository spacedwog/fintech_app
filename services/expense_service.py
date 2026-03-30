import sqlite3
from datetime import date

class ExpenseService:

    def __init__(self, db):
        self.db = db

    def add_expense(self, user_id, category_id, valor, data=date.today()):
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero")

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO expenses (user_id, category_id, valor, data)
            VALUES (?, ?, ?, ?)
        """, (user_id, category_id, valor, data))

        conn.commit()
        conn.close()

    def get_expenses_by_period(self, user_id, start, end):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM expenses
            WHERE user_id=? AND data BETWEEN ? AND ?
        """, (user_id, start, end))

        return cursor.fetchall()