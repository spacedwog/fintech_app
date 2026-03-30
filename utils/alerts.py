# ===============================
# utils/alerts.py
# ===============================
from database import get_connection

class Alerts:

    @staticmethod
    def check_budget(user_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT limit_value FROM budgets WHERE user_id=?", (user_id,))
        budget = cursor.fetchone()

        cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id=?", (user_id,))
        total = cursor.fetchone()[0]

        conn.close()

        if budget and total:
            if total > budget[0]:
                return True
        return False