import random

par_certo = 0
impar_certo = 0

while par_certo == 0 or impar_certo == 0:
    print(" Par ou Impar? ")
    escolha = input().upper()
    escolhaCPU = random.randrange(11)

    if escolha == "IMPAR" and escolhaCPU == 1 or 3 or 5 or 7 or 9:
        impar_certo = 1
    elif escolha == "PAR" and escolhaCPU == 2 or 4 or 6 or 8 or 10:
        par_certo = 1

    if par_certo == impar_certo:
        print(f"Perdeste, disseste {escolha} e eu estava a pensar no numero {escolhaCPU}")
    if par_certo == 1:
        print(f"Ganhaste, disseste PAR, e eu estava a pensar no numero {escolhaCPU}")
    if impar_certo == 1:
        print(f"Ganhaste, disseste IMPAR, e eu estava a pensar no numero {escolhaCPU}")
