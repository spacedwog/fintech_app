# ===============================
# models/budget.py
# ===============================
class Budget:
    def __init__(self, user_id, limit_value, month):
        self.user_id = user_id
        self.limit_value = limit_value
        self.month = month