resposta = "S"
lista = []

while resposta == "S":
    num = int(input("Adicione um numero: "))
    if num in lista:
        print("Esse numero já está na lista")
    else:
        lista.append(num)
        print("Valor adicionado com sucesso")
        lista.sort()
    resposta = input("Deseja continuar [S/N]?: ").upper()

print(lista[::-1])
