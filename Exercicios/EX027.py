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
