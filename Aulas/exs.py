import time
import random

'''#ex001

ola_mundo = "Olá Mundo"
print(ola_mundo)

print("\b")
#ex002

print("--------------------------")
print("------ Bem vindo :) ------")
print("--------------------------")

print("\b")
#ex003

first_number = int(input("Input your first number: "))
second_number = int(input("Input your second number: "))
resultado = first_number + second_number


print(f"{first_number} + {second_number} = {resultado}")

print("\b")
#ex004
number = int(input('input your number: '))
number_minus = number - 1
number_plus = number + 1

print(f'The number before {number} is {number_minus} and the number after {number} is {number_plus}')'''

# ex005

'''a = int(input("Input your first number: "))
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
print(f"{a} % {b} = {resto}")'''

'''# ex006

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
'''

'''# ex007

# pedir ano nascimento
ano_utilizador = int(input("Introduza o seu ano de nascimento: "))
ano_atual = int(input("Introduza o ano atual: "))
idade = ano_atual - ano_utilizador

# Exibir idade no ecra
print(f"A tua idade é {idade}")
'''

'''# ex008

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
'''

"""# ex009

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
print("==========================================")"""

'''# ex010

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
'''

'''# Ex 011

frase = input("Introduza uma frase: ")
frase_maiuscula = frase.upper()
letra_a = frase_maiuscula.count("A")
posicao_primeira_a = frase_maiuscula.find("A")
posicao_ultima_a = frase_maiuscula.rfind("A")

print(f"A sua frase contem a letra A {letra_a} vezes")
print(f"aparece pela primeira vez em {posicao_primeira_a + 1}")
print(f"Aparece pela ultima vez em {posicao_ultima_a + 1}")
'''

'''# Ex 012

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
'''

'''# Ex 013

# Introdução de Dados
palavra = input('Escreva uma palavra com 6 Letras: ').

# Print da Palavra ao contrario
print(palavra[::-1])
'''

'''# Ex 014

velocidade = int(input("Introduza a sua velocidade: "))
multa = (velocidade - 80) * 7 + 100

if velocidade > 80:
    print(f"Multado: {multa}€ ")
else:
    print("Não Multado")
'''

'''# Ex 015

numero = int(input("Digite um numero: "))
if numero % 2:
    print(f"O numero {numero} é Impar")
else:
    print(f"O numero {numero} é Par")
'''

"""# EX 016

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
"""

'''# Ex 017

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
'''

'''# Ex018

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
'''

'''# Ex 019

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
'''

'''# EX 020

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
'''
'''# Solução do stor

lista = [1, 2, 3]
CPUpick = random.choice(lista)
print("Escolha uma das seguintes: ")
print("1: Pedra")
print("2: Papel")
print("3: Tesoura")
playerPick = int(input(":"))

if playerPick - CPUpick == 0:
    print("Empate")
elif playerPick - CPUpick == -2 or playerPick - CPUpick:
    print("Ganhaste")
else:
    print("Perdeste")
'''
'''# ex021
timer = 11
for x in range(0, 10):
    timer = timer - 1
    print(timer)
    time.sleep(1)
    if timer == 1:
        print("Feliz Ano Novo!!!")
'''
# ex 022
'''for x in range(0, 100, 2):
    if x > 0:
        print(x)
'''
'''# Solução do stor

i = 0
f = 100

for x in range(i, f):
    if x == 0:
        continue
    elif x % 2 == 0:
        print(x)
'''

'''# ex 023

# Pedir um Numero
num = int(input("Digite um Numero: "))

# Tabuada do numero introduzido
for x in range(0, 10):
    print(num, " x ", x + 1, " = ", num * (x + 1))
'''
'''# ex 024

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
'''

'''# ex 025

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
'''
'''# ex 026

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
'''
'''# Solução do stor

from datetime import date

data_atual = date.today().year
# Iniciar variaveis de controlo
tot_maior = 0
tot_menor = 0

for pessoa in range(0, 7):
    pessoa = pessoa + 1
    nascimento = int(input(f"Digite em que ano a {pessoa}ª pessoa nasceu: "))
    idade = data_atual - nascimento
    if idade >= 18:
        tot_maior += 1
    else:
        tot_menor += 1

# Exibir no ecra os dados
print(f"Ao todo tivemos {tot_maior} pessoas maiores de idade.")
print(f"Ao todo tivemos {tot_menor} pessoas menores de idade.")
'''
"""# ex 027

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

# Solução do stor

# iniciar variaveis de controlo
maior = 0
menor = 0

for pessoa in range(0, 10):
    idade = int(input(f"{pessoa + 1} - digite a sua idade: "))
    if pessoa == 0:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        elif idade < menor:
            menor = idade

print(f"a maior idade encontrada foi {maior} anos")
print(f"a menor idade encontrada foi {menor} anos")"""

'''# ex 028

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
'''

# ex 029

'''numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
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
