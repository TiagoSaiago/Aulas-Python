lista_total = []
lista_pares = []
lista_impares = []

for x in range(0, 5):
    num = int(input("Digite um numero: "))
    lista_total.append(num)
    if (num % 2) == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print(lista_total)
print(lista_pares)
print(lista_impares)
