# ===============================
# services/auth_service.py
# ===============================
import requests
from database import get_connection

class AuthService:

    @staticmethod
    def login(cpf):
        # API ReceitaWS
        url = f"https://www.receitaws.com.br/v1/cpf/{cpf}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            name = data.get("nome", "Usuário")

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users WHERE cpf=?", (cpf,))
            user = cursor.fetchone()

            if not user:
                cursor.execute("INSERT INTO users (cpf, name) VALUES (?, ?)", (cpf, name))
                conn.commit()

            conn.close()
            return name

        return None