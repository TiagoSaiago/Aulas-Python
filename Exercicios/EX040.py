import random

numeros_aleatorios = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

numeros_selecionados = (numeros_aleatorios[random.randrange(1, 10)], numeros_aleatorios[random.randrange(1, 10)],
                        numeros_aleatorios[random.randrange(1, 10)], numeros_aleatorios[random.randrange(1, 10)],
                        numeros_aleatorios[random.randrange(1, 10)])

numeros_sorted = sorted(numeros_selecionados)

print(f"Os numeros escolhidos foram {numeros_selecionados}")
print(f"O maior numero é o numero {numeros_sorted[0]}")
print(f"O menor numero é o numero {numeros_sorted[-1]}")
