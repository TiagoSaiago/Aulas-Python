series = {"titulo": "Game Of Thrones", "temp": 8}

print(series["titulo"])

series["rate"] = 9.6

print(series.values())
print(series.keys())
print(series.items())

for k, v in series.items():
    print(f"A chave {k} tem {v}")

'''aluno = {"Nome": "César", "Média": 14}

print(aluno["Nome"])

print(f"O aluno {aluno["Nome"]} tem a média de {aluno["Média"]} valores")

print(f" O aluno {aluno['Nome']} tem a média de {aluno['Média']} valores")

if aluno["Média"] >= 9.5:
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situação"] = "Reprovado"

print(aluno)
'''

'''aluno = dict()

aluno["Nome"] = input("Digite o nome do aluno: ")
aluno["EX001"] = int(input("Digite a nta do ex001: "))
aluno["EX002"] = int(input("Digite a nta do ex002: "))
aluno["EX003"] = int(input("Digite a nta do ex003: "))

aluno["Média"] = (aluno["EX001"] + aluno["EX002"] + aluno["EX003"]) / 3

print(aluno.items())

del aluno["Média"]

print(aluno.items())
'''

cidade = {"Nome": "Porto", "Código": "OPO", "Baixa": "Ribeira", "Rio": "Douro"}
cidade2 = {"Nome": "Lisboa", "Código": "LX", "Baixa": "Chiado", "Rio": "Tejo"}

pais = list()

pais.append(cidade)
pais.append(cidade2)

print(pais)

for elemento in cidade.items():
    print(elemento)

for k, v in cidade.items():
    print(f"O {k} é {v}")

for c in range(0, len(pais)):
    print(f"Cidade {pais[c]["Nome"]} --> Registada")
