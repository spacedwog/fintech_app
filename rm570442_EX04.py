# Menu de opções
print("Escolha o tipo de investimento:")
print("1. CDB")
print("2. LCI")
print("3. LCA")

# Entrada com validação
while True:
    tipo = int(input("Digite o tipo de investimento (1,2 ou 3): "))
    if tipo in [1, 2, 3]:
        break
    else:
        print("Opção inválida! Tente novamente.")

# Entrada dos demais dados
valor = float(input("Digite o valor a ser resgatado: "))
dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

# Verificação do tipo de investimento
if tipo == 1:  # CDB (tem IR)
    
    # Definição da alíquota conforme os dias
    if dias <= 180:
        aliquota = 0.225
    elif dias <= 360:
        aliquota = 0.20
    elif dias <= 720:
        aliquota = 0.175
    else:
        aliquota = 0.15

    imposto = valor * aliquota

else:  # LCI ou LCA (isentos)
    imposto = 0.0

# Formatação no padrão brasileiro
imposto_fmt = f"{imposto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Saída
print(f"O valor do imposto de renda a ser pago é: R${imposto_fmt}")