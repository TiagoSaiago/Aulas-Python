cliente = dict()

cliente["Nome"] = input("Digite o seu Nome: ")
cliente["Ano"] = int(input("Ano de nascimento: "))
cliente["Rendimentos Mensais"] = int(input("Digite os seu rendimentos mensais: "))
cliente["Despesas Mensais"] = int(input("Digite as suas despesas mensais: "))
cliente["Montante de Crédito"] = int(input("Digite o seu montante do crédito: "))
cliente["Prazo em Anos"] = int(input("Deseja pagar em quantos anos? :"))

cliente["Idade"] = (2023 - cliente["Ano"])
cliente["Após Despesas"] = (cliente["Rendimentos Mensais"] - cliente["Despesas Mensais"])

cliente["Valor Mensal"] = (cliente["Montante de Crédito"] / cliente["Prazo em Anos"])
if cliente["Após Despesas"] > cliente["Valor Mensal"]:
    print("Crédito Aprovado")
else:
    print("Nope")
