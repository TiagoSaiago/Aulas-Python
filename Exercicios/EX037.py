continuar = "S"
menor_idadeH = 0
maior_25 = 0
mulheres = 0
menor_idade = 0

while continuar == "S":
    idade_pergunta = int(input("Qual a sua idade?: "))
    sexo_pergunta = input("Qual seu genero? [M] / [F]: ").upper()
    if sexo_pergunta == "F":
        mulheres = mulheres + 1
    if idade_pergunta >= 25:
        maior_25 = maior_25 + 1
    if idade_pergunta < 18 and sexo_pergunta == "H":
        menor_idadeH = menor_idadeH + 1
    if idade_pergunta < 18:
        menor_idade = menor_idadeH + 1

    print("Deseja Continuar?")
    continuar = input("[S] Para continuar / [N] Para Parar").upper()
print(f"Foram registados {maior_25} pessoas com mais de 25 anos.")
print(f"Foram registados {menor_idadeH} Homens com menos de 17 anos.")
print(f"Foram registadas {mulheres} mulheres.")
print(f"Foram registados {menor_idade} menores de idade.")
