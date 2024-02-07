# Introdução de dados pela parte do utiizador
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))

# Comparação dos dados
if numero1 > numero2:
    print(f"O {numero1} é maior que {numero2}")
elif numero2 > numero1:
    print(f"O {numero2} é maior que {numero1}")
elif numero1 == numero2:
    print(f"O {numero1} é igual a {numero2}")
