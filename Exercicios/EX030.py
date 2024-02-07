print("Bem vindo a calculadora! :D ")
print("Insira 3 numeros : ")
valor1 = int(input(" "))
valor2 = int(input(" "))
valor3 = int(input(" "))

soma = valor1 + valor2 + valor3
multi = valor1 * valor2 * valor3
maior = max(valor1, valor2, valor3)
resposta = 3
while resposta != 5:
    print("=====================")
    print("Insira o numero indicado para o calculo que deseja!")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos Numeros")
    print("[5] Sair")
    print("=====================")

    resposta = int(input(":"))

    if resposta == 1:
        print(f"{valor1} + {valor2} + {valor3} = {soma}")
    if resposta == 2:
        print(f"{valor1} x {valor2} x {valor3} = {multi}")
    if resposta == 3:
        print(f"O maior numero é o numero {maior}")
    if resposta == 4:
        print("Insira 3 numeros : ")
        valor1 = int(input(" "))
        valor2 = int(input(" "))
        valor3 = int(input(" "))
        soma = valor1 + valor2 + valor3
        multi = valor1 * valor2 * valor3
        maior = max(valor1, valor2, valor3)

'''
# Solução do stor


'''
