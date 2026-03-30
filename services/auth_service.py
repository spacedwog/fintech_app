# ===============================
# services/auth_service.py
# ===============================

import requests
import os
from database import get_connection


class AuthService:
    """
    Serviço de autenticação baseado em CPF
    Integração com API externa + fallback local
    """

    # 🔐 Use variável de ambiente para segurança
    API_KEY = os.getenv("CPF_API_KEY", "SUA_API_KEY_AQUI")

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """
        Validação básica de CPF (formato + dígitos verificadores)
        """
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        # Validação do primeiro dígito
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        dig1 = (soma * 10 % 11) % 10

        # Validação do segundo dígito
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        dig2 = (soma * 10 % 11) % 10

        return cpf[-2:] == f"{dig1}{dig2}"

    @staticmethod
    def buscar_cpf_api(cpf: str) -> dict:
        """
        Consulta API externa de CPF
        """
        url = f"https://api.cpf-brasil.org/cpf/{cpf}"
        headers = {
            "X-API-Key": AuthService.API_KEY,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code == 200:
            return response.json()

        raise Exception(f"Erro API: {response.status_code}")

    @staticmethod
    def salvar_usuario(cpf: str, name: str):
        """
        Salva usuário no banco local
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE cpf=?", (cpf,))
        user = cursor.fetchone()

        if not user:
            cursor.execute(
                "INSERT INTO users (cpf, name) VALUES (?, ?)",
                (cpf, name)
            )
            conn.commit()

        conn.close()

    @staticmethod
    def login(cpf: str) -> str:
        """
        Fluxo completo de login
        """

        cpf = ''.join(filter(str.isdigit, cpf))

        # 1️⃣ Validar CPF
        if not AuthService.validar_cpf(cpf):
            raise ValueError("CPF inválido")

        try:
            # 2️⃣ Buscar na API real
            data = AuthService.buscar_cpf_api(cpf)

            # ajuste conforme resposta real da API
            name = data.get("nome") or data.get("name") or "Usuário"

        except Exception:
            # 3️⃣ Fallback (API indisponível)
            name = f"Usuário {cpf[-4:]}"

        # 4️⃣ Persistência local
        AuthService.salvar_usuario(cpf, name)

        return name