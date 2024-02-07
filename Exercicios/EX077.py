from time import sleep


class Conta_bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        valor = int(input("Deseja depositar quanto? "))
        if valor >= 400:
            print("O limite diario é 400 ")
        else:
            self.saldo += valor
            print(f"O valor {valor}€ foi depositado com sucesso na sua conta, o seu montante é {self.saldo}€")

    def sacar(self):
        valor = int(input("Deseja levantar quanto? "))
        self.saldo -= valor
        print(f"O valor {valor}€ foi levantado da sua conta com sucesso, o seu montante é {self.saldo}€")

    def mostrar_montante(self):
        print(f"O seu montante atual é de {self.saldo}€")


print("==========")
print("Bem Vindo")
print("==========")
sleep(0.5)
conta1 = Conta_bancaria(titular=input("Qual o nome do titular da conta?: "),
                        saldo=int(input("Quanto saldo tem na conta?: ")))
sleep(0.5)
while True:
    print("[ 1 ] - Depositar Dinheiro")
    print("[ 2 ] - Levantar Dinheiro")
    print("[ 3 ] - Mostrar Montante")
    print("[ 0 ] - Sair")
    sleep(1)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        sleep(0.5)
        Conta_bancaria.depositar(conta1)

    elif opcao == "2":
        sleep(0.5)
        Conta_bancaria.sacar(conta1)

    elif opcao == "3":
        sleep(0.5)
        Conta_bancaria.mostrar_montante(conta1)

    elif opcao == "0":
        sleep(0.5)
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
