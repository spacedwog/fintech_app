import streamlit as st
from database.db import Database
from services.expense_service import ExpenseService
from services.alert_service import AlertService
from utils.api_receita import validar_cpf
from datetime import date

db = Database()
expense_service = ExpenseService(db)
alert_service = AlertService()

st.set_page_config(page_title="Fintech Inteligente", layout="wide")

st.title("💰 Controle Inteligente de Gastos")

# LOGIN
st.sidebar.header("Login")
cpf = st.sidebar.text_input("CPF")

if st.sidebar.button("Entrar"):
    nome = validar_cpf(cpf)
    if nome:
        st.session_state["user"] = {"cpf": cpf, "nome": nome}
        st.success(f"Bem-vindo {nome}")
    else:
        st.error("CPF inválido")

if "user" in st.session_state:

    user = st.session_state["user"]

    st.sidebar.success(f"Logado: {user['nome']}")

    menu = st.sidebar.selectbox("Menu", [
        "Registrar Despesa",
        "Visualizar Gastos",
        "Resumo Mensal",
        "Definir Orçamento"
    ])

    # US1 - Registrar despesa
    if menu == "Registrar Despesa":
        st.header("Nova Despesa")

        valor = st.number_input("Valor", min_value=0.0)
        categoria = st.selectbox("Categoria", ["Alimentação", "Transporte", "Moradia", "Lazer"])
        data = st.date_input("Data", value=date.today())

        if st.button("Salvar"):
            expense_service.add_expense(1, 1, valor, data)
            st.success("Despesa registrada!")

    # US3 - Visualizar gastos
    elif menu == "Visualizar Gastos":
        st.header("Gastos por Período")

        inicio = st.date_input("Início")
        fim = st.date_input("Fim")

        if st.button("Buscar"):
            dados = expense_service.get_expenses_by_period(1, inicio, fim)

            if dados:
                total = sum([d[3] for d in dados])
                st.write("Total gasto:", total)
                st.dataframe(dados)
            else:
                st.info("Nenhum dado encontrado")

    # US5 - Resumo mensal
    elif menu == "Resumo Mensal":
        st.header("Resumo")

        dados = expense_service.get_expenses_by_period(1, "2026-03-01", "2026-03-30")

        total = sum([d[3] for d in dados])

        st.metric("Total gasto", total)

    # US4 - Orçamento
    elif menu == "Definir Orçamento":
        st.header("Orçamento")

        limite = st.number_input("Limite mensal")

        if st.button("Salvar limite"):
            st.session_state["limite"] = limite

        if "limite" in st.session_state:
            dados = expense_service.get_expenses_by_period(1, "2026-03-01", "2026-03-30")
            total = sum([d[3] for d in dados])

            alerta = alert_service.check_budget(total, st.session_state["limite"])

            if alerta:
                st.warning(alerta)