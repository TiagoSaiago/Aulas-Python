lista = [2, 3, 4, 5]
nova_lista = lista[:]

nova_lista[0] = 7

print(f"ésta é a lista principal: {lista}")
print(f"ésta é a lista secundaria: {nova_lista}")

for i, v in enumerate(lista):
    print(f"O index é {i} e o valor é {v}")

for cont in range(0, 5):
    num = int(input("Digite um número: "))
    lista.append(num)
    print(f"O número {num} foi adicionado com sucesso")

for valor in lista:
    print(valor, end=" ")

for valor in lista:
    print("\n", valor, end=" ")
