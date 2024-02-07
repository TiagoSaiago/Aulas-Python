# Imports

# Funções
def mensagem_adaptavel(msg):
    linhas = "="
    espaco = " " * 4
    contador = len(msg) + 8
    print(linhas * contador)
    print(f"{espaco}{msg}{espaco}")
    print(linhas * contador)


# Código Principal

mensagem = input("Insira a mensagem: ")
print()
mensagem_adaptavel(mensagem)
