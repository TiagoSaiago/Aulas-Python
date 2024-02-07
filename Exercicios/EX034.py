# Inserção de dados pelos utilizador
nota_matematica = float(input("insira a sua nota a matematica: "))
nota_portugues = float(input("insira a sua nota a portuges: "))
nota_filosofia = float(input("insira a sua nota a filosofia: "))
nota_geografia = float(input("insira a sua nota a geografia: "))
nota_ingles = float(input("insira a sua nota a ingles: "))

# calculo da média
media = (nota_portugues + nota_ingles + nota_geografia + nota_filosofia + nota_matematica) / 5
# calculo da maior nota
maior = max(nota_matematica, nota_ingles, nota_geografia, nota_filosofia, nota_portugues)
# calculo da menor nota
menor = min(nota_matematica, nota_ingles, nota_geografia, nota_filosofia, nota_portugues)

# Exibição das notas
print(f" A sua média foi {media}")
print(f"A tua melhor nota foi {maior} ")
print(f"A tua pior nota foi {menor}")
