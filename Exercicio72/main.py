import divisao
import multiplicaçao
import soma
import subtraçao


while True:
    print("[ 1 ] - Soma")
    print("[ 2 ] - Subtração")
    print("[ 3 ] - Multiplicação")
    print("[ 4 ] - Divisão")
    print("[ 5 ] - Tabuada")
    print("[ 6 ] - Par ou Impar")
    print("[ 7 ] - Numeros Primos")
    print("[ 8 ] - Factorial")
    print("[ 0 ] - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        soma.soma(num1,num2)

    elif opcao == "2":
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        print(f"{num1} - {num2} = {subtraçao.subtraçao(num1,num2)}")
    elif opcao == "3":
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        try:
            multiplicaçao.multiplicaçao(num1,num2)
        except Exception as erro:
            print(f"ERRO ---{erro}")
    elif opcao == "4":
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        try:
            divisao.divisao(num1,num2)
        except Exception as erro:
            print(f"ERRO ---{erro}")
    elif opcao == "5":
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
    elif opcao == "6":
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
    elif opcao == "7":
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
    elif opcao == "8":
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
    elif opcao == "0":
        print("Saindo do programa. Até mais!")
        break
