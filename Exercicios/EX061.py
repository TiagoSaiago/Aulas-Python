def maior(*num):
    resposta = "S"
    lista = []
    while resposta == "S":
        num = int(input("Digite um parametro inteiro: "))
        lista.append(num)
        resposta = input("Deseja continuar [S/N]? :").upper()
    print(f"O maior parametro inserido foi {max(lista)}")


maior()
