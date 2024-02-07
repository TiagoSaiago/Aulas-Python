class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def descrever(self):
        print(f"O produto {self.nome} tem como quantidade {self.quantidade}")

    def aumentar(self):
        valor = int(input("Deseja aumentar a quantidade por quanto?"))
        self.quantidade += valor


produto1 = Produto("Brinquedos", 5)
produto2 = Produto("Jogos", 6)

print(Produto.descrever(produto1))

Produto.aumentar(produto1)

print(Produto.descrever(produto1))
