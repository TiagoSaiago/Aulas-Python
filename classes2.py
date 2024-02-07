'''class ContaBancaria:
    def __init__(self, titular, saldo):
        print("Nova conta criada com sucesso...")
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        self.__saldo += valor


conta = ContaBancaria("Tiago", 1200)

print(conta.get_saldo())

nome = "Ricardo"
print(nome)


def set_nome(novo_nome):
    nome = novo_nome
'''


class Conta:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.__saldo = saldo
        self.limite = limite

    @property
    def saldo(self):
        return f"O saldo de conta é: {self.__saldo}€"

    @saldo.setter
    def saldo(self, valor):
        if valor > 1000:
            print(f"O valor {valor}€ é superior ao limite permitido")
        else:
            self.__saldo = valor


conta1 = Conta("Tiago", 1250, 500)

print(conta1.saldo)

conta1.saldo = 999

print(conta1.saldo)
