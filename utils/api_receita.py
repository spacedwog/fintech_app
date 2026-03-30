import requests

def validar_cpf(cpf):
    url = f"https://www.receitaws.com.br/v1/cpf/{cpf}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get("nome")
    return None