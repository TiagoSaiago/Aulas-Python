# Loop que repete 7 vezes pedindo uma idade de cada vez e dizendo se é maior de idade ou não.
for x in range(0, 7):
    anoNasc = int(input("introduza o ano nascimento: "))
    if anoNasc < 2005:
        print("é maior de idade")
    # Se for 2005 pergunta se a pessoa já vez anos para poder verificar se é maior de idade ou não
    elif anoNasc == 2005:
        fezanos = input("Já fez anos? sim/não: ")
        if fezanos == "sim":
            print("é maior de idade")
        else:
            print("é menor de idade")
    else:
        print("é menor de idade")
