# ===============================
# services/expense_service.py
# ===============================
from database import get_connection

class ExpenseService:

    @staticmethod
    def add_expense(user_id, category_id, amount, date, description):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO expenses (user_id, category_id, amount, date, description)
        VALUES (?, ?, ?, ?, ?)
        """, (user_id, category_id, amount, date, description))

        conn.commit()
        conn.close()

    @staticmethod
    def get_expenses(user_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM expenses WHERE user_id=?", (user_id,))
        data = cursor.fetchall()

        conn.close()
        return data