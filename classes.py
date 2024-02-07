'''class Jogo:
    def __init__(self, titulo, consola, preco):
        self.titulo = titulo
        self.consola = consola
        self.preco = preco


jogo = Jogo("Palworld", "PC", 29.90)

print(jogo.titulo)
print(jogo.consola)
print(jogo.preco)
'''


class Conta:
    def __int__(self, identidade, titular, saldo, limite):
        self.identidade = identidade
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def levantar(self, valor):
        if valor > self.limite:
            print("O seu limite é de 400€ diarios.")
        else:
            if self.saldo > valor:
                self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def extrato(self):
        print(f"A conta {self.identidade} tem {self.saldo}€ disponiveis")
    
