import math

'''# Maneira Facil
print("Insira um numero para calculamos o seu fatorial ")
numero = int(input())
print(math.factorial(numero))
'''
# Maneira Bonita

num = int(input("Digite um numero para ver o seu factorial: "))

# Iniciar contador

c = num

# iniciar o factorial . tem de iniciar em 1 porque multiplicar por zero da zero e por um dá o mesmo

f = 1

# calcular o factorial

while c > 0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f"{f}")
