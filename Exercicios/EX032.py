# Começo do programa com uma mensagem introdutoria para que o utilizador saiba o que introduzir
print("Insira um numero inteiro para que possamos mostrar os 4 primeiros elementos de uma sequência de Fibonacci.")

# variavel onde vamos guardar o numero introduzido pelo utiizador
numero = int(input())

# loop onde vamos mostrar os primeiros x elementos de uma sequencia de Fibonacci
for x in range(0, 4):
    numero = numero + x
    print(f"{numero} : {numero - 1} + {numero - 2} = {(numero - 1) + (numero - 2)}")
