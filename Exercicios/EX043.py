lista = []

for cont in range(0, 5):
    num = int(input("Digite um número: "))
    lista.append(num)
    print(f"O número {num} foi adicionado com sucesso")

lista_sorted = sorted(lista)

menor = min(lista_sorted)
maior = max(lista_sorted)

print(f"O maior valor foi {maior} e o seu index é {lista_sorted.index(maior)}")
print(f"O menor valor foi {menor} e o seu index é {lista_sorted.index(menor)}")
