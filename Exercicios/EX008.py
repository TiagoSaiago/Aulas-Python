# Introdução dos dados pelo utilizador
km_percorrido = float(input("Introduza a quantidade de KM percorrido: "))
dias_alugado = int(input("Introduza quantos dias alugou: "))
# variaveis de calculo
custo_km = 0.456
custo_dia = 60
# Calculo do total a pagar
total = dias_alugado * custo_dia + km_percorrido * custo_km

# Apresentação de dados
print(f"O seu total a pagar é: {total}€")
