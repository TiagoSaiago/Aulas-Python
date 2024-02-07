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
