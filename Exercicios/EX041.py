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
