from time import sleep

while True:
    sleep(1)
    print("-----------------------------")
    print("----- MENU DE EXECICIOS -----")
    print("-----------------------------")
    print("\n")
    print("Digite o numero do Exercicio que deseja ver")
    print()
    print("Escreva 'lista' ou 'l' para ver a lista de exercicios")
    print()
    opcao = input()

    if opcao == "lista" or opcao == "l":
        print("1 - 1-10")
        print("2 - 11-20")
        print("3 - 21-30")
        print("4 - 31-40")
        print("5 - 41-50")

    if opcao == "1":
        ola_mundo = "Olá Mundo"
        print(ola_mundo)

        print("\b")
    if opcao == "2":
        print("--------------------------")
        print("------ Bem vindo :) ------")
        print("--------------------------")

        print("\b")

    if opcao == "3":
        first_number = int(input("Input your first number: "))
        second_number = int(input("Input your second number: "))
        resultado = first_number + second_number

        print(f"{first_number} + {second_number} = {resultado}")

        print("\b")

    if opcao == "4":
        number = int(input('input your number: '))
        number_minus = number - 1
        number_plus = number + 1

        print(f'The number before {number} is {number_minus} and the number after {number} is {number_plus}')

    if opcao == "5":
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))

        plus = a + b
        minus = a - b
        multi = a * b
        divide = a / b
        resto = a % b

        print(f"{a} + {b} = {plus}")
        print(f"{a} - {b} = {minus}")
        print(f"{a} * {b} = {multi}")
        print(f"{a} / {b} = {divide}")
        print(f"{a} % {b} = {resto}")

    if opcao == "6":
        # Introdução dos dados pelo lado do utilizador
        num1 = float(input("Introduza a sua primeira nota: "))
        num2 = float(input("Introduza a sua segunda nota: "))
        num3 = float(input("Introduza a sua terceira nota: "))
        num4 = float(input("Introduza a sua quarta nota: "))
        num5 = float(input("Introduza a sua quinta nota: "))

        # Soma dos 5 valores introduzidos
        total_nums = num1 + num2 + num3 + num4 + num5

        # Media aritmetica
        media_aritmetica = total_nums / 5

        # Exibir media no ecra
        print(f"A tua média aritmética é: {media_aritmetica}")

    if opcao == "7":
        # pedir ano nascimento
        ano_utilizador = int(input("Introduza o seu ano de nascimento: "))
        ano_atual = int(input("Introduza o ano atual: "))
        idade = ano_atual - ano_utilizador

        # Exibir idade no ecra
        print(f"A tua idade é {idade}")

    if opcao == "8":
        # Introdução dos dados pelo utilizador
        km_percorrido = float(input("Introduza a quantidade de KM percorrido: "))
        dias_alugado = int(input("Introduza quantos dias alugou: "))
        # variaveis de calculo
        custo_km = 0.456
        custo_dia = 60
        # Calculo do total a pagar
        total = dias_alugado * custo_dia + km_percorrido * custo_km

        # Apresentação de dados
        print(f"O seu total a pagar é: {total}€")

    if opcao == "9":
        # Introdução de dados pela parte do utilizador
        nome = input("Digite o seu nome completo: ")

        # Trocar " " por ""
        nome_sem_espaco = nome.replace(" ", "")

        # Separar o nome em frases
        nome_separado = nome.split()

        # Contar a primeira frase
        nome_primeiro_tamanho = len(nome_separado[0])

        # Print o nome em letras maiusculas
        print(f"o seu nome em maiusculas é {nome.upper()}")
        print("==========================================")
        # Print o nome em letras minusculas
        print(f"o seu nome em minusculas é {nome.lower()}")
        print("==========================================")
        # Print o nome sem espaços
        print(f"o seu nome sem espaços é : {nome_sem_espaco}")
        print("==========================================")
        # Print o numero de carateres sem sepaços
        print(f"O seu nome sem espaços tem {len(nome_sem_espaco)} carateres")
        print("==========================================")
        # Print o numero de carateres do primeiro nome
        print(f"o seu primeiro nome é {nome_separado[0]} e tem {nome_primeiro_tamanho} carateres")
        print("==========================================")

    if opcao == "10":
        # Introdução de dados pelo Utilizador
        numero = int(input("Insira um numero de 0 a 9999: "))

        # Tratrar os Dados

        unidade = numero // 1 % 10
        dezena = numero // 10 % 10
        centena = numero // 100 % 10
        milhar = numero // 1000 % 10

        # Mostrar o Numero inserido pelo Utilizador
        print(f"O seu numero é {numero}")
        # Mostrar o Index 3
        print(f"Unidade: {unidade}")
        # Mostrar o Index 2
        print(f"Dezena:{dezena}")
        # Mostrar o Index 1
        print(f"Centena: {centena}")
        # Mostrar o Index 0
        print(f"Milhar: {milhar}")

    if opcao == "11":
        # Introdução de dados pelo utilizador
        frase = input("Introduza uma frase: ")
        # Formatação da frase para maiusculo para facilidade
        frase_maiuscula = frase.upper()
        letra_a = frase_maiuscula.count("A")
        posicao_primeira_a = frase_maiuscula.find("A")
        posicao_ultima_a = frase_maiuscula.rfind("A")

        print(f"A sua frase contem a letra A {letra_a} vezes")
        print(f"aparece pela primeira vez em {posicao_primeira_a + 1}")
        print(f"Aparece pela ultima vez em {posicao_ultima_a + 1}")

    if opcao == "12":
        # Introdução de dados
        nome = input("Insira o seu Primeiro e Ultimo Nome: ")
        # Manipulação do 'string'
        nome_separado = nome.split()
        primeiro_nome = nome_separado[0]
        ultimo_nome = nome_separado[-1]
        primeira_letra = primeiro_nome[0]
        nome_Capitalizado = primeiro_nome + ultimo_nome.capitalize()

        # Mostrar ao utilizador
        print(f"Olá {primeiro_nome}, o seu registo está completo.")
        print(f"O seu email é {primeira_letra.lower()}.{ultimo_nome.lower()}.edu@empresa.pt ")

    if opcao == "13":
        # Introdução de Dados
        palavra = input('Escreva uma palavra com 6 Letras: ')

        # Print da Palavra ao contrario
        print(palavra[::-1])

    if opcao == "14":
        velocidade = int(input("Introduza a sua velocidade: "))
        multa = (velocidade - 80) * 7 + 100

        if velocidade > 80:
            print(f"Multado: {multa}€ ")
        else:
            print("Não Multado")

    if opcao == "15":
        numero = int(input("Digite um numero: "))
        if numero % 2:
            print(f"O numero {numero} é Impar")
        else:
            print(f"O numero {numero} é Par")

    if opcao == "16":
        NotaMatematica = float(input("Digite a Sua nota a Matematica: "))

        NotaIngles = float(input("Digite a Sua nota a Ingles: "))

        NotaPortugues = float(input("Digite a Sua nota a Portuges: "))

        NotaHistoria = float(input("Digite a Sua nota a História: "))

        NotaFrances = float(input("Digite a Sua nota a Frances: "))

        media = (NotaFrances + NotaHistoria + NotaPortugues + NotaMatematica + NotaIngles) / 5

        print(f"Matematica: {NotaMatematica}")
        print(f"Ingles: {NotaIngles}")
        print(f"Portugues: {NotaPortugues}")
        print(f"História: {NotaHistoria}")
        print(f"Frances: {NotaFrances}")
        print("============================================")
        if media >= 9.5:
            print(f"Parabens! Passaste a tua média é {media}")
        elif media < 8:
            print(f"A tua media é {media} infelizmente reprovaste, boa sorte para o ano!")
        else:
            print(f"A sua média é {media}, está em recuperação")

    if opcao == "17":
        # Introdução de Dados pelo Utilizador
        numero = int(input("Escolha um numero: "))

        # Informação ao Utilizador do programa
        print("Deseja converter para que tipo? ")
        print("Escolha 1 para Binario")
        print("Escolha 2 para Octal")
        print("Escolha 3 para Hexadecimal")

        # Escolha pela parte do utilizador
        escolha = int(input(("Qual é a sua opção? :")))

        # Retorno da coversão
        if escolha == 1:
            print(f"O seu numero em binario é {bin(numero)[2:]}")
        elif escolha == 2:
            print(f"O seu numero em Octal é {oct(numero)[2:]}")
        elif escolha == 3:
            print(f"O seu numero em Hexadecimal é {hex(numero)[2:]}")
        else:
            print("Olha ai o autismo, escolhe uma das opções")

    if opcao == "18":
        # Introdução de dados pela parte do utiizador
        numero1 = int(input("Digite um numero: "))
        numero2 = int(input("Digite outro numero: "))

        # Comparação dos dados
        if numero1 > numero2:
            print(f"O {numero1} é maior que {numero2}")
        elif numero2 > numero1:
            print(f"O {numero2} é maior que {numero1}")
        elif numero1 == numero2:
            print(f"O {numero1} é igual a {numero2}")

    if opcao == "19":
        import random
        import time

        # Variavel que guarda um número random de 0 a 7
        numeros = random.randint(0, 7)

        # Escolha do número pela parte do utilizador
        numeroEscolhido = int(input('Estou a pensar num numero de 0 a 7 consegues adivinhar?  '))

        print("Hmm....")
        time.sleep(2)
        print("....")
        time.sleep(2)

        # Condição para verificar se o utilizador escolheu o número certo
        if numeroEscolhido == numeros:
            print(f"Acertaste! o numero que eu pensei era {numeros}")
        else:
            print(f"Perdeste :( , eu escolhi {numeros} e tu disseste {numeroEscolhido}")

    if opcao == "20":
        import random

        playerPick = input("Escolha entre Pedra, Papel ou Tesoura: ").upper()
        lista = ["PEDRA", "PAPEL", "TESOURA"]
        pcPick = random.choice(lista)

        if playerPick == "PEDRA" and pcPick == "PAPEL":
            print(f"Perdeste, eu escolhi {pcPick} e tu escolheste {playerPick}")
        elif playerPick == "PEDRA" and pcPick == "TESOURA":
            print(f"Ganhaste, eu escolhi {pcPick} e tu escolheste {playerPick}")
        elif playerPick == pcPick:
            print("Empate!")
        elif playerPick == "TESOURA" and pcPick == "PEDRA":
            print(f"Perdeste, eu escolhi {pcPick} e tu escolheste {playerPick}")
        elif playerPick == "TESOURA" and pcPick == "PAPEL":
            print(f"Ganhaste, eu escolhi {pcPick} e tu escolheste {playerPick}")
        elif playerPick == "PAPEL" and pcPick == "TESOURA":
            print(f"Perdeste, eu escolhi {pcPick} e tu escolheste {playerPick}")
        elif playerPick == "PAPEL" and pcPick == "PEDRA":
            print(f"Ganhaste, eu escolhi {pcPick} e tu escolheste {playerPick}")
        elif playerPick == "TESOURA" and pcPick == "PEDRA":
            print(f"Perdeste, eu escolhi {pcPick} e tu escolheste {playerPick}")

    if opcao == "21":
        import time

        timer = 11
        for x in range(0, 10):
            timer = timer - 1
            print(timer)
            time.sleep(1)
            if timer == 1:
                print("Feliz Ano Novo!!!")

    if opcao == "22":
        for x in range(0, 100, 2):
            if x > 0:
                print(x)

    if opcao == "23":
        # Pedir um Numero
        num = int(input("Digite um Numero: "))

        # Tabuada do numero introduzido
        for x in range(0, 10):
            print(num, " x ", x + 1, " = ", num * (x + 1))

    if opcao == "24":
        # Introdução do numero por parte do utilizador
        i = int(input("Digite um numero inteiro: "))

        total = 0

        # Formula de verificação se o numero introduzido é primo ou não

        for x in range(1, i + 1):
            if i % x == 0:
                total += 1
        if total == 2:
            print(f"O numero {i} é primo, foi divisivel {total} vezes")
        else:
            print(f"o numero {i} não é primo, foi divisivel {total} vezes")

    if opcao == "25":
        # Introdução da frase pelo utilizador
        frase = input("Escreve uma frase e eu verifico se é um palíndromo ou não: ").replace(" ", "").upper()
        # Tornar string numa lista
        fraseLista = list(frase)
        # ler a lista ao contrario
        fraseReversed = fraseLista[::-1]

        print(fraseLista)
        print(fraseReversed)

        # check se a frase ao contrario é igual a frase
        if fraseLista == fraseLista and fraseLista == fraseReversed:
            print("A sua frase é um palíndromo")
        else:
            print("a sua frase não é um palindromo")

    if opcao == "26":
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

    if opcao == "27":
        # Lista vazia para guardar as idades
        idades = []

        # loop que repete 10 vezes perguntando ao utilizador a idade de cada pessoa
        for pessoa in range(1, 11):
            idade = int(input(f"Digite a idade da {pessoa}ª pessoa: "))
            # introduzir o input na lista inicialmente vazia
            idades.append(idade)
        # sortear a lista do menor para o maior
        idades.sort()

        # apresentação de dados
        print(f"A pessoa mais nova tem {idades[0]} anos e a mais velha tem {idades[-1]} anos ")

    if opcao == "28":
        # Primeira Pergunta
        print("Portugal é um país?.")
        print("[V / F] ?")
        resp = input("--->").strip().upper()

        # loop para ter resposta adequada
        while resp not in 'VF':
            print("Por favor digite 'V para verdadeiro e 'F' para Falso")
            resp = input("--->").strip().upper()

        # validação resposta 1
        if resp in 'F':
            print("Está errado!!")
        elif resp in "V":
            print("Está certo!!")

        print("Uma centopeia tem 100 patas?")
        print("[V / F] ?")
        resp = input("--->").strip().upper()

        while resp not in 'VF':
            print("Por favor digite 'V para verdadeiro e 'F' para Falso")
            resp = input("--->").strip().upper()

        # validação resposta 2
        if resp in 'F':
            print("Está errado!!")
        elif resp in "V":
            print("Está certo!!")

        print("França é um país?")
        print("[V / F] ?")
        resp = input("--->").strip().upper()

        while resp not in 'VF':
            print("Por favor digite 'V para verdadeiro e 'F' para Falso")
            resp = input("--->").strip().upper()

        # validação resposta 3
        if resp in 'F':
            print("Está errado!!")
        elif resp in "V":
            print("Está certo!!")

    if opcao == "29":
        import random

        cpu_pick = random.randint(1, 10)
        tentativas = 1

        print("Consegues adivinhar em que numero estou a pensar entre 1 e 10?")
        resposta_utilizador = int(input("--->"))

        while resposta_utilizador != cpu_pick:
            if resposta_utilizador > cpu_pick:
                print("errado! mais baixo, tenta mais uma vez")
                tentativas += 1
                resposta_utilizador = int(input("--->"))
            elif resposta_utilizador < cpu_pick:
                print("errado! mais alto, tenta mais uma vez")
                tentativas += 1
                resposta_utilizador = int(input("--->"))

        print(f"Acertaste , tentaste {tentativas} vezes mas chegaste lá")

    if opcao == "30":
        print("Bem vindo a calculadora! :D ")
        print("Insira 3 numeros : ")
        valor1 = int(input(" "))
        valor2 = int(input(" "))
        valor3 = int(input(" "))

        soma = valor1 + valor2 + valor3
        multi = valor1 * valor2 * valor3
        maior = max(valor1, valor2, valor3)
        resposta = 3
        while resposta != 5:
            print("=====================")
            print("Insira o numero indicado para o calculo que deseja!")
            print("[1] Somar")
            print("[2] Multiplicar")
            print("[3] Maior")
            print("[4] Novos Numeros")
            print("[5] Sair")
            print("=====================")

            resposta = int(input(":"))

            if resposta == 1:
                print(soma)
            if resposta == 2:
                print(multi)
            if resposta == 3:
                print(maior)
            if resposta == 4:
                print("Insira 3 numeros : ")
                valor1 = int(input(" "))
                valor2 = int(input(" "))
                valor3 = int(input(" "))
                soma = valor1 + valor2 + valor3
                multi = valor1 * valor2 * valor3
                maior = max(valor1, valor2, valor3)

    if opcao == "31":
        import math

        print("Insira um numero para calculamos o seu fatorial ")
        numero = int(input())
        multiplicador = ""
        while multiplicador != 0:
            multiplicador = numero - 1
        print(math.factorial(numero))

    if opcao == "32":
        # Começo do programa com uma mensagem introdutoria para que o utilizador saiba o que introduzir
        print(
            "Insira um numero inteiro para que possamos mostrar os 4 primeiros elementos de uma sequência de Fibonacci.")

        # variavel onde vamos guardar o numero introduzido pelo utiizador
        numero = int(input())

        # loop onde vamos mostrar os primeiros x elementos de uma sequencia de Fibonacci
        for x in range(0, 4):
            numero = numero + x
            print(f"{numero} : {numero - 1} + {numero - 2} = {(numero - 1) + (numero - 2)}")

    if opcao == "33":
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

    if opcao == "34":
        # Inserção de dados pelos utilizador
        nota_matematica = float(input("insira a sua nota a matematica: "))
        nota_portugues = float(input("insira a sua nota a portuges: "))
        nota_filosofia = float(input("insira a sua nota a filosofia: "))
        nota_geografia = float(input("insira a sua nota a geografia: "))
        nota_ingles = float(input("insira a sua nota a ingles: "))

        # calculo da média
        media = (nota_portugues + nota_ingles + nota_geografia + nota_filosofia + nota_matematica) / 5
        # calculo da maior nota
        maior = max(nota_matematica, nota_ingles, nota_geografia, nota_filosofia, nota_portugues)
        # calculo da menor nota
        menor = min(nota_matematica, nota_ingles, nota_geografia, nota_filosofia, nota_portugues)

        # Exibição das notas
        print(f" A sua média foi {media}")
        print(f"A tua melhor nota foi {maior} ")
        print(f"A tua pior nota foi {menor}")

    if opcao == "35":
        # Atribuição de um numero só para que o While comece
        numero = 99999999

        # While com a condição que a variavel "numero" seja maior que 0
        while numero > 0:
            # Input de dados pelo utilizador para que possamos mostrar a adequada tabuada
            numero = int(input("Insira o numero que deseja ver a tabuada: "))
            # condição caso o utilizador escolha o numero 0 ou menor que 0 para fechar o programa
            if numero <= 0:
                quit()
            # caso a condição anterior não seja ativada, mostra a tabuada
            else:
                for x in range(1, 10):
                    print(f"{numero} * {x} = {numero * x}")

    if opcao == "36":
        import random

        par_certo = 0
        impar_certo = 0

        while par_certo == 0 or impar_certo == 0:
            print(" Par ou Impar? ")
            escolha = input().upper()
            escolhaCPU = random.randrange(11)

            if escolha == "IMPAR" and escolhaCPU == 1 or 3 or 5 or 7 or 9:
                impar_certo = 1
            elif escolha == "PAR" and escolhaCPU == 2 or 4 or 6 or 8 or 10:
                par_certo = 1

            if par_certo == impar_certo:
                print(f"Perdeste, disseste {escolha} e eu estava a pensar no numero {escolhaCPU}")
            if par_certo == 1:
                print(f"Ganhaste, disseste PAR, e eu estava a pensar no numero {escolhaCPU}")
            if impar_certo == 1:
                print(f"Ganhaste, disseste IMPAR, e eu estava a pensar no numero {escolhaCPU}")

    if opcao == "37":
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

    if opcao == "38":
        numeros = (
            "zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
            "treze",
            "catorze",
            "quinze", "dezasseis", "dezoito", "dezanove", "vinte")

        num = int(input("Digite um numero de 0 a 20: "))

        print(numeros[num])

    if opcao == "39":
        import time

        equipas = (
            "Real Madrid", "Girona", "Atl.Madrid", "Barcelona", "Ath.Bilbao", "Real Sociedad", "Betis", "Getafe",
            "Valencia",
            "Las Palmas", "Rayo Vallecano", "Osasuna", "Villareal", "Mallorca", "Alaves", "Sevilla", "Celta Vigo",
            "Cadiz",
            "Granada", "Almeria")

        equipas_lista = sorted(equipas)

        print("-------------------------")
        time.sleep(2)

        print("Os primeiros 5 qualificados são :")
        for e in equipas[0:5]:
            print(f"{e}")

        print("-------------------------")
        time.sleep(2)
        print("Os ultimos 4 qualificados são: ")
        for e in equipas[-5:-1]:
            print(e)

        print("-------------------------")
        time.sleep(2)
        print(" Aqui esta a lista total de equipas por ordem alfabetica :")
        for e in sorted(equipas):
            print(e)

        print("-------------------------")
        time.sleep(2)
        print(f"Las Palmas encontra-se na posição {equipas.index("Las Palmas") + 1}")

    if opcao == "40":
        import random

        numeros_aleatorios = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        numeros_selecionados = (
            numeros_aleatorios[random.randrange(1, 10)], numeros_aleatorios[random.randrange(1, 10)],
            numeros_aleatorios[random.randrange(1, 10)], numeros_aleatorios[random.randrange(1, 10)],
            numeros_aleatorios[random.randrange(1, 10)])

        numeros_sorted = sorted(numeros_selecionados)

        print(f"Os numeros escolhidos foram {numeros_selecionados}")
        print(f"O maior numero é o numero {numeros_sorted[0]}")
        print(f"O menor numero é o numero {numeros_sorted[-1]}")

    if opcao == "41":
        primeiro_numero = int(input("Digite o Primeiro numero: "))
        segundo_numero = int(input("Digite o Segundo numero: "))
        terceiro_numero = int(input("Digite o Terceiro numero: "))
        quarto_numero = int(input("Digite o Quarto numero: "))

        numeros = (primeiro_numero, segundo_numero, terceiro_numero, quarto_numero)

        numeros_pares = 0

        if (primeiro_numero % 2) == 0:
            numeros_pares = numeros_pares + 1
        if (segundo_numero % 2) == 0:
            numeros_pares = numeros_pares + 1
        if (terceiro_numero % 2) == 0:
            numeros_pares = numeros_pares + 1
        if (quarto_numero % 2) == 0:
            numeros_pares = numeros_pares + 1

        print(f"O numero 7 foi digitado {numeros.count(7)} vezes")

        if 5 in numeros:
            print(f"O numero 5 foi digitado na posição {numeros.index(5) + 1}")
        else:
            print(f"O numero 5 não foi digitado na posição")
        print(f"Foram digitados {numeros_pares} numeros pares")

    if opcao == "42":
        pass
    if opcao == "43":
        lista = []

        for cont in range(0, 5):
            num = int(input("Digite um número: "))
            lista.append(num)
            print(f"O número {num} foi adicionado com sucesso")

        lista_sorted = sorted(lista)

        menor = min(lista_sorted)
        maior = max(lista_sorted)

        print(f"O maior valor foi {maior} e o seu index é {lista_sorted.index(maior)}")
        print(f"O menor valor foi {menor} e o seu index é {lista_sorted.index(menor)}")

    if opcao == "44":
        resposta = "S"
        lista = []

        while resposta == "S":
            num = int(input("Adicione um numero: "))
            if num in lista:
                print("Esse numero já está na lista")
            else:
                lista.append(num)
                print("Valor adicionado com sucesso")
                lista.sort()
            resposta = input("Deseja continuar [S/N]?: ").upper()

        print(lista[::-1])

    if opcao == "45":
        lista = list()

        for c in range(0, 5):
            num = int(input("Digite um numero: "))
            if c == 0 or num > lista[-1]:
                lista.append(num)
                print("Numero adicionado com sucesso")
            else:
                indice = 0
                while indice < len(lista):
                    if num <= lista[indice]:
                        lista.insert(indice, num)
                        break
                    indice += 1

        print(lista)

    if opcao == "46":
        lista_total = []
        lista_pares = []
        lista_impares = []

        for x in range(0, 5):
            num = int(input("Digite um numero: "))
            lista_total.append(num)
            if (num % 2) == 0:
                lista_pares.append(num)
            else:
                lista_impares.append(num)

        print(lista_total)
        print(lista_pares)
        print(lista_impares)

    if opcao == "47":
        equacao = input("digite uma equação: ")

        if equacao.count("(") == equacao.count(")"):
            print("a sua equação está correta!")
        else:
            print("a sua equação está errada!")

    if opcao == "48":
        pares = []
        impares = []

        for x in range(0, 10):
            num = int(input("Digite um numero: "))
            if (num % 2) == 0:
                pares.append(num)
            else:
                impares.append(num)

        lista = list()

        lista.append(pares[:])

        lista.append(impares[:])

        print(lista)

    if opcao == "49":
        pass
    if opcao == "50":
        pass
