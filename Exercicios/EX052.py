aluno = dict()

resposta = "S"

while resposta == "S":
    aluno["Nome"] = input("Insira o Nome do Aluno: ")
    aluno["Média"] = int(input("Insira a média: "))

    print("Situação:")
    if aluno["Média"] <= 9.5:
        print(f"O aluno {aluno["Nome"]} com a Média de {aluno["Média"]} encontra-se Reprovado")
    else:
        print(f"O aluno {aluno["Nome"]} com a Média de {aluno["Média"]} encontra-se Aprovado")

    resposta = input("Deseja continuar= [S/N]?: ").upper()
