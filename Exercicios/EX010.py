# Introdução de dados pelo Utilizador
numero = int(input("Insira um numero de 0 a 9999: "))

# Tratrar os Dados

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

# Mostrar o Numero inserido pelo Utilizador
print(f"O seu numero é {numero}")
# Mostrar o Index 3
print(f"Unidade: {unidade}")
# Mostrar o Index 2
print(f"Dezena:{dezena}")
# Mostrar o Index 1
print(f"Centena: {centena}")
# Mostrar o Index 0
print(f"Milhar: {milhar}")
