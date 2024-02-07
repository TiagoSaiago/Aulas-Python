# Atribuição de um numero só para que o While comece
numero = 99999999

# While com a condição que a variavel "numero" seja maior que 0
while numero > 0:
    # Input de dados pelo utilizador para que possamos mostrar a adequada tabuada
    numero = int(input("Insira o numero que deseja ver a tabuada: "))
    # condição caso o utilizador escolha o numero 0 ou menor que 0 para fechar o programa
    if numero <= 0:
        quit()
    # caso a condição anterior não seja ativada, mostra a tabuada
    else:
        for x in range(1, 10):
            print(f"{numero} * {x} = {numero * x}")
