import streamlit as st
from models import Epic, UserStory, INVESTValidation, Prioridade
from pdf_generator import PDFGenerator

st.title("📊 Fintech - Planejamento Ágil")

# =====================
# ÉPICO
# =====================
epic = Epic(
    "Controle de Gastos e Receitas",
    "Este épico é essencial para permitir que o usuário tenha uma visão completa de sua saúde financeira."
)

# =====================
# USER STORIES
# =====================
stories = [
    UserStory(
        "Como usuário do aplicativo, quero registrar meus gastos, para controlar melhor minhas despesas.",
        ["Dado que estou logado, quando registrar gasto, então ele deve ser salvo",
         "Deve permitir inserir valor e categoria"]
    ),
    UserStory(
        "Como usuário do aplicativo, quero registrar receitas, para acompanhar minha renda.",
        ["Permitir inserir valor",
         "Salvar no histórico"]
    ),
    UserStory(
        "Como usuário do aplicativo, quero visualizar meu saldo, para entender minha situação financeira.",
        ["Mostrar saldo atualizado",
         "Atualizar após cada transação"]
    ),
    UserStory(
        "Como pessoa que deseja organizar suas finanças, quero ver histórico, para analisar gastos.",
        ["Listar transações",
         "Permitir filtro por data"]
    ),
    UserStory(
        "Como usuário do aplicativo, quero categorizar gastos, para melhor análise.",
        ["Permitir criar categorias",
         "Associar categoria ao gasto"]
    ),
]

# =====================
# INVEST
# =====================
invest_list = [
    INVESTValidation(
        stories[0].descricao,
        {
            "I": "Independente pois pode ser desenvolvida separadamente",
            "N": "Pode ser ajustada conforme necessidade",
            "V": "Entrega valor direto ao usuário",
            "E": "Fácil de estimar esforço",
            "S": "Pequena e implementável rapidamente",
            "T": "Pode ser testada com inputs de gastos"
        }
    ),
    INVESTValidation(
        stories[2].descricao,
        {
            "I": "Não depende de outras histórias complexas",
            "N": "Pode mudar formato de exibição",
            "V": "Ajuda na tomada de decisão",
            "E": "Simples de estimar",
            "S": "Pequena",
            "T": "Testável com valores simulados"
        }
    )
]

# =====================
# PRIORIDADES
# =====================
prioridades = [
    Prioridade(stories[0].descricao, "Base do sistema"),
    Prioridade(stories[1].descricao, "Complementa o controle financeiro"),
    Prioridade(stories[2].descricao, "Mostra valor ao usuário"),
    Prioridade(stories[3].descricao, "Análise posterior"),
    Prioridade(stories[4].descricao, "Melhoria avançada")
]

# =====================
# INTERFACE
# =====================
st.header("📌 Épico")
st.write(epic.nome)
st.write(epic.justificativa)

st.header("📖 User Stories")
for s in stories:
    st.subheader(s.descricao)
    for c in s.criterios:
        st.write(f"- {c}")

st.header("✅ INVEST")
for inv in invest_list:
    st.subheader(inv.historia)
    for k, v in inv.validacoes.items():
        st.write(f"{k}: {v}")

st.header("📊 Prioridades")
for p in prioridades:
    st.subheader(p.historia)
    st.write(p.justificativa)

# =====================
# GERAR PDF
# =====================
if st.button("📄 Gerar PDF"):
    pdf = PDFGenerator("fintech_planejamento.pdf")
    pdf.gerar_pdf(epic, stories, invest_list, prioridades)
    st.success("PDF gerado com sucesso!")