# for loop para dar começo ao programa onde possamos guardar as variaveis para no futuro sejam contadas
for x in range(1, 9999):
    total = 0
    opcao = ""
    parar = "S"
    # outro loop dentro do loop para que possamos adicionar ao total e continuar a contar o numero de "tentativas"
    for contagem in range(1, 9999):
        print("Digite um numero inteiro")
        opcao = int(input())
        total = total + opcao
        print("Deseja Continuar?")
        print("Digite S para continuar o programa ou N para parar")
        parar = input().upper()
        # condição onde se o utilizador escrever "N"
        if parar == "N":
            break
    # Após o utilizador parar mostra o numero de tentativas e o total de cada numero introduzido
    print(f"Insiriste {contagem} numeros!")
    print(f"a soma entre eles é : {total}")
    quit()
