from time import sleep

from time import sleep

from time import sleep


def contador(inicio, fim, passo):
    inicio = int(inicio)
    passo = int(passo)
    fim = int(fim)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f"Contando de {inicio} até {fim} de {passo} em {passo}")
    sleep(1)
    cont = int(inicio)
    if inicio < fim:
        while cont <= fim:
            print(f"{cont}", end=" ", flush=True)
            cont += passo
        print("Fim")
    elif inicio > fim:
        while cont >= fim:
            print(f"{cont}", end=" ", flush=True)
            cont -= passo
        print("Fim")
    else:
        print(f"{cont}")


contador(1, 20, 2)
contador(10, 0, 1)
print()
print("-" * 23)
print("Chegou a hora de personalizar a contagem!")
i = input("Inicio: ")
f = input("Fim: ")
p = int(input("Passo: "))
contador(i, f, p)
