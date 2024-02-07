# Criar conta bancaria
# Identidade, titular, saldo, limite
# levantar dinheiro, depositar dinheiro, extrato

def levantar_dinheiro(valor):
    if valor > conta["limite"]:
        print("O seu limite é 400")
    else:
        conta["saldo"] -= valor


def depositar_dinheiro(valor):
    conta["saldo"] += valor


def extrato():
    print(f"A conta {conta["identidade"]} tem o saldo de {conta["saldo"]}")


contas = list()

conta = {"identidade": "A275FGU",
         "titular": "Ricardo",
         "saldo": 1250.25,
         "limite": 400
         }
contas.append(conta)

print("Extrato")
extrato()
print("Deposito de 1000")
depositar_dinheiro(1000)
extrato()
levantar_dinheiro(1000)
