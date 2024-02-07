import math


def fatorial(a, b=1):
    c = a
    f = 1
    resposta = input("Pretende mostrar o calculo? [S/N]: ").upper()
    if resposta == "S":
        while c > 0:
            print(f"{c}", end="")
            print(" x " if c > 1 else " = ", end="")
            f *= c
            c -= 1
        print(f"{f}")
    else:
        print(math.factorial(num))


print("Insira um numero para calculamos o seu fatorial ")
num = int(input())
fatorial(num)
