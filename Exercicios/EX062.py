def calculo_de_media():
    a = input("Insira o seu nome: ")
    resposta = "S"
    b = []
    while resposta == "S":
        nota = int(input("Insira uma nota: "))
        if nota == "":
            nota = 0
        b.append(nota)
        resposta = input("Deseja continuar [S/N]? ").upper()
    media = sum(b) / len(b)
    print(f"Nome do Aluno: {a}")
    print(f"Média do Aluno: {media}")
    if media >= 9.5:
        print(f"Estado do Aluno: Aprovado")
    else:
        print(f"Estado do Aluno: Reprovado")


calculo_de_media()
