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
