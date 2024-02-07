numeros = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

pares = []

for x in range(0, 3):
    for y in range(0, 3):
        numeros[x][y] = int(input(f"Escreva um numero para [{x}][{y}]: "))

for x in range(0, 3):
    for y in range(0, 3):
        print(f"[{numeros[x][y]}]", end=" ")
    print()
