pares = []
impares = []

for x in range(0, 10):
    num = int(input("Digite um numero: "))
    if (num % 2) == 0:
        pares.append(num)
    else:
        impares.append(num)

lista = list()

lista.append(pares[:])

lista.append(impares[:])

print(lista)
