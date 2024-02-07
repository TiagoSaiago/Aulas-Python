class ContaBancaria:
    def __init__(self, nib=None, titular=None, saldo=None, limite=None):
        print("Nova conta adicionada com sucesso")
        self.__nib = nib
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def set_nib(self, nib):
        self.__nib = nib

    def set_titular(self, titular):
        self.__titular = titular

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def set_limite(self, limite):
        self.__limite = limite


conta = ContaBancaria()

titular = input("Qual o seu nome? ")
conta.set_titular(titular)
print()

nib = int(input("Qual o seu nib? "))
conta.set_nib(nib)
print()

limite = int(input("Qual o limite diario? "))
conta.set_limite(limite)
print()

saldo = float(input("Quanto saldo possui na conta? "))
conta.set_saldo(saldo)

print(f"\nInformações da conta:")
print(f"NIB: {}")
print(f"Titular: {conta.set_titular()}")
print(f"Saldo: {conta.set_saldo()}")
print(f"Limite: {conta.set_limite()}")
