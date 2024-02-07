from time import sleep


class Circulo:
    def __init__(self, raio):
        self.__raio = raio
        self.__pi = 3.14159265359

    def get_raio(self):
        print(f"O raio do Circulo é {self.__raio}")

    def set_raio(self, raio):
        print(f"O raio do Circulo foi modificado para {raio}")
        self.__raio = raio

    def calcular_area(self):
        print(f"A area do atributo é: {self.__raio * self.__pi ** 2}")

    def calcular_perimetro(self):
        print(f"O perimetro do curculo é: {2 * self.__pi * self.__raio}")


print("==========")
print("Bem Vindo")
print("==========")
sleep(0.5)
circulo1 = Circulo(raio=float(input("Qual é o raio do Circulo?: ")))
sleep(0.5)
while True:
    print("[ 1 ] - Mostrar Raio")
    print("[ 2 ] - Modificar Raio")
    print("[ 3 ] - Calcular Area")
    print("[ 4 ] - Calcular Perimetro")
    print("[ 0 ] - Sair")
    sleep(1)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        sleep(0.5)
        Circulo.get_raio(circulo1)

    elif opcao == "2":
        sleep(0.5)
        Circulo.set_raio(circulo1, raio=float(input("Quao raio deseja?")))

    elif opcao == "3":
        sleep(0.5)
        Circulo.calcular_area(circulo1)

    elif opcao == "4":
        sleep(0.5)
        Circulo.calcular_perimetro(circulo1)

    elif opcao == "0":
        sleep(0.5)
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
