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
