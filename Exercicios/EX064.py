from time import sleep


# Funçoes
def mensagem_bem_vindo(msg):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(msg)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


def conversor(a):
    temp = a * 1.8 + 32
    print(f"Inseriu {a}º graus celcius o que equivale a {temp}º graus Fahrenheit!")


mensagem_bem_vindo("Bem vindo ao conversor de temperatura!")
sleep(1)
graus = float(input("Insira a a temperatura desejada: "))
sleep(1)
conversor(graus)
