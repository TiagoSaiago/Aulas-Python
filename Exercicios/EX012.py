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
