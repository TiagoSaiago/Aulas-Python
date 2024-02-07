# Imports

# Funções
def boas_vindas(msg):
    print("-=-=-=-=-=-=-=-=-=-=-=-=")
    print(msg)
    print("-=-=-=-=-=-=-=-=-=-=-=-=")


def area(a, b):
    c = a * b / 2
    print(f"A area do terreno é igual a {c}")


# Código Principal

boas_vindas("Bem Vindo")
a = int(input("Digite uma das dimensões: "))
b = int(input("Digite a outra dimensão: "))

area(a, b)
