# ===============================

create_tables()

st.set_page_config(page_title="Fintech Inteligente", layout="wide")

st.title("💰 Fintech - Controle Inteligente")

# Login
cpf = st.text_input("Digite seu CPF:")

if st.button("Login"):
    name = AuthService.login(cpf)
    if name:
        st.session_state["user"] = name
        st.success(f"Bem-vindo {name}")
    else:
        st.error("Erro na API")

if "user" in st.session_state:
    st.sidebar.title("Menu")
    menu = st.sidebar.selectbox("Opções", [
        "Registrar Despesa",
        "Resumo Mensal",
        "Alertas"
    ])

    # US1 + US2
    if menu == "Registrar Despesa":
        st.subheader("Nova Despesa")

        amount = st.number_input("Valor")
        date = st.date_input("Data")
        description = st.text_input("Descrição")

        if st.button("Salvar"):
            ExpenseService.add_expense(1, 1, amount, str(date), description)
            st.success("Despesa registrada!")

    # US3 + US5
    elif menu == "Resumo Mensal":
        st.subheader("Resumo")
        data = ReportService.monthly_summary(1)

        st.bar_chart({m: v for m, v in data})

    # US4
    elif menu == "Alertas":
        if Alerts.check_budget(1):
            st.warning("⚠️ Você ultrapassou o orçamento!")
        else:
            st.success("Tudo sob controle!")