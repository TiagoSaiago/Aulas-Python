lista = list()

for c in range(0, 5):
    num = int(input("Digite um numero: "))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print("Numero adicionado com sucesso")
    else:
        indice = 0
        while indice < len(lista):
            if num <= lista[indice]:
                lista.insert(indice, num)
                break
            indice += 1

print(lista)
