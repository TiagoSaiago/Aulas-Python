# Imports


# Definir Funçoes
def insere_linha():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


def cabeçalho(msg):
    insere_linha()
    print(msg)
    insere_linha()


def soma(a, b):
    s = a + b
    print(f"A soma entre {a} e {b} é igual a {s}")


def conta_numeros(*num):
    print(f"inseriu {len(num)} numeros")
    for numeros in num:
        print(f"{numeros}", end=" ")
        print()


# Programa Principal

insere_linha()
print("Olá Mundo")
insere_linha()

cabeçalho("Buenas")

print("Função Soma")
soma(4, 4)

soma(55, 54)

soma(45, 76)
print()

print("Função Desempacotar")

conta_numeros(55, 2, 3, 65)

conta_numeros(1, 2, 3)

conta_numeros(2, 5, 6, 8, 9)
