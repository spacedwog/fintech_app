# ===============================
# services/report_service.py
# ===============================
from database import get_connection

class ReportService:

    @staticmethod
    def monthly_summary(user_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT strftime('%m', date), SUM(amount)
        FROM expenses
        WHERE user_id=?
        GROUP BY strftime('%m', date)
        """, (user_id,))

        data = cursor.fetchall()
        conn.close()
        return data