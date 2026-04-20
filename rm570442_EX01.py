# Lista de dias válidos
dias_validos = [
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira"
]

# Dicionário para contar votos
votos = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0
}

# Entrada do número de colaboradores
num_colaboradores = int(input("Informe o número de colaboradores: "))

# Coleta de votos
for i in range(num_colaboradores):
    while True:
        dia = input("Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").lower()
        
        if dia in dias_validos:
            votos[dia] += 1
            break
        else:
            print("Dia inválido! Tente novamente.")

# Descobrir o(s) dia(s) mais votado(s)
maior_voto = max(votos.values())
dias_mais_votados = [dia for dia, qtd in votos.items() if qtd == maior_voto]

# Verificação de empate
if len(dias_mais_votados) == 1:
    print(f"O dia escolhido pelos colaboradores é: {dias_mais_votados[0]}")
else:
    print("Houve empate entre os dias:")
    for dia in dias_mais_votados:
        print(dia)