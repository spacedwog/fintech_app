# Entrada do valor da dívida
divida = float(input("Digite o valor da dívida: "))

# Dados de parcelas e juros (%)
parcelas = [1, 3, 6, 9, 12]
juros_percentuais = [0, 10, 15, 20, 25]

# Loop para calcular e exibir a tabela
for i in range(len(parcelas)):
    qtd = parcelas[i]
    juros_percentual = juros_percentuais[i] / 100

    valor_juros = divida * juros_percentual
    total = divida + valor_juros
    valor_parcela = total / qtd

    # Formatação padrão brasileiro
    total_fmt = f"{total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    juros_fmt = f"{valor_juros:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    parcela_fmt = f"{valor_parcela:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    print(f"Total: R$ {total_fmt} Juros: {juros_fmt} Número de parcelas {qtd}, Valor da Parcela:R${parcela_fmt}")