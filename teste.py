'''num = 7

for x in range(0, 10):
    print(num, " x ", x + 1, " = ", num * (x + 1))
'''

'''i = 1
f = 10
salto = 2

for x in range(i, f, salto):
    print(x)
'''

'''tentativas = 0
mensagem = "Bem Vindo"
password = "password"

for x in range(0, 3):
    entrada = input("insira a password: ")
    if entrada == password:
        print(mensagem)
    else:
        tentativas = tentativas + 1
        print("Tente novamente...\n")
    if tentativas == 3:
        print("Utilizador Bloqueado")
'''

opcao = 0

while opcao != 4:
    print("[ 1 ] - Regstar pessoa")
    print("[ 2 ] - Nº Pessoas registadas")
    print("[ 3 ] - Apagar um registo")
    print("[ 4 ] - Sair")
    print("Qual a sua opção")
    opcao = int(input("-----> "))
    if opcao == 1:
        nome = input("Digite o nome da pessoa")
        idade = int(input("Digite a idade da pessoa"))
        print(f"{nome} registado com sucesso.")
    elif opcao == 2:
        print("Há X pessoas registadas")
    elif opcao == 3:
        print("Um registo foi apagado!")
    elif opcao < 1 or opcao > 4:
        break
    elif opcao == 4:
        break
print("Obrigado e volte sempre!")
