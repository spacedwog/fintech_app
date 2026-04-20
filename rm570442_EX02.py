# Entrada
preco = float(input("Digite o preço do carro: "))

# Preço à vista com 20% de desconto
preco_vista = preco * 0.8
print(f"O preço final à vista com desconto 20% é: {preco_vista}")

# Dados de parcelas e acréscimos
parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
acrescimos = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# Loop para gerar a tabela
for i in range(len(parcelas)):
    qtd = parcelas[i]
    percentual = acrescimos[i] / 100
    
    preco_final = preco * (1 + percentual)
    valor_parcela = preco_final / qtd

    # Formatação no padrão brasileiro
    preco_formatado = f"{preco_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    parcela_formatada = f"{valor_parcela:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    print(f"O preço final parcelado em {qtd} x é de R$ {preco_formatado} com parcelas de R$ {parcela_formatada}")