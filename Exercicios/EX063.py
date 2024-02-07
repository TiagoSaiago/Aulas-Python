from time import sleep


def tabuada(num):
    for x in range(0, 10):
        print(num, " x ", x + 1, " = ", num * (x + 1))
        sleep(0.5)


num = int(input("Insira o Numero que deseja ver a tabuada: "))
tabuada(num)
